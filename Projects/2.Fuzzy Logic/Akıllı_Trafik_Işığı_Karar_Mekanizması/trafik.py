import numpy as np
import fuzzyPy as fuzz
import matplotlib.pyplot as plt

# --- 1. DEĞİŞKENLERİN TANIMLANMASI ---

# GİRİŞ 1: Yol A'daki Araç Yoğunluğu (0 ile 100 araç arası)
x_Yogunluk = np.arange(0, 101, 1)

# GİRİŞ 2: Yol B'deki Bekleme Süresi (Diğer yoldakiler ne kadar süredir bekliyor? 0-60 sn)
x_Bekleme = np.arange(0, 61, 1)

# ÇIKIŞ: Yol A için Yeşil Işık Süresi (0 ile 60 saniye arası verilebilir)
x_Sure = np.arange(0, 61, 1)


# --- 2. ÜYELİK FONKSİYONLARI (Kelimeleri Sayıya Çevirme) ---

# Yol A Yoğunluğu: Az, Orta, Çok
Yogunluk_Az = fuzz.trapez(x_Yogunluk, "SOL", [20, 40])     # 0-40 arası az (20-40 arası azalıyor)
Yogunluk_Orta = fuzz.ucgen(x_Yogunluk, [20, 50, 80])       # 20-80 arası orta
Yogunluk_Cok = fuzz.trapez(x_Yogunluk, "SAG", [60, 80])    # 60'tan sonrası çok

# Yol B Bekleme: Kısa, Orta, Uzun
Bekleme_Kisa = fuzz.trapez(x_Bekleme, "SOL", [10, 25])
Bekleme_Orta = fuzz.ucgen(x_Bekleme, [15, 30, 45])
Bekleme_Uzun = fuzz.trapez(x_Bekleme, "SAG", [35, 50])

# ÇIKIŞ (Yeşil Işık Süresi): Kısa, Orta, Uzun
Sure_Kisa = fuzz.trapez(x_Sure, "SOL", [10, 25])      # Hızlıca geç (kısa yeşil)
Sure_Orta = fuzz.ucgen(x_Sure, [15, 30, 45])          # Normal süre
Sure_Uzun = fuzz.trapez(x_Sure, "SAG", [35, 50])      # Uzun süre yak


# --- 3. GRAFİKLERİ ÇİZME (Görmek için) ---
# Burası senin önceki kodunla aynı mantık, sadece isimler değişti.

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 10))

# Yoğunluk Grafiği
ax0.plot(x_Yogunluk, Yogunluk_Az, 'r', label="Az")
ax0.plot(x_Yogunluk, Yogunluk_Orta, 'g', label="Orta")
ax0.plot(x_Yogunluk, Yogunluk_Cok, 'b', label="Çok")
ax0.set_title("Giriş 1: Yol A Yoğunluğu")
ax0.legend()

# Bekleme Grafiği
ax1.plot(x_Bekleme, Bekleme_Kisa, 'r', label="Kısa")
ax1.plot(x_Bekleme, Bekleme_Orta, 'g', label="Orta")
ax1.plot(x_Bekleme, Bekleme_Uzun, 'b', label="Uzun")
ax1.set_title("Giriş 2: Yol B Bekleme Süresi")
ax1.legend()

# Çıkış Süre Grafiği
ax2.plot(x_Sure, Sure_Kisa, 'r', label="Kısa Süre")
ax2.plot(x_Sure, Sure_Orta, 'g', label="Orta Süre")
ax2.plot(x_Sure, Sure_Uzun, 'b', label="Uzun Süre")
ax2.set_title("Çıkış: Yeşil Işık Süresi")
ax2.legend()

plt.tight_layout()
plt.savefig('trafik_uyelikleri.png')
print("Grafikler kaydedildi: trafik_uyelikleri.png")


# --- 4. KULLANICIDAN VERİ ALMA ---
print("-" * 30)
print("TRAFİK KONTROL SİSTEMİNE HOŞGELDİNİZ")
print("-" * 30)

input_yogunluk = float(input("Yol A'daki araç yoğunluğu nedir? (0-100): "))
input_bekleme = float(input("Yol B'deki araçlar ne kadar süredir bekliyor? (0-60 sn): "))

# --- 5. BULANIKLAŞTIRMA (Fuzzification) ---
# Girilen sayının hangi kümeye ne kadar girdiğini hesaplıyoruz.

# Yoğunluk üyelikleri
u_yogunluk_az = fuzz.uyelik(x_Yogunluk, Yogunluk_Az, input_yogunluk)
u_yogunluk_orta = fuzz.uyelik(x_Yogunluk, Yogunluk_Orta, input_yogunluk)
u_yogunluk_cok = fuzz.uyelik(x_Yogunluk, Yogunluk_Cok, input_yogunluk)

# Bekleme üyelikleri
u_bekleme_kisa = fuzz.uyelik(x_Bekleme, Bekleme_Kisa, input_bekleme)
u_bekleme_orta = fuzz.uyelik(x_Bekleme, Bekleme_Orta, input_bekleme)
u_bekleme_uzun = fuzz.uyelik(x_Bekleme, Bekleme_Uzun, input_bekleme)

print(f"\nAnaliz: Yoğunluk üyelikleri -> Az:{u_yogunluk_az:.2f}, Orta:{u_yogunluk_orta:.2f}, Çok:{u_yogunluk_cok:.2f}")


# --- 6. KURALLAR (RULE BASE) ---
# Mantık şu:
# - Eğer Yol A çok yoğunsa VE Diğer yol az beklediyse -> Yol A'ya UZUN süre ver.
# - Eğer Yol A boşsa -> Yol A'ya KISA süre ver (Hemen diğer yola geçsin).
# - Eğer Diğer yol (B) çok beklediyse -> Yol A'ya KISA süre ver (B'ye sıra gelsin).

# Kural 1: Yol A Az Yoğun VE Yol B Uzun Bekliyor -> Süre KISA
kural1 = np.fmin(u_yogunluk_az, u_bekleme_uzun)

# Kural 2: Yol A Orta Yoğun VE Yol B Orta Bekliyor -> Süre ORTA
kural2 = np.fmin(u_yogunluk_orta, u_bekleme_orta)

# Kural 3: Yol A Çok Yoğun VE Yol B Kısa Bekliyor -> Süre UZUN
kural3 = np.fmin(u_yogunluk_cok, u_bekleme_kisa)

# Ek Kurallar (Daha hassas olması için):
# Kural 4: Yol A Çok Yoğun VE Yol B Uzun Bekliyor -> Süre ORTA (İkisi de sıkışık, adil ol)
kural4 = np.fmin(u_yogunluk_cok, u_bekleme_uzun)


# Kuralları Sonuç Kümelerine Bağlama (Kesme İşlemi)
# Hangi kural hangi çıkışı tetikliyor?
out_kisa_aktivasyon = np.fmin(kural1, Sure_Kisa) # Kural 1 çalışırsa Kısa Süre grafiğini kes
out_orta_aktivasyon = np.fmin(np.fmax(kural2, kural4), Sure_Orta) # Kural 2 veya 4 çalışırsa Orta Süre
out_uzun_aktivasyon = np.fmin(kural3, Sure_Uzun) # Kural 3 çalışırsa Uzun Süre


# --- 7. BİRLEŞTİRME VE DURULAŞTIRMA (Aggregation & Defuzzification) ---

# Tüm çıktı grafiklerini birleştir (Maximum alarak yığın oluştur)
bilesik_sonuc = np.fmax(out_kisa_aktivasyon, np.fmax(out_orta_aktivasyon, out_uzun_aktivasyon))

# Ağırlık Merkezini Hesapla (Crisp Output)
sonuc_saniye = fuzz.durulastir(x_Sure, bilesik_sonuc, 'agirlik_merkezi')

print("\n" + "="*40)
print(f"HESAPLANAN YEŞİL IŞIK SÜRESİ: {sonuc_saniye:.2f} Saniye")
print("="*40)

# --- 8. SONUÇ GRAFİĞİ ---
# Sonucun grafikte gösterimi (Dolu alanları boyama)

fig, ax_sonuc = plt.subplots(figsize=(7, 4))

ax_sonuc.plot(x_Sure, Sure_Kisa, 'r', linestyle='--', linewidth=0.5)
ax_sonuc.plot(x_Sure, Sure_Orta, 'g', linestyle='--', linewidth=0.5)
ax_sonuc.plot(x_Sure, Sure_Uzun, 'b', linestyle='--', linewidth=0.5)

# Çıkan birleşik alanı boya
ax_sonuc.fill_between(x_Sure, 0, bilesik_sonuc, facecolor='orange', alpha=0.7)
# Ağırlık merkezini çizgiyle göster
ax_sonuc.vlines(sonuc_saniye, 0, 1, colors='k', linestyles='solid', linewidth=2, label="Sonuç")

ax_sonuc.set_title(f'Sonuç: {sonuc_saniye:.2f} sn Yeşil Işık')
ax_sonuc.legend()

plt.tight_layout()
plt.savefig('trafik_sonuc.png')
print("Sonuç grafiği kaydedildi: trafik_sonuc.png")