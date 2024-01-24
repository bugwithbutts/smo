import numpy as np
import random

def genEvents(eventsInSec, timeIntervalInSec, numberOfTasks):

    lastEventTime = 0
    events = []

    # Generate events in seconds
    while lastEventTime < timeIntervalInSec:
        # Interval between events is exponential distributed
        delta = np.random.exponential(scale = 1 / eventsInSec)
        lastEventTime += delta
        # Event = [time of event, number of task]
        events.append([int(lastEventTime), random.randrange(numberOfTasks)])        

    return events
  
def genTasks(minTestingTimeInSec, maxTestingTimeInSec, numberOfTasks):
    
    tasks = []
    for _ in range(0, numberOfTasks):
        tasks.append(random.randrange(minTestingTimeInSec, maxTestingTimeInSec + 1))

    return tasks