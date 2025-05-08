import json # json dosyası ile çalışabilmek için
import os # Dosya işlemleri ve dosya yolu kontrolü

# ******* Konsol Kullanımı *******
# özellikler :Görev Ekleme, Listeleme, Düzenleme, Tamamlama, Silme, Uygulamadan Çıkış Yapabilme
# Tamamlanan Görevler ve aktif görevler ayrı olarak listelenecel

# ********** Fonksiyonlar **********
# Veri Yükle, Veri Kaydet, Görev Ekle, Görev Listele, Görev Düzenle, Görev Tamamla, Görev Sil






konsol_dosya_isim = "konsol_gorevler.json" # ... isimli json dosyası

def veri_yukle(): # json uzantılı dosyadan görevleri yükler
    if os.path.exists(konsol_dosya_isim): # dosyanın varlığını kontrol etme
        with open(konsol_dosya_isim, "r", encoding="utf-8") as dosya: # utf-8 ile dosya okuma modunda('r') aç
            try:
                return json.load(dosya) # okunan dosyayı json olarak yükle
            except json.JSONDecodeError:
                return [] # boş liste dön

    else:
        return [] # dosya yok ise boş liste dön


def veri_kaydet(gorevler): # görev listesini json dosyasına kaydet
    with open(konsol_dosya_isim, "w", encoding="utf-8") as dosya: # utf-8 ile  yazma(write) modunda aç 'w'
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4) # görevleri json formatında yaz

def gorev_ekle(gorevler): # yeni gorev ekleme fonksiyonu

    baslik = input("Görev Başlığı: ").strip() # görev başlığını kullanıcıdan alma / strip ile temiz girdi alma
    aciklama = input("Açıklama(Boş Bırakılabilir): ").strip() # kullanıcıdan açıklama alma

    yeni_gorev = { # yeni görevin bileşenleri/ sözlüğü oluşturulur
        "baslik": baslik,
        "aciklama": aciklama,
        "durum": "aktif" # varsayılan olarak aktif görev olur
    }

    gorevler.append(yeni_gorev) # gorevler listesine yeni görev i atama
    veri_kaydet(gorevler) # güncellenmiş görevler listesini kaydet
    print("✅ Görev Başarıyla Eklendi\n*****\n") # bilgilendirme mesajı


def gorev_listele(gorevler): # gorevleri listeleme
    if not gorevler: # liste boş ise
        print("\n❌ Görev Listesi Boş!") # bilgilendirme mesajı
        return

    aktif_gorevler = [g for g in gorevler if g["durum"] == "aktif"] # eğer görev durumu aktif ise  -> aktif görevler filtrelenir
    tamamlanan_gorevler = [g for g in gorevler if g["durum"] == "tamamlandi"] # eğer durum tamamlandi ise -> tamamlanan görevler filtrelenir

    # güzel görünmesi adına işlemler yapılır
    print("\n" + "=" * 40)
    print("📌 Aktif Görevler".center(40))
    print("=" * 40)
    if aktif_gorevler:
        for i, gorev in enumerate(aktif_gorevler, 1): # aktif görevleri numaralandırarak listele
            print(f"{i}. {gorev['baslik']}") # i. sayı ile görev baslığını yazdır
            print(f"   Açıklama: {gorev['aciklama'] or 'Açıklama Yok!'}")
            print("-" * 40)

    else:
        print("🔹 Aktif Görev Yok!") # bilgilendirme mesajı

    print("\n" + "=" * 40)
    print("✅ Tamamlanan Görevler".center(40))
    print("=" * 40)
    if tamamlanan_gorevler:
        for i, gorev in enumerate(tamamlanan_gorevler, 1): # tamamlanan görevleri listele numaralandırarak
            print(f"{i}. {gorev['baslik']}")
            print(f"   Açıklama: {gorev['aciklama'] or 'Açıklama Yok!'}")
            print("-" * 40)

    else:
        print("🔹 Tamamlanan Görev Yok!") # bilgilendirme mesajı

def gorev_duzenle(gorevler): # görev düzenleme fonksiyonu
    if not gorevler:
        print("❌ Düzenlenecek Görev Yok!") # bilgilendirme mesajı
        return

    # aktive ve tamamlanan görevleri filtreler
    aktif_gorevler = [g for g in gorevler if g["durum"] == "aktif"]
    tamamlanan_gorevler = [g for g in gorevler if g["durum"] == "tamamlandi"]

    # kullanıcıdan görev türü seçimini alır
    print("\nDüzenlemek istediğiniz görev türünü seçin:")
    print("1. Aktif Görev")
    print("2. Tamamlanan Görev")

    try:
        secim_turu = int(input("Seçim (1/2): ")) # kullanıcıdan görev türü alınır
        if secim_turu == 1 and aktif_gorevler: # eğer girdi 1 ise aktif görevleri döndür
            print("\n✏️ Aktif Görevler")
            for i, gorev in enumerate(aktif_gorevler, 1): # aktif görevleri listele
                print(f"{i}. {gorev['baslik']} - {gorev['aciklama'] or 'Açıklama Yok!'}")
            secim = int(input("Düzenlemek istediğiniz görev numarası: ")) # düzenelenecek görev numarasını kullanıcıdan al
            if 1 <= secim <= len(aktif_gorevler): # seçim 1 ile aktif görevler listesi uzunluğu arasındaysa
                secilen = aktif_gorevler[secim - 1] # secilene değişkenine aktif görevler listesinden secim -1 i ata
                yeni_baslik = input("Yeni başlık (boş bırakılırsa değişmez): ").strip()
                yeni_aciklama = input("Yeni açıklama (boş bırakılırsa değişmez): ").strip()

                # kullanıcıdan alınan yeni baslik ve yani aciklamayı güncelle
                if yeni_baslik:
                    secilen["baslik"] = yeni_baslik
                if yeni_aciklama:
                    secilen["aciklama"] = yeni_aciklama

                veri_kaydet(gorevler)
                print("✅ Görev başarıyla güncellendi.")
            else:
                print("❌ Geçersiz görev numarası!")

        # tamamlanan görevler için aynı işlemler
        elif secim_turu == 2 and tamamlanan_gorevler:
            print("\n✏️ Tamamlanan Görevler")
            for i, gorev in enumerate(tamamlanan_gorevler, 1):
                print(f"{i}. {gorev['baslik']} - {gorev['aciklama'] or 'Açıklama Yok!'}")
            secim = int(input("Düzenlemek istediğiniz görev numarası: "))
            if 1 <= secim <= len(tamamlanan_gorevler):
                secilen = tamamlanan_gorevler[secim - 1]
                yeni_baslik = input("Yeni başlık (boş bırakılırsa değişmez): ").strip()
                yeni_aciklama = input("Yeni açıklama (boş bırakılırsa değişmez): ").strip()

                if yeni_baslik:
                    secilen["baslik"] = yeni_baslik
                if yeni_aciklama:
                    secilen["aciklama"] = yeni_aciklama

                veri_kaydet(gorevler)
                print("✅ Görev başarıyla güncellendi.")
            else:
                print("❌ Geçersiz görev numarası!")

        else:
            print("❌ Geçersiz seçim ya da seçilen türde görev yok.")

    except ValueError:
        print("❌ Sayı girmeniz gerekiyor.")

def gorev_tamamla(gorevler): # görev tamamlanmış olarak işaretleme fonksiyonu

    aktif_gorevler = [g for g in gorevler if g["durum"] == "aktif"] # durumu aktif olarak gözükenleri filtrele

    if not aktif_gorevler: # aktif görev yok ise döndür
        print("\n❌ Aktif Görev Bulunamadı!")
        return

    print("\n" + "=" * 40)
    print("🔄 Tamamlanacak Görevler".center(40))
    print("=" * 40)

    for i, gorev in enumerate(aktif_gorevler, 1): #  aktif görevleri listele
        print(f"{i}. {gorev['baslik']} - {gorev['aciklama'] or 'Açıklama Yok!'}")
        print("-" * 40)

    try:
        secim = int(input("Tamamlanan Görevin Numarasını Giriniz: ")) # tamamlanmış olarak işaretlenecek görev numarasını al
        if 1 <= secim <= len(aktif_gorevler):
            secilen_gorev = aktif_gorevler[secim -1]

            for g in gorevler:
                if g == secilen_gorev:
                    g['durum'] = 'tamamlandi' # tamamlandı olarak işaretle
                    break # durdur

            veri_kaydet(gorevler) # güncellenmiş listeyi kaydet
            print("\n✅ Görev Tamamlandı Olarak İşaretlendi!") # bilgilendirme mesajı

        else:
            print("❌ Geçersiz Seçim!")

    except ValueError: # mevcut liste dışı seçim yapılırsa döndür
        print("❌ Geçerli Bir Seçim Yapın!") # bilgilendirme mesajı

def gorev_sil(gorevler): # görev silme fonksiyonu

    if not gorevler:
        print("❌ Silinecek Görev Yok!")
        return

    # filtrele
    aktif_gorevler = [g for g in gorevler if g["durum"] == "aktif"]
    tamamlanan_gorevler = [g for g in gorevler if g["durum"] == "tamamlandi"]

    # silinecek görevin türünün seçimini kullanıcıdan alma
    print("\nSilmek istediğiniz görev türünü seçin:")
    print("1. Aktif Görev")
    print("2. Tamamlanan Görev")

    try:
        secim_turu = int(input("Seçim (1/2): "))
        if secim_turu == 1 and aktif_gorevler:
            print("\n🗂️ Aktif Görevler")
            for i, gorev in enumerate(aktif_gorevler, 1):
                print(f"{i}. {gorev['baslik']} - {gorev['aciklama'] or 'Açıklama Yok!'}")
            secim = int(input("Silmek istediğiniz görev numarası: "))
            if 1 <= secim <= len(aktif_gorevler):
                silinecek = aktif_gorevler[secim - 1]
                gorevler.remove(silinecek) # seçilen görevi listeden sil
                veri_kaydet(gorevler)
                print("🗑️ Görev başarıyla silindi.")
            else:
                print("❌ Geçersiz görev numarası!")

        elif secim_turu == 2 and tamamlanan_gorevler:
            print("\n🗂️ Tamamlanan Görevler")
            for i, gorev in enumerate(tamamlanan_gorevler, 1):
                print(f"{i}. {gorev['baslik']} - {gorev['aciklama'] or 'Açıklama Yok!'}")
            secim = int(input("Silmek istediğiniz görev numarası: "))
            if 1 <= secim <= len(tamamlanan_gorevler):
                silinecek = tamamlanan_gorevler[secim - 1]
                gorevler.remove(silinecek)
                veri_kaydet(gorevler)
                print("🗑️ Görev başarıyla silindi.")
            else:
                print("❌ Geçersiz görev numarası!")

        else:
            print("❌ Geçersiz seçim ya da seçilen türde görev yok.")

    except ValueError:
        print("❌ Sayı girmeniz gerekiyor.")








if __name__ == "__main__": # main çalıştır
    gorevler = veri_yukle()  # verileri yükle

    # ana menü açık kalsın while true iken
    while True:
        print("\n" + "*" * 40)
        print("📋 To-Do List".center(40))
        print("*" * 40)
        print("1. ➕ Görev Ekle")
        print("2. 📄 Görevleri Listele")
        print("3. ✏️ Görevleri Düzenle")
        print("4. ✅ Görevleri Tamamla")
        print("5. 🗑️ Görevleri Sil")
        print("6. ❌ Çıkış Yap")
        print("*" * 40)

        secim = input("İlgili Başlık Numarasını Giriniz: ").strip() # ilgili görev fonksiyonunun numarsını girdi olarak kullanıcıdan alma
        if secim == "1":
            gorev_ekle(gorevler)
        elif secim == "2":
            gorev_listele(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_tamamla(gorevler)
        elif secim == "5":
            gorev_sil(gorevler)
        elif secim == "6":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Geçersiz Seçim!")