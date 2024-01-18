import numpy as np
import random
from fifo import FifoQueue
from onlyask import OnlyAskQueue
from gen import genEvents, genTasks
from model import launchModel

# Moments of time when tasks were sent
events = genEvents(eventsInSec = 0.01, timeIntervalInSec = 5 * 60 * 60, numberOfTasks = 13)

# Average testing time for every task
tasks = genTasks(minTestingTimeInSec = 5, maxTestingTimeInSec = 200, numberOfTasks = 13)

# Run models
expectedWaitTime1 = launchModel(events = events, tasks = tasks, queue = FifoQueue(numberJudges = 4))
expectedWaitTime2 = launchModel(events = events, tasks = tasks, queue = OnlyAskQueue(numberJudges = 4))

# Print in minutes
print("Average fifo time: ", expectedWaitTime1 / 100 / 60)
print("Average only ask time: ", expectedWaitTime2 / 100 / 60)