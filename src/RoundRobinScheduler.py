from typing import List, Tuple

class Scheduler:
    pass  

class proceso:
    def __init__(self, pid: str, tiempo_restante: int):
        self.pid = pid
        self.tiempo_restante = tiempo_restante

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        self.quantum = quantum

    def planificar(self, procesos: List[proceso]) -> List[Tuple[str, int, int]]:
        tiempo_actual = 0
        gantt = []
        cola = procesos[:]
        while cola:
            proceso = cola.pop(0)
            if proceso.tiempo_restante > self.quantum:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + self.quantum))
                tiempo_actual += self.quantum
                proceso.tiempo_restante -= self.quantum
                cola.append(proceso)
            else:
                gantt.append((proceso.pid, tiempo_actual, tiempo_actual + proceso.tiempo_restante))
                tiempo_actual += proceso.tiempo_restante
                proceso.tiempo_restante = 0
        return gantt
