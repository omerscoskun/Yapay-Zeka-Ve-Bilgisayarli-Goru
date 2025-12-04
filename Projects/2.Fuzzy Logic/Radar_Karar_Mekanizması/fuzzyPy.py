import numpy as np

def ucgen(x, abc):
    
    # a<=b<=c olmalıdır.
    assert len(abc) == 3, 'Baslangıc, Tepe ve Bitis Degerleri Verilmelidir!'
    a, b, c = np.r_[abc] #Zero-Indexing in Python
    assert a <= b and b<= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'

    y = np.zeros(len(x))

    #Sol
    if a != b:
        idx = np.nonzero(np.logical_and(a<x, x<b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    #Sag
    if b != c:
        idx = np.nonzero(np.logical_and(b<x, x<c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
    
    idx = np.nonzero(x == b)
    y[idx] = 1
    
    return y

def trapez(x, rot, abc):
    
    y = np.zeros(len(x))
    
    if(rot == "ORTA"):
        
        assert len(abc) == 3, 'Baslangıc, Tepe ve Bitis Degerleri Verilmelidir!'
        a, b, c = np.r_[abc]
        assert a <= b and b<= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'

        idx = np.nonzero(np.logical_and(x >= 0, x < a))[0]
        y[idx] = x[idx] / float(a)
        idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
        y[idx] = 1
        idx = np.nonzero(np.logical_and(x > b, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
        
        return y
    
    else:
        
        assert len(abc) == 2, 'Baslangıc, Tepe ve Bitis Degerleri Verilmelidir!'
        a, b = np.r_[abc]
        
        if(rot == "SOL"):
            
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'

            idx = np.nonzero(x <= a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
            y[idx] = (x[idx] - b) / float(a - b)

            return y
        
        elif(rot == "SAG"):

            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'

            idx = np.nonzero(x > a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x > a, x <= b))[0]
            y[idx] = (x[idx] - a) / float(b - a)

            return y