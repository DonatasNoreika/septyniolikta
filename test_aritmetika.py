import unittest
from aritmetika import (sudetis, atimtis, dalyba, daugyba)


class TestAritmetika(unittest.TestCase):
    def test_sudetis(self):
        self.assertEqual(10, sudetis(5, 5))
        self.assertEqual(0, sudetis(-1, 1))
        self.assertEqual(-8, sudetis(-3, -5))

    def test_atimtis(self):
        self.assertEqual(5, atimtis(10, 5))
        self.assertEqual(-6, atimtis(-5, 1))
        self.assertEqual(-1, atimtis(-4, -3))

    def test_daugyba(self):
        self.assertEqual(50, daugyba(10, 5))
        self.assertEqual(-1, daugyba(-1, 1))
        self.assertEqual(1, daugyba(-1, -1))

    def test_dalyba(self):
        self.assertEqual(2, dalyba(10, 5))
        self.assertEqual(-1, dalyba(-1, 1))
        self.assertEqual(1, dalyba(-1, -1))
        self.assertEqual(2.5, dalyba(5, 2))
        # self.assertRaises(ZeroDivisionError, dalyba, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            dalyba(10, 0)
