# tests/test_ana_modul.py

import unittest
from PIL import Image
from io import BytesIO
from src.ana_modul.fonksiyonlar import create_image

class TestAnaModul(unittest.TestCase):

    def test_create_image(self):
        # Test için kullanılacak parametreler
        test_params = {
            'prompt': 'Test Prompt',
            'style': 'Test Style',
            'negative_prompt': 'Test Negative Prompt',
            'output_type': 'Test Output Type',
            'num_inference_steps': 15,
            'guidance_scale': 0.8,
            'lcm_origin_steps': 8,
            'width': 800,
            'height': 600
        }

        # create_image fonksiyonunu test et
        result_image = create_image(test_params)

        # Test sonuçlarını kontrol et
        self.assertIsInstance(result_image, Image.Image)

if __name__ == '__main__':
    unittest.main()
