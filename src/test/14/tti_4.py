# pip install git+https://github.com/kashif/diffusers.git@wuerstchen-v3
import torch
from diffusers import StableCascadeDecoderPipeline, StableCascadePriorPipeline

device = "cuda"
num_images_per_prompt = 2

prior = StableCascadePriorPipeline.from_pretrained("/data/hub/stabilityai/stable-cascade-prior",low_cpu_mem_usage=True,  torch_dtype=torch.float64).to(device)
decoder = StableCascadeDecoderPipeline.from_pretrained("/data/hub/stabilityai/stable-cascade", low_cpu_mem_usage=True,  torch_dtype=torch.float64).to(device)

prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."
negative_prompt = ""

prior_output = prior(
    prompt=prompt,
    height=1024,
    width=1024,
    negative_prompt=negative_prompt,
    guidance_scale=4.0,
    num_images_per_prompt=num_images_per_prompt,
    num_inference_steps=20
)
decoder_output = decoder(
    image_embeddings=prior_output.image_embeddings.half(),
    prompt=prompt,
    negative_prompt=negative_prompt,
    guidance_scale=0.0,
    output_type="pil",
    num_inference_steps=10
).images

images = decoder_output
#Now decoder_output is a list with your PIL images
#########################
from datetime import datetime
from PIL import Image
import os


# Specify the directory where you want to save the images
output_directory = "tmp"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through images and save them
for i, image in enumerate(images):    
    # Get current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Save the image with a filename containing the current date and time
    image_filename = f"stabilityai_{current_datetime}_{i}.png"
    output_path = os.path.join(output_directory, image_filename)   
    image.save(output_path)

print("All images have been saved to:", output_directory)