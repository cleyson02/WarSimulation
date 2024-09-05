class Jogador:
    def __init__(self, cor, objetivo, territorio):
        self.cor = cor
        self.objetivo = objetivo
        self.territorio = territorio
    
    def get_cor(self):
        return self.cor
    def get_objetivo(self):
        return self.objetivo
    def get_territorio(self):
        return self.territorio
    def get_id(self):
        return self.id