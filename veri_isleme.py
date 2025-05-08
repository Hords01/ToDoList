import json
import os

dosya_isim = "gorevler.json"

def veri_yukleme():
    if not os.path.exists(dosya_isim):
        return []
    with open(dosya_isim, "r", encoding="utf-8") as dosya:
        return json.load(dosya)

def veri_kaydetme(gorevler):
    with open(dosya_isim, "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4)

