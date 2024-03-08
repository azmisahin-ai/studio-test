# pip install --upgrade diffusers transformers scipy
import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

images = pipe(prompt=prompt).images
image = images[0]

import os

# Bulunduğunuz dosyanın klasörünü al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dosya adını oluştur
file_name = "03.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image.save(file_path)
