# tests/test_text_to_image.py

import unittest
from PIL import Image
from lib.metin_donusturucu.text_to_image import text_to_image

class TestTextToImage(unittest.TestCase):

    def test_text_to_image(self):
        text = "Hello, World!"
        output_path = 'test_output_image.png'

        # Çağırdığımız fonksiyonu test ediyoruz
        text_to_image(text, output_path)

        # Oluşturulan resmi kontrol ediyoruz
        with Image.open(output_path) as image:
            width, height = image.size
            self.assertEqual(width, 500)  # Örnek değer, gerçek değeri projenize göre ayarlayın
            self.assertEqual(height, 500)  # Örnek değer, gerçek değeri projenize göre ayarlayın

        # Test sonrasında oluşturulan dosyayı silelim
        import os
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
