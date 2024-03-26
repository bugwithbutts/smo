import numpy as np
import random
from fifo import FifoQueue
from onlyask import OnlyAskQueue
# from gen import genEvents, genTasks

def launchModel(events, tasks, queue):  

    nextEventIndex = 0
    # Iterate through seconds from first event to last
    for moment in range(events[0][0], events[-1][0] + 1): 
        # If some tasks were sent add it to the queue   
        while nextEventIndex != len(events) and events[nextEventIndex][0] == moment:
            # To first wrong testing or full-package testing
            if len(events[nextEventIndex]) != 2:
                queue.pushTests(testingTime = tasks[events[nextEventIndex][1]], moment = moment, testF = events[nextEventIndex][2], taskInd = events[nextEventIndex][1])
            else:
                queue.push(testingTime = tasks[events[nextEventIndex][1]], moment = moment)
            nextEventIndex += 1
        # Update queue
        queue.tact(moment)

    # Finish requests in queue
    moment = events[-1][0] + 1
    while not queue.empty():
        queue.tact(moment)
        moment += 1

    queue.printStatistic()
