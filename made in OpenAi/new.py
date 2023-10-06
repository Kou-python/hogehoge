# 必要なライブラリをインポートする
import tweepy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# フォントのパスを取得する
font_path = fm.findfont(fm.FontProperties(family='Hiragino Mincho ProN'))

# フォントを読み込む
font_prop = fm.FontProperties(fname=font_path)

# Twitter APIの認証情報を設定する
consumer_key = 'oLTjoAsEn8NlZZvHCTSG98Rxm'
consumer_secret = 'TgOR4fIQn2KJC6UngEHJ5JcWhgoD711CKuvpBFmexiJvL4ofxK'
access_token = '1603169053098803200-jMcmlqjKa7Ayh5eGOhYxh533q0DPnS'
access_token_secret = 'zhaQQJSs6H3VwiiOS7NnpSsdUgi5deUJuEFO2MNAtN6Rr'

# 認証情報を使用してAPIに接続する
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイートを検索する
search_word = 'スマブラ'
tweets = api.search_tweets(q=search_word, lang='ja', count=1000)

# ツイートの本文から単語を抽出し、出現頻度を数える
words = []
for tweet in tweets:
    text = tweet.text
    for word in text.split():
        if word.startswith('#'):
            word = word[1:]
        if word.startswith('@'):
            continue
        if len(word) < 2:
            continue
        words.append(word)

# ワードクラウドを作成する
wordcloud = WordCloud(background_color='white', font_path=font_path, width=800,
                      height=600).generate(' '.join(words))

# ワードクラウドを表示する
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
