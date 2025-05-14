from typing import List, Tuple

class Proceso:
    def __init__(self, pid: str, tiempo_llegada: int, duracion: int):
        self.pid = pid
        self.tiempo_llegada = tiempo_llegada
        self.duracion = duracion

def calcular_metricas(gantt: List[Tuple[str, int, int]], procesos: List[Proceso]):
    tiempos_respuesta = []
    tiempos_espera = []
    tiempos_retorno = []

    for pid, inicio, fin in gantt:
        proceso = next(p for p in procesos if p.pid == pid)
        tiempo_respuesta = inicio - proceso.tiempo_llegada
        tiempo_retorno = fin - proceso.tiempo_llegada
        tiempo_espera = tiempo_retorno - proceso.duracion

        tiempos_respuesta.append(tiempo_respuesta)
        tiempos_espera.append(tiempo_espera)
        tiempos_retorno.append(tiempo_retorno)

    return {
        'tiempo_respuesta_medio': sum(tiempos_respuesta) / len(tiempos_respuesta),
        'tiempo_espera_medio': sum(tiempos_espera) / len(tiempos_espera),
        'tiempo_retorno_medio': sum(tiempos_retorno) / len(tiempos_retorno),
    }
