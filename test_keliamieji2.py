import unittest
from keliamieji2 import ar_keliamieji


class TestKeliamieji2(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(1996))
        self.assertFalse(ar_keliamieji(2100))
        self.assertFalse(ar_keliamieji(1998))
