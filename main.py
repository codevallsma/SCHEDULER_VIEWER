# coding=utf-8
import numpy as np
from Process import Process, ProcessPriority, ProcessSRT
from operator import attrgetter

from SchedulerAlgorithms import RoundRobin, ShortestRemainingTimeOrPriority


def createClassList(data, limitRows, subclass=False):
    numberOfProcesses = data.__len__() / limitRows
    # empty list
    processes = np.split(np.array(data), numberOfProcesses)
    processesList = []
    petitionTimes = []
    for x in range(0, numberOfProcesses):
        currentArray = processes.__getitem__(x)
        petitionTimes.append(int(currentArray.__getitem__(1)))
        if limitRows == 4:
            processClass = ProcessPriority(currentArray.__getitem__(0), currentArray.__getitem__(1),
                                           currentArray.__getitem__(2), currentArray.__getitem__(3))
        else:
            if subclass:
                processClass = ProcessSRT(currentArray.__getitem__(0), currentArray.__getitem__(1),
                                          currentArray.__getitem__(2), None)
            else:
                processClass = Process(currentArray.__getitem__(0), currentArray.__getitem__(1),
                                       currentArray.__getitem__(2), None)
        processesList.append(processClass)
    processesList = sorted(processesList, key=attrgetter('petitionTime'), reverse=False)
    return processesList, petitionTimes


def chooseMenu(string, beginning, end):
    while True:
        print(string)
        option = input()
        if beginning <= option <= end:
            return option
        print ('Input not correct, just write ' + str(beginning) + ' or ' + str(end) + '\n')


def escullAlgoritme():
    option = chooseMenu(
        'Choose the algorithm:\n1. RoundRobin\n2. Preemptive priotity algorithm (La prioritat més alta correspon al '
        'número més baix.)\n3. Shortest Remaining Time\nOption: ', 1, 3)
    # reading the data file
    fileObject = open("Data.txt", "r")
    data = fileObject.read().splitlines()

    if option == 1:
        # round robin
        print('Choose the quantum value: ')
        option = input()
        processList, petitionTimes = createClassList(data, 3)
        rr = RoundRobin(option, processList)
        rr.startRoundRobin()
        rr.printaTemps()
    elif option == 2:
        processList, petitionTimes = createClassList(data, 4, True)
        srt = ShortestRemainingTimeOrPriority(processList, petitionTimes, "startPriorityAlgortithm.xlsx")
        srt.startShortestRemainingTimeOrPriority()
        srt.printaTemps()
    elif option == 3:
        processList, petitionTimes = createClassList(data, 3, True)
        srt = ShortestRemainingTimeOrPriority(processList, petitionTimes, "startShortestRemainingTime.xlsx")
        srt.startShortestRemainingTimeOrPriority()
        srt.printaTemps()
    print "File created!\n"


if __name__ == "__main__":
    escullAlgoritme()
