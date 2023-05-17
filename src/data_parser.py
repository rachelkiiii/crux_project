"""


import pickle

def find_task(timestamp, event_logs):
	for i in range(len(event_logs)):
		if event_logs[i].timestamp > timestamp:
			return event_logs[i-1].timestamp, event_logs[i].timestamp

def consolidate_data():
	all_events = {'left': [],
						'right': [],
						'up': [],
						'down': [],
						'grasp': []
						'rest': []}
	with open('motion_gui_logs', 'rb') as f:
    	all_logs = pickle.load(f)
    data_logs = all_logs['data']
    event_logs = all_logs['events']
    for data_log in data_logs:
    	task = find_task(data_log.timestamp, event_logs)
"""

import pickle

with open('motion_gui_logs.pickle', 'rb') as f:
	data = pickle.load(f)['DATA_LOG']
	for chunk in data:
		time = chunk['data']