import requests

api_url = "https://api.chatgpt.com/v1/chatgpt"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {APIキー}"
}

data = {
    "message": "こんにちは、ChatGPTさん"
}

response = requests.post(api_url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result["messages"])
else:
    print("エラーが発生しました。")