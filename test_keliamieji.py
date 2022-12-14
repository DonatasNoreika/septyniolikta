import unittest
from keliamieji import ar_keliamieji


class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji(self):
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
        self.assertEqual("Keliamieji", ar_keliamieji(1996))
        self.assertEqual("Nekeliamieji", ar_keliamieji(2100))
        self.assertEqual("Nekeliamieji", ar_keliamieji(1998))


if __name__ == "__main__":
    unittest.main()
