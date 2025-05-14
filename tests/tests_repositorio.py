# tests/test_repositorio.py
import pytest
from src.proceso import Proceso
from src.repositorio import RepositorioProcesos as repositori_procesos
from src.repositorio import RepositorioProcesos

def test_agregar_proceso():
    repo = RepositorioProcesos()
    p = Proceso("P1", 10, 1)
    repo.agregar_proceso(p)
    assert repo.obtener_proceso("P1") == p

def test_guardar_cargar_json():
    repo = RepositorioProcesos()
    p = Proceso("P1", 10, 1)
    repo.agregar_proceso(p)
    repo.guardar_json("procesos.json")
    repo.cargar_json("procesos.json")
    assert repo.obtener_proceso("P1").duracion == 10

