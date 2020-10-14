print("_-_"*10)
print("Günlük Kontrol","\n")

a=str(input("Enerjikmisin(e/h)?: "))

if a == "e":
    print("_-_"*10)
    print("Yapılacaklar listesini görmek istermisin?")

    b=str(input("evet yada hayır (e/h): "))

    if b == "e":
        print("Blender3D de tasarım","\n","="*5,"\n","Udemy den ders alma","\n","="*5,"Chocobo ile ilgilenme","\n","="*5,"Pasta yap komşuya ver","\n","="*5)
        pass
    elif b == "h":
        print("papağanı al sev yatağa uzan")
        pass

elif a == "h":
    c=str(input("Kahve istermisin?(e/h): "))

    if c == "e":
        print("Kahveni iç 10-20dk sonra tekrar gel")
        pass
    elif c == "h":
        d=str(input("Moralinmi bozuk?(e/h): "))
        if d == "h":
            print("Mevsimsel Problem olabilir")
            pass
        elif d == "e":
            e=str(input("Problem aile içimi aile dışımı(i/d)?: "))
            if e == "d":
                f=str(input("Durumu Özkana anlatmak istermisin?(e/h)"))
                if f == "h":
                    print("Bu zaman dilimi geçicek eline kitap al ve okumaya bak müzik eşliğinde yada meme bak")
                    pass
                elif f == "e":
                    g=str(input("Peki anlatmadan önce haklı taraf senmisin?(e/h): "))
                    if g == "e":
                        print("Anlat ve biraz ondanda fikir al, numarası hesabında")
                        pass
                    elif g == "h":
                        print("Önce hatanı kabullen ve özkanı boş yere konuşmak için değil","\n", "aksine eksiklerini bulmak için fikir almaya bak")
                        pass
                    pass
            elif e == "i":
                print("Aile içi problem zaman içinde geçecektir","\n", "o yüzden iç problemini fikir almaya yada psikolojik desteğe ihtiyaç duymadıkça dışa vurma","\n", "ama eğer özkana ihtiyaç duyuyorsanda ara onu")
                pass
pass