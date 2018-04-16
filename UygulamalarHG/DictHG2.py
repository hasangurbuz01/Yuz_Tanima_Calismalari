Dersler={"Efe Berke":["Algoritma","Yapay Zeka","Python","C#","C++"],"Biray":["Uzay Matematiği","Python"],"Hasan":["C++"]}
isim =input("İsim Giriniz:")

print("-----{} ın Aldığı Dersler-----".format(isim))
sayac=1
for i in Dersler[isim]:
    print("{0}.{1}".format(sayac,i))
    sayac+=1
