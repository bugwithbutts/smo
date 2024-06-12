import numpy as np
import random
import string
from fifo import FifoQueue
from onlyask import OnlyAskQueue
from model import launchModel
from testbytest import TestByTestQueue
from probtest import ProbTestQueue
from sorttest import SortTestQueue
from maxfirst import MaxFirstQueue
from events import Event
import matplotlib.pyplot as plt
from compare import compareQueues

# Generating events
def genEvents1(ev_in_sec):
	tasks = [[1, 6], [2, 10], [2, 25], [5, 7], [1, 30]]
	events1 = []
	lastEventTime = 0
	while lastEventTime <= 60 * 60:
		delta = np.random.exponential(scale = 1 / ev_in_sec)
		lastEventTime += delta
		rnd = random.randrange(5)
		events1.append(Event(time=int(lastEventTime), numberTests=tasks[rnd][1], tl = tasks[rnd][0], letter = rnd, wa=0))
	return events1

def genEvents2():
	tasks = [[1, 6], [2, 10], [2, 25], [5, 7], [1, 30]]
	events2 = []
	file = open('parsed_data/parsed_2019', 'r')
	for i in file.readlines():
		rnd = random.randrange(5)
		events2.append(Event(time=int(i[:-1]), numberTests=1, letter = rnd, tl=tasks[rnd]))
	file.close()
	return events2

def genEvents3(ev_in_sec):
	tasks = [[2, 18], [2, 18], [1, 1], [2, 36], [2, 45], [2, 38], [2, 32], [2, 45], [2, 156], [5, 47], [8, 80], [4, 90], [2, 39]]
	events3 = []
	file = open('parsed_data/parsed_ptz', 'r')
	lastEventTime = 0
	for i in file.readlines():
		data = i.split(' ')
		delta = np.random.exponential(scale = 1 / ev_in_sec)
		lastEventTime += delta
		tsk = string.ascii_uppercase.index(data[0])
		events3.append(Event(time=int(lastEventTime), numberTests=tasks[tsk][1], wa = int(data[1][:-1]), tl = tasks[tsk][0], letter = tsk))
	file.close()
	return events3
# events1 = genEvents1(1 / 10)
# launchModel(events=events1, queue=FifoQueue(numberJudges = 4)).printStatistic()
# launchModel(events=events1, queue=OnlQueue(numberJudges = 4)).printStatistic()
compareQueues(FifoQueue(numberJudges = 4), TestByTestQueue(numberJudges = 4), genEvents1)