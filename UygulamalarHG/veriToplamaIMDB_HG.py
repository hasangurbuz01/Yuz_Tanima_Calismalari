import requests
from bs4 import BeautifulSoup
imdburl="http://www.imdb.com/chart/top"
r=requests.get(imdburl)
soup=BeautifulSoup(r.content,"html.parser")
gelen_veri=soup.find_all('table',{'class':'chart full-width'})
print(gelen_veri)
print("-"*20)
print(len(gelen_veri))