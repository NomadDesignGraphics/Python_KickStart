"""
and (ve)

or (veya)

not (değil)
"""

"""
#Burdaki kod "or" mantığını açıklar denemek için kodu çeevreleyen tırnakları siliniz

print("Lütfen şunlardan birini seçiniz: ","\n","Mandalina/Portakal/Patlıcan/kara üzüm")
a = str(input("Seçiminiz: "))

if a == "Mandalina" or a == "Portakal":
    print("Turuncu")
    pass
elif a == "Patlıcan" or a== "kara üzüm":
    print("mor renkler")
    pass

"""
#Psikolojik Destek Konsolu (PDK) ilk burda yazıldı
#PDK yoluyla 2D resimli/resimsiz RPG yapma kilidini açtın (Başarım Kilidi Açıldı: Özkanın onayı)

"""
Burdaki kod "and" mantığını açıklamak için var

n = int(input("Sayı gir: "))

if n >= 0 and n <= 100:
     print("Rakamınız 0 ile 100 arasındadır")
     pass
elif n > 100 and n < 1000:
    print("sayınız 100 ile 1000 arasındadır")
    pass
else:
    print("Seyının seviyesi belirlenemiyor")
    pass

"""

"""
burda "not" komutunun anlamlandıran kod

c = input("1.Veri girişi : ")

if not bool(c):
    print("Veri girmediniz")
    pass
else:
    print("Veri girişi yapıldı")
    pass
"""