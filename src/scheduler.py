from abc import ABC, abstractmethod
from typing import List, Tuple

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[object]) -> List[Tuple[str, int, int]]:
        pass
    