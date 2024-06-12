import numpy as np
import random
from testbytest import TestByTestQueue
from copy import deepcopy
class ProbTestQueue(TestByTestQueue):
    def __init__(self, numberJudges):
        super().__init__(numberJudges)
        self.stats = [[0 for _ in range(1000)] for _ in range(26)]
        self.submits = [0 for _ in range(26)]

    def newTaskForJudge(self, judge, moment):

        while len(self.queue) and self.id[self.queue[0].id] == 0:
            self.queue.pop(0)

        if len(self.queue) != 0:
            ind = 0
            lst = -1
            mn = 0
            cnt = 0
            for i in range(len(self.queue)):
                tl = self.queue[i].tl
                time = self.queue[i].time
                test = self.queue[i].test
                id = self.queue[i].id
                letter = self.queue[i].letter
                # Skip not the first test of the task
                if False:
                    continue
                else:
                    cnt += tl
                    lst = id
                p = 0
                if self.submits[letter] != 0:
                    p = self.stats[letter][test] / self.submits[letter]
                delta = -(self.id[id] - tl) * p + 2 * tl
                if delta < mn:
                    mn = delta
                    ind = i

            self.remainTimeOnJudge[judge] = self.queue[ind].tl
            self.startWaiting[judge] = self.queue[ind].time
            self.info[judge] = self.queue[ind]
            self.queue.pop(ind)

    def freeJudge(self, moment, judge):
        super().freeJudge(moment, judge)
        if self.info[judge].test == self.info[judge].wa:
            self.stats[self.info[judge].letter][self.info[judge].test] += 1
            self.submits[self.info[judge].letter] += 1

    # def push(self, event):
    #     submission_id = len(self.id)
    #     ev = deepcopy(event)
    #     ev.id = submission_id
    #     self.id.append(0)
    #     tmp = []
    #     for i in range(ev.numberTests):
    #         self.id[submission_id] += ev.tl
    #         tmpEvent = deepcopy(ev)
    #         tmpEvent.test = i + 1
    #         tmp.append(tmpEvent)
    #     tmp.sort(key=lambda x: self.stats[x.letter][x.test], reverse=True)
    #     for i in tmp:
    #         self.queue.append(i)

