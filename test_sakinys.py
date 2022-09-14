from unittest import TestCase
import sakinys


class TestSakinys(TestCase):
    def setUp(self) -> None:
        self.objektas = sakinys.Sakinys("Laba diena, Lietuva")

    def test_atbulai(self):
        self.assertEqual("avuteiL ,aneid abaL", self.objektas.atbulai())

    def test_didziosiomis(self):
        self.assertEqual("LABA DIENA, LIETUVA", self.objektas.didziosiomis())

    def test_mazosiomis(self):
        self.assertEqual("laba diena, lietuva", self.objektas.mazosiomis())

    def test_ieskoti(self):
        self.assertEqual(4, self.objektas.ieskoti("a"))

    def test_pakeisti(self):
        self.assertEqual("Lbbb dienb, Lietuvb", self.objektas.pakeisti("a", "b"))

    def test_atspausdinti_zodi(self):
        self.assertEqual("diena,", self.objektas.atspausdinti_zodi(1))

    def test_info(self):
        self.assertEqual("Žodžių kiekis: 3, Skaičiai: 0, Didžiosios: 2, Mažosios: 14", self.objektas.info())
