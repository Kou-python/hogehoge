favorite_musician={
    "花譜": "さよなら、花泥棒さん", 
    "星街すいせい": "GHOST",
    "あらき": "虎視眈々", 
    "めいちゃん": "よもすがら君を想う", 
    "Gero": "うどん", 
    "VESPERBELL": "Ecllipse" 
    }

have_gone= (35.57865794607058, 139.65998098034248)

my_characters = {
    "趣味": "歌唱",
    "好きな色": "青色",
    "特技": "口笛"
    }

def output_my_characters():
    print(my_characters.keys())
    key=input("俺の何を知りたい？ >")
    print(my_characters[key])

# set は、順序がなく、異なる型でも値が等価であれば重複していると見なされる。
s={1, 1.0, True, False}
print(s)

def match_characters():
    print(my_characters.keys())
    