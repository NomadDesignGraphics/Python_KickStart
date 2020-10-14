#Format metodunu kullanarak string biçimlendirme
"""
a = """
#E:Fuck World
#T:{} {}

""".format("Merhaba","Dünya")

print(a)
"""


"""
niggers = "abcdefghıijklmn"

for dick in niggers:
    print("Niggers getting kicked: {}".format(dick))
"""

"""
Konumları Belirleme
Sözcük atama

:> "sağa yaslama ve alana ayırma"
:< "sola yaslama ve alan ayırma"
:^ "Merkezde alan ayırma"
:s "yalnızca string ifade"
:d "yalnızca sayısal ifade"
:b "ikili sistemde karışıklık"
"""
#Python saymaya 0 dan başlar sana bunu kanıtlayabilirim

a1 = "Gökhan"
a2 = "TOSUN"

aa = "{0}{1}".format(a1,a2)
print(aa)

ab = "{1}{0}".format(a1,a2)
print(ab)

ac = "{ad}{soyad}".format(ad = a1,soyad = a2)
print(ac)

ad = "|{:>15}|".format(a1)
print(ad)

af = "|{:<15}|".format(a2)
print(af)

ag = "{}".format(12)
print(ag)

ah = "|{:b}|".format(1024)
print(ah)

aj = "{:,}".format(21486146841)
print(aj)