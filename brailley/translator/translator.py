from abc import ABC, abstractmethod
from typing import Any


class Translator(ABC):
    @abstractmethod
    def translate(self, input: Any) -> Any:
        pass
