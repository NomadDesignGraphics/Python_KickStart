### Karşılaştırma Operatörleri
"""
    == -----> eşitse
    != -----> eşit değilse
    >  -----> büyükse
    <  -----> küçükse
    >= -----> Büyük veya eşitse
    <= -----> Küçük veya eşitse

"""

###eşitse
a=45
b=45
if (a == b):
    print("2 sayıda birbirine eşit")
elif (a != b):
    print("2 sayıda birbirine eşit değil")

### büyükse / küçükse / küçük eşit / büyük eşit
kredi = 4.0

if (kredi <= 2.5):
    print("Kaldınız")
elif (kredi > 2.6 and kredi < 3):
    print("Sorunlu geçti")
elif (kredi > 3 and kredi < 4):
    print("geçti")
elif (kredi == 4):
    print("o Dersten muaf sayılıyorsunuz artık")