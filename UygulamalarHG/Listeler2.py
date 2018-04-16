liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)

# Demet içindeki herbir elemanı almak için pratik yöntem
liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print(i,j)


# Demet içindeki elemanları çarpalım.
liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for (i,j,k) in liste:
    print(i * j * k)


# liste1'den liste2'yi oluşturalım.
liste1 = [1, 2, 3, 4, 5]
liste2 = list()  # veya liste2 = [] ikisi de boş liste oluşturur.
for i in liste1:
    liste2.append(i)  # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.
print(liste2)


#Acaba bu kodumuzu list comprehension ile daha kısa yazabilir miyiz ?
liste1 = [1,2,3,4,5] # Örnek 1
liste2 = [i for i in liste1] # List Comprehension
print(liste2)

liste1 = [1,2,3,4,5] # Örnek 2
liste2 = [i*2 for i in liste1] # List Comprehension
print(liste2)

liste1 = [(1,2),(3,4),(5,6)] # Örnek 3
liste2 = [i*j for (i,j) in liste1] # List Comprehension
print(liste2)


liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
print(liste2)

s = "Python"  # Örnek 5
liste = [i * 3 for i in s] # List Comprehension
print(liste)


liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste2 = [x for i in liste for x in i] # Biraz karmaşık
print(liste2)