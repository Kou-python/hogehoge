from genericpath import exists
import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
##
url= "https://news.yahoo.co.jp/categories/it"
html= requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")
out_folder= Path("download2")
out_folder.mkdir(exist_ok=True)
##

#ITトピックの最新記事のulテキストと絶対url
for i in soup.find(class_="sc-cRULEh epopbv").find_all("a"):
    get_url= i.get("href")
    #ここのリンクはぎりぎり階層構造になっていないのでurllibは使用しなくてもOK、だが最後の「もっと見る」は相対URLになっているので今回は使用した
    link= urllib.parse.urljoin(url, get_url)
    print(i.text, link)

"""
#imgタグのurl取得
for i in soup.find_all("img"):
    src=i.get("src")
    #絶対url作成
    img_url= urllib.parse.urljoin(url, src)
    imgdata= requests.get(img_url)
    #name
    filename= img_url.split("/")[-1]
    #file名
    out_path= out_folder.joinpath(filename)
    #画像データ書き出し*withはファイルを開いたり閉じたりする処理を簡略化して書いたもの
    #mode="wb"はバイナリファイル(テキストファイル以外)を書き込むためのオプション
    with open(out_path, mode="wb") as f:
        f.write(imgdata.content)
"""