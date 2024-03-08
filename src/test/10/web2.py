from flask import Flask, render_template, request
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import os
import pickle
from PIL import Image
import torch
app = Flask(__name__)

# DiffusionPipeline'ı bir kere yükle ve bellekte tut

from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL
)

# Load VAE component
vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix", 
    torch_dtype=torch.float16
)

# Configure the pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "cagliostrolab/animagine-xl-3.0", 
    vae=vae,
    torch_dtype=torch.float16, 
    use_safetensors=True, 
)
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')


# Önbellek dosyasını kontrol et
cache_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_web_animagine.pkl")
if os.path.exists(cache_file_path):
    # Önbellek dosyasından sonuçları yükle
    with open(cache_file_path, 'rb') as cache_file:
        images = pickle.load(cache_file)
else:
    # Varsa oluştur, yoksa boş bir resim oluştur
    images = [Image.new("RGB", (1, 1))]

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html', image_path="cached_result_web.png")

# Formdan veri al ve işlemi gerçekleştir
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']

    negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

    # DiffusionPipeline'ı kullanarak işlemi gerçekleştir
    images = pipe(
        prompt,
         negative_prompt=negative_prompt, 
        ).images

    # Sonuçları önbelleğe kaydet
    with open(cache_file_path, 'wb') as cache_file:
        pickle.dump(images, cache_file)

    # İmage'ı belirtilen dosya adı ve yola kaydet
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"static", "cached_result_web.png")
    images[0].save(image_path)

    return render_template('index.html', image_path="cached_result_web.png")

if __name__ == '__main__':
    app.run(debug=True)
