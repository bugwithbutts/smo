import numpy as np
import random
from queue import Queue

class MaxFirstQueue(Queue):
    def newTaskForJudge(self, judge, moment):

        if len(self.queue) == 0:
            return

        minIndex = None        
        sum_i = 0
        mx = 0
        for i in range(len(self.queue)):
            testingTime_i = self.queue[i].tl * self.queue[i].numberTests
            submissionTime_i = self.queue[i].time
            sum_i += testingTime_i
            myTime = sum_i + (moment - submissionTime_i)

            if myTime > mx:
                mx = myTime
                minIndex = i
        if judge != 0:
            minIndex = 0
        self.remainTimeOnJudge[judge] = self.queue[minIndex].tl * self.queue[minIndex].numberTests
        self.startWaiting[judge] = self.queue[minIndex].time
        self.queue.pop(minIndex)