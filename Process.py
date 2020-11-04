class Process(object):
    temps_Liurament = 0
    temps_Espera = 0
    temps_resposta = 0
    start_execute_time = 0
    first_time = True

    def __init__(self, processName, petitionTime, cpuUsage, priority):
        # Assign the argument to the instance's name attribute
        self.processName = processName
        self.petitionTime = int(petitionTime)
        self.cpuUsage = int(cpuUsage)
        self.remainingCpuUsage = int(cpuUsage)
        if priority != None:
            self.priority = int(priority)
        else:
            self.priority = None

    def __lt__(self, other):
        if self.petitionTime == other.petitionTime:
            return self.remainingCpuUsage <= other.remainingCpuUsage
        else:
            return self.petitionTime <= other.petitionTime

    def __eq__(self, other):
        return self.remainingCpuUsage == other.remainingCpuUsage and self.petitionTime == other.petitionTime


class ProcessPriority(Process):
    def __init__(self, processName, petitionTime, cpuUsage, priority):
        super(ProcessPriority, self).__init__(processName, petitionTime, cpuUsage, priority)

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.processName < other.processName
        return self.priority < other.priority


class ProcessSRT(Process):
    def __init__(self, processName, petitionTime, cpuUsage, priority):
        super(ProcessSRT, self).__init__(processName, petitionTime, cpuUsage, priority)

    def __lt__(self, other):
        return self.remainingCpuUsage < other.remainingCpuUsage
