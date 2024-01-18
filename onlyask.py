import numpy as np
import random

class OnlyAskQueue(object):

    # Queue of waiting requests. Element is [time for testing, moment when added, skip limit]
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

        if len(self.queue) == 0:
            return

        # Find possible minumum time element in queue
        minTask = 10000000
        minIndex = None        
        ind = 0

        for i in self.queue:
            if i[0] < minTask:
                minTask = i[0]
                minIndex = ind            
            ind += 1
        
        # Skip ahead possible min element        
        if minTask <= self.queue[0][2]:
            self.remainTimeOnJudge[judge] = self.queue[minIndex][0]
            self.startWaiting[judge] = self.queue[minIndex][1]                                         
            self.queue[0][2] -= minTask
            self.queue.pop(minIndex)
        else:
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
        self.queue.append([testingTime, moment, testingTime // 2])        

    def getMeanWaitTime(self):  
        print("Max only ask time: ", max(self.waitTimes) / 100 / 60)         
        return np.mean(self.waitTimes)

    def empty(self):        
        return len(self.queue) != 0 or max(self.remainTimeOnJudge) == 0