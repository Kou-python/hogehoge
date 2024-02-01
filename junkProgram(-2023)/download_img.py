import os
import requests
from bs4 import BeautifulSoup
import re

# ターゲットのウェブサイトのURLを指定します
url = "https://www.0101.co.jp/078/info/?from=01_pc_st078_top_head-floor"

# ウェブページの内容を取得します
response = requests.get(url)  # requestsで取得
soup = BeautifulSoup(response.text, "html.parser")

# 画像を保存するディレクトリを作成します
download_dir = "downloaded_images"
os.makedirs(download_dir, exist_ok=True)

# クラス名が「p-floor__contents_wrap」の要素を取得します
elements = soup.find(class_="p-floor__contents_wrap")

kaiso = soup.find_all(class_="p-floor__contents_wrap")
for i in kaiso:
    print(i.attr["img"])
