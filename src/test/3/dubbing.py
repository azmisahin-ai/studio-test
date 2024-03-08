from gtts import gTTS
import os

# Metni belirtilen dilde ve belirtilen dosya adıyla seslendir
def seslendir(metin, dil, dosya_adi):
    tts = gTTS(text=metin, lang=dil)
    tts.save(dosya_adi)
    os.system(dosya_adi)

# Metni ve dilinizi buraya girin
metin = """
Once upon a time, a boy named Lalik lived in Colorful Town.
Lalik was the most cheerful and energetic child in the town.
He was a master of humor who always managed to make everyone around him laugh.
One day, he decided to add color to the gray walls of the town.
Lalik brought colored paint bottles and brushes all over the town.
They started to color the town square with their volunteer friends.
They decorated walls, benches and even trees with colorful paints.
The town suddenly began to shine with vibrant colors.
The townspeople loved this colorful change.
Everyone thanked Lalik and gave him the title of "King of Color."
Lalik, smiling, said, "Life should not be gray, it should be colorful!" said.
However, Uncle Grumpy, the gray-walled and monotonous house owner of the town, opposed the colorful change.
He stood against Lalik and warned him to restore the town.
But Color King Lalik was determined to change Uncle Grumpy's heart.
Lalik went to Uncle Grumpy's house and gave him a colorful painting as a gift.
Even though Uncle Grumpy looked at the painting with a resentful expression when he first saw it,
he realized that the colors colored the black-white world.
He started to smile slowly.
Eventually, everyone, including the townspeople and Uncle Grumpy, accepted the colorful change brought by the Color King Lalik.
The town has become a place overflowing with all colours, not just grey.
And Lalik went down in the town's history as the Color King.
With a smile on everyone's face and colorful walls everywhere,
everyone continued to live happily and peacefully in Colorful Town.
"""

dil = 'en'  # Metnin dilini belirtin ('en' İngilizce için)
dosya_adi = 'dubbing.mp3'  # Ses dosyasının adını belirtin

# Seslendirme işlemini başlat
seslendir(metin, dil, dosya_adi)
