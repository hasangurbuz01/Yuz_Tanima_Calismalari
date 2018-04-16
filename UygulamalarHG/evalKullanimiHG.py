#Her bir ayın kaç gün çektiğini tanımlıyoruz
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28

#Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79

aylıkSarfiyat = int(input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: "))

#Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

ay = eval(dönem) #ayın değerini alıyoruz

#Kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = aylıkSarfiyat / ay

fatura = birimFiyat * aylıkSarfiyat

print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")