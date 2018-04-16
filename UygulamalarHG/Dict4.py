# Metodları kullanmadan sözlük üzerinde gezinmek - Sadece anahtarları alabiliyoruz.
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük:
    print(eleman)

# keys() - Aynı şey
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.keys():
    print(eleman)

# values()
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for eleman in sözlük.values():
    print(eleman)

# items()
sözlük = {"bir":1,"iki":2,"üç":3,"dört":4}

for (i,j) in sözlük.items():
    print("Anahtar:",i,"Değer:",j)

