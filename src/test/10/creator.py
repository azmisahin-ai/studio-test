# creator_04.py
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import os
import pickle

current_directory = os.path.dirname(os.path.abspath(__file__))
cache_file_path = os.path.join(current_directory, "cached_result_04.pkl")

# DiffusionPipeline'ı bir kere yükle ve bellekte tut
if 'pipe' not in locals():
    model_id = "stabilityai/stable-diffusion-2-1"

    # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

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
file_name = "04.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image = images[0]
image.save(file_path)
