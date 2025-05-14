import pytest
from src.proceso import Proceso

def test_creacion_proceso():
    p = Proceso("P1", 10, 1)
    assert p.pid == "P1"
    assert p.duracion == 10
    assert p.prioridad == 1