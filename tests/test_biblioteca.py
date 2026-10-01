import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from biblioteca import mensaje_bienvenida


class TestBiblioteca(unittest.TestCase):
    def test_mensaje_bienvenida(self):
        self.assertEqual(mensaje_bienvenida(), "Bienvenido a BibliotecaFP")


if __name__ == "__main__":
    unittest.main()
