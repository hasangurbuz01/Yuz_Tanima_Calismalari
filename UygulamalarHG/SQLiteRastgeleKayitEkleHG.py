import sqlite3
import random
import datetime
import time

baglanti=sqlite3.connect("Dersler.db")
cursor=baglanti.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Mesai(Zaman REAL,Tarih TEXT, anahtarKelime TEXT,Deger REAL)")
def rastgeleKayitEkle():
    _zaman=time.time()
    _tarih=str(datetime.datetime.fromtimestamp(_zaman).strftime('%Y-%m-%d: %H:%M:%S'))
    _anahtarKelime="Python "
    _deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Mesai(Zaman,Tarih,anahtarKelime,Deger) Values(?,?,?,?)",(_zaman,_tarih,_anahtarKelime,_deger))
    baglanti.commit()

tabloOlustur()
i=0
while i<10:
    rastgeleKayitEkle()
    time.sleep(1)
    i+=1
baglanti.close()