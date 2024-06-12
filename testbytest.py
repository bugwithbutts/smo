import numpy as np
import random
from enum import Enum
from queue import Queue
from copy import deepcopy

class TestByTestQueue(Queue):
    def __init__(self, numberJudges):
        super().__init__(numberJudges) 
        self.id = []
        self.info = [None for _ in range(numberJudges)]

    def newTaskForJudge(self, judge, moment):
        while len(self.queue) and self.id[self.queue[0].id] == 0:
            self.queue.pop(0)
        if len(self.queue) != 0:
            self.remainTimeOnJudge[judge] = self.queue[0].tl
            self.startWaiting[judge] = self.queue[0].time
            self.info[judge] = self.queue[0]
            self.queue.pop(0)

    def freeJudge(self, moment, judge):
        self.id[self.info[judge].id] -= self.info[judge].tl 
        if self.id[self.info[judge].id] == 0 or self.info[judge].test == self.info[judge].wa: 
            self.id[self.info[judge].id] = 0
            self.waitTimes.append(moment - self.startWaiting[judge])
        self.startWaiting[judge] = None

    def push(self, event): 
        submission_id = len(self.id)
        ev = deepcopy(event)
        ev.id = submission_id
        self.id.append(0)
        for i in range(ev.numberTests):
            self.id[submission_id] += ev.tl  
            tmpEvent = deepcopy(ev)
            tmpEvent.test = i + 1          
            self.queue.append(tmpEvent)