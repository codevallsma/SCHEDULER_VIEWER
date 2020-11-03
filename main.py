import operator

import numpy as np
from Process import Process
from operator import attrgetter

from SchedulerAlgorithms import RoundRobin


def createClassList(data, limitRows):
    numberOfProcesses = data.__len__() / limitRows
    # empty list
    processes = np.split(np.array(data), numberOfProcesses)
    processesList = []
    for x in range(0, numberOfProcesses):
        currentArray = processes.__getitem__(x)
        if limitRows == 4:
            processClass = Process(currentArray.__getitem__(0), currentArray.__getitem__(1),
                                   currentArray.__getitem__(2), currentArray.__getitem__(3))
        else:
            processClass = Process(currentArray.__getitem__(0), currentArray.__getitem__(1),
                                   currentArray.__getitem__(2), None)
        processesList.append(processClass)
    processesList = sorted(processesList, key=attrgetter('petitonTime'), reverse=False)
    return processesList


def escullAlgoritme(processList):
    while True:
        print('Choose the algorithm:\n1. RoundRobin\n2. SF\nOption: ')
        option = str(input()).lower()

        if option == '1' or option == '2':
            break
        print('Input not correct, just write 1 or 2')

    if option == '1':
        print('Choose the quantum value: ')
        option = input()
        rr =RoundRobin(option, processList)
        rr.startRoundRobin()
        rr.printaTemps()

def read_dataset():
    """
    Show dataset's menu and read it
    """
    while True:
        print('Choose the dataset option:\n1. Amb prioritats\n2. Sense prioritats\nOption: ')
        option = str(input()).lower()

        if option == '1' or option == '2':
            break
        print('Input not correct, just write 1 or 2')

    fileObject = open("Data.txt", "r")
    data = fileObject.read().splitlines()

    if option == '1':
        return createClassList(data, 4), option
    else:
        return createClassList(data, 3), option


if __name__ == "__main__":
    processList, option = read_dataset()
    escullAlgoritme(processList)