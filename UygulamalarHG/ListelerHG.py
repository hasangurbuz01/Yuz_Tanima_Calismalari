"""
Listeler, içerisinde farklı türden verileri barındırabilen taşıyıcılardır. Python'ı güçlü kılan özelliklerden biri
olan listelerde, her bir eleman bir indis (index) numarasına sahiptir ve bir listenin başlangıç indisi 0 (sıfır)'dır.
"""

liste1=[4,56,7,"Elma",56,100,54]
liste2=[34,65,74,76,85,65]
meyveler=["Portakal","Elma","Kavun","Şeftali","Çilek"]

print("Liste1'in 4.elemanı:",liste1[3])
print(meyveler[1:3])
print(meyveler[:3])
print(meyveler[1:])
#1. indisden başlayıp son indisine kadar olan elemanları ikişer ikişer atlayarak ekrana yazdıralım
print("iki atla:",liste1[0::2])
print("liste1'in elaman sayısı:",len(liste1))
print("56 adedi:",liste1.count(56))
print("liste2'nin toplam Değeri:",sum(liste2))
print("liste2'nin Ortalama Değeri:",sum(liste2)/len(liste2))

#Listeye kayıt ekleme
takimlar = ['Galatasaray', 'Fenerbahçe', 'Beşiktaş','Adana Spor']
takimlar.append('Trabzonspor')
print("append ile Trabzon.. eklendi:",takimlar)

#Remove: Listeden eleman silmeye yarayan metottur. Parametre olarak silinecek elemanın değerini alır.
takimlar.remove('Beşiktaş')
print("Remove ile Beşiktaş silindi:",takimlar)

#del : Yine liste içerisinden bir elemanı silmek için kullanılır. remove() metodundan farkı, parametre olarak silinecek elemanın indis numarasını almasıdır.
del takimlar[1]
print("del ile 1 indexli kayıt silindi:",takimlar)

#pop:Liste içerisinden eleman silmenin başka bir yoludur. İçerisinde belirttiğiniz indisteki elemanı listeden çıkartır ve çıkardığı elemanı ekrana yazar.
takimlar.pop()
print("pop ile son kayıt silindi",takimlar)

takimlar.pop(1)
print("pop ile 1 indexli kayıt silindi",takimlar)

sayilar=[43,32,1,567,9000,5]
sayilar.sort()
print(sayilar)

meyveler.reverse()
print(meyveler)
