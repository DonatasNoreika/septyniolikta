from unittest import TestCase
from funkcijos import (skaiciu_suma,
                       saraso_suma,
                       didziausias_skaicius,
                       stringas_atbulai,
                       info_apie_sakini,
                       unikalus_sarasas,
                       ar_pirminis,
                       isrikiuoti_nuo_galo,
                       ar_keliamieji,
                       patikrinti_data)
import datetime


class TestFunkcijos(TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(56, skaiciu_suma(45, 5, 6))

    def test_saraso_suma(self):
        skaiciai = [45, 65, 25, 12]
        self.assertEqual(147, saraso_suma(skaiciai))

    def test_didziausias_skaicius(self):
        self.assertEqual(789, didziausias_skaicius(5, 8, 789, 94, 78))

    def test_stringas_atbulai(self):
        self.assertEqual("akieroN satanoD", stringas_atbulai("Donatas Noreika"))

    def test_info_apie_sakini(self):
        self.assertEqual("Žodžių: 6, didžiosios: 1, mažosios: 20, skaičiai: 3",
                         info_apie_sakini("Laba diena laba diena lab 522"))

    def test_unikalus_sarasas(self):
        self.assertEqual([4, 5, 'Labas', 6, True, 10], unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(11))
        self.assertFalse(ar_pirminis(12))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual("keturi trys du Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(1996))
        self.assertFalse(ar_keliamieji(2100))
        self.assertFalse(ar_keliamieji(1998))

    def test_patikrinti_data(self):
        now = datetime.datetime(2022, 9, 14, 12, 0, 0)
        lukestis1 = (22, 264, 1184, 8291, 199007.0, 11940467.0, 716428068)
        lukestis2 = (32, 384, 1696, 11874, 284999.0, 17099987.0, 1025999268)
        self.assertEqual(lukestis1, patikrinti_data("2000-01-01 12:12:12", now=now))
        self.assertEqual(lukestis2, patikrinti_data("1990-03-11 12:12:12", now=now))
