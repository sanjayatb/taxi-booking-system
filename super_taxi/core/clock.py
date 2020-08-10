import time
from threading import Thread


class TimerCallBack:
    def time_tick(self,__time_counter):
        pass


class Clock(Thread):
    def __init__(self,call_backs:TimerCallBack = None):
        Thread.__init__(self)
        self.__time_counter = 0
        self.time_unit = 5 # 5 seconds as 1 unit of time
        self.running = False
        self.call_backs = call_backs

    def tick(self):
        self.__time_counter +=1

    def run(self) -> None:
        self.running = True
        while self.running:
            time.sleep(self.time_unit)
            self.__time_counter += 1
            print("#########################################")
            print("System Time now :", self.__time_counter)
            for call_back in self.call_backs:
                call_back.time_tick(self.__time_counter)

    def stop(self):
        self.running = False

    def reset(self,value=0):
        self.__time_counter = value
