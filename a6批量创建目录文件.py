import sys
sys.stdout.reconfigure(encoding='utf-8')
from utils import Utils
import csv
import os
import json


movies_name=['流浪地球1.mp4','原神.mkv','秦时明月之龙腾万里.mp4']
# 根目录
base_path='./movies/'
# 电影所在的文件夹的目录，集合
dir_movies=[Utils.generate_random_str(18) for _ in range(len(movies_name))]
# 拼接路径
dir_paths=[base_path+i+'/' for i in dir_movies]
# print(dir_paths)

# # 创建目录（exist_ok=True 表示目录已存在时不报错）
for i in dir_paths:
    os.makedirs(i, exist_ok=True)
# json数据
data = {
    "title": "",
    "cover_image": "img.png",
    "sources": [
    {"quality": "1080p", "path": "video_1080p.mkv"}
    ]
}
movies_title=[]
movies_form=[]
for i in movies_name:
    movies_title.append(os.path.splitext(i)[0])
    movies_form.append(Utils.get_format(i))
n=0
for i in dir_paths:
    with open(i+'data.json', "w", encoding="utf-8") as f:
        data['title'] = movies_title[n]
        data["sources"][0]["path"] = "video_1080p"+'.'+movies_form[n]   # 改嵌套
        n=n+1
        json.dump(data, f, ensure_ascii=False, indent=4)

# 写入CSV
with open('./makeshift/output4.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_ALL)
     # 先写表头
    writer.writerow(['目录名', '电影名','格式'])
    # 使用zip将多个列表按行组合
    rows = zip(dir_movies,movies_title,movies_form)
    for row in rows:
        writer.writerow(row)

print(movies_title)

