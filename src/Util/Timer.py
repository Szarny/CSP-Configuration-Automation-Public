import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.time_list = []

    def start(self):
        self.start_time = time.time()

    def stop(self):
        print("stop")
        self.time_list.append(time.time() - self.start_time)

    def get_total_time(self):
        return sum(self.time_list)