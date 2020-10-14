#ekrana paralel kenar çizdirecez

def cizsl(adet):
    for a in range(int(adet)):
        print("/",end="")

def cizsg(adet):
    for a in range(int(adet)):
        print("\\",end="")

def satiratla(adet):
    for a in range(int(adet)):
        print()

def bslk(adet):
    for a in range(int(adet)):
        print(" ",end="")

def ustbolge(cap):
    kickempty = cap / 2 - 1
    for a in range(int(cap / 2)):
        bslk(kickempty - a)
        cizsl(1)
        bslk(a * 2)
        cizsg(1)
        satiratla(1)

def altbolge(cap):
    fuckempty = cap - 2
    for a in range(int(cap / 2)):
        bslk(a)
        cizsg(1)
        bslk(fuckempty - a * 2)
        cizsl(1)
        satiratla(1)

def PK(cap):
    cap = int(input("Çapı giriniz: "))
    ustbolge(cap)
    altbolge(cap)


PK(1) # buraya 1 yazsan dahi işin özünde yukarıdaki input değerini işleme geçirecektir 

#Bundan sonraki dersler PyCharm da gerçekleşecektir