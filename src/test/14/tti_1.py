# pip install diffusers --upgrade
# pip install invisible_watermark transformers accelerate safetensors
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("/data/hub/stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda")

# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()

prompt = "An astronaut riding a green horse"

images = pipe(prompt=prompt).images


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
    image_filename = f"tti_1_{current_datetime}_{i}.png"
    output_path = os.path.join(output_directory, image_filename)   
    image.save(output_path)

print("All images have been saved to:", output_directory)

###############################################
# pip install matplotlib numpy
# import matplotlib.pyplot as plt
# import numpy as np

# # 'images' değişkenini bir NumPy dizisine dönüştür
# image_array = np.array(images)

# # Eğer birden çok görüntü varsa, her birini ayrı ayrı göster
# for i, image in enumerate(image_array):
#     plt.subplot(1, len(image_array), i + 1)
#     plt.imshow(image)
#     plt.axis('off')    

# plt.show()

# Name: Python Image Preview
# Id: 076923.python-image-preview
# Description: Numpy, Pillow, OpenCV, Matplotlib, Plotly, ImageIO, Scikit Image, Tensorflow, Pytorch Image Preview
# Version: 0.1.2
# Publisher: 윤대희
# VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview