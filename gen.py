import numpy as np
import random

def genEvents(eventsInSec, timeIntervalInSec):

    lastEventTime = 0
    events = []

    # Generate events in santiseconds (1/100 of second)
    while lastEventTime < timeIntervalInSec * 100:
        # Interval between events is exponential distributed
        delta = np.random.exponential(scale = 100 / eventsInSec)
        lastEventTime += delta
        events.append(int(lastEventTime))        

    return events
  
def genTasks(minTestingTimeInSec, maxTestingTimeInSec, numberOfTasks):

    # From seconds to santiseconds
    minTestingTimeInSec *= 100
    maxTestingTimeInSec *= 100
    tasks = []
    for _ in range(0, numberOfTasks):
        tasks.append(random.randrange(minTestingTimeInSec, maxTestingTimeInSec + 1))

    return tasks