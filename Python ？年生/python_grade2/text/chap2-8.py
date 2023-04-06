import requests
from bs4 import BeautifulSoup

url="https://www.ymori.com/books/python2nen/test2.html"
html=requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")

for w in soup.find_all("a"):
    print(w.text)
    url1=w.get("href")
    print(url1)