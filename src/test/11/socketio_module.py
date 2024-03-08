# socketio_module.py

from flask_socketio import emit
from text_to_image_service import text_to_image

def text_to_image_socketio(data):
    params = data.get('params', {})
    result = text_to_image(params)
    emit('text_to_image_result', result)
