from typing import Text
import requests

from bs4 import BeautifulSoup

url="https://www.ymori.com/books/python2nen/test1.html"
html=requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")

print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)