import random


def hangman(word):
    wrong = 0
    stages = [
        "",
        "__________          ",
        "|         |          ",
        "|         |         ",
        "|         O         ",
        "|        /|\        ",
        "|        / \        ",
        "|                   ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字を予想してね")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break


word_list = [
    "cat",
    "dog",
    "bird",
    "fish",
    "snake",
    "rabbit",
    "mouse",
    "pig",
    "cow",
    "horse",
]
hangman(word_list[random.randint(0, len(word_list) - 1)])

