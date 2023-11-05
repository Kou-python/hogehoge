# print("""line 1
# line 2
# line 3
# """)

# name= "Taro"
# sex="male"
# print("こんにちは{}の{}さん".format(sex,name))
# print(f"こんにちは、{name}さん")

# 1
for i in "カミュ":
    print(i)
# 2
# x=input("何をかく？ >")
# y= input("誰に送る？ >")
# print(f"私は昨日{x}を書いて、{y}に送った")
# 3
print("i have a pen".capitalize())
# 4
print("どこで？　誰が？　いつ？".split("　"))
# 5
sentence = ("The fox jumped over the fence .").split(" ")
print("変更前: ", sentence)
print(" ".join(sentence))
# 6
print("A screaming comes across the sky.".replace("s", "$"))
# 7
print("hemingway".index("m"))
# 8
print('I have a "nice" pen')
# 9
sentence2 = "three"
print(sentence2 + sentence2 + sentence2)
print(sentence2 * 3)
# 10
print("4月の晴れた寒い日で、時計がどれも一三時を打っていた。"[:10])