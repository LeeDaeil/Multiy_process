import threading
from time import sleep

class P_2(threading.Thread):
    def __init__(self, shared_mem):
        threading.Thread.__init__(self)
        self.mem = shared_mem

    def run(self):
        while True:
            self.mem[0] += 1
            print('{} : {}'.format(self, self.mem))
            if self.mem[1] == 4:
                break
            sleep(0.5)