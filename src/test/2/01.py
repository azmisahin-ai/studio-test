# pip install diffusers --upgrade
# pip install invisible_watermark transformers accelerate safetensors
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

images = pipe(prompt=prompt).images
image = images[0]

import os

# Bulunduğunuz dosyanın klasörünü al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dosya adını oluştur
file_name = "01.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image.save(file_path)
