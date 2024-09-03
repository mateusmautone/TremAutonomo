import unittest
from controle_trem import TremAutonomo 

class TestTremAutonomo(unittest.TestCase):
    def setUp(self):
        self.trem = TremAutonomo()

    def test_movimento_basico(self):
        self.assertEqual(self.trem.mover(["DIREITA", "DIREITA"]), "Movimento concluído. Posição final: 2")

    def test_movimento_limite(self):
        self.assertEqual(self.trem.mover(["DIREITA"] * 50), "Limite de movimentos atingido. Posição final: 50")

    def test_movimento_consecutivo_excedido(self):
        self.assertEqual(self.trem.mover(["ESQUERDA"] * 21), "Erro: Mais de 20 movimentos consecutivos na mesma direção. Posição final: -20")

    def test_comando_invalido(self):
        self.assertEqual(self.trem.mover(["AVANCAR"]), "Erro: Comando inválido.")


if __name__ == "__main__":
    unittest.main()
