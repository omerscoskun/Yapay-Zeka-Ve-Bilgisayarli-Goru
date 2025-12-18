import numpy as np

def trapez(x,rot,abc):

    y = np.zeros(len(x))

    if(rot == "ORTA"):
        assert len(abc) == 3, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
        a, b, c = np.r_[abc]
        assert a <= b and b <= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
        
        idx = np.nonzero(np.logical_and(x >= 0, x < a))[0]
        y[idx] = (x[idx] ) / float(a)

        idx = np.nonzero(np.logical_and(x >= a, x <b))[0]
        y[idx] = 1

        idx = np.nonzero(np.logical_and(x >= b, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

        print("!")
        return y

    else:
        assert len(abc) == 2, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
        a, b = np.r_[abc]     # Zero-indexing in Python
        if( rot == "SOL"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
            idx = np.nonzero(x < a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
            y[idx] = (x[idx] - b) / float(a - b)
            return y        
        elif (rot == "SAG"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
            idx = np.nonzero(x > a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x > a, x <= b))[0]
            y[idx] = (x[idx] - a) / float(b - a)
            return y        

def ucgen(x, abc):

    # a <= b <= c olmalıdır
    assert len(abc) == 3, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
    a, b, c = np.r_[abc]     # Zero-indexing in Python
    assert a <= b and b <= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
    
    y = np.zeros(len(x))

    # Sol
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    # Sağ
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

    idx = np.nonzero(x == b)
    y[idx] = 1
    return y

#Gerçek bir değerin bir üyelik fonksiyonuna olan üyelik degerini hesaplayan fonksiyon
def uyelik(x, xmf, xx, zero_outside_x=True):
    if not zero_outside_x:
        kwargs = (None, None)
    else:
        kwargs = (0.0, 0.0)
    # Numpy'in İnterpolasyon Fonksiyonu:
    return np.interp(xx, x, xmf, left=kwargs[0], right=kwargs[1])


# --- SUGENO ÇIKIŞ FONKSİYONLARI (POLİNOMLAR) ---
# Hocanın istediği kısım burası. Çıkışlar birer formül olacak.
# z = p*x + q*y + r (Birinci dereceden Sugeno Modeli)

def sugeno_output_hesapla(yogunluk_degeri, bekleme_degeri, kural_tipi):
    """
    Bu fonksiyon, o anki giriş değerlerine göre çıkış polinomunu hesaplar.
    """
    z = 0
    if kural_tipi == "KISA_SURE":
        # Polinom 1: Sabit veya çok basit denklem.
        # Trafik azsa, yoğunluk ne olursa olsun minimum süre ver.
        # Denklem: z = 10 (Sabit)
        z = 10 
        
    elif kural_tipi == "ORTA_SURE":
        # Polinom 2: Girişlere bağlı lineer denklem.
        # Trafik arttıkça süre biraz artsın.
        # Denklem: z = 15 + (0.2 * Yogunluk)
        z = 15 + (0.2 * yogunluk_degeri)
        
    elif kural_tipi == "UZUN_SURE":
        # Polinom 3: Daha agresif bir denklem.
        # Hem yoğunluk hem bekleme süresi hesaba katılsın.
        # Denklem: z = 20 + (0.4 * Yogunluk) - (0.1 * Bekleme)
        # Not: Bekleme arttıkça süreyi biraz kısıyoruz ki diğer tarafa ayıp olmasın.
        z = 20 + (0.4 * yogunluk_degeri) - (0.1 * bekleme_degeri)
        
        # Sonucun negatif çıkmasını veya mantıksız olmasını engellemek için sınır koyabiliriz
        if z > 90: z = 90
        
    return z