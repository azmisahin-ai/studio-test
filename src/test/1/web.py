# web.py

from image_processor import process_image
from image_cache import ImageCache
from flask import Flask, jsonify, render_template, request


cache_dir = "static"
static_url_path = "/static"
static_folder="../static"
web = Flask(__name__, static_url_path=static_url_path, static_folder=static_folder)

# ImageCache sınıfını oluştur
cache = ImageCache(cache_dir=cache_dir)

# Önce varsayılan model kimliği belirleme
default_model_id = "cagliostrolab/animagine-xl-3.0"

# CustomDiffusionPipeline'ı bir kere yükle ve bellekte tut
custom_pipe = None

# Ana sayfa
@web.route('/')
def home():
    default_image_path = ""
    return render_template('index.html', image_path=default_image_path, model_id=default_model_id)

# Formdan veri al ve işlemi gerçekleştir
@web.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

    # Kullanıcıdan gelen model kimliğini al
    model_id = request.form.get('model_id', default_model_id)

    # CustomDiffusionPipeline'ı güncelle
    custom_pipe.update_model_id(model_id)
    
    # Kullanıcıdan gelen model kimliğini kullanarak işlemi gerçekleştir
    image_path = process_image(custom_pipe.pipe, prompt, negative_prompt, cache)
    
    return render_template('index.html', image_path=image_path, model_id=model_id)

@web.route('/load_models')
def load_models():
    from diffusion_pipeline import CustomDiffusionPipeline
    global custom_pipe
    if custom_pipe is None:
        custom_pipe = CustomDiffusionPipeline(model_id=default_model_id)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    web.run(debug=True)
