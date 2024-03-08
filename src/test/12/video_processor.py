# video_processor.py
from text_processor import process_text
from dubbing_processor import process_dubbing
from image_processor import generate_image

default_params = None

def generate_video(pipe, cache, params):
    global default_params  # global anahtar kelimesini ekledik
    default_params = params
    
    processText = process_text(params["prompt"])
    processDubbing = process_dubbing(processText)
    processImages = process_images_list(processDubbing, pipe, cache)
    response_data = {
        "message": 'Video generation request received',
        "text": params["prompt"],
        "lines": processText,
        "dubbings": processDubbing,
        "images": processImages,
    }
    return response_data

def process_images_list(textArray, pipe, cache):
    response_data = []

    for item in textArray:
        response_data.append({
            "file": item["file"],
            "text": item["text"],
            "image": create_image(pipe, cache, item["text"]),
        })

    return response_data

def create_image(pipe, cache, prompt):
    global default_params  # global anahtar kelimesini ekledik
    
    default_params["prompt"] = prompt  
    
    # Kullanıcıdan gelen model kimliğini kullanarak işlemi gerçekleştir
    image_path = generate_image(pipe, cache, default_params)

    return image_path
