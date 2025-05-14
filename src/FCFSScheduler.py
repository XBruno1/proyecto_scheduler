from typing import List, Tuple
from scheduler import Scheduler
from proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[Tuple[str, int, int]]:
        tiempo_actual = 0
        gantt = []
        for proceso in sorted(procesos, key=lambda p: p.tiempo_llegada):
            proceso.tiempo_inicio = tiempo_actual
            proceso.tiempo_fin = tiempo_actual + proceso.duracion
            gantt.append((proceso.pid, proceso.tiempo_inicio, proceso.tiempo_fin))
            tiempo_actual += proceso.duracion
        return gantt