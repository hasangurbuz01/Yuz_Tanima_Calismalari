name = "python4hackers"
print (name.replace("python", "piton"))
name = "Türk Dil Kurumu"
print (name.split(" "))
print()
liste=name.split(" ")
for i in liste:
    print(i)


print (name.splitlines())
print(name.lower())
print(name.upper())

okul="Adana Koleji"
print(okul.islower())

okul="Adana Koleji"
print(okul.isupper())

Universite = "Çukurova Üniversitesi"
print ("startswith=",Universite.startswith("T"))
print ("endswith=",Universite.endswith("sitesi"))
print (Universite.capitalize())
print (Universite.title())
print (Universite.swapcase())

Universite = ">Çukurova Üniversitesi>"
print (Universite.strip(">"))
print (Universite.lstrip(">"))
print (Universite.rstrip(">"))
print ("count=",Universite.count("i"))
print ("index=",Universite.index(">"))
print ("rindex=",Universite.rindex(">"))
print ("find=",Universite.find("Ü"))
print ("rfind=",Universite.rfind("s"))
isim="Hasan GÜRBÜZ"
print ("center=",isim.center(50))
print ("partition=",isim.partition(" "))
print ("rpartition=",isim.rpartition("gü"))
print ("encode=",isim.encode("cp857"))

name = "james bon007"
print (name.isalpha())

name = "007"
print (name.isdigit())

name = "jamesbon007"
print ("isalnum=",name.isalnum())

tr = "şçöğüıŞÇÖĞÜİ"
en = "scoguiSCOGUI"
dictionary = str.maketrnas(tr, en,'')
text = "Şemsi paşa pasajında sesi büzüşesiceler"
print(text.translate(dictionary))


