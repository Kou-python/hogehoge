# 1
movie = ["ウォーキング・デッド", "アントラージュ", "ヴァンパイア・タリアリーズ"]

# 2
# for i in range(25,51): #range(25,51)は25から50までの数字を返す。
#     print(i)

# 3
for i in enumerate(movie):
    print(i)

# 4
numbers = [1, 23, 62, 11, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


def take_guess():
    """
    ユーザーに数字を入力させる。
    入力された数字がnumbersに含まれているかどうかを判定する。
    """
    while True:
        guess = input("数字を入力してください。qを入力で終了します。>>>")
        if guess == "q":
            break
        try:
            guess = int(guess)
        except ValueError:
            print("不正な値です。数字を再入力してください")
        if guess in numbers:
            print("正解です。")
        else:
            print("不正解です。")


# 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)
print(list3)
