# video_processor.py
from text_processor import process_text
from dubbing_processor import process_dubbing
from image_processor import generate_image

def generate_video(pipe, cache, text):
    processText = process_text(text)
    processDubbing = process_dubbing(processText)
    processImages = process_images_list(processDubbing, pipe, cache)
    response_data = {
        "message": 'Video generation request received',
        "text": text,
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

def create_image(pipe, cache, text):
    image_path = generate_image(
        pipe,
        prompt=text,
        negative_prompt="nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name",
        output_type="pil",
        num_inference_steps=30,
        guidance_scale=3.0,
        lcm_origin_steps=3,
        width=512,
        height=512,
        cache=cache
    )

    return image_path
