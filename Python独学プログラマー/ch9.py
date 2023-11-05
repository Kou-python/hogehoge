# 1
with open("anything.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 2
# answer = input("what is your name?")
# with open("anything.txt", "w", encoding="utf-8") as f:
#     f.write(answer)

# 3
"""
csvファイル新規作成
リストをcsvファイルに書き込む
"""

import csv

movies = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"],
]
with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies:
        w.writerow(i)

# 4
movies_ja = [
    ["トップガン", "リスキービジネス", "マイノリティリポート"],
    ["タイタニック", "ザ・レヴェナント", "インセプション"],
    ["トレーニングデイ", "マンオンファイア", "フライト"],
]
with open("movies_ja.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for i in movies_ja:
        w.writerow(i)
        print(i)
