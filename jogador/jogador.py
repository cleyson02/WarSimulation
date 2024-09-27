from pydantic import BaseModel
from jogador.ataque.ataque_strategy import AtaqueStrategy

class Jogador:
    def __init__(self, id, cor, objetivo, territorio, posicao, qtd_exercito):
        self.id = id
        self.cor = cor
        self.objetivo = objetivo
        self.territorio = territorio
        self.posicao = posicao
        self.qtd_exercito = qtd_exercito

    def get_cor(self):
        return self.cor
    
    def get_objetivo(self):
        return self.objetivo
    
    def get_territorio(self):
        return self.territorio
    
    def get_id(self):
        return self.id
    
    def get_posicao(self):
        return self.posicao
    
    def get_qtd_exercito(self):
        return self.qtd_exercito
    
    def set_posicao(self,lugar):
        self.posicao = lugar
        
    def set_ataque_strategy(self, strategy):
        self.ataque_strategy = strategy

    def atacar(self, defensor, dados_atacante, dados_defensor):
        if self.ataque_strategy:
            self.ataque_strategy.atacar(self, defensor, dados_atacante, dados_defensor)
        else:
            raise Exception("Estratégia de ataque não definida")