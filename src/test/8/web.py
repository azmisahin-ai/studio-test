# web.py

from image_processor import generate_image
from image_cache import ImageCache
from flask import Flask, jsonify, render_template, request

from video_processor import generate_video


cache_dir = "static"
static_url_path = "/static"
static_folder="../static"
web = Flask(__name__, static_url_path=static_url_path, static_folder=static_folder)

# ImageCache sınıfını oluştur
cache = ImageCache(cache_dir=cache_dir, use_cache=False)

# Önce varsayılan model kimliği belirleme
default_model_id = "stabilityai/stable-diffusion-2-1"

# CustomDiffusionPipeline'ı bir kere yükle ve bellekte tut
custom_pipe = None

def loadModel():
    global custom_pipe  # global ifadesi fonksiyonun içinde yer almalı
    if custom_pipe is None:
        from diffusion_pipeline import CustomDiffusionPipeline
        custom_pipe = CustomDiffusionPipeline(model_id=default_model_id)

    return True


@web.route('/load_models')
def load_models():
    loadModel()

    return jsonify({"status": "success"})

# Ana sayfa
@web.route('/')
def home():
    default_image_path = ""
    return render_template('index.html', image_path=default_image_path, model_id=default_model_id)

@web.route('/generate_image')
def generate_image_get():
    default_image_path = ""
    return render_template('generate_image.html', image_path=default_image_path, model_id=default_model_id)

# Formdan veri al ve işlemi gerçekleştir
@web.route('/generate_image', methods=['POST'])
def generate_image_post():
    prompt = request.form['prompt']
    negative_prompt = request.form['negative_prompt']
    output_type = request.form['output_type']
    num_inference_steps = request.form['num_inference_steps']
    guidance_scale = request.form['guidance_scale']
    lcm_origin_steps = request.form['lcm_origin_steps']
    width = request.form['width']
    height = request.form['height']

    try:
        num_inference_steps = int(request.form['num_inference_steps'])
        guidance_scale = float(request.form['guidance_scale'])  # Eğer float değer istiyorsanız
        lcm_origin_steps = int(request.form['lcm_origin_steps'])
        width = int(request.form['width'])
        height = int(request.form['height'])
    except ValueError as e:
        # Eğer dönüşüm başarısız olursa (değerler sayısal bir ifade değilse) ValueError hatası alırsınız.
        # Bu durumu ele alabilir veya uygun bir hata mesajını kullanıcıya gönderebilirsiniz.
        print("Hata:", e)
        # Hata mesajını kullanıcıya göndermek için uygun bir mekanizma ekleyebilirsiniz.
        # Örneğin, hata mesajını bir değişkene atayarak template'e gönderebilirsiniz.

    # Kullanıcıdan gelen model kimliğini al
    model_id = request.form.get('model_id', default_model_id)

    # CustomDiffusionPipeline'ı güncelle
    custom_pipe.update_model_id(model_id)
    
    # Kullanıcıdan gelen model kimliğini kullanarak işlemi gerçekleştir
    image_path = generate_image(custom_pipe.pipe, prompt, negative_prompt,output_type,num_inference_steps,guidance_scale,lcm_origin_steps,width,height, cache)
    
    return render_template('generate_image.html', image_path=image_path, model_id=model_id)

@web.route('/generate_video', methods=['POST'])
def generate_video_process():
    try:
        # CustomDiffusionPipeline'ı güncelle
        loadModel()
        
        data = request.get_json()
        video_text = data['text']
        result = generate_video(cache=cache,pipe=custom_pipe.pipe,text=video_text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    web.run(host="0.0.0.0", port=5000)
