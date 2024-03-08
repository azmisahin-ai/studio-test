import os
import pickle
import time

CACHE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cached_result_web.pkl")

def is_expired(timestamp, expiration_time=3600):
    current_time = time.time()
    return (current_time - timestamp) > expiration_time

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