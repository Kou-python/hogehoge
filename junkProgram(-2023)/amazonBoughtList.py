import requests
from bs4 import BeautifulSoup

# ウェブページのURLを指定
url = 'https://www.python.org/'

# ウェブページからデータを取得
response = requests.get(url)

# ページが正常に取得できたかを確認
if response.status_code == 200:
    # HTMLコンテンツを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # ウェブページから情報を抜き取りたい部分を特定して抽出
    title = soup.title.text  # タイトルを抽出
    header = soup.find('div', {'class': 'introduction'}).p.text  # 特定のクラス内のテキストを抽出
    
    # 結果を表示
    print('タイトル:', title)
    print('ヘッダー:', header)
else:
    print('ウェブページの取得に失敗しました。')

