import matplotlib.pyplot as plt
import numpy as np

# Betimleme detayları
renk_turuncu = [1.0, 0.647, 0.0]  # Turuncu rengi RGB formatında float
gokyuzu_yukseklik = 10
gokyuzu_genislik = 100
gokyuzu = np.full((gokyuzu_yukseklik, gokyuzu_genislik, 3), renk_turuncu, dtype=float)

# Ufuk çizgisi üzerinde gökdelenlerin siluetleri
gokdelen_yukseklikleri = [2, 5, 8]
for yukseklik in gokdelen_yukseklikleri:
    gokyuzu[yukseklik:, :] = [0, 0, 0]  # Siyah renk ile siluet

# Kır çiçekleri çimenlerin üzerinde hafif rüzgarla dalgalanıyor
cimen_rengi = [0, 1, 0]  # Yeşil renk RGB formatında float
cimen_yukseklik = 2
cimenler = np.full((gokyuzu_yukseklik - cimen_yukseklik, gokyuzu_genislik, 3), cimen_rengi, dtype=float)
gokyuzu[:-cimen_yukseklik, :] = cimenler

# Oluşturulan görüntüyü göster
plt.imshow(gokyuzu)
plt.axis('off')  # Eksenleri kapat
plt.show()
