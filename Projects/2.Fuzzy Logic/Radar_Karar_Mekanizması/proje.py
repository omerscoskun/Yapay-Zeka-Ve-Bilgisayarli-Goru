import numpy as np
import fuzzyPy as fuzz
import matplotlib.pyplot as plt

# input degerlerin tanimli oldugu araliklar
x_R = np.arange(0,91,1)
x_W = np.arange(0,11,1)
x_S = np.arange(0,151,1)
x_E = np.arange(0,21,1)

# output degerlerin tanimli oldugu araliklar
x_Out = np.arange(0,101,1)

# Yol Yapısı Üyelik Fonksiyonları
R_kotu = fuzz.trapez(x_R,"SOL",[30,45])
R_normal = fuzz.ucgen(x_R,[30,45,60])
R_iyi = fuzz.trapez(x_R,"SAG",[45,60])

# Hava Durumu Üyelik Fonksiyonları
W_kotu = fuzz.ucgen(x_W,[0,0,5])
W_normal = fuzz.ucgen(x_W,[0,5,10])
W_iyi = fuzz.ucgen(x_W,[5,10,10])

# Ortalama Hız Üyelik Fonksiyonları
S_az = fuzz.ucgen(x_S,[0,0,70])
S_ort = fuzz.ucgen(x_S,[0,70,130])
s_cok = fuzz.trapez(x_S,"SAG",[70,130])

# Kullanıcı Tecrübesi Üyelik Fonksiyonları
E_az = fuzz.ucgen(x_E,[0,0,10])
E_ort = fuzz.ucgen(x_E,[0,10,20])
E_cok = fuzz.ucgen(x_E,[10,20,20])

# Çıkış Kümeleri
O_az = fuzz.trapez(x_Out,"SOL",[25,50])
O_orta = fuzz.ucgen(x_Out,[25,50,85])
O_cok = fuzz.trapez(x_Out,"SAG",[50,85])

# Grafik Çizimleri
fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(6, 10))

# Yol Yapısı için Grafik
ax0.plot(x_R, R_kotu, 'r', linewidth=2, label="Kötü")
ax0.plot(x_R, R_normal, 'g', linewidth=2, label="Normal")
ax0.plot(x_R, R_iyi, 'b', linewidth=2, label="İyi")
ax0.set_title("Yol viraj ve eğimi")
ax0.legend()

# Hava Şartları için Grafik
ax1.plot(x_W, W_kotu, 'r', linewidth=2, label="Kötü")
ax1.plot(x_W, W_normal, 'g', linewidth=2, label="Normal")
ax1.plot(x_W, W_iyi, 'b', linewidth=2, label="İyi")
ax1.set_title("Hava Şartları")
ax1.legend()

# sürücü Ortalama Hız için Grafik
ax2.plot(x_S, S_az, 'r', linewidth=2, label="Az")
ax2.plot(x_S, S_ort, 'g', linewidth=2, label="Orta")
ax2.plot(x_S, s_cok, 'b', linewidth=2, label="Çok")
ax2.set_title("Sürücü Ortalama Hızı (km/h)")
ax2.legend()

# Kullanıcı Tecrübesi için Grafik
ax3.plot(x_E, E_az, 'r', linewidth=2, label="Az")
ax3.plot(x_E, E_ort, 'g', linewidth=2, label="Orta")
ax3.plot(x_E, E_cok, 'b', linewidth=2, label="Çok")
ax3.set_title("Kullanıcı Tecrübesi (Yıl)")
ax3.legend()

# Çıkış Hız Sınırı için Grafik
ax4.plot(x_Out, O_az, 'r', linewidth=2, label="Az")
ax4.plot(x_Out, O_orta, 'g', linewidth=2, label="Orta")
ax4.plot(x_Out, O_cok, 'b', linewidth=2, label="Çok")
ax4.set_title("Önerilen Hız Sınırı (km/h)")
ax4.legend()

plt.tight_layout()
plt.savefig('fuzzy_membership.png')