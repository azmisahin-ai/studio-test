# lib/metin_donusturucu/text_to_image.py

from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, output_path='output_image.png'):
    """
    Belirtilen metni bir resme dönüştürüp kaydeden fonksiyon.

    :param text: Resme eklenmek istenen metin.
    :param output_path: Kaydedilecek dosya adı.
    """
    # Resmi oluştur
    image_size = (500, 500)
    background_color = (255, 255, 255)
    image = Image.new('RGB', image_size, background_color)
    draw = ImageDraw.Draw(image)

    # Pillow'un içindeki bir fontu kullan
    font = ImageFont.load_default()

    # Metni resme ekle
    text_width, text_height = draw.textbbox((0, 0), text, font)[2:]
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))

    # Resmi kaydet
    image.save(output_path)

if __name__ == '__main__':
    metin = input("Metni girin: ")
    dosya_adi = input("Kaydedilecek dosya adını girin (örn: output_image.png): ")

    if not dosya_adi:
        dosya_adi = 'output_image.png'

    text_to_image(metin, output_path=dosya_adi)

    print(f"{dosya_adi} adlı resim oluşturuldu.")
