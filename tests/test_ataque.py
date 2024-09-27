import unittest
from jogador.jogador import Jogador
from jogador.ataque.ataque_basico import AtaqueBasico

class TestAtaque(unittest.TestCase):
    def test_ataque_basico(self):
        atacante = Jogador(1, 'Vermelha', 'Conquistar', [], 1, 10)
        defensor = Jogador(2, 'Azul', 'Defender', [], 2, 5)
        atacante.set_ataque_strategy(AtaqueBasico())
        atacante.atacar(defensor, 3, 2)

if __name__ == '__main__':
    unittest.main()
