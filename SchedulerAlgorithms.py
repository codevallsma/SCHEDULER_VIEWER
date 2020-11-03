import heapq
import shutil
from Queue import PriorityQueue, Queue

from excel import ExcelPainter
from Process import Process


class Algorithms:

    def __init__(self):
        pass


class ShortestRemainingTime:
    inService = PriorityQueue()
    results = []

    def __init__(self, processes, petitionTimes):
        shutil.copy("Plantilla_scheduling .xlsx", "startShortestRemainingTime.xlsx")
        self.excelPainter = ExcelPainter("startShortestRemainingTime.xlsx", 9, 2)
        for pr in processes:
            self.excelPainter.saveValue(ord(pr.processName) - ord('A') + 17, 1, pr.processName)
            self.excelPainter.saveValue(ord(pr.processName) - ord('A') + 9, 1, pr.processName)
        self.processList = processes
        self.petitionTimes = petitionTimes

    def startShortestRemainingTime(self):
        global diferencia
        time = 0
        self.inService.put(self.processList.__getitem__(0))
        self.processList.pop(0)
        results = []
        index = 0
        while self.inService.empty() is False:
            currentProcess = self.inService.get()
            timeStart = time
            if self.processList:
                if currentProcess.first_time:
                    index += 1
                    diferencia = abs(time - self.petitionTimes[index])
                else:
                    diferencia = currentProcess.remainingCpuUsage

            print currentProcess.processName + " is in execution"

            # the process has ended?
            if currentProcess.remainingCpuUsage - diferencia <= 0:
                # yes
                results.append(currentProcess)
                time += currentProcess.remainingCpuUsage
                if self.processList:
                    if self.processList.__getitem__(0).petitionTime <= time:
                        self.inService.put(self.processList.__getitem__(0))
                        self.processList.pop(0)
            else:
                # no
                time += diferencia
                currentProcess.remainingCpuUsage -= diferencia
                if self.processList:
                    self.inService.put(self.processList.__getitem__(0))
                    self.inService.put(currentProcess)
                    self.processList.pop(0)
                else:
                    self.inService.put(currentProcess)

            if currentProcess.first_time:
                currentProcess.start_execute_time = timeStart
                currentProcess.temps_resposta = timeStart - currentProcess.petitionTime
                currentProcess.first_time = False

            currentProcess.temps_Espera = (time - currentProcess.petitionTime) - currentProcess.cpuUsage
            currentProcess.temps_Liurament = (time - currentProcess.petitionTime)

            print 'Temps de lliurament = ' + str(currentProcess.temps_Liurament)
            print 'Temps de espera = ' + str(currentProcess.temps_Espera)
            print 'Temps de resposta = ' + str(currentProcess.temps_resposta)
            print 'from ' + str(timeStart) + ' to ' + str(time) + '\n'
            self.excelPainter.paintCells(timeStart, time, ord(currentProcess.processName) - ord('A'))
        self.results = results

    def printaTemps(self):
        for res in self.results:
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 2, str(res.temps_resposta))
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 4, str(res.temps_Espera))
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 6, str(res.temps_Liurament))

        self.excelPainter.saveFile()


class RoundRobin:
    inService = Queue()
    results = []

    def __init__(self, quantum, processes):
        shutil.copy("Plantilla_scheduling .xlsx", "startRoundRobin.xlsx")
        self.excelPainter = ExcelPainter("startRoundRobin.xlsx", 9, 2)
        for pr in processes:
            self.excelPainter.saveValue(ord(pr.processName) - ord('A') + 17, 1, pr.processName)
            self.excelPainter.saveValue(ord(pr.processName) - ord('A') + 9, 1, pr.processName)
        self.quantum = quantum
        self.processList = processes

    def startRoundRobin(self):
        time = 0
        self.inService.put(self.processList.__getitem__(0))
        self.processList.pop(0)
        results = []
        while self.inService.empty() is False:
            currentProcess = self.inService.get()
            timeStart = time
            print currentProcess.processName + " is in execution"
            # the process has ended?

            if currentProcess.remainingCpuUsage - self.quantum <= 0:
                # yes
                results.append(currentProcess)
                time += currentProcess.remainingCpuUsage
                if self.processList:
                    if self.processList.__getitem__(0).petitionTime <= time:
                        self.inService.put(self.processList.__getitem__(0))
                        self.processList.pop(0)
            else:
                # no
                time += self.quantum
                currentProcess.remainingCpuUsage -= self.quantum
                if self.processList:
                    if self.processList.__getitem__(0).petitionTime <= time:
                        self.inService.put(self.processList.__getitem__(0))
                        self.inService.put(currentProcess)
                    else:
                        self.inService.put(currentProcess)
                        self.inService.put(self.processList.__getitem__(0))
                    self.processList.pop(0)
                else:
                    self.inService.put(currentProcess)

            if currentProcess.first_time:
                currentProcess.start_execute_time = timeStart
                currentProcess.temps_resposta = timeStart - currentProcess.petitionTime
                currentProcess.first_time = False

            currentProcess.temps_Espera = (time - currentProcess.petitionTime) - currentProcess.cpuUsage
            currentProcess.temps_Liurament = (time - currentProcess.petitionTime)

            print 'Temps de lliurament = ' + str(currentProcess.temps_Liurament)
            print 'Temps de espera = ' + str(currentProcess.temps_Espera)
            print 'Temps de resposta = ' + str(currentProcess.temps_resposta)
            print 'from ' + str(timeStart) + ' to ' + str(time) + '\n'
            self.excelPainter.paintCells(timeStart, time, ord(currentProcess.processName) - ord('A'))
        self.results = results

    def printaTemps(self):
        for res in self.results:
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 2, str(res.temps_resposta))
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 4, str(res.temps_Espera))
            self.excelPainter.saveValue(ord(res.processName) - ord('A') + 17, 6, str(res.temps_Liurament))

        self.excelPainter.saveFile()
