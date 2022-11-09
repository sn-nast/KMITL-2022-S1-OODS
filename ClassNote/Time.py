import time

class Time:
    def __init__(self):
        self.start = time.time()
        self.stop = 0
    
    def get_time(self):
        print(f'time: {time.time() - self.start} s') 
    
    def reset(self):
        self.start = time.time()