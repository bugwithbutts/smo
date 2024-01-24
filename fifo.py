import numpy as np
import random

class FifoQueue(object):

    # Queue of waiting requests. Element is [time for testing, moment when added]
    queue = []

    # Waiting times of all requests
    waitTimes = []

    # Time needed to finish processed request for every judge
    remainTimeOnJudge = []

    # Time when request processed on judge was added to queue
    startWaiting = []

    numberJudges = 0

    def __init__(self, numberJudges):
        self.numberJudges = numberJudges
        self.remainTimeOnJudge = [0 for _ in range(numberJudges)]
        self.startWaiting = [None for _ in range(numberJudges)] 

    def newTaskForJudge(self, judge):
        if len(self.queue) > 0:
            self.remainTimeOnJudge[judge] = self.queue[0][0]
            self.startWaiting[judge] = self.queue[0][1]                 
            self.queue.pop(0)

    def tact(self, moment):       

        # Iterate through judges 
        for judge in range(self.numberJudges):

            if self.remainTimeOnJudge[judge] > 0:
                self.remainTimeOnJudge[judge] -= 1

            if self.remainTimeOnJudge[judge] == 0:
                
                # Add waiting time when request has been finished
                if self.startWaiting[judge] != None:                    
                    self.waitTimes.append(moment - self.startWaiting[judge])
                    self.startWaiting[judge] = None

                # Begin process new request
                self.newTaskForJudge(judge)

    def push(self, testingTime, moment):              
        self.queue.append([testingTime, moment])

    def printStatistic(self):        
        # Print in minutes
        print("Max fifo time: ", max(self.waitTimes) / 60)          
        print("Average fifo time: ", np.mean(self.waitTimes) / 60)                     

    def empty(self):        
        return len(self.queue) != 0 or max(self.remainTimeOnJudge) == 0