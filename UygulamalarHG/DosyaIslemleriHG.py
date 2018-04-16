import os
import sys
dosya=open("bilgiler.txt","a")
print("Merhaba Dünya",file=dosya)
print("Merhaba Dünyalı",file=dosya)
#dosya.close() #bu komuttan sonra dosyaya yazılır.

print(os.getcwd()) #Dosyanın oluştuğu dizini gösterir.

print("Adana Koleji",file=sys.stdout)
print("Python ve yapay zeka",file=dosya,flush=True) #flush=True dosya close() olmadan dosyaya yazdırır.
print(sys.stdout)
sys.stdout=dosya #çıktıların standart olarak dosyaya yazılmasını sağladık.
print(sys.stdout,flush=True)
print("artık file belirtmeden dosayaya yaz")

f = open("veriler.dat") # f adında dosya nesnesi
for line in f: # Her satırı metin olarak oku
    print(line.strip()) # Sondaki yeni satır karakterini sil
f.close() # Dosyayı kapat
with open("veriler.dat") as f: # f adında dosya nesnesi
    for line in f: # Her satırı metin olarak oku
        print(line.strip()) # Sondaki yeni satır karakterini sil
f.close() # Dosyayı kapat
