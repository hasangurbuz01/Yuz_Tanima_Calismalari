liste=[]
kenarlar=["a","b","c","d"]

def geometrik(gelen_liste):
    uzunluk=len(gelen_liste)
    print("----------------------")
    for i in range(uzunluk):
        kenarlar[i]=gelen_liste[i]
        print(kenarlar[i])
    print("----------------------")

    if uzunluk==4:
        a=gelen_liste[0]
        b = gelen_liste[1]
        c = gelen_liste[2]
        d = gelen_liste[3]
        print("4 elemanlı")
        if a==b and a==c and a==d:
            print("ikiz kenar dörtgen")
    elif uzunluk==3:
        a = gelen_liste[0]
        b = gelen_liste[1]
        c = gelen_liste[2]
        print("3 elemanlı üçgen")

while True:
    eleman_sayisi=int(input("Elaman Sayısı="))
    if eleman_sayisi==0:
        break
    for i in range(eleman_sayisi):
        kenarlar[i]=int(input("{} kenarını giriniz:".format(kenarlar[i])))
        liste.append(kenarlar[i])


print(liste)
geometrik(liste)