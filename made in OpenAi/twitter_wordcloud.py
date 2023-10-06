import tweepy

# APIキーの設定
consumer_key = "zXfRFnuQdju14czfwkfQhVk3f"
consumer_secret = "exR8LqkPQXuteHyZmcFcVYJ0mtlTQhrMijOZPErCXVnDg2Jenh"
access_token = "1603169053098803200-6pZSkwWa4vLrMP3J57tlyV7S9seWo4"
access_token_secret = "BOGg2C4PfKGw8mYcQSzEYFlC9ucix3OHFv4h6tchVHNGp"

# 認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# APIインスタンスを作成
api = tweepy.API(auth)

# 例
# tweepyで検索を行う
search_results = api.search_tweets(
    q="大谷翔平", result_type="recent", tweet_mode='extended', count=5)
