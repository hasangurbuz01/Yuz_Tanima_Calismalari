dosya=open("veriler.dat","a")
dosya.write("Hasan")
dosya.write(" Gürbüz")
dosya=open("veriler.dat","r")
icerik=dosya.read()

f = open("veriler.dat") # f adında dosya nesnesi, varsayılan parametre r'dir.
for line in f: # Her satırı metin olarak oku
    print(line.strip()) # Sondaki yeni satır karakterini sil
f.close() # Dosyayı kapat


with open("veriler.dat") as f: # f adında dosya nesnesi
    for line in f: # Her satırı metin olarak oku
        print(line.strip()) # Sondaki yeni satır karakterini sil
f.close() # Dosyayı kapat
