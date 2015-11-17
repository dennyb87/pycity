#!/usr/bin/env python3
"""StopWatch

Write a test program that measures the execution time
of adding numbers from 1 to 1,000,000.
"""
from datetime import datetime


class StopWatch:

    def __init__(self):
        self.__startTime = 0
        self.__endTime = 0

    def start(self):
        self.__startTime = datetime.now()

    def stop(self):
        self.__endTime = datetime.now()

    def get_start_time(self):
        return self.__startTime

    def get_end_time(self):
        return self.__endTime

    def get_elapsed_time(self):
        return self.get_end_time() - self.get_start_time()

    def timeit(self, func):
        self.start()
        func()
        self.stop()

if __name__ == "__main__":

    def test():
        L = []
        for n in range(1000000):
            L.append(n)
        return sum(L)

    watcher = StopWatch()
    watcher.timeit(test)
    elapsed = watcher.get_elapsed_time()
    print(elapsed)
