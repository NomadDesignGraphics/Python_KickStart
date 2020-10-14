#BOSS 2
ds="--------------"
#Kontrollü Makina kick start
print("""

[1]Topla
[2]Çıkar
[3]Böl
[4]Çarp
[5]Üst al
[Q]Çıkış


""")

login=input("İşleminizi seçiniz: ")

if login=="":
    print("Lütfen birdahaki sefere düzgünce isteğinizi belirtiniz")
    pass
elif login == 1 or login == "Topla" or login == "topla":
    print("Toplama işlemini seçtiniz","\n")
    a=float(input("1.Sayınız: "))
    b=float(input("2.Sayınız: "))
    print(ds)
    print("sonucunuz:",a+b)
    print(ds)
    pass
elif login == "2" or login == "Çıkar" or login == "çıkar":
    print("Çıkarma işlemini seçtiniz","\n")
    a=float(input("1.Sayınız: "))
    b=float(input("2.Sayınız: "))
    print(ds)
    print("sonucunuz:",a-b)
    print(ds)
    pass
elif login == "3" or login == "Böl" or login == "böl" or login == "Bölme" or login == "bölme":
    print("Bölme işlemini seçtiniz","\n")
    a=float(input("1.Sayınız: "))
    b=float(input("2.Sayınız: "))
    print(ds)
    print("sonucunuz:",a/b)
    print(ds)
    pass
elif login == "4" or login == "Çarp" or login == "çarp" or login == "Çarpma" or login=="çarpma":
    print("Çarpma işlemini seçtiniz","\n")
    a=float(input("1.Sayınız: "))
    b=float(input("2.Sayınız: "))
    print(ds)
    print("sonucunuz:",a*b)
    print(ds)
    pass
elif login == "5" or login == "Üst" or login == "üst" or login == "Üst al" or login == "üst al" or login=="Üstal" or login=="üstal":
    print("Bölme işlemini seçtiniz","\n")
    a=float(input("1.Sayınız: "))
    b=float(input("2.Sayınız: "))
    print(ds)
    print("sonucunuz:",a**b)
    print(ds)
    pass
if login == "Q" or login=="q" or login == "Çıkış" or login == "çıkış" or login == "Çık" or login=="çık":
    print("İşlem iptal edilmiştir")
    quit()