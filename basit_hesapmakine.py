###Hesap Makinesi Basit

a = float(input("1.Sayıyı giriniz: "))
b = float(input("2.Sayıyı giriniz: "))
c= input("işleminiz nedir (+,/,*,-)")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
else:
    print("Lütfen 4 işlemden biriniz seçiniz.")