## A simple interface for users, where the screen prompts left/right motion and records ensuing keystrokes. Useful for later annotations of eeg data.
## Later on I can intermesh this code with the BCI 2000 software so this runs as data is being collected; we could possibly annotate the data WHILE the experiment is running.

import pygame, time, pickle
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import time

## SETUP DATA COLLECTION

BoardShim.enable_dev_board_logger()
params = BrainFlowInputParams()
params.ip_port = 6677
params.ip_port_aux = 6678
params.ip_address = "225.1.1.1"
params.ip_address_aux = "225.1.1.1"
params.master_board = BoardIds.SYNTHETIC_BOARD
board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)

## DEFINE CONSTANTS

white = (255, 255, 255)
black = (0, 0, 0)

width, height = 1800, 1000

TOTAL_TRIALS = 1

running = True
intro_passed = False
trial_count = 0

## SET UP PYGAME STUFF

pygame.init()

screen = pygame.display.set_mode((width, height))
screen.fill(white)

## SET UP EVENTS FOR RECORDING TRIAL

class Event:
    def __init__(self, timestamp, event_type, task=None, key=None):
        self.timestamp = timestamp
        self.type = event_type
        self.task = task
        self.key = key

loop_timestamp = time.time()
init_time = time.time()

event_log = [Event(timestamp=time.time(), event_type='START_OF_TRIAL')]
data_log = []

## START STREAM

board.prepare_session()
board.start_stream()

## MAIN LOOP

while running:
    # Gather data asynchronously
    data = board.get_board_data(256)
    if data.size > 0:
        data_log.append({'time': time.time(), 'data': data})

    screen.fill(white)
    
    # Intro Message
    if (time.time() - loop_timestamp) < 1 and not intro_passed:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Please fixate on the following cross until trials begin.', True, black)
        textRect = text.get_rect()
        textRect.center = (width // 2, height // 2)
        screen.blit(text, textRect)
        if event_log[-1].type != 'INTRO' :
            event_log.append(Event(timestamp=time.time()-init_time, event_type='INTRO'))

    # Cross pattern to focus subject
    elif (time.time() - loop_timestamp) < 3:
        pygame.draw.rect(screen, black, pygame.Rect(width/2 - 10, height/2 - 50, 20, 100))
        pygame.draw.rect(screen, black, pygame.Rect(width/2 - 50, height/2 - 10, 100, 20))
        if event_log[-1].task != 'WAIT':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='WAIT'))
    
    # Arrow pointing left
    elif (time.time() - loop_timestamp) < 6:
        pygame.draw.polygon(screen, black, ((width/2 + 150, height/2 + 50),
                                                                (width/2 +150, height/2 - 100 + 50),
                                                                (width/2 - 50, height/2 - 100 + 50),
                                                                (width/2 - 50, height/2 - 200 + 50),
                                                                (width/2 - 225, height/2 - 50 + 50),
                                                                (width/2 - 50, height/2 + 100 + 50),
                                                                (width/2 - 50, height/2 + 50)))
        if event_log[-1].task != 'LEFT':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='LEFT'))

    # Arrow pointing right
    elif (time.time() - loop_timestamp) < 9:
        pygame.draw.polygon(screen, black, ((width/2 -150, height/2 - 50),
                                                                (width/2 -150, height/2 + 100 - 50),
                                                                (width/2 + 50, height/2 + 100 - 50),
                                                                (width/2 + 50, height/2 + 200 - 50),
                                                                (width/2 + 225, height/2 + 50 - 50),
                                                                (width/2 + 50, height/2 - 100 - 50),
                                                                (width/2 + 50, height/2 - 50)))
        if event_log[-1].task != 'RIGHT':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='RIGHT'))
   
   # Arrow pointing up
    elif (time.time() - loop_timestamp) < 12:
        pygame.draw.polygon(screen, black, ((width/2 - 150, height/2 - 100),
                                                            (width/2 - 0, height/2 - 200),
                                                            (width/2 + 150, height/2 - 100),
                                                              (width/2 - 80, height/2 - 100),
                                                            (width/2 - 80, height/2 + 50),
                                                            (width/2 + 80, height/2 + 50),
                                                            (width/2 + 80, height/2 - 100),
                                                            ))
        if event_log[-1].task != 'UP':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='UP'))
   
    # Arrow pointing down
    elif (time.time() - loop_timestamp) < 15:
        pygame.draw.polygon(screen, black, ((width/2 - 150, height/2 + 50),
                                                            (width/2 - 0, height/2 + 150),
                                                            (width/2 + 150, height/2 + 50),
                                                            (width/2 - 80, height/2 + 50),
                                                            (width/2 - 80, height/2 - 100),
                                                            (width/2 + 80, height/2 - 100),
                                                            (width/2 + 80, height/2 + 50)
                                                            ))
        if event_log[-1].task != 'DOWN':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='DOWN'))
   
   #Two Arrows for both hands meaning closing hand
    elif (time.time() - loop_timestamp) < 18:
        pygame.draw.polygon(screen, black, ((width/2 + 150 - 80, height/2 + 50),
                                                                (width/2 +150 - 80, height/2 - 100 + 50),
                                                                (width/2 - 50 - 80, height/2 - 100 + 50),
                                                                (width/2 - 50 - 80, height/2 - 200 + 50),
                                                                (width/2 - 225 - 80, height/2 - 50 + 50),
                                                                (width/2 - 50 - 80, height/2 + 100 + 50),
                                                                (width/2 - 50 - 80, height/2 + 50)))
        pygame.draw.polygon(screen, black, ((width/2 -150 + 80, height/2 - 50),
                                                                (width/2 -150 + 80, height/2 + 100 - 50),
                                                                (width/2 + 50 + 80, height/2 + 100 - 50),
                                                                (width/2 + 50 + 80, height/2 + 200 - 50),
                                                                (width/2 + 225 + 80, height/2 + 50 - 50),
                                                                (width/2 + 50 + 80, height/2 - 100 - 50),
                                                                (width/2 + 50 + 80, height/2 - 50)))
        if event_log[-1].task != 'CLOSE':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='CLOSE'))

   #Circle for resting that counts for opening hand
    elif (time.time() - loop_timestamp) < 21:
        pygame.draw.circle(screen, black, (width/2, height/2), 100)
        if event_log[-1].task != 'OPEN':
            event_log.append(Event(timestamp=time.time()-init_time, event_type='TASK_CHANGE', task='OPEN'))
   
    # Once one trial complete, check for more
    elif trial_count < TOTAL_TRIALS:
        loop_timestamp = time.time()
        intro_passed = True
        trial_count += 1
    # Otherwise exit the loop
    else:
        running = False
    pygame.display.flip()

    # Check for events such as exiting or clicking a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

event_log.append(Event(timestamp=0, event_type='END_OF_TRIAL'))

# Conclude stream
board.stop_stream()

## SAVE FILE

with open('motion_gui_logs.pickle', 'wb') as handle:
    pickle.dump({'EVENT_LOG': event_log, 'DATA_LOG': data_log}, handle)
"""

import pickle

class Event:
    def __init__(self, timestamp, event_type, task=None, key=None):
        self.timestamp = timestamp
        self.type = event_type
        self.task = task
        self.key = key

all_logs = pickle.load(open('motion_gui_logs.pickle', 'rb'))

print(all_logs)

""