import torch
from diffusers import LCMScheduler, AutoPipelineForText2Image

model_id = "Lykon/dreamshaper-7"
adapter_id = "latent-consistency/lcm-lora-sdv1-5"

pipe = AutoPipelineForText2Image.from_pretrained(model_id, torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
pipe.to("cuda")

# load and fuse lcm lora
pipe.load_lora_weights(adapter_id)
pipe.fuse_lora()

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

images = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=0.0).images
image = images[0]

import os

# Bulunduğunuz dosyanın klasörünü al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Dosya adını oluştur
file_name = "07.png"
file_path = os.path.join(current_directory, file_name)

# İmage'ı belirtilen dosya adı ve yola kaydet
image.save(file_path)
