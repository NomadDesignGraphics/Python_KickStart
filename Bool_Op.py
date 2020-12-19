###Bool Operatörleri
"""
and
or
not
"""

### and
if (2+3 == 5 and 1+4 ==5):
    print("2+3 ve 1+4 ün toplamı 5 eder")

### or
if (11 == 11 or 22 == 10):
    print("or komutu 2 adetten biri false olsada iş götürür gene")
elif (11 == 10 or 22 == 99):
    print("eğer bu kod çalışsaydı zaten bilgisayarın beyni yanardı")

### not
a = input("değer testi: ")

if (not bool(a)):
    print("değer içermiyor")
else:
    print("değer içeriyor")
