# app.py
from flask import Flask, render_template, request
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from image_processor import process_image
import os
import torch
web = Flask(__name__)

# DiffusionPipeline'ı bir kere yükle ve bellekte tut
model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

# Ana sayfa
@web.route('/')
def home():
    return render_template('index.html', image_path="cached_result_web.png")

# Formdan veri al ve işlemi gerçekleştir
@web.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"
    process_image(pipe, prompt,negative_prompt)
    return render_template('index.html', image_path="cached_result_web.png")

if __name__ == '__main__':
    web.run(debug=True)
