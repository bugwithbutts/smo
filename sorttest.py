import numpy as np
import random
from testbytest import TestByTestQueue
from copy import deepcopy

class SortTestQueue(TestByTestQueue):
    def __init__(self, numberJudges):
        super().__init__(numberJudges)
        self.stats = [[0 for _ in range(1000)] for _ in range(26)]

    def freeJudge(self, moment, judge):
        super().freeJudge(moment, judge)
        if self.info[judge].test == self.info[judge].wa:
            self.stats[self.info[judge].letter][self.info[judge].test] += 1

    def push(self, event):
        submission_id = len(self.id)
        ev = deepcopy(event)
        ev.id = submission_id
        self.id.append(0)
        tmp = []
        for i in range(ev.numberTests):
            self.id[submission_id] += ev.tl
            tmpEvent = deepcopy(ev)
            tmpEvent.test = i + 1
            # print(tmpEvent.test)
            tmp.append(tmpEvent)
        tmp.sort(key=lambda x: self.stats[x.letter][x.test], reverse=True)
        for i in tmp:
            # print(i.test)
            self.queue.append(i)