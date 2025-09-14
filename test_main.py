import unittest
from src.main import saludar

class TestMain(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(saludar("ChatGPT"), "Hola, ChatGPT!")

if __name__ == "__main__":
    unittest.main()
