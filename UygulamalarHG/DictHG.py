#Sözlükler,“anahtar-değer” çiftlerinden oluşan bir veri tipidir.
ornekSozlük={"Python":"Gelecek yüzyılın dili","Java":"Script dili","C#":"Programlama Dili"}

print(type(ornekSozlük))
print(ornekSozlük["Python"])

for i in ornekSozlük:
    print(i)

print("---------------------")

for i in ornekSozlük.items():
    print(i)

print("---------------------")

for i in ornekSozlük.items():
    print(i[0]+"\t:"+i[1])

print("---------------------")

for i,j in ornekSozlük.items():
    print(i+"\t\t:"+j)