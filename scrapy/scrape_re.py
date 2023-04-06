# 書籍のURLとタイトル
import re
from html import unescape
from urllib.parse import urljoin

with open("dp.html") as f:
    html=f.read()

# re.DOTALL=re.S:.が改行を含むすべての文字列にマッチするようになる
for i in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.S):
    url=re.search(r'<a itemprop="url" href="(.*?)">', i).group(1)
    url=urljoin("https://gihyo.jp/", url) #相対→絶対
    name=re.search(r'<p itemprop="name".*?</p>', i).group(0)
    name=name.replace("<br>", " ") #str.replaceは変数strの文字列を置換する
    name=re.sub(r'<.*?>',"", name)
    name=unescape(name)
    print(url, name)