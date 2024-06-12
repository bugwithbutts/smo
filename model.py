import numpy as np
import random
from fifo import FifoQueue
from onlyask import OnlyAskQueue
# from gen import genEvents, genTasks
from copy import deepcopy

def launchModel(events, queue): 
    q = deepcopy(queue) 
    nextEventIndex = 0
    # Iterate through seconds from first event to last
    for moment in range(0, 5 * 60 * 60 + 1): 
        # If some tasks were sent add it to the queue   
        while nextEventIndex != len(events) and events[nextEventIndex].time == moment:
            q.push(events[nextEventIndex])
            nextEventIndex += 1
        # Update queue
        q.tact(moment)

    # Finish requests in queue
    moment = 5 * 60 * 60 + 1
    while not q.empty():
        q.tact(moment)
        moment += 1

    # q.printStatistic()
    return q
