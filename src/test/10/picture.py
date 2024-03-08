# creator.py
from diffusers import DiffusionPipeline
import torch
import os
import pickle

current_directory = os.path.dirname(os.path.abspath(__file__))
cache_file_path = os.path.join(current_directory, "cached_result.pkl")

# DiffusionPipeline'ı bir kere yükle ve bellekte tut
if 'pipe' not in locals():
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")

# Önbellek dosyasını kontrol et
if os.path.exists(cache_file_path):
    # Önbellek dosyasından sonuçları yükle
    with open(cache_file_path, 'rb') as cache_file:
        images = pickle.load(cache_file)
else:
    # DiffusionPipeline'ı kullanarak işlemi gerçekleştir
    prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."
    images = pipe(prompt=prompt).images

    # Sonuçları önbelleğe kaydet
    with open(cache_file_path, 'wb') as cache_file:
        pickle.dump(images, cache_file)

# Dosya adını oluştur
file_name = "01.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image = images[0]
image.save(file_path)
