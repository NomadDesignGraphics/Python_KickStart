# "is" kodu
# "id" fonksiyonu

a = 5
b= 5

if a == b:
    print("Aynılar")
    pass

if a is b:
    print("aynılar")
    pass

"""

"""

print(id(a))    #bunlara sistem üzerinden .md5 kimliği atıyor
print(id(b))
print(id(5))

"""
id atayıpta kontrol etmek için is kullanılıyor ama her an
her yerde kullanılmıyor ondan dolaylı genel olarak "==" kullanılır
"""