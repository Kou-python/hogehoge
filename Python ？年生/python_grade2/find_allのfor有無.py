#F5を押すとでバックされる
import requests
from bs4 import BeautifulSoup

url= "https://www.ymori.com/books/python2nen/test2.html"
html= requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")

#forなしだと順番に読み取って出力が直後に出てくる
print(soup.find_all("li"))

#forにすると全部読み切った上でプリントが実行される
for i in soup.find_all("li"):
    print(i.text)