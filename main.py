import numpy as np
import random
import string
from fifo import FifoQueue
from onlyask import OnlyAskQueue
from gen import genEvents, genTasks
from model import launchModel
from testbytest import TestByTestQueue
from probtest import ProbTestQueue
from sorttest import SortTestQueue
from maxfirst import MaxFirstQueue
# Parametrs of contest
eventsInSec = 1 / 30
numberOfTasks = 13
eps = 0

# Generating events
events1 = genEvents(eventsInSec = eventsInSec, timeIntervalInSec = 3 * 60 * 60, numberOfTasks = numberOfTasks)

events2 = []
file = open('parsed_data/parsed_2019', 'r')
for i in file.readlines():
	events2.append([int(i[:-1]), random.randrange(5)])
file.close()
events2 = events2[200:600]

events3 = []
file = open('parsed_data/parsed_ptz', 'r')
lastEventTime = 0
for i in file.readlines():
	data = i.split(' ')
	delta = np.random.exponential(scale = 1 / eventsInSec)
	lastEventTime += delta
	events3.append([int(lastEventTime), string.ascii_uppercase.index(data[0]), int(data[1][:-1])])
file.close()

# Generating average testing times for full-package testing
tasks = genTasks(minTestingTimeInSec = 5, maxTestingTimeInSec = 120, numberOfTasks = numberOfTasks)
tasks1 = [6, 20, 50, 35, 30]
# Times for test-by-test testing
tasks2 = [[1 for _ in range(6)], [2 for _ in range(10)], [2 for _ in range(25)], [5 for _ in range(7)], [1 for _ in range(30)]]
tasks3 = [[2 for _ in range(18)], [2 for _ in range(18)], [1 for _ in range(1)], [2 for _ in range(36)], [2 for _ in range(45)], [2 for _ in range(38)], [2 for _ in range(32)], [2 for _ in range(45)], [2 for _ in range(156)], [5 for _ in range(47)], [8 for _ in range(80)], [4 for _ in range(90)], [2 for _ in range(39)]]

# Run models
# launchModel(events = events1, tasks = tasks1, queue = FifoQueue(numberJudges = 4, eps = eps))
# launchModel(events = events1, tasks = tasks1, queue = OnlyAskQueue(numberJudges = 4, eps = eps))
# launchModel(events = events1, tasks = tasks1, queue = MaxFirstQueue(numberJudges = 4, eps = eps))
# launchModel(events = events1, tasks = tasks2, queue = TestByTestQueue(numberJudges = 4, eps = eps))
# launchModel(events = events1, tasks = tasks2, queue = BigTestFirstQueue(numberJudges = 4))


# launchModel(events = events2, tasks = tasks1, queue = FifoQueue(numberJudges = 4))
# launchModel(events = events2, tasks = tasks1, queue = OnlyAskQueue(numberJudges = 4))
# launchModel(events = events2, tasks = tasks2, queue = TestByTestQueue(numberJudges = 4))
# launchModel(events = events2, tasks = tasks2, queue = BigTestFirstQueue(numberJudges = 4))

launchModel(events = events3, tasks = tasks3, queue = TestByTestQueue(numberJudges = 4, eps = eps))
launchModel(events = events3, tasks = tasks3, queue = ProbTestQueue(numberJudges = 4, tasks = tasks3, eps = eps))
launchModel(events = events3, tasks = tasks3, queue = SortTestQueue(numberJudges = 4, tasks = tasks3, eps = eps))
