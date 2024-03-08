import os
def process_image(pipe, prompt,negative_prompt):

 
        # DiffusionPipeline'ı kullanarak işlemi gerçekleştir
        images = pipe(prompt, negative_prompt=negative_prompt).images

        # İmage'ı belirtilen dosya adı ve yola kaydet
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "cached_result.png")
        images[0].save(image_path)
        




