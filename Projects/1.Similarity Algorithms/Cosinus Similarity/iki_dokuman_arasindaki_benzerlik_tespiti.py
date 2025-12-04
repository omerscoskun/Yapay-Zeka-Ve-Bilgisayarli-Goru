# region Imports

import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from nltk import download

# endregion

# region Definitions



# endregion

# region Main



# endregion

# region Tests

stop_words = stopwords.words('turkish')

model = KeyedVectors.load_word2vec_format('C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\Cosinus Similarity\\trmodel', binary=True)
model2 = KeyedVectors.load_word2vec_format('C:\\Users\\ASUS\\Desktop\\python_calismalari\\.resources\\2. Projeler\\Cosinus Similarity\\trmodel', binary=True)
print("\n")

# Similarity Model Yükleme
benzerlik = model.similarity("çay", "araba")
print("Çay-Araba Benzerliği: " + str(benzerlik))
print("\n")

# Most Similar Words
benzerler = model.most_similar("çay")
print("Çaya en benzer kelimeler:" + str(benzerler))
print("\n")

# Pozlamalı Most Similar Words

benzerler_pozlamali = model.most_similar(positive=["kral", "kadın"], negative=["adam"])
print("Pozlamalı Benzer Kelimeler (kral + kadın - adam): " + str(benzerler_pozlamali))
print("\n")

# Doesn't Match Fonksiyonu
uyumsuz_kelime = model.doesnt_match("elma muz portakal araba".split())
print("Uyumsuz Kelime: " + str(uyumsuz_kelime))
print("\n")

# WM Mesafesi Algoritması ile Cümele Benzerliği Hesaplama

cumle_1 = 'Galatasaray Fenerbahçe maçı kaç kaç bitti'.lower().split()
cumle_2 = 'Bu yıl Beşiktaş şampiyon olur'.lower().split()
mesafe = model2.wmdistance(cumle_1, cumle_2)
print(mesafe)
print("\n")

# endregion

