class Proceso:
    def __init__(self, pid: str, duracion: int, prioridad: int):
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_llegada = 0
        self.tiempo_inicio = None
        self.tiempo_fin = None

    def __repr__(self):
        return f"Proceso(pid={self.pid}, duracion={self.duracion}, prioridad={self.prioridad})"
