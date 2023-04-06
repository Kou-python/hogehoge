import requests, urllib, pathlib
from bs4 import BeautifulSoup

url="https://sp.mmo-logres.com/news/"
html= requests.get(url)
soup= BeautifulSoup(html.content, "html.parser")
#どーやって「ガチャ」タグだけ抽出すんねん！！！！
tag= soup.find(class_="icon gacha").parent
print(tag)