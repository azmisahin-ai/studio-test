# api_module.py

from flask import jsonify
from text_to_image_service import text_to_image

def text_to_image_api(params):
    result = text_to_image(params)
    return jsonify(result)
