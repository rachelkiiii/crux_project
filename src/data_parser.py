import pickle
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

event_log = {}

left = np.array([])
right = np.array([])

with open('motion_gui_logs_darren.pickle', 'rb') as f:
    file = pickle.load(f)
    
    for event in file['EVENT_LOG']:
        event_data = vars(event)
        event_log[event_data['timestamp']] = event_data['task']
    
    read_data = file['DATA_LOG']
    for chunk in read_data:
        if event_log[chunk['time']] == 'LEFT':
            if left.size:
                left = np.concatenate((left, chunk['data'][:8]), axis=1)
            else:
                left = chunk['data'][:8]
        elif event_log[chunk['time']] == 'RIGHT':
            if right.size:
                right = np.concatenate((right, chunk['data'][:8]), axis=1)
            else:
                right = chunk['data'][:8]

