import sqlite3
baglanti=sqlite3.connect("Dersler.db")
cursor=baglanti.cursor()
def kayitSil():
    cursor.execute("select * from Ogrenciler")
    kayitlar=cursor.fetchall()
    print("----Silinmeden Önce-----")
    for i in kayitlar:
        print(i)

    cursor.execute("DELETE FROM Ogrenciler where Notu<60")
    baglanti.commit()

    print("-------Silindikten Sonra------")
    cursor.execute("select * from Ogrenciler")
    kayitlar = cursor.fetchall()
    for i in kayitlar:
        print(i)

kayitSil()

baglanti.close()