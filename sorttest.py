import numpy as np
import random
from testbytest import TestByTestQueue

class SortTestQueue(TestByTestQueue):
    def __init__(self, numberJudges, tasks, eps):
        super().__init__(numberJudges, eps)
        self.stats = []
        self.submits = [0 for _ in range(len(tasks))]
        for i in tasks:
            self.stats.append([0 for _ in range(len(i))])

    def freeJudge(self, moment, judge):
        if self.finalTest[judge] == self.Status.wrong_test:
                self.submits[self.info[judge][1]] += 1
                self.stats[self.info[judge][1]][self.info[judge][0]] += 1
        if self.finalTest[judge] != self.Status.skip_test:
            self.id[self.info[judge][2]] = 0
            self.waitTimes.append(moment - self.startWaiting[judge])
        self.startWaiting[judge] = None

    def pushTests(self, testingTime, moment, testF, taskInd):
        submission_id = len(self.id)
        self.id.append(0)
        testF -= 1
        v = []
        for i in range(len(testingTime)):
            p = 0
            if self.submits[taskInd]:
                p = self.stats[taskInd][i] / self.submits[taskInd]
            v.append([-p, i])
        v.sort()
        for i in range(len(testingTime)):
            if v[i][1] == testF:
                testF = i
                break
        for i in range(len(testingTime) - 1):
            self.id[submission_id] += testingTime[v[i][1]]  
            status = self.Status.skip_test
            if i == testF:
                status = self.Status.wrong_test
            self.queue.append([testingTime[v[i][1]], moment, status, [testF, taskInd, submission_id]])

        self.id[submission_id] += testingTime[v[-1][1]]
        status = self.Status.skip_test
        if testF == len(testingTime) - 1:
            status = self.Status.wrong_test
        elif testF == -1:
            status = self.Status.final_test
        self.queue.append([testingTime[v[-1][1]], moment, status, [testF, taskInd, submission_id]])