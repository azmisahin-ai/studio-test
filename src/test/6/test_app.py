# tests/test_app.py

import binascii
import time
import unittest
import requests
import socket
import json
import base64  # base64 modülünü ekledik
from io import BytesIO
from PIL import Image, UnidentifiedImageError

class TestApp(unittest.TestCase):

    def test_api(self):
        # API testi için kullanılacak parametreler
        api_params = {
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

        # API'ye POST isteği gönder
        api_url = 'http://127.0.0.1:5000/create_image'
        api_response = requests.post(api_url, json=api_params)

        # API'den dönen JSON verisini kontrol et
        try:
            api_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"API Error: {err}")
            print(api_response.text)  # API'nin döndüğü hata mesajını görüntüle
            raise

        # API'den dönen base64 formatındaki resmi PIL Image objesine çevir
        img_data = api_response.json()['image'].encode('utf-8')
        img_data = BytesIO(base64.b64decode(img_data))
        img = Image.open(img_data)

        # Resmin boyutlarını kontrol et
        self.assertEqual(img.width, api_params['width'])
        self.assertEqual(img.height, api_params['height'])

    def test_socket(self):
        # Soket testi için kullanılacak parametreler
        socket_params = {
            'prompt': 'Test Prompt Socket',
            'style': 'Test Style Socket',
            'negative_prompt': 'Test Negative Prompt Socket',
            'output_type': 'Test Output Type Socket',
            'num_inference_steps': 12,
            'guidance_scale': 0.6,
            'lcm_origin_steps': 6,
            'width': 600,
            'height': 400
        }

        # Soket sunucusuna bağlan ve parametreleri gönder
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect(('127.0.0.1', 5555))
        socket_client.send(json.dumps(socket_params).encode('utf-8'))

        # Soketten dönen base64 formatındaki resmi PIL Image objesine çevir
        img_data_socket = socket_client.recv(1024).decode('utf-8')
        img_data_socket = BytesIO(base64.b64decode(img_data_socket))
        img_socket = Image.open(img_data_socket)

        # Resmin boyutlarını kontrol et
        self.assertEqual(img_socket.width, socket_params['width'])
        self.assertEqual(img_socket.height, socket_params['height'])

        socket_client.close()

if __name__ == '__main__':
    unittest.main()
