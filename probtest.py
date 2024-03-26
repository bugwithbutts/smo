import numpy as np
import random
from testbytest import TestByTestQueue

class ProbTestQueue(TestByTestQueue):
    def __init__(self, numberJudges, tasks, eps):
        super().__init__(numberJudges, eps)
        self.stats = []
        self.submits = [0 for _ in range(len(tasks))]
        for i in tasks:
            self.stats.append([0 for _ in range(len(i))])

    def newTaskForJudge(self, judge, moment):

        while len(self.queue) != 0 and self.id[self.queue[0][3][2]] == 0:
            self.queue.pop(0)

        if len(self.queue) != 0:
            ind = 0
            sum_i = 0
            lst_i = -1
            mn = 1e9
            for i in range(len(self.queue)):
                testingTime_i, submitTime_i, status_i, info_i = self.queue[i]
                # if info_i[2] == lst_i:
                #     continue
                if self.id[info_i[2]] == 0:
                    continue
                if lst_i != info_i[2]:
                    sum_i += self.id[info_i[2]]
                lst_i = info_i[2]
                p = 0
                if self.submits[info_i[1]] != 0:
                    p = self.stats[info_i[1]][info_i[0]] / self.submits[info_i[1]]
                myTime = sum_i + (moment - submitTime_i)
                ok = 0
                sum_j = 0
                lst_j = -1
                for j in range(i):
                    testingTime_j, submitTime_j, status_j, info_j = self.queue[j]
                    if self.id[info_j[2]] == 0 or info_j[2] == info_i[2]:
                        continue
                    if lst_j != info_j[2]:
                        sum_j += self.id[info_j[2]]
                    lst_j = info_j[2]
                    thatTime = sum_j + (moment - submitTime_j)
                    if myTime <= thatTime + testingTime_i:
                        ok = 1
                        break
                delta = -(self.id[info_i[2]] - testingTime_i) * p + (info_i[2] - self.queue[0][3][2]) * testingTime_i
                if ok == 0 and delta < mn:
                    mn = delta
                    ind = i
            
            self.id[self.queue[ind][3][2]] -= self.queue[ind][0]
            self.info[judge] = self.queue[ind][3]
            self.finalTest[judge] = self.queue[ind][2]
            self.remainTimeOnJudge[judge] = self.queue[ind][0]
            self.startWaiting[judge] = self.queue[ind][1]   
            self.queue.pop(ind)

    def freeJudge(self, moment, judge):
        if self.finalTest[judge] == self.Status.wrong_test:
                self.submits[self.info[judge][1]] += 1
                self.stats[self.info[judge][1]][self.info[judge][0]] += 1
        if self.finalTest[judge] != self.Status.skip_test:
            self.id[self.info[judge][2]] = 0
            self.waitTimes.append(moment - self.startWaiting[judge])
        self.startWaiting[judge] = None
