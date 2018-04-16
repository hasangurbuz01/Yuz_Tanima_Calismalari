import sqlite3
con=sqlite3.connect("Dersler.db")
cursor=con.cursor()
isim=input("İsim Giriniz\t:")
soyisim=input("Soyisim Giriniz\t:")
OkulNo=input("Okul Numaranızı Giriniz\t:")
Notunuz=input("Notunuzu Giriniz\t:")

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Ogrenciler(Ad TEXT,Soyad TEXT,Numara INT, Notu INT)")
def kayitEkle():
     cursor.execute("INSERT INTO Ogrenciler VALUES('"+isim+"','"+soyisim+"',"+OkulNo+","+Notunuz+")")
     con.commit()


tabloOlustur()
kayitEkle()
def kayitlariGoruntule():
    cursor.execute("SELECT * FROM Ogrenciler where Notu=100")
    kayitlar=cursor.fetchall()
    for i in kayitlar:
        print(i)

kayitlariGoruntule()
con.close()