# graphql_module.py

from text_to_image_service import text_to_image

def text_to_image_graphql(params):
    result = text_to_image(params)
    return {'image': result['image'], 'num_images': result['num_images']}
