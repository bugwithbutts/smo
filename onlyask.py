import numpy as np
import random
from queue import Queue

class OnlyAskQueue(Queue):
    def newTaskForJudge(self, judge, moment):

        if len(self.queue) == 0:
            return

        minIndex = 0     
        minTime = 1e9
        for i in range(len(self.queue)):
            testingTime_i = self.queue[i][0]
            if minTime > testingTime_i:
                minTime = testingTime_i
                minIndex = i

        self.remainTimeOnJudge[judge] = self.queue[minIndex][0]
        self.startWaiting[judge] = self.queue[minIndex][1]
        self.queue.pop(minIndex)