## A simple interface for users, where the screen prompts left/right motion and records ensuing keystrokes. Useful for later annotations of eeg data.
## Later on I can intermesh this code with the BCI 2000 software so this runs as data is being collected; we could possibly annotate the data WHILE the experiment is running.

import pygame, time, pickle
from event import Event
from const import *
from board import board

## SET UP ARROW PRESENTATIONS

def point_left():
    pygame.draw.polygon(screen, BLACK, 
        ((WIDTH/2 + 150, HEIGHT/2 + 50),
        (WIDTH/2 +150, HEIGHT/2 - 100 + 50),
        (WIDTH/2 - 50, HEIGHT/2 - 100 + 50),
        (WIDTH/2 - 50, HEIGHT/2 - 200 + 50),
        (WIDTH/2 - 225, HEIGHT/2 - 50 + 50),
        (WIDTH/2 - 50, HEIGHT/2 + 100 + 50),
        (WIDTH/2 - 50, HEIGHT/2 + 50)))

def point_right():
    pygame.draw.polygon(screen, BLACK, (
        (WIDTH/2 -150, HEIGHT/2 - 50),
        (WIDTH/2 -150, HEIGHT/2 + 100 - 50),
        (WIDTH/2 + 50, HEIGHT/2 + 100 - 50),
        (WIDTH/2 + 50, HEIGHT/2 + 200 - 50),
        (WIDTH/2 + 225, HEIGHT/2 + 50 - 50),
        (WIDTH/2 + 50, HEIGHT/2 - 100 - 50),
        (WIDTH/2 + 50, HEIGHT/2 - 50)))

def point_up():
    pygame.draw.polygon(screen, BLACK, (
        (WIDTH/2 - 150, HEIGHT/2 - 100),
        (WIDTH/2 - 0, HEIGHT/2 - 200),
        (WIDTH/2 + 150, HEIGHT/2 - 100),
        (WIDTH/2 - 80, HEIGHT/2 - 100),
        (WIDTH/2 - 80, HEIGHT/2 + 50),
        (WIDTH/2 + 80, HEIGHT/2 + 50),
        (WIDTH/2 + 80, HEIGHT/2 - 100),))

def point_down():
    pygame.draw.polygon(screen, BLACK, ((WIDTH/2 - 150, HEIGHT/2 + 50),
        (WIDTH/2 - 0, HEIGHT/2 + 150),
        (WIDTH/2 + 150, HEIGHT/2 + 50),
        (WIDTH/2 - 80, HEIGHT/2 + 50),
        (WIDTH/2 - 80, HEIGHT/2 - 100),
        (WIDTH/2 + 80, HEIGHT/2 - 100),
        (WIDTH/2 + 80, HEIGHT/2 + 50)))

def point_to_grasp():
    pygame.draw.polygon(screen, BLACK, ((WIDTH/2 + 150 - 80, HEIGHT/2 + 50),
        (WIDTH/2 +150 - 80, HEIGHT/2 - 100 + 50),
        (WIDTH/2 - 50 - 80, HEIGHT/2 - 100 + 50),
        (WIDTH/2 - 50 - 80, HEIGHT/2 - 200 + 50),
        (WIDTH/2 - 225 - 80, HEIGHT/2 - 50 + 50),
        (WIDTH/2 - 50 - 80, HEIGHT/2 + 100 + 50),
        (WIDTH/2 - 50 - 80, HEIGHT/2 + 50)))
    pygame.draw.polygon(screen, BLACK, ((WIDTH/2 -150 + 80, HEIGHT/2 - 50),
        (WIDTH/2 -150 + 80, HEIGHT/2 + 100 - 50),
        (WIDTH/2 + 50 + 80, HEIGHT/2 + 100 - 50),
        (WIDTH/2 + 50 + 80, HEIGHT/2 + 200 - 50),
        (WIDTH/2 + 225 + 80, HEIGHT/2 + 50 - 50),
        (WIDTH/2 + 50 + 80, HEIGHT/2 - 100 - 50),
        (WIDTH/2 + 50 + 80, HEIGHT/2 - 50)))

## SET UP PYGAME STUFF

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

## SET UP EVENTS FOR RECORDING TRIAL

loop_timestamp = time.time()
init_time = time.time()
trial_count = 0

running = True
intro_passed = False

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

    screen.fill(WHITE)
    
    # Intro Message
    if (time.time() - loop_timestamp) < 1 and not intro_passed:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Please fixate on the following cross until trials begin.', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, textRect)
        if event_log[-1].type != 'INTRO' :
            event_log.append(Event(timestamp=time.time(), event_type='INTRO'))

    # Cross pattern to focus subject
    elif (time.time() - loop_timestamp) < 3:
        pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH/2 - 10, HEIGHT/2 - 50, 20, 100))
        pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH/2 - 50, HEIGHT/2 - 10, 100, 20))
        if event_log[-1].task != 'WAIT':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='WAIT'))
    
    # Arrow pointing left
    elif (time.time() - loop_timestamp) < 6:
        point_left()
        if event_log[-1].task != 'LEFT':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='LEFT'))

    # Arrow pointing right
    elif (time.time() - loop_timestamp) < 9:
        point_right()
        if event_log[-1].task != 'RIGHT':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='RIGHT'))
   
   # Arrow pointing up
    elif (time.time() - loop_timestamp) < 12:
        point_up()
        if event_log[-1].task != 'UP':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='UP'))
   
    # Arrow pointing down
    elif (time.time() - loop_timestamp) < 15:
        point_down()
        if event_log[-1].task != 'DOWN':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='DOWN'))
   
   #Two Arrows for both hands meaning closing hand
    elif (time.time() - loop_timestamp) < 18:
        point_to_grasp()
        if event_log[-1].task != 'CLOSE':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='CLOSE'))

   #Circle for resting that counts for opening hand
    elif (time.time() - loop_timestamp) < 21:
        pygame.draw.circle(screen, BLACK, (WIDTH/2, HEIGHT/2), 100)
        if event_log[-1].task != 'OPEN':
            event_log.append(Event(timestamp=time.time(), event_type='TASK_CHANGE', task='OPEN'))
   
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
