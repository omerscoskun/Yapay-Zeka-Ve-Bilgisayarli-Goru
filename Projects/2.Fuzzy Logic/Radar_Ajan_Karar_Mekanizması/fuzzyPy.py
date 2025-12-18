import numpy as np

# --- Temel Fonksiyonlar (Aynen Kalıyor) ---
def trapez(x,rot,abc):
    y = np.zeros(len(x))
    if(rot == "ORTA"):
        assert len(abc) == 3, 'Hata'
        a, b, c = np.r_[abc]
        idx = np.nonzero(np.logical_and(x >= 0, x < a))[0]
        y[idx] = (x[idx] ) / float(a)
        idx = np.nonzero(np.logical_and(x >= a, x <b))[0]
        y[idx] = 1
        idx = np.nonzero(np.logical_and(x >= b, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
        return y
    else:
        assert len(abc) == 2, 'Hata'
        a, b = np.r_[abc]
        if( rot == "SOL"):
            idx = np.nonzero(x < a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
            y[idx] = (x[idx] - b) / float(a - b)
            return y        
        elif (rot == "SAG"):
            idx = np.nonzero(x > a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x > a, x <= b))[0]
            y[idx] = (x[idx] - a) / float(b - a)
            return y        

def ucgen(x, abc):
    a, b, c = np.r_[abc]
    y = np.zeros(len(x))
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
    idx = np.nonzero(x == b)
    y[idx] = 1
    return y

def uyelik(x, xmf, xx, zero_outside_x=True):
    kwargs = (0.0, 0.0) if zero_outside_x else (None, None)
    return np.interp(xx, x, xmf, left=kwargs[0], right=kwargs[1])

def durulastir(x, LFX, model='agirlik_merkezi'):
    # Basitleştirilmiş hali
    sum_moment_area = 0.0
    sum_area = 0.0
    if len(x) == 1:
        return x[0]*LFX[0] / np.fmax(LFX[0], np.finfo(float).eps).astype(float)
    
    for i in range(1, len(x)):
        x1 = x[i - 1]
        x2 = x[i]
        y1 = LFX[i - 1]
        y2 = LFX[i]
        if not(y1 == y2 == 0.0 or x1 == x2):
            if y1 == y2:
                moment = 0.5 * (x1 + x2)
                area = (x2 - x1) * y1
            elif y1 == 0.0 and y2 != 0.0:
                moment = 2.0 / 3.0 * (x2-x1) + x1
                area = 0.5 * (x2 - x1) * y2
            elif y2 == 0.0 and y1 != 0.0:
                moment = 1.0 / 3.0 * (x2 - x1) + x1
                area = 0.5 * (x2 - x1) * y1
            else:
                moment = (2.0 / 3.0 * (x2-x1) * (y2 + 0.5*y1)) / (y1+y2) + x1
                area = 0.5 * (x2 - x1) * (y1 + y2)
            sum_moment_area += moment * area
            sum_area += area
    return sum_moment_area / np.fmax(sum_area, np.finfo(float).eps).astype(float)


# --- SİSTEM HESAPLA ---
def sistem_hesapla(input_R, input_W, input_S, input_E, p_O_az, p_O_ort, p_O_cok):
    x_R = np.arange(0, 91, 1)
    x_W = np.arange(0, 11, 1)
    x_S = np.arange(0, 151, 1)
    x_E = np.arange(0, 21, 1)
    x_O = np.arange(0, 140, 1)

    # Girişler
    R_kotu = trapez(x_R, "SOL", [30, 45])
    R_normal = ucgen(x_R, [30, 45, 60])
    R_iyi = trapez(x_R, "SAG", [45, 60])

    W_kotu = ucgen(x_W, [0, 0, 5])
    W_normal = ucgen(x_W, [0, 5, 10])
    W_iyi = ucgen(x_W, [5, 10, 10])
    
    S_az = ucgen(x_S, [0, 0, 70])
    S_ort = ucgen(x_S, [0, 70, 130])
    S_cok = trapez(x_S, "SAG", [70, 130])

    E_az = ucgen(x_E, [0, 0, 10])
    E_ort = ucgen(x_E, [0, 10, 20])
    E_cok = ucgen(x_E, [10, 20, 20])

    # Çıkışlar (Parametrik)
    O_az = trapez(x_O, "SOL", p_O_az)
    O_ort = ucgen(x_O, p_O_ort)
    O_cok = trapez(x_O, "SAG", p_O_cok)

    # Bulanıklaştırma
    R_fit_kotu = uyelik(x_R, R_kotu, input_R)
    R_fit_normal = uyelik(x_R, R_normal, input_R)
    R_fit_iyi = uyelik(x_R, R_iyi, input_R)

    W_fit_kotu = uyelik(x_W, W_kotu, input_W)
    W_fit_normal = uyelik(x_W, W_normal, input_W)
    W_fit_iyi = uyelik(x_W, W_iyi, input_W)

    S_fit_az = uyelik(x_S, S_az, input_S)
    S_fit_ortalama = uyelik(x_S, S_ort, input_S)
    S_fit_cok = uyelik(x_S, S_cok, input_S)

    E_fit_az = uyelik(x_E, E_az, input_E)
    E_fit_ortalama = uyelik(x_E, E_ort, input_E)
    E_fit_cok = uyelik(x_E, E_cok, input_E)

    # Kurallar
    rule1 = np.fmin(np.fmin(R_fit_kotu, W_fit_kotu), O_az)
    rule2 = np.fmin(np.fmin(R_fit_normal, W_fit_normal), O_ort)
    rule3 = np.fmin(np.fmin(R_fit_iyi, W_fit_iyi), O_cok)
    rule4 = np.fmin(np.fmax(S_fit_az, E_fit_az), O_az)
    rule5 = np.fmin(np.fmax(S_fit_ortalama, E_fit_ortalama), O_ort)
    rule6 = np.fmin(np.fmax(S_fit_cok, E_fit_cok), O_cok)

    out_az = np.fmax(rule1, rule4)
    out_ortalama = np.fmax(rule2, rule5)
    out_cok = np.fmax(rule3, rule6)

    mutlak_bulanik_sonuc = np.fmax(out_az, np.fmax(out_ortalama, out_cok))
    durulastirilmis_sonuc = durulastir(x_O, mutlak_bulanik_sonuc, 'agirlik_merkezi')
    
    return durulastirilmis_sonuc

# --- AJAN FONKSİYONU (GÜNCELLENDİ) ---
def ajan_optimizasyon(OGRENME_ORANI, p_O_az, p_O_ort, p_O_cok):
    """
    Kullanıcı geri bildirimine göre sınırları günceller ve GERİ DÖNDÜRÜR.
    """
    print("\n--- [AJAN] OPTİMİZASYON BAŞLATILIYOR ---")
    print("Sistem eleştirildi. Sınır değerleri gevşetiliyor...")
    
    # Listeler güncelleniyor
    p_O_az = [x + OGRENME_ORANI for x in p_O_az]
    p_O_ort = [x + OGRENME_ORANI for x in p_O_ort]
    p_O_cok = [x + OGRENME_ORANI for x in p_O_cok]
    
    print(f"Yeni Parametreler -> Az: {p_O_az}, Orta: {p_O_ort}, Çok: {p_O_cok}")
    print("Sistem güncellendi.\n")
    
    # !!! ÖNEMLİ: Yeni değerleri ana programa geri gönderiyoruz !!!
    return p_O_az, p_O_ort, p_O_cok