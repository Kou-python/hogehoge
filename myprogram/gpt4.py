import openai

openai.api_key = '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'

def generate_text(prompt, conversation_history):
    # プロンプトを会話履歴に追加
    conversation_history.append({"role": "user", "content": prompt})

    # GPT-4モデルを使用する場合
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history
    )
    message = ""

    for choice in response.choices:
        message += choice.message['content']

    # 応答文を会話履歴に追加
    conversation_history.append({"role": "assistant", "content": message})
    return message

if __name__ == "__main__":
    # 会話履歴を格納するためのリストを初期化
    conversation_history = []

    while True:
        # ユーザーに質問を入力させる
        input_prompt = input("プロンプト: ")
        generated_text = generate_text(input_prompt, conversation_history)
        print("応答:", generated_text)