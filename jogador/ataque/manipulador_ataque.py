class ManipuladorAtaque:
    def __init__(self, atacante, defensor, estrategia):
        self.atacante = atacante
        self.defensor = defensor
        self.estrategia = estrategia

    def execute_ataque(self, dados_atacante, dados_defensor):
        try:
            resultado = self.estrategia.atacar(self.atacante, self.defensor, dados_atacante, dados_defensor)
            return {"status": "sucesso", "mensagem": resultado}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
