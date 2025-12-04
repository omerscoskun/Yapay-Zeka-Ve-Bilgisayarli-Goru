# region Imports

import numpy as np

# endregion

# region Definitions

def arrange (item, dimension, min, max):

    item_count,i = len(item),0

    for i in range(dimension):
        if i <= item_count:
            item[i] = item[i] / ((max - min) / 100) # Percent Value
        else:
            item[i] = 50 / ((max - min) / 100) # Default Value
    return item

def kokal (x):
    return x**(1/2)

def usal (x,y):
    return x**y

def vectorSimilarity (A,B):
    
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] - (A[i]),2)
        distance =  kokal(total)

    max_distance = 0
    for i in range(len_):
        max_distance += usal(100,2)
    max_distance = kokal(max_distance)

    return 1 - (distance / max_distance)

# endregion

kirmizi = [255,0,0]
koyuKirmizi = [181,25,25]
kahverengi = [48,34,15]
siyah = [0,0,0]
beyaz = [255,255,255]
gri = [128,128,128]

kirmizi_normalized = arrange(kirmizi,3,0,255)
koyuKirmizi_normalized = arrange(koyuKirmizi,3,0,255)
kahverengi_normalized = arrange(kahverengi,3,0,255)
siyah_normalized = arrange(siyah,3,0,255)
beyaz_normalized = arrange(beyaz,3,0,255)
gri_normalized = arrange(gri,3,0,255)

benzerlik_orani = vectorSimilarity(kirmizi_normalized,koyuKirmizi_normalized)
print("Kırmızı ile Koyu Kırmızı arasındaki renk benzerlik oranı: ",benzerlik_orani) # Cevap yaklaşık %81 gelecektir.

benzerlik_orani = vectorSimilarity(siyah_normalized,beyaz_normalized)
print("Siyah ile Beyaz arasındaki renk benzerlik oranı: ",benzerlik_orani) # Cevap yaklaşık %0 gelecektir.

benzerlik_orani = vectorSimilarity(siyah_normalized,gri_normalized)
print("Siyah ile Gri arasındaki renk benzerlik oranı: ",benzerlik_orani) # Cevap yaklaşık %0 gelecektir.