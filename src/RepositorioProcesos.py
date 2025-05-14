import json
import csv

class Proceso:
    def __init__(self, pid: str, duracion: int, prioridad: int):
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso):
        if proceso.pid in self.procesos:
            raise ValueError("PID duplicado")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self):
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str):
        if pid in self.procesos:
            del self.procesos[pid]

    def obtener_proceso(self, pid: str):
        return self.procesos.get(pid)

    def guardar_json(self, archivo: str):
        with open(archivo, 'w') as f:
            json.dump([proceso.__dict__ for proceso in self.procesos.values()], f)

    def cargar_json(self, archivo: str):
        with open(archivo, 'r') as f:
            procesos = json.load(f)
            self.procesos = {p['pid']: Proceso(**p) for p in procesos}

    def guardar_csv(self, archivo: str):
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad'])
            for proceso in self.procesos.values():
                writer.writerow([proceso.pid, proceso.duracion, proceso.prioridad])

    def cargar_csv(self, archivo: str):
        with open(archivo, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.procesos = {row['pid']: Proceso(row['pid'], int(row['duracion']), int(row['prioridad'])) for row in reader}
