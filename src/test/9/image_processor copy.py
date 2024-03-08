# image_processor.py
import os
import pickle
from PIL import Image
import time

CACHE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_web.pkl")

def clear_cache_if_needed():
    if is_expired(get_last_clear_timestamp(), expiration_time=300):  # 300 saniye = 5 dakika
        clear_cache()
        update_last_clear_timestamp()

def clear_cache():
    if os.path.exists(CACHE_FILE_PATH):
        os.remove(CACHE_FILE_PATH)

def update_last_clear_timestamp():
    with open(CACHE_FILE_PATH, 'wb') as cache_file:
        timestamp = time.time()
        pickle.dump(timestamp, cache_file)

def get_last_clear_timestamp():
    if os.path.exists(CACHE_FILE_PATH):
        with open(CACHE_FILE_PATH, 'rb') as cache_file:
            timestamp = pickle.load(cache_file)
            return timestamp if isinstance(timestamp, (int, float)) else 0
    return 0


def process_image(pipe, prompt):

    # Eğer gerekli ise, önbelleği temizle
    clear_cache_if_needed()

    negative_prompt = "nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name"

    # Önbellekten veriyi kontrol et
    cached_data = get_cached_result()

    if cached_data is None or prompt_changed(cached_data, prompt):
        # Önbellekte veri yoksa veya prompt değiştiyse, DiffusionPipeline'ı kullanarak işlemi gerçekleştir
        images = pipe(prompt, negative_prompt=negative_prompt).images

        # Sonuçları önbelleğe kaydet
        cache_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_web.pkl")
        with open(cache_file_path, 'wb') as cache_file:
            # prompt ve zaman damgasını önbelleğe dahil et
            pickle.dump((images, prompt, time.time()), cache_file)

        # İmage'ı belirtilen dosya adı ve yola kaydet
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "cached_result_web.png")
        images[0].save(image_path)

def get_cached_result():
    cache_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_web.pkl")

    if os.path.exists(cache_file_path):
        try:
            with open(cache_file_path, 'rb') as cache_file:
                data = pickle.load(cache_file)
                if isinstance(data, tuple) and len(data) == 3:
                    return data
                else:
                    print(f"Warning: Invalid data structure in cache file. Expected tuple of length 3, got: {data}")
                    return None  # Invalid data structure, return None
        except Exception as e:
            print(f"Error loading cache file: {e}")
            return None  # Error loading cache file, return None

    return None


        
def prompt_changed(cached_data, current_prompt):
    if cached_data and isinstance(cached_data, tuple) and len(cached_data) == 3:
 
        (cached_images, cached_prompt, cached_timestamp) = cached_data

        # Eğer cached_prompt bir string değilse, varsayılan bir değer kullanabiliriz
        cached_prompt_str = str(cached_prompt) if isinstance(cached_prompt, str) else ""

        # cached_prompt'ı küçük harfe çevirip başındaki ve sonundaki boşlukları temizle
        cached_prompt_lower = cached_prompt_str.lower().strip()

        result = cached_prompt_lower != current_prompt.strip().lower() or is_expired(cached_timestamp)
        print(f"Debug: result={result}, cached_prompt_lower={cached_prompt_lower}, current_prompt={current_prompt.strip().lower()}, cached_timestamp={cached_timestamp}")
        return result
    else:
        return True


def is_expired(timestamp, expiration_time=3600):
    current_time = time.time()
    return (current_time - timestamp) > expiration_time
