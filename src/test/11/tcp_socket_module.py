# tcp_socket_module.py

from text_to_image_service import text_to_image

def text_to_image_tcp_socket(data):
    params = data.get('params', {})
    result = text_to_image(params)
    return result
