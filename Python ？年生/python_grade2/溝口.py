import folium
import pandas as pd
from pathlib import Path

of= Path("download")
of.mkdir(exist_ok=True)

#データフレームを読み込む
df= pd.read_csv("CSV/facility.csv", encoding="shift_jis")
# 地図作成
m=folium.Map([35.599358400000000, 139.610445600000000], zoom_start=18)
# 地点をリスト化：配列形式になる
store= df[["lat","lon","name_ja"]].values
#ヘッダー出力
# print(list(df.columns.values))
#記述複雑注意!!!最後にadd_to(m)つける
for i in store:
    folium.Marker([i[0],i[1]], tooltip= i[2]).add_to(m)
m.save("download/mizonokuchi.html")
print("出力完了")