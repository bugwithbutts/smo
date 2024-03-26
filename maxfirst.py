import numpy as np
import random
from queue import Queue

class MaxFirstQueue(Queue):
    def newTaskForJudge(self, judge, moment):

        if len(self.queue) == 0:
            return

        minIndex = None        
        sum_i = 0
        for i in range(len(self.queue)):
            testingTime_i, submissionTime_i = self.queue[i]
            sum_i += testingTime_i
            myTime = sum_i + (moment - submissionTime_i)

            sum_j = 0
            ok = 0
            for j in range(0, i):
                testingTime_j, submissionTime_j = self.queue[j]
                sum_j += testingTime_j
                thatTime = sum_j + (moment - submissionTime_j)
                if myTime <= thatTime + testingTime_i:
                    ok = 1
                    break
                    
            if ok == 0:
                minIndex = i

        self.remainTimeOnJudge[judge] = self.queue[minIndex][0]
        self.startWaiting[judge] = self.queue[minIndex][1]
        self.queue.pop(minIndex)