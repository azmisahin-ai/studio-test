from diffusers import StableDiffusionXLPipeline
import torch
pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")
# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()

# Olmasın dediklerin neler
neg_prompt = "ugly, blurry, poor quality" # Negative prompt here

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

images = pipe(prompt=prompt, negative_prompt=neg_prompt).images
image = images[0]

import os

# Bulunduğunuz dosyanın klasörünü al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dosya adını oluştur
file_name = "09.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image.save(file_path)