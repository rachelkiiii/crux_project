import pickle

class Event:
    def __init__(self, timestamp, event_type, task=None, key=None):
        self.timestamp = timestamp
        self.type = event_type
        self.task = task
        self.key = key

data = pickle.load(open("motion_gui_logs_redo.pickle", "rb"))
print(data)