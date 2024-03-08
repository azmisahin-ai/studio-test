# image_processor.py
def process_image(pipe, prompt, negative_prompt, cache):
    """
    DiffusionPipeline kullanarak bir resmi işleyen ve önbellekte saklayan fonksiyon.

    Parameters:
    - pipe: DiffusionPipeline objesi.
    - prompt (str): İmage oluşturmak için kullanılacak anahtar kelime.
    - negative_prompt (str): İmage oluştururken kullanılacak negatif anahtar kelime.
    - cache (ImageCache): Resim önbelleğini yöneten ImageCache objesi.

    Returns:
    - str: İşlenmiş resmin dosya yolunu içeren bir string.
    """
    # Önbellekte dosya mevcut mu kontrol et
    if cache.is_cached(prompt, negative_prompt):
        # Mevcut ise önbellekten getir
        image_path = cache.get_from_cache(prompt, negative_prompt)
    else:
        # DiffusionPipeline'ı kullanarak işlemi gerçekleştir
        images = pipe(prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=3,
            guidance_scale=2,
            lcm_origin_steps=5,
            output_type="pil",
            width=512,
            height=512
            ).images

        # İmage'ı önbelleğe kaydet
        image_path = cache.get_cached_path(prompt, negative_prompt)
        cache.save_to_cache(prompt, negative_prompt, images[0])

    return image_path
