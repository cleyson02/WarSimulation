import unittest
from jogador.ataque.ataque_basico import AtaqueBasico
from jogador.jogador import Jogador
from jogador.ataque.manipulador_ataque import ManipuladorAtaque

class TestAtaque(unittest.TestCase):

    def setUp(self):
        self.atacante = Jogador(1, "AZUL", "objetivo", "territorio", "posicao", 5)
        self.defensor = Jogador(2, "VERMELHO", "objetivo", "territorio", "posicao", 3)
        self.ataque = AtaqueBasico()

    def test_atacar_atacante_ganha(self):
        resultado = self.ataque.atacar(self.atacante, self.defensor, 5, 3)
        self.assertEqual(resultado, "Atacante ganhou")

    def test_atacar_defensor_ganha(self):
        resultado = self.ataque.atacar(self.atacante, self.defensor, 2, 4)
        self.assertEqual(resultado, "Defensor ganhou")

    def test_atacar_dados_invalidos(self):
        with self.assertRaises(ValueError) as context:
            self.ataque.atacar(self.atacante, self.defensor, 7, 3)
        self.assertEqual(str(context.exception), "Dados devem estar entre 1 e 6")

        with self.assertRaises(ValueError) as context:
            self.ataque.atacar(self.atacante, self.defensor, 5, 0)
        self.assertEqual(str(context.exception), "Dados devem estar entre 1 e 6")

    def test_manipulador_ataque_success(self):
        manipulador = ManipuladorAtaque(self.atacante, self.defensor, self.ataque)
        resultado = manipulador.execute_ataque(5, 3)
        self.assertEqual(resultado["status"], "sucesso")
        self.assertEqual(resultado["mensagem"], "Atacante ganhou")

    def test_manipulador_ataque_error(self):
        manipulador = ManipuladorAtaque(self.atacante, self.defensor, self.ataque)
        resultado = manipulador.execute_ataque(7, 3)
        self.assertEqual(resultado["status"], "erro")
        self.assertIn("Dados devem estar entre 1 e 6", resultado["mensagem"])

if __name__ == "__main__":
    unittest.main()