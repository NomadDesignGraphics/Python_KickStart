#Else if ek denemesi kolay hali mantık bölgesi
a = int(input("Lütfen Sayınızı giriniz (1 ile 100 arası zorunludur): "))

if a < 0 or a > 100:
    print("Lütfen 1 ile 100 arası rakam giriniz")
    pass
elif a == 0 or a <= 50:
    print("Sayı 50 den küçüktür")
    pass
elif a == 50:
    print("Sayınız tam ellidir")
    pass
else: print("Sayınız 50 den büyüktür")
