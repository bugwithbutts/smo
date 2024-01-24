import numpy as np
import random
from fifo import FifoQueue
from onlyask import OnlyAskQueue
from gen import genEvents, genTasks
from model import launchModel

# Moments of time when tasks were sent
events1 = genEvents(eventsInSec = 0.04, timeIntervalInSec = 5 * 60 * 60, numberOfTasks = 5)
print(len(events1))

interval1 = 0
lst = 0
for i in events1:
	interval1 += (i[0] - lst)
interval1 /= len(events1) - 1
print(interval1)
print('-------------------')
events2 = []
file = open('parsed', 'r')
for i in file.readlines():
	events2.append([int(i[:-1]), random.randrange(5)])
print(len(events2))
interval2 = 0
lst = 0
for i in events2:
	interval2 += (i[0] - lst)
interval2 /= len(events2) - 1
print(interval2)
# Average testing time for every task
tasks = genTasks(minTestingTimeInSec = 5, maxTestingTimeInSec = 120, numberOfTasks = 13)
tasks = [6, 20, 50, 35, 30]
# Run models
launchModel(events = events1, tasks = tasks, queue = FifoQueue(numberJudges = 4))
launchModel(events = events1, tasks = tasks, queue = OnlyAskQueue(numberJudges = 4))
launchModel(events = events2, tasks = tasks, queue = FifoQueue(numberJudges = 4))
launchModel(events = events2, tasks = tasks, queue = OnlyAskQueue(numberJudges = 4))