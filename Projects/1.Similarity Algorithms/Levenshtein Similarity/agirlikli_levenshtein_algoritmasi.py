# region Imports

import numpy

# endregion

# region Functions

def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    if b<=c and b<=a:
        return b
    if c<=a and c<=b:
        return c

def max(a,b):
    if(a<b):
        return b
    else:
        return a

def normalize(X,size):
    if len(X) < size:
        fark = size - len(X)
        for i in range(fark):
            X = X + " "
    return X

# endregion

# region Levenshtein Distance

near_keys = {
        'a': ['s','q','w','z'],
        'b': ['v','g','h','n'],
        'c': ['x','d','f','v'],
        'ç': ['l','ö','ş','.'],
        'd': ['s','e','r','f','c','x'],
        'e': ['w','s','d','r'],
        'f': ['d','r','t','g','v','c'],
        'g': ['f','t','y','h','b','v'],
        'ğ': ['p','ş','ü','i'],
        'h': ['g','y','u','j','n','b'],
        'ı': ['u','j','k','o'],
        'i': ['ğ','ü','ş','.','p'],
        'j': ['h','u','ı','k','m','n'],
        'k': ['j','i','o','l','m','ö'],
        'l': ['k','o','p','ö','ç','ş'],
        'm': ['n','j','k','ö'],
        'n': ['b','h','j','m'],
        'o': ['i','k','l','p'],
        'ö': ['k','l','ç','m'],
        'p': ['o','l','ş','ğ'],
        'q': ['w','a'],
        'r': ['e','d','f','t'],
        's': ['a','w','e','d','x','z'],
        'ş': ['l','ç','p','i','ğ','.'],
        't': ['r','f','g','y'],
        'u': ['y','h','j','ı'],
        'v': ['c','f','g','b'],
        'w': ['q','a','s','e'],
        'x': ['z','s','d','c'],
        'y': ['t','g','h','u'],
        'z': ['a','s','x']
    }
second_nearest_keys = {
    'a': ['d', 'e', 'x', 'c'],
    'b': ['f', 't', 'y', 'm','c','j'],
    'c': ['z', 's', 'e', 'r', 'b','g'],
    'ç': ['k', 'p', 'o', 'm','i'],
    'd': ['a', 'w', 't', 'g', 'v','z'],
    'e': ['a', 'q', 'f', 'x', 'z','c','t'],
    'f': ['s', 'e', 'y', 'h', 'b','x'],
    'g': ['d', 'r', 'u', 'j', 'n','c'],
    'ğ': ['l', 'o', 'ç', '.'],
    'h': ['f', 't', 'ı', 'k', 'm','v'],
    'ı': ['y', 'h', 'l', 'ö','n','m','p'],
    'i': ['p', 'ç', 'l'],
    'j': ['b', 'g', 't', 'o', 'ö', 'l'],
    'k': ['h', 'n', 'u', 'ş', 'p','ç'],
    'l': ['ı', 'j', 'm', 'ğ', 'i','.'],
    'm': ['b', 'h', 'u', 'ı', 'l','ç'],
    'n': ['v', 'g', 'y', 'u', 'k','ö'],
    'o': ['u', 'j', 'm', 'ö', 'ç','ş','ğ'],
    'ö': ['n', 'j', 'ı', 'o', 'p','ş','.'],
    'p': ['ı', 'k', 'ö', 'ü','i','ç'],
    'q': ['s', 'e', 'z'],
    'r': ['w','s', 'x', 'c','v', 'g', 'y'],
    's': ['q', 'r', 'f', 'c'],
    'ş': ['k', 'ö', 'ü', 'o'],
    't': ['e', 'd', 'c', 'v','b', 'h', 'u'],
    'u': ['t', 'g', 'b','n','m', 'k', 'o'],
    'v': ['x','d', 'r', 't', 'y', 'h','n'],
    'w': ['x', 'z', 'd', 'r'],
    'x': ['a', 'w', 'e', 'f','v'],
    'y': ['r', 'f', 'v', 'b', 'n','j','ı'],
    'z': ['q', 'w', 'd', 'c']
    }
    
def weightedLevenshteinMesafesi(A,B,yerdegistirme = 0):

    A = A.lower()
    B = B.lower()

    K = numpy.zeros((len(A)+1,len(B)+1))

    A_len = len(A)
    B_len = len(B)

    for i in range(A_len+1):
        K[i][0] = i
    for j in range(B_len+1):
        K[0][j] = j

    for i in range(1,A_len+1):
        for j in range(1,B_len+1):
            if A[i-1] == B[j-1]:
                K[i][j] = K[i-1][j-1]
            elif A[i-1] in near_keys and B[j-1] in near_keys[A[i-1]]:
                yerdegistirme = K[i-1][j-1] + 0.25
                K[i][j] = yerdegistirme
            elif A[i-1] in second_nearest_keys and B[j-1] in second_nearest_keys[A[i-1]]:
                yerdegistirme = K[i-1][j-1] + 0.5
                K[i][j] = yerdegistirme
            else:
                yerdegistirme = K[i-1][j-1] + 1
                K[i][j] = yerdegistirme

    return K[A_len-1][B_len-1]

# endregion

kelime_1 = "Mehmet"
kelime_2 = "Ahmet"

max_len = max(len(kelime_1),len(kelime_2))
kelime_1 = normalize(kelime_1,max_len)
kelime_2 = normalize(kelime_2,max_len)
mesafe = weightedLevenshteinMesafesi(kelime_1,kelime_2)
print("'" + kelime_1 + "' ile '" + kelime_2 + "' arasındaki Ağırlıklı Levenshtein Mesafesi: ",mesafe)

benzerlik_orani = (max_len - mesafe) / max_len
print("Benzerlik Oranı: ",benzerlik_orani)