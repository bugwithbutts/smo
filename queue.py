import numpy as np
import random

class Queue(object):
    def __init__(self, numberJudges):
        self.queue = []
        self.waitTimes = []
        self.numberJudges = numberJudges
        self.remainTimeOnJudge = [0 for _ in range(numberJudges)]
        self.startWaiting = [None for _ in range(numberJudges)] 

    def newTaskForJudge(self, judge, moment):
        if len(self.queue) != 0:
            self.remainTimeOnJudge[judge] = self.queue[0].tl * self.queue[0].numberTests
            self.startWaiting[judge] = self.queue[0].time  
            self.queue.pop(0)

    def freeJudge(self, moment, judge):
        self.waitTimes.append(moment - self.startWaiting[judge])
        self.startWaiting[judge] = None

    def tact(self, moment):
        # Iterate through judges 
        for judge in range(self.numberJudges):

            if self.remainTimeOnJudge[judge] > 0:
                self.remainTimeOnJudge[judge] -= 1

            if self.remainTimeOnJudge[judge] == 0:
                # Add waiting time when request has been finished
                if self.startWaiting[judge] != None: 
                    self.freeJudge(moment, judge)                   

                # Begin process new request
                self.newTaskForJudge(judge, moment)

    def push(self, event):              
        self.queue.append(event)

    def printStatistic(self):
        print(f"Max {self.__class__.__name__} time: ", max(self.waitTimes))          
        print(f"Average {self.__class__.__name__} time: ", np.mean(self.waitTimes)) 

    def getMax(self):
        return max(self.waitTimes)
        
    def getAverage(self):
        return np.mean(self.waitTimes)

    def empty(self):        
        return len(self.queue) != 0 or max(self.remainTimeOnJudge) == 0