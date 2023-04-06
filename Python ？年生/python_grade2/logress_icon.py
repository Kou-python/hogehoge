import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
##
url= "https://xn--o9jm2rjb7re3701dqh4b0p9e.gamewith.jp/article/show/41927"
html= requests.get(url)
soup=BeautifulSoup(html.content, "html.parser")
# パス
out_folder= Path("download2")
out_folder.mkdir(exist_ok=True)
##
cnt=1
#imgタグのurl取得
for i in soup.find(class_="sorttable").find_all("img"):
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
    print(str(cnt) + "/" + str(len(soup.find(class_="sorttable").find_all("img"))))
    cnt+=1