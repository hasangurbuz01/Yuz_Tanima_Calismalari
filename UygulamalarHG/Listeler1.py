
isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
liste = list(zip(isim,soyisim))
liste.sort()
print(liste)

for i,j in liste:
    print(i,j)