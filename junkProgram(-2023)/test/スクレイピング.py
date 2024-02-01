import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com/')
r.raise_for_status()  # エラーチェック
r.encoding = 'utf-8'
s = BeautifulSoup(r.text, "html.parser") # or "lxml" or "html5lib"
print(s)                                        # HTML全体
s.select('a')                            # <a ...> タグ
[x.get('href') for x in s.select('a')]   # <a ...> タグの中のhref