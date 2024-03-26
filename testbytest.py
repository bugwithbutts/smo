import numpy as np
import random
from enum import Enum
from queue import Queue

class TestByTestQueue(Queue):

    class Status(Enum):
        skip_test = 0
        final_test = 1
        wrong_test = 3

    def __init__(self, numberJudges, eps):
        super().__init__(numberJudges, eps) 
        self.id = []
        self.info = [[] for _ in range(numberJudges)]
        self.finalTest = [self.Status.skip_test for _ in range(numberJudges)]

    def newTaskForJudge(self, judge, moment):
        while len(self.queue) and len(self.id) and self.id[self.queue[0][3][2]] == 0:
            self.queue.pop(0)
        if len(self.queue) != 0:
            self.finalTest[judge] = self.queue[0][2]
            self.remainTimeOnJudge[judge] = self.queue[0][0]
            self.startWaiting[judge] = self.queue[0][1]
            if len(self.id):
                self.info[judge] = self.queue[0][3]    
            self.queue.pop(0)

    def freeJudge(self, moment, judge):
        if self.finalTest[judge] != self.Status.skip_test: 
            if len(self.id):    
                self.id[self.info[judge][2]] = 0               
            self.waitTimes.append(moment - self.startWaiting[judge])
        self.startWaiting[judge] = None

    def pushTests(self, testingTime, moment, testF, taskInd):
        submission_id = len(self.id)
        self.id.append(0)
        testF -= 1
        for i in range(len(testingTime) - 1):
            self.id[submission_id] += testingTime[i]  
            status = self.Status.skip_test
            if i == testF:
                status = self.Status.wrong_test
            self.queue.append([testingTime[i], moment, status, [testF, taskInd, submission_id]])

        self.id[submission_id] += testingTime[-1]
        status = self.Status.skip_test
        if testF == len(testingTime) - 1:
            status = self.Status.wrong_test
        elif testF == -1:
            status = self.Status.final_test
        self.queue.append([testingTime[-1], moment, status, [testF, taskInd, submission_id]])

    def push(self, testingTime, moment): 
        for i in range(len(testingTime) - 1):            
            self.queue.append([testingTime[i], moment - len(self.queue) * self.eps, self.Status.skip_test])
        self.queue.append([testingTime[-1], moment - len(self.queue) * self.eps, self.Status.final_test])