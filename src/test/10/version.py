# version.txt dosyasındaki sayıyı oku
file = "data/version.txt"

"""
Version Number
"""
def get():
    try:
        with open(file, 'r') as dosya:
            sayi_str = dosya.read().strip()
            sayi = int(sayi_str)
            return sayi_str.zfill(6)
    except FileNotFoundError:
        # Dosya bulunamazsa veya okuma hatası olursa 1 ile başla
        return "000001"

# sayac.txt dosyasındaki sayıyı güncelle
def update(sayi):
    with open(file, 'w') as dosya:
        dosya.write(str(sayi).zfill(6))

# Her seferinde bir sonraki sayı ile başlamak için uygulama
def new_version():
   # Sayıyı dosyadan oku
    mevcut_sayi = get()

    # İşlemleri gerçekleştir
    print("Bu seferki sayı:", mevcut_sayi)
    yeni_sayi = int(mevcut_sayi) + 1

    # Yeni sayıyı dosyaya yaz
    update(yeni_sayi)

    return get()

if __name__ == "__main__":
    new_version()
