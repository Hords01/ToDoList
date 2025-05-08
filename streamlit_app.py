import streamlit as st # web tabanlı arayüz için
from veri_isleme import veri_yukleme, veri_kaydetme # veri yükleme ve veri kaydetme fonksiyonlarını içe aktarma

st.set_page_config(page_title="To-Do List", page_icon="🗂️") # sayfa başlığı ve simgesi ayarlaması

st.title("🗂️ Görev Yönetim Sistemi") # başlık arayüzde görüntüleme

gorevler = veri_yukleme() # görev verileri yüklemesi

# görevlerin filtrelenmesi
aktif_gorevler = [g for g in gorevler if g["durum"] == "aktif"]
tamamlanan_gorevler = [g for g in gorevler if g["durum"] == "tamamlandi"]

# yeni görev ekleme fonksiyonu için alt başlık
st.subheader("➕ Yeni Görev Ekle")
with st.form("gorev_ekleme"): # yeni görev eklemek için, form başlatılması
    baslik = st.text_input("Görev Başlığı") # kullanıcıdan görev başlığı almak
    aciklama = st.text_area("Açıklama") # kullanıcıdan açıklma alma
    ekle = st.form_submit_button("Görev Ekle") # alınan bilgilerin forma işlenmesi için buton

    if ekle and baslik.strip(): # yeni görev görevler listesine eklenir
        gorevler.append({"baslik": baslik, "aciklama": aciklama, "durum": "aktif"})
        veri_kaydetme(gorevler)
        st.success("Görev Eklendi. Sayfayı yenileyin veya sidebar kısmından tekrar açın.")

st.subheader("📌 Aktif Görevler") # aktif görevlerin listelenmesi
for i, gorev in enumerate(aktif_gorevler): # aktif görevler için görev döngüsü
    with st.expander(f"{gorev['baslik']}"): #  görev başlığına göre genişleyebilen dinamik bir başlık kutusu expander ile oluşturulur
        st.write(gorev["aciklama"] or "_(Açıklama Yok)_")
        col1, col2 = st.columns(2) # iki sütun oluşturma
        if col1.button("✅ Tamamla", key=f"tamamla_{i}"): # 1.sütun tamamla butonu için
            gorev["durum"] = "tamamlandi"
            veri_kaydetme(gorevler)
            st.rerun()
        if col2.button("🗑️ Görev Sil", key=f"sil_{i}"): # 2. sütun görev silme butonu için
            gorevler.remove(gorev) # sil
            veri_kaydetme(gorevler) # kaydet
            st.rerun() # yenile

st.subheader("✅ Tamamlanan Görevler") # tamamlanan görevler için alt başlık
for i, gorev in enumerate(tamamlanan_gorevler):
    with st.expander(f"{gorev['baslik']}"):
        st.write(gorev["aciklama"] or "_(Açıklama Yok)_")
        if st.button("🗑️ Görev Sil", key=f"sil_tamam_{i}"):
            gorevler.remove(gorev)
            veri_kaydetme(gorevler)
            st.rerun()