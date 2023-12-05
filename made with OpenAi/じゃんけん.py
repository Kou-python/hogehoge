import random

# じゃんけんの手を表す定数
ROCK = 0
PAPER = 1
SCISSORS = 2

# じゃんけんの手を表す文字列
HANDS = {
    ROCK: "グー",
    PAPER: "パー",
    SCISSORS: "チョキ"
}

# 勝敗を表す定数
WIN = 0
LOSE = 1
DRAW = 2

# 勝敗を表す文字列
RESULTS = {
    WIN: "勝ち",
    LOSE: "負け",
    DRAW: "あいこ"
}

# プレイヤーの手を入力する
player_hand = None
while player_hand not in HANDS.keys():
    print("じゃんけんの手を入力してください。")
    print("[0]: グー, [1]: パー, [2]: チョキ")
    player_hand = int(input("> "))

# コンピュータの手をランダムに選択する
computer_hand = random.choice(list(HANDS.keys()))

# 勝敗を判定する
if player_hand == computer_hand:
    result = DRAW
elif player_hand == ROCK and computer_hand == SCISSORS:
    result = WIN
elif player_hand == PAPER and computer_hand == ROCK:
    result = WIN
elif player_hand == SCISSORS and computer_hand == PAPER:
    result = WIN
else:
    result = LOSE

# 結果を表示する
print("あなたの手: {}".format(HANDS[player_hand]))
print("コンピュータの手: {}".format(HANDS[computer_hand]))
print("結果: {}".format(RESULTS[result]))
