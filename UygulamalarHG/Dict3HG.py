#Sözlükler,“anahtar-değer” çiftlerinden oluşan bir veri tipidir.
sehirler={"İstanbul" :"34" , "Adana":"01" , "Isparta":"32"}
siparis_rehberi= {  "Çorbacı":"444 44 44",
                    "Pizzacı"  :"555 55 55",
                    "Kebapçı":"666 66 66" }
print("Çorbacı Telefonu:",siparis_rehberi["Çorbacı"])

#siparis_rehberi'ne yeni değer ekleme
siparis_rehberi["Balıkçı"]="664 333 555"
print(siparis_rehberi)

#Sözlük ögesini değiştirme
siparis_rehberi["Balıkçı"]="800 333 555"
print(siparis_rehberi)

#Dikkat
siparis_rehberi["balıkçı"]="800 000 000"
print(siparis_rehberi)

#Sözlük Ögelerini Silmek
del  siparis_rehberi["Pizzacı"]
print(siparis_rehberi)

siparis_rehberi.pop("balıkçı")
print(siparis_rehberi)
print(siparis_rehberi.items())

siparis_rehberi.popitem()
print(siparis_rehberi)

#KEYS() VE VALUES()

#keys():Sözlükteki anahtarları yazdırır.
print(siparis_rehberi.keys())

#values(): Sözlükteki değerleri bize yazdırır.
print (siparis_rehberi.values())

yeni_siparisler =siparis_rehberi.copy()
print (yeni_siparisler)

#GET()
#get:Bir öğenin sözlük içinde olup olmamasını kontrol ediyoruz.

siparis_rehberi.get("Tost" , "yok") #yok

print(siparis_rehberi.get("Tost","Yok"))
print(siparis_rehberi.get("Çorbacı","Yok"))

siparis_rehberi.clear()
print(siparis_rehberi)


del siparis_rehberi
