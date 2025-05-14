# tests/test_metrics.py
import pytest
from src.proceso import Proceso
from src.metrics import calcular_metricas

def test_calcular_metricas():
    p1 = Proceso("P1", 10, 1)
    p2 = Proceso("P2", 5, 2)
    gantt = [("P1", 0, 10), ("P2", 10, 15)]
    metrics = calcular_metricas(gantt, [p1, p2])
    assert metrics['tiempo_respuesta_medio'] == 0
    assert metrics['tiempo_espera_medio'] == 5
    assert metrics['tiempo_retorno_medio'] == 12.5
