# src/ana_modul/fonksiyonlar.py

def welcome_message():
    return "Merhaba, bu ana modülün fonksiyonlarından biri!"

# ana_modul/fonksiyonlar.py

from PIL import Image, ImageDraw, ImageFont

def create_image(params):
    print("YENİ RESİM ***********************************")
    # İmage oluşturmak için kullanılacak parametreleri al
    prompt = params.get('prompt', 'Default Prompt')
    style = params.get('style', 'Default Style')
    negative_prompt = params.get('negative_prompt', 'Default Negative Prompt')
    output_type = params.get('output_type', 'Default Output Type')
    num_inference_steps = params.get('num_inference_steps', 10)
    guidance_scale = params.get('guidance_scale', 0.5)
    lcm_origin_steps = params.get('lcm_origin_steps', 5)
    width = params.get('width', 500)
    height = params.get('height', 500)

    # Resmi oluştur
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default(size=20)

    # Metni resme ekle
    text = f"Prompt: {prompt}\nStyle: {style}\nNegative Prompt: {negative_prompt}\nOutput Type: {output_type}\nNum Inference Steps: {num_inference_steps}\nGuidance Scale: {guidance_scale}\nLCM Origin Steps: {lcm_origin_steps}"
    text_width, text_height = draw.textbbox((0, 0), text, font)[2:]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    print("*******************************OLUŞTURULDU****")
    return image
