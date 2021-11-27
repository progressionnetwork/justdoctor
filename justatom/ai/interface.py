import abc
from typing import List, Dict


class AI(abc.ABC):
    @abc.abstractmethod
    def predict(self, txt: str, **kwargs) -> List[Dict]:
        pass
