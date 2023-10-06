# 1
with open("anything.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 2
# answer = input("what is your name?")
# with open("anything.txt", "w", encoding="utf-8") as f:
#     f.write(answer)

# 3
import csv
movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for movie_list in movies:
        w.writerow(movie_list)
