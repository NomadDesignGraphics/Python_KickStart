print("="*20)
a=input("Şifre kaydı: ")
print("\n","Şifreniz Kayıt edildi")
print("="*20)

#giriş

print("="*20)
b = input("Giriş Yapınız: ")
if b == a:
    print("Giriş başarılı")
    pass
else:
    print("Şifre uyuşmuyor")
    pass
print("="*20)