# pip install diffusers transformers accelerate scipy safetensors
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

model_id = "/data/hub/stabilityai/stable-diffusion-2-1-base"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

# Düşündüğün şey nedir
prompt = "Children playing video games suddenly turn into heroes helping nature. cinematic."

#images = pipe(prompt=prompt).images

#######################################
import os
from datetime import datetime


# Specify the directory where you want to save the images
output_directory = "tmp"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

def save_image(image):
    # Get current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Save the image with a filename containing the current date and time
    image_filename = f"stabilityai_{current_datetime}_{i}.png"
    output_path = os.path.join(output_directory, image_filename)   
    image.save(output_path)

####
num_images = 5  # Set the desired number of variations
for i in range(num_images):
    images = pipe(prompt=prompt, noise_seed=i).images  # Use a different noise seed each time
    save_image(images[0])
    # Process or save the generated images
    # ...
##########


# Iterate through images and save them
# for i, image in enumerate(images):    
#  save_image(image)