import requests
from bs4 import BeautifulSoup

url="https://www.yahoo.co.jp/"
html=requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")

topic=soup.find(class_="_1XAfHUWtx6tfYZuWDVjNxZ")
for w in topic.find_all("a"):
    print(w.text)