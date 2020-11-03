class Process(object):
    temps_Liurament = 0
    temps_Espera = 0
    temps_resposta = 0
    start_execute_time =0
    first_time = True

    def __init__(self, processName, petitonTime, cpuUsage, priority):
        # Assign the argument to the instance's name attribute
        self.processName = processName
        self.petitonTime = int(petitonTime)
        self.cpuUsage = int(cpuUsage)
        self.remainingCpuUsage = int(cpuUsage)
        if priority != None:
            self.priority = int(priority)
        else:
            self.priority = None

    def __lt__(self, other):
        if self.petitonTime == other.petitonTime:
            return self.remainingCpuUsage <= other.remainingCpuUsage
        else:
            return self.petitonTime <= other.petitonTime

    def __eq__(self, other):
        return self.remainingCpuUsage == other.remainingCpuUsage and self.petitonTime == other.petitonTime
