import sqlite3
con=sqlite3.connect("Dersler.db")
cursor=con.cursor()


def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(Ad TEXT,Soyad TEXT,Numara INT, Notu INT)")

tabloOlustur()

def kayitlariGoruntule():
    cursor.execute("SELECT * FROM Ogrenciler where Notu=100")
    kayitlar=cursor.fetchall()
    for i in kayitlar:
        print(i)

def kayitGuncelle():
    cursor.execute("SELECT * FROM Ogrenciler")
    kayitlar = cursor.fetchall()
    print("----Kayıtlar İlk Hali--------")
    for i in kayitlar:
        print(i)

    cursor.execute("UPDATE Ogrenciler SET Notu=Notu+10 WHERE Notu<=75")

    cursor.execute("SELECT * FROM Ogrenciler")
    kayitlar = cursor.fetchall()
    print("----Güncellemeden Sonra Kayıtlar--------")
    for i in kayitlar:
        print(i)


kayitGuncelle()
con.commit()
con.close()