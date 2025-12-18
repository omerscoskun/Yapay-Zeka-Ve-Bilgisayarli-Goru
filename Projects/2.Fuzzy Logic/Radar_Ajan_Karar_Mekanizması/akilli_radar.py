import fuzzyPy as fuzz

# --- Çıkış Hız Sınırı Parametreleri (Daha gerçekçi değerler) ---
p_O_az = [40, 70]       
p_O_ort = [60, 90, 120]  
p_O_cok = [100, 130]      

# Optimizasyon (Eğitim) Katsayısı
OGRENME_ORANI = 5 

# ================= ANA PROGRAM =================
print("-" * 40)
print("RADAR KARAR MEKANİZMASI (AJAN DESTEKLİ)")
print("-" * 40)

# Kullanıcı Girişleri
try:
    in_R = float(input("Yol viraj düzeyi (0-90): "))
    in_W = float(input("Hava durumu (0-10): "))
    in_S = float(input("Sürücü ortalama hızı (30-150): "))
    in_E = float(input("Kullanıcı deneyim yılı (0-20): "))
    in_AnlikHiz = float(input("Aracın Şu Anki Hızı (km/h): "))
except ValueError:
    print("Lütfen sayısal değer girin!")
    exit()

# 1. HESAPLAMA 
hesaplanan_sinir = fuzz.sistem_hesapla(in_R, in_W, in_S, in_E, p_O_az, p_O_ort, p_O_cok)

print(f"\n[SİSTEM] Hesaplanan Hız Sınırı: {hesaplanan_sinir:.2f} km/h")
print(f"[ARAÇ]   Aracın Anlık Hızı:     {in_AnlikHiz:.2f} km/h")

# Ceza Kontrolü
if in_AnlikHiz > hesaplanan_sinir:
    fark = in_AnlikHiz - hesaplanan_sinir
    ceza_tutar = fark * 10 
    
    print("\n" + "!"*40)
    print(f"CEZA YAZILDI! Hız sınırını {fark:.2f} km/h aştınız.")
    print(f"Tutar: {ceza_tutar:.2f} TL")
    print("!"*40)
    
    # --- AJAN DEVREYE GİRİYOR ---
    geri_bildirim = input("\n[AJAN]: Bu cezanın yasal/adil olduğunu düşünüyor musunuz? (E/H): ").lower()
    
    if geri_bildirim == 'h':
        # !!! ÖNEMLİ: Fonksiyondan dönen yeni değerleri buradaki değişkenlere kaydediyoruz !!!
        p_O_az, p_O_ort, p_O_cok = fuzz.ajan_optimizasyon(OGRENME_ORANI, p_O_az, p_O_ort, p_O_cok)
        
        # Sistemi YENİ parametrelerle tekrar çalıştırıp farkı gösterelim
        yeni_sinir = fuzz.sistem_hesapla(in_R, in_W, in_S, in_E, p_O_az, p_O_ort, p_O_cok)
        
        print(f"[SİSTEM] Optimizasyon Sonrası Yeni Hız Sınırı: {yeni_sinir:.2f} km/h")
        
        if in_AnlikHiz <= yeni_sinir:
            print("[AJAN] Mutlu haber! Yeni kurallara göre ceza iptal edildi.")
        else:
            print(f"[AJAN] Sistem esnetildi ama hızınız hala çok yüksek. ({in_AnlikHiz} > {yeni_sinir:.2f})")
            
    else:
        print("[AJAN]: Geri bildiriminiz için teşekkürler. Sistem stabil kalacak.")

else:
    print("\n[SİSTEM] Hızınız yasal sınırlar içinde. İyi yolculuklar.")