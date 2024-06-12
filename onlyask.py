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
            testingTime_i = self.queue[i].tl * self.queue[i].numberTests
            if minTime > testingTime_i:
                minTime = testingTime_i
                minIndex = i
        self.remainTimeOnJudge[judge] = self.queue[minIndex].tl * self.queue[minIndex].numberTests
        self.startWaiting[judge] = self.queue[minIndex].time
        self.queue.pop(minIndex)