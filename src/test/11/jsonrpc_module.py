# jsonrpc_module.py

from text_to_image_service import text_to_image

def text_to_image_rpc(**params):
    result = text_to_image(params)
    return result
