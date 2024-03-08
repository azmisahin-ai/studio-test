# ImageCache.py
from pathlib import Path
import os
class ImageCache:
    def __init__(self, cache_dir="static"):
        """
        Resim önbelleğini yöneten sınıf.

        Parameters:
        - cache_dir (str): Önbellek dosyalarının saklanacağı klasörün adı.
        """
        self.cache_dir = cache_dir
        # Klasör yoksa oluştur
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)

    def get_cached_path(self, prompt, negative_prompt):
        """
        Belirtilen prompt ve negative_prompt için önbellek dosyasının yolunu oluşturur.

        Parameters:
        - prompt (str): İmage oluşturmak için kullanılacak anahtar kelime.
        - negative_prompt (str): İmage oluştururken kullanılacak negatif anahtar kelime.

        Returns:
        - str: Önbellek dosyasının tam yolunu içeren bir string.
        """
        # Önbellekte dosya adını oluştur
        cache_key = f"{prompt}_{negative_prompt}"
        cache_filename = f"{hash(cache_key)}.png"
        cache_path = os.path.join(self.cache_dir, cache_filename)
        
        return cache_path

    def is_cached(self, prompt, negative_prompt):
        """
        Belirtilen prompt ve negative_prompt için önbellekte bir dosyanın olup olmadığını kontrol eder.

        Parameters:
        - prompt (str): İmage oluşturmak için kullanılacak anahtar kelime.
        - negative_prompt (str): İmage oluştururken kullanılacak negatif anahtar kelime.

        Returns:
        - bool: Önbellekte dosya varsa True, yoksa False.
        """
        # Önbellekte dosya mevcut mu kontrol et
        cache_path = self.get_cached_path(prompt, negative_prompt)
        return os.path.exists(cache_path)

    def save_to_cache(self, prompt, negative_prompt, image):
        """
        Belirtilen prompt ve negative_prompt için bir resmi önbelleğe kaydeder.

        Parameters:
        - prompt (str): İmage oluşturmak için kullanılacak anahtar kelime.
        - negative_prompt (str): İmage oluştururken kullanılacak negatif anahtar kelime.
        - image: Kaydedilecek Image objesi.
        """
        # İmage'ı önbelleğe kaydet
        cache_path = self.get_cached_path(prompt, negative_prompt)
        image.save(cache_path)

    def get_from_cache(self, prompt, negative_prompt):
        """
        Belirtilen prompt ve negative_prompt için önbellekteki bir resmi getirir.

        Parameters:
        - prompt (str): İmage oluşturmak için kullanılacak anahtar kelime.
        - negative_prompt (str): İmage oluştururken kullanılacak negatif anahtar kelime.

        Returns:
        - str: Önbellekteki resmin dosya yolunu içeren bir string.
        """
        # Önbellekten İmage'ı al
        cache_path = self.get_cached_path(prompt, negative_prompt)
        return cache_path
