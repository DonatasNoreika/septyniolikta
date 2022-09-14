import unittest
from keliamieji3 import Keliamieji


class TestKeliamieji3(unittest.TestCase):
    def setUp(self):
        self.keliamieji1 = Keliamieji()

    def test_tikrinti(self):
        self.assertTrue(self.keliamieji1.tikrinti(2000))
        self.assertTrue(self.keliamieji1.tikrinti(1996))
        self.assertFalse(self.keliamieji1.tikrinti(2100))
        self.assertFalse(self.keliamieji1.tikrinti(1998))

    def test_diapazonas(self):
        rezultatas = self.keliamieji1.diapazonas(1980, 2001)
        lukestis = [1980, 1984, 1988, 1992, 1996, 2000]
        self.assertEqual(lukestis, rezultatas)
