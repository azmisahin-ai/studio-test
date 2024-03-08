# tests/test_fonksiyonlar.py

import unittest
from src.ana_modul.fonksiyonlar import welcome_message

class TestFonksiyonlar(unittest.TestCase):

    def test_welcome_message(self):
        result = welcome_message()
        self.assertEqual(result, "Merhaba, bu ana modülün fonksiyonlarından biri!")

if __name__ == '__main__':
    unittest.main()
