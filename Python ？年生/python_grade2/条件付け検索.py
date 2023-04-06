#F5を押すとでバックされる
import requests
from bs4 import BeautifulSoup

url= "https://www.ymori.com/books/python2nen/test2.html"
html= requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")

#id:HTMLファイルに1つしかない
#print(soup.find_all(id="chap1"))
#class:同じデザインの要素に使う。HTMLファイルに1つ以上ある**class_=""
#print(soup.find_all(class_="クラス名"))

#soupの後にfind2つ以上付けてより条件を絞ることができる
for i in soup.find(id="chap2").find_all("li"):
    print(i.text)