import numpy as np
import random

def genEvents(eventsInSec, timeIntervalInSec):

    lastEventTime = 0
    events = []

    # Generate events in santiseconds (1/100 of second)
    while lastEventTime < timeIntervalInSec * 100:
        # Interval between events is exponential distributed
        delta = np.random.exponential(scale = 1 / eventsInSec * 100)
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

class Queue(object):

    # Queue of waiting requests. Element is [time for testing, moment when added]
    queue = []

    # Waiting times of all requests
    waitTimes = []

    # Time needed to finish processed request for every judge
    remainTimeOnJudge = []

    # Time when request processed on judge was added to queue
    startWaiting = []

    numberJudges = 0

    def __init__(self, numberJudges):
        self.numberJudges = numberJudges
        self.remainTimeOnJudge = [0 for _ in range(numberJudges)]
        self.startWaiting = [None for _ in range(numberJudges)] 

    def tact(self, moment):       

        # Iterate through judges 
        for judge in range(self.numberJudges):

            if self.remainTimeOnJudge[judge] > 0:
                self.remainTimeOnJudge[judge] -= 1

            if self.remainTimeOnJudge[judge] == 0:
                
                # Add waiting time when request has been finished
                if self.startWaiting[judge] != None:                    
                    self.waitTimes.append(moment - self.startWaiting[judge])
                    self.startWaiting[judge] = None

                # Begin process new request
                if len(self.queue) > 0:
                    self.remainTimeOnJudge[judge] = self.queue[0][0]
                    self.startWaiting[judge] = self.queue[0][1]                 
                    self.queue.pop(0)

    def push(self, testingTime, moment):        
        self.queue.append([testingTime, moment])

    def getMeanWaitTime(self):           
        return np.mean(self.waitTimes)

    def empty(self):        
        return len(self.queue) != 0 or max(self.remainTimeOnJudge) == 0

def launchModel(events, tasks, numberJudges):  

    # Queue include queue of requests and judges 
    queue = Queue(numberJudges = numberJudges)

    nextEventIndex = 0

    # Iterate through santiseconds(1/100 of second) from first event to last
    for moment in range(events[0], events[-1] + 1): 

        # If some task was sent add it to the queue   
        if nextEventIndex != len(events) and events[nextEventIndex] == moment:            
            queue.push(testingTime = tasks[random.randrange(len(tasks))], moment = moment)
            nextEventIndex += 1

        # Update queue
        queue.tact(moment)

    # Finish requests in queue
    moment = events[-1] + 1
    while not queue.empty():
        queue.tact(moment)
        moment += 1

    return queue.getMeanWaitTime()

# Moments of time when tasks were sent
events = genEvents(eventsInSec = 0.01, timeIntervalInSec = 5 * 60 * 60)

# Average time for task for every task
tasks = genTasks(minTestingTimeInSec = 5, maxTestingTimeInSec = 500, numberOfTasks = 13)

# Run model
expectedWaitTime = launchModel(events = events, tasks = tasks, numberJudges = 4)

# Print in minutes
print(expectedWaitTime / 100 / 60)