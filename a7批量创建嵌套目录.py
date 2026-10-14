import sys
sys.stdout.reconfigure(encoding='utf-8')
from utils import Utils
import csv
import os
import json

# 目录结构
tv_shows =[
    {
        "name": "秦时明月",
        "seasons": [
            {"season": 1, "episodes": 3,"name":"百步飞剑","form":"mp4"},
            {"season": 2, "episodes": 4,"name":"夜尽天明","form":"flv"},
            {"season": 3, "episodes": 3,"name":"诸子百家","form":"flv"},
            {"season": 4, "episodes": 4,"name":"万里长城","form":"mp4"},
            {"season": 5, "episodes": 2,"name":"君临天下","form":"mp4"}
        ]
    },
    {
        "name": "果宝特攻",
        "seasons": [
            {"season": 1, "episodes": 2, "name":"果宝特攻第1季","form":"mp4"},
            {"season": 2, "episodes": 2, "name":"果宝特攻第2季","form":"mp4"},
            {"season": 3, "episodes": 6, "name":"果宝特攻第3季","form":"mp4"},
            {"season": 4, "episodes": 1, "name":"果宝特攻第4季","form":"mp4"}
        ]
    },
    {
        "name": "果冻三剑客",
        "seasons": [
            {"season": 1, "episodes": 1, "name":"果冻三剑客","form":"mp4"}
        ]
    },
    {
        "name": "天行九歌",
        "seasons": [
            {"season": 1, "episodes": 3, "name":"天行九歌","form":"mp4"}
        ]
    },
    {
        "name": "爬虫",
        "seasons": [
            {"season": 1, "episodes": 4, "name":"爬虫教程","form":"mp4"}
        ]
    }
]

# 根目录
base_path='./tvshows/'
# 电视剧所在的文件夹的目录，集合
dir_tvshows=[Utils.generate_random_str(18) for _ in range(len(tv_shows))]
# 每季电视剧的目录结构
data = {
    "title": "",
    "cover_image": "img.png",
    "sources": [
    {"quality": "1080p", "path": "video_1080p.mkv"}
    ]
}

# 剧名
tv_names=[]

n=0
for show in tv_shows:
    tv_names.append(show['name'])
    for s in show["seasons"]:
        # 目录名，季
        dir_path = os.path.join(base_path,dir_tvshows[n] , f"season{s['season']}")
        os.makedirs(dir_path, exist_ok=True)
        json_path=dir_path +'/data.json'
        with open(json_path, "w", encoding="utf-8") as f:
            data['title'] = s['name']
            data["sources"][0]["path"] = "video_1080p"+'.'+s['form']   # 改嵌套
            json.dump(data, f, ensure_ascii=False, indent=4)
    n=n+1


# 写入CSV
with open('./makeshift/output5.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_ALL)
     # 先写表头
    writer.writerow(['目录名', '电视剧名'])
    # 使用zip将多个列表按行组合
    rows = zip(dir_tvshows,tv_names)
    for row in rows:
        writer.writerow(row)




