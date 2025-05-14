# tests/test_scheduler.py
import pytest
from src.proceso import Proceso
from src.scheduler import FCFSScheduler, RoundRobinScheduler

def test_fcfs_scheduler():
    p1 = Proceso("P1", 10, 1)
    p2 = Proceso("P2", 5, 2)
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar([p1, p2])
    assert gantt == [("P1", 0, 10), ("P2", 10, 15)]

def test_round_robin_scheduler():
    p1 = Proceso("P1", 10, 1)
    p2 = Proceso("P2", 5, 2)
    scheduler = RoundRobinScheduler(quantum=3)
    gantt = scheduler.planificar([p1, p2])
    assert gantt == [("P1", 0, 3), ("P2", 3, 6), ("P1", 6, 9), ("P1", 9, 10), ("P2", 10, 12)]
    assert gantt == [("P1", 0, 3), ("P2", 3, 6), ("P1", 6, 9), ("P1", 9, 10), ("P2", 10, 12)]
    assert gantt == [("P1", 0, 3), ("P2", 3, 6), ("P1", 6, 9), ("P1", 9, 10), ("P2", 10, 12)]