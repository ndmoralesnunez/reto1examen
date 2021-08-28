import threading
import random
import time
from datetime import datetime


# how many threads we want to start
THREADS_COUNT = 3

   

class Threaded_worker(threading.Thread):
    def __init__(self, sleep_time):
        threading.Thread.__init__(self)
        self.sleep_time = sleep_time
    def run(self):
        threadName = threading.currentThread().getName()
        print("[%s] Hello, I am %s and I will sleep %d seconds." % (datetime.now().strftime('%H:%M:%S'), threadName, sleep_time))
        time.sleep(self.sleep_time)
        print("[%s] I am %s and I have waken up." % (datetime.now().strftime('%H:%M:%S'), threadName))

print('Starting %d threads...' % THREADS_COUNT)
for i in range(THREADS_COUNT):
    sleep_time = random.randint(1,10)
    td = Threaded_worker(sleep_time)
    td.start()
