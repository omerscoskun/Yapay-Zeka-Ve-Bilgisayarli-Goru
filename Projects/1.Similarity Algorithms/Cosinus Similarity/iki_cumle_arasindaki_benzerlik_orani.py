# region Imports

# endregion

# region Definitions

def stopWord(kelime):
    stopWords = ["acaba", "ama", "aslında", "az", "bazı", "belki", "biri", "birkaç", "birşey", "biz", "bu",
                 "çok", "çünkü", "da", "daha", "de", "defa", "diye", "eğer", "en", "gibi", "hem",
                 "hep", "hepsi", "her", "hiç", "için", "ile", "ise", "kez", "ki", "kim", "mı",
                 "mi", "mu", "mü", "nasıl", "ne", "neden", "nerde", "nerede", "nereye", "niçin",
                 "niye", "o", "sanki", "şey", "şu", "tüm", "ve", "veya", "ya", "yani"]
    flag = True
    for i in range(len(stopWords)):
        if stopWords[i] == kelime:
            return True
        else:
            flag = False   
    return flag

def ara(dizi, kelime):
    flag = False
    for eleman in dizi:
        if eleman == kelime:
            return True
        else:
            flag = False
    return flag

def sozlukOku(dizi):
    sozluk = []
    for cumle in dizi:
        kelimeler = cumle.split(" ")
        for kelime in kelimeler:
            if stopWord(kelime):
                continue
            else:
                if len(sozluk) == 0:
                    sozluk.append(kelime)
                else:
                    if ara(sozluk, kelime):
                        continue
                    else:
                        sozluk.append(kelime)
    return sozluk

def cumle2Vector(cumle, sozluk):
    vector = []
    kelimeler = cumle.split(" ")
    for sozcuk in sozluk:
        sozcukSayi = 0
        for kelime in kelimeler:
            if kelime == sozcuk:
                sozcukSayi += 1
        vector.append([sozcuk, sozcukSayi])
    return vector

def noktasalCarpim(vector1, vector2):
    if len(vector1) != len(vector2):
        return -1
    
    carpim = 0
    for i in range(len(vector1)):
        carpim += vector1[i][1] * vector2[i][1]
    return carpim

def vektorBüyüklüğü(vector):
    büyüklük = 0
    for i in range(len(vector)):
        büyüklük += vector[i][1] ** 2
    return büyüklük ** 0.5

def cosinusBenzerligi(vector1, vector2):
    noktasal_carpim = noktasalCarpim(vector1, vector2)
    büyüklük_çarpımı = vektorBüyüklüğü(vector1) * vektorBüyüklüğü(vector2)
    if büyüklük_çarpımı == 0:
        return 0
    return noktasal_carpim / büyüklük_çarpımı

# endregion

# region Main

print("\n")

cumle_1 = "Merhabalar benim adım Ömer"
cumle_2 = "Selam benim adım Ömer"

sozluk = sozlukOku([cumle_1, cumle_2])
print(sozluk)

benzerlik_orani = cosinusBenzerligi(cumle2Vector(cumle_1, sozluk), cumle2Vector(cumle_2, sozluk))
print("Benzerlik Oranı: ", str(benzerlik_orani))

print("\n")

cumle_1 = "BEIVA'nın yazarı, Ömer Sait Coşkun'dur."
cumle_2 = "Ömer Sait Coşkun, BEIVA'nın yazarıdır."

sozluk = sozlukOku([cumle_1, cumle_2])
print(sozluk)

benzerlik_orani = cosinusBenzerligi(cumle2Vector(cumle_1, sozluk), cumle2Vector(cumle_2, sozluk))
print("Benzerlik Oranı: ", str(benzerlik_orani))

print("\n")

cumle_1 = "Geçenlerde Cansu sana ne söyledi?"
cumle_2 = "Cansu bana dün çok yorulduğunu söyledi."

sozluk = sozlukOku([cumle_1, cumle_2])
print(sozluk)

benzerlik_orani = cosinusBenzerligi(cumle2Vector(cumle_1, sozluk), cumle2Vector(cumle_2, sozluk))
print("Benzerlik Oranı: ", str(benzerlik_orani))

# endregion