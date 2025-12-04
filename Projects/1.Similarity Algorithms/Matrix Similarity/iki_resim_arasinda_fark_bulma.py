# region Imports

import math
from tkinter import Image
import cv2
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# endregion

# region Functions

def gorselMatrisiYazdir(gorsel):
    for i in gorsel:
        for pixel in i:
            print(pixel, end=" ")
        print("\n")

def pixelFark(pixel_1, pixel_2):
    fark = 0
    for i in range(3):
        fark += abs(pixel_1[i] - pixel_2[i]) / 255
    return fark 

def farkMatris(matris1, matris2):

    yukseklik, genislik = matris1.shape[0], matris1.shape[1]
    matris = np.zeros(shape=(yukseklik, genislik, 3), dtype=np.uint8)

    for i in range(yukseklik):
        for j in range(genislik):
                if pixelFark(matris1[i][j],matris2[i][j]) == 0:
                    matris[i,j,0] = 255
                    matris[i,j,1] = 255
                    matris[i,j,2] = 255
                    continue
                else:
                    matris[i,j,0] == matris2[i][j][0]
                    matris[i,j,1] == matris2[i][j][1]
                    matris[i,j,2] == matris2[i][j][2]
                    
    img = Image.fromarray(matris, 'RGB')
    img.save('farkMatris.png')

# endregion

# region Main

gorsel_1 = cv2.imread("C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\matrix Similarity\\gorsel_1.png")
gorsel_2 = cv2.imread("C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\matrix Similarity\\gorsel_2.png")

print(gorsel_1.shape)
# Beklenen değer: (360,920,3)
print(gorsel_2.shape)
# Beklenen değer: (360,920,3)

# gorselMatrisiYazdir(gorsel_1) -> Beklenen değer: (360,920,3) 

yukseklik = gorsel_1.shape[0]
genislik = gorsel_1.shape[1]

fark = 0
for i in range(yukseklik):
    for j in range(genislik):
        fark += pixelFark(gorsel_1[i][j], gorsel_2[i][j])

farklilik_oran = 100 * fark / (genislik * yukseklik * 3)
print("İki görsel arasındaki farklılık oranı :" + str(farklilik_oran))

benzerlik_oran = 100 - farklilik_oran
print("İki görsel arasındaki benzerlik oranı :" + str(benzerlik_oran))
farkMatris(gorsel_1, gorsel_2)
print("İki görsel arasındaki farklılıklar, fark.png dosyası olarak kayıt edildi")

# endregion