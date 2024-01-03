musteri_veritabani = []

musteri_veritabani = []

def musteri_ekle(isim, email):
    yeni_musteri = {"isim": isim, "email": email}
    musteri_veritabani.append(yeni_musteri)
    print(f"{isim} adlı müşteri veritabanına eklendi.")

def musteri_sil(isim):
    silinecek_musteri = 0
    for musteri in musteri_veritabani:
        if musteri["isim"] == isim:
            silinecek_musteri = musteri
            break

    if silinecek_musteri:
        musteri_veritabani.remove(silinecek_musteri)
        print(f"{isim} adlı müşteri veritabanından silindi.")
    else:
        print(f"{isim} adlı müşteri bulunamadı.")


while True:
    print("1 - Müşteri Ekle")
    print("2 - Müşteri Sil")
    print("3 - Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3): ")

    if secim == "1":
        isim = input("Müşteri adını girin: ")
        email = input("Müşteri e-posta adresini girin: ")
        musteri_ekle(isim, email)
    elif secim == "2":
        isim = input("Silmek istediğiniz müşterinin adını girin: ")
        musteri_sil(isim)
    elif secim == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
