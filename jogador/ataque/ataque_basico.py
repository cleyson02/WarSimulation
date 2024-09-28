from jogador.ataque.ataque_strategy import AtaqueStrategy

class AtaqueBasico(AtaqueStrategy):
    def atacar(self, atacante, defensor, dados_atacante, dados_defensor):
        if not (1 <= dados_atacante <= 6) or not (1 <= dados_defensor <= 6):
            raise ValueError("Dados devem estar entre 1 e 6")

        if dados_atacante > dados_defensor:
            self.vitoria_atacante(atacante, defensor)
            return "Atacante ganhou"
        else:
            self.vitoria_defensor(defensor)
            return "Defensor ganhou"

    def vitoria_atacante(self, atacante, defensor):
        pass

    def vitoria_defensor(self, defensor):
        pass