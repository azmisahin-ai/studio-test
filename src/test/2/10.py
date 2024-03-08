import torch
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

# Define prompts and generate image

# Olmasın dediklerin neler
negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

images = pipe(prompt, 
    negative_prompt=negative_prompt, 
    # width=832,
    # height=1216,
    # guidance_scale=7,
    # num_inference_steps=28
    ).images
image = images[0]

import os

# Bulunduğunuz dosyanın klasörünü al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dosya adını oluştur
file_name = "10.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image.save(file_path)