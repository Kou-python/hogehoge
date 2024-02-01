import random

board=[[" "," "," "],[" "," "," "],[" "," "," "]]

"""
while:
    ぼーど
    俺→相手
    判定

勝敗→break
"""

# 関数宣言
line=None
result = None
player_select = board[select_row][select_line]


#初期設定
print("3目並べスタート！")
turn=random.randint(1, 2)
if turn==1:
    print("あなたは◯です(先行)")
    player_mark="◯"
    cpu_mark="×"
else:
    print("あなたは×です（後行）")
    player_mark="×"
    cpu_mark="◯"

# 入力を受け取る
def get_input(player):
    while True:
        try:
            row = int(input("Enter row number (1-3): "))
            col = int(input("Enter column number (1-3): "))
            if board[row-1][col-1] != " ":
                print("That spot is already taken. Please try again.")
            else:
                board[row-1][col-1] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 3.")

def cpu_input(cpu):
    while True:
        row=random.randint(0, 2)
        col=random.randint(0, 2)
        if board[row][col] != " ":
            continue
        else:
            board[row][col]=cpu
            break


#ゲームのメインループ
while True:
    # ボード表示
    # print(*board, sep="\n")
    for row in board : print("|".join(row))

    #入力
    get_input(player)


    #出力
    player_select=player_mark

    # 判定
    for i in len(board):


    #終わり
    if result==win:
        print("You Win! Congratulations！")
        break
    elif result==lose:
        print("You Lose...")
        break