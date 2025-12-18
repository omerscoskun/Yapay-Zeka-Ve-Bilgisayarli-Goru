import numpy as np
import fuzzyPy as fuzz
import matplotlib.pyplot as plt

# --- 1. GİRİŞ DEĞİŞKENLERİ VE ARALIKLARI ---
# Sugeno'da çıkış aralığı tanımlamaya gerek yoktur, çünkü sonuç matematiktir.

x_Yogunluk = np.arange(0, 101, 1) # 0-100 arası araç yoğunluğu
x_Bekleme = np.arange(0, 61, 1)   # 0-60 saniye bekleme süresi

# --- 2. GİRİŞ ÜYELİK FONKSİYONLARI (Fuzzification) ---
# Burası Mamdani ile AYNI. Girdiyi yine "Az", "Uzun" diye etiketlememiz lazım.

# Yol A Yoğunluğu
Yogunluk_Az = fuzz.trapez(x_Yogunluk, "SOL", [20, 40])
Yogunluk_Orta = fuzz.ucgen(x_Yogunluk, [20, 50, 80])
Yogunluk_Cok = fuzz.trapez(x_Yogunluk, "SAG", [60, 80])

# Yol B Bekleme
Bekleme_Kisa = fuzz.trapez(x_Bekleme, "SOL", [10, 25])
Bekleme_Orta = fuzz.ucgen(x_Bekleme, [15, 30, 45])
Bekleme_Uzun = fuzz.trapez(x_Bekleme, "SAG", [35, 50])

# --- 3. KULLANICIDAN VERİ ALMA ---
print("-" * 40)
print("AKILLI TRAFİK SİSTEMİ (SUGENO MODELİ)")
print("-" * 40)

input_yogunluk = float(input("Yol A Yoğunluğu (0-100): "))
input_bekleme = float(input("Yol B Bekleme Süresi (0-60): "))

# --- 4. BULANIKLAŞTIRMA ---
u_yogunluk_az = fuzz.uyelik(x_Yogunluk, Yogunluk_Az, input_yogunluk)
u_yogunluk_orta = fuzz.uyelik(x_Yogunluk, Yogunluk_Orta, input_yogunluk)
u_yogunluk_cok = fuzz.uyelik(x_Yogunluk, Yogunluk_Cok, input_yogunluk)

u_bekleme_kisa = fuzz.uyelik(x_Bekleme, Bekleme_Kisa, input_bekleme)
u_bekleme_orta = fuzz.uyelik(x_Bekleme, Bekleme_Orta, input_bekleme)
u_bekleme_uzun = fuzz.uyelik(x_Bekleme, Bekleme_Uzun, input_bekleme)
print(f"\nÜyelik Değerleri -> Y_Az:{u_yogunluk_az:.2f}, Y_Orta:{u_yogunluk_orta:.2f}, Y_Çok:{u_yogunluk_cok:.2f}")

# --- 5. KURALLAR VE AĞIRLIK HESABI (W) ---
# Mamdani'de 'kesme' yapıyorduk, Sugeno'da kuralın 'ateşleme gücünü' (weight - w) buluyoruz.

# Kural 1: Yol A Az Yoğun VE Yol B Uzun Bekliyor -> Çıktı: KISA_SURE
# Operatör: VE (Min)
w1 = np.fmin(u_yogunluk_az, u_bekleme_uzun)
z1 = fuzz.sugeno_output_hesapla(input_yogunluk, input_bekleme, "KISA_SURE")

# Kural 2: Yol A Orta Yoğun -> Çıktı: ORTA_SURE
# Basit kural: Sadece A'nın orta olmasına bakalım.
w2 = u_yogunluk_orta
z2 = fuzz.sugeno_output_hesapla(input_yogunluk, input_bekleme, "ORTA_SURE")

# Kural 3: Yol A Çok Yoğun VE Yol B Kısa Bekliyor -> Çıktı: UZUN_SURE
w3 = np.fmin(u_yogunluk_cok, u_bekleme_kisa)
z3 = fuzz.sugeno_output_hesapla(input_yogunluk, input_bekleme, "UZUN_SURE")

# Kural 4: Yol A Çok Yoğun VE Yol B Uzun Bekliyor -> Çıktı: ORTA_SURE (Uzlaşma)
w4 = np.fmin(u_yogunluk_cok, u_bekleme_uzun)
z4 = fuzz.sugeno_output_hesapla(input_yogunluk, input_bekleme, "ORTA_SURE")

# --- 6. SUGENO DURULAŞTIRMA (Ağırlıklı Ortalama) ---
# Formül: (w1*z1 + w2*z2 + ...) / (w1 + w2 + ...)

toplam_agirlik = w1 + w2 + w3 + w4
toplam_deger = (w1 * z1) + (w2 * z2) + (w3 * z3) + (w4 * z4)

print("\n--- Kural Analizi ---")
print(f"Kural 1 (Kısa)   -> Ateşleme(w): {w1:.2f} | Çıkış(z): {z1:.2f}")
print(f"Kural 2 (Orta)   -> Ateşleme(w): {w2:.2f} | Çıkış(z): {z2:.2f}")
print(f"Kural 3 (Uzun)   -> Ateşleme(w): {w3:.2f} | Çıkış(z): {z3:.2f}")
print(f"Kural 4 (Uzlaşma)-> Ateşleme(w): {w4:.2f} | Çıkış(z): {z4:.2f}")

if toplam_agirlik == 0:
    # Hiçbir kural çalışmadıysa güvenli bir varsayılan değer
    sonuc = 15.0
    print("Uyarı: Hiçbir kural tetiklenmedi, varsayılan değer atandı.")
else:
    sonuc = toplam_deger / toplam_agirlik

print("\n" + "="*40)
print(f"SUGENO SONUCU (Yeşil Işık): {sonuc:.2f} Saniye")
print("="*40)

# --- 7. Görselleştirme (Opsiyonel) ---
# Sugeno'da çıkış alanı boyanmaz, ama girişleri görebiliriz.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 6))

ax0.plot(x_Yogunluk, Yogunluk_Az, 'r', label="Az")
ax0.plot(x_Yogunluk, Yogunluk_Orta, 'g', label="Orta")
ax0.plot(x_Yogunluk, Yogunluk_Cok, 'b', label="Çok")
ax0.vlines(input_yogunluk, 0, 1, colors='k', linestyles='dashed')
ax0.set_title("Giriş 1: Yoğunluk")
ax0.legend()

ax1.plot(x_Bekleme, Bekleme_Kisa, 'r', label="Kısa")
ax1.plot(x_Bekleme, Bekleme_Orta, 'g', label="Orta")
ax1.plot(x_Bekleme, Bekleme_Uzun, 'b', label="Uzun")
ax1.vlines(input_bekleme, 0, 1, colors='k', linestyles='dashed')
ax1.set_title("Giriş 2: Bekleme")
ax1.legend()

plt.tight_layout()
plt.savefig('sugeno_girisler.png')
print("Giriş grafiği kaydedildi.")