# 🗂️ Görev Yönetim Sistemi (To-Do List)

Bu proje, iki farklı şekilde görev takibi yapımına olanak tanır:

- **Konsol tabanlı kullanım (`main.py`)**
- **Web arayüzlü kullanım (`streamlit_app.py`)**

Her iki uygulama da görevleri JSON formatında kaydeder ve işler. Konsol ve web sürümleri farklı veri dosyaları kullanır ve birbirinden bağımsız çalışır.
Dosyalar Yerel Olarak Kaydedilir ve uygulamadan çıkılması halinde json formatında ki veriler kaybedilmez.

---

## 🚀 Özellikler

### ✅ Ortak Özellikler

- Görev ekleme
- Görevleri Listeleme
- Görevleri Tamamlama
- Görevleri Düzenleme
- Görevleri silme
- JSON tabanlı veri saklama

---

## 🧱 Proje Yapısı
```
📦 ToDoList/
├── main.py # Konsol tabanlı görev yöneticisi
├── streamlit_app.py # Web tabanlı görev yöneticisi (Streamlit)
├── veri_isleme.py # JSON veri işlemleri modülü
├── konsol_gorevler.json # Konsol uygulamasına ait veri dosyası
└── gorevler.json # Web arayüzüne ait veri dosyası
```

## 🖥️ Konsol Uygulaması (`main.py`)

- **Kullanım:** Terminal/Konsol üzerinden görev yönetimi sağlar.
- **Veri Dosyası:** `konsol_gorevler.json`

> Konsol uygulaması basit ve hızlı bir görev yönetimi deneyimi sunar.

---

## 🌐 Web Uygulaması (`streamlit_app.py` + `veri_isleme.py`)

- **Kullanım:** Streamlit tabanlı etkileşimli web arayüzü.
- **Veri Dosyası:** `gorevler.json`
- **Bağımlı Dosya:** `veri_isleme.py` – Görev verilerini yükleme ve kaydetme işlemlerini yapar.

### Web Arayüzünü Başlatmak İçin:
```bash
streamlit run Streamlit_app.py
