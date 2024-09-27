from abc import ABC, abstractmethod

class AtaqueStrategy(ABC):
    @abstractmethod
    def atacar(self, atacante, defensor, dados_atacante, dados_defensor):
        pass
