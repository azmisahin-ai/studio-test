# pip install diffusers --upgrade
# pip install invisible_watermark transformers accelerate safetensors
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

from diffusers import StableDiffusionPipeline
import torch

model_id = "/data/hub/runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# images = pipe(prompt).images
  
def generate(word,definition):
    # prompt = "a photo of an astronaut riding a horse on mars"
    images = pipe(definition).images  
    images[0].save(f"/data/images/{word}.png") 

# #################
# from datetime import datetime
# from PIL import Image
# import os


# # Specify the directory where you want to save the images
# output_directory = "tmp"

# # Create the output directory if it doesn't exist
# os.makedirs(output_directory, exist_ok=True)

# # Iterate through images and save them
# for i, image in enumerate(images):    
#     # Get current date and time
#     current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
#     # Save the image with a filename containing the current date and time
#     image_filename = f"tti_2_{current_datetime}_{i}.png"
#     output_path = os.path.join(output_directory, image_filename)   
#     image.save(output_path)

# print("All images have been saved to:", output_directory)

# ###############################################
# # pip install matplotlib numpy
# # import matplotlib.pyplot as plt
# # import numpy as np

# # # 'images' değişkenini bir NumPy dizisine dönüştür
# # image_array = np.array(images)

# # # Eğer birden çok görüntü varsa, her birini ayrı ayrı göster
# # for i, image in enumerate(image_array):
# #     plt.subplot(1, len(image_array), i + 1)
# #     plt.imshow(image)
# #     plt.axis('off')

# # plt.show()

# # # Name: Python Image Preview
# # # Id: 076923.python-image-preview
# # # Description: Numpy, Pillow, OpenCV, Matplotlib, Plotly, ImageIO, Scikit Image, Tensorflow, Pytorch Image Preview
# # # Version: 0.1.2
# # # Publisher: 윤대희
# # # VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=076923.python-image-preview