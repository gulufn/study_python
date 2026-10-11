from pathlib import Path
from mutagen import File
import sys
sys.stdout.reconfigure(encoding='utf-8')
import csv

def get_format(s):
    pos = s.rfind(".")        # 从右往左找第一个点
    result = s[pos + 1:]      # 取点后面的部分
    return result

file_path='./asses/music/'
dir_path = Path(file_path)
a = []
b = []
c=[]
# 只遍历该目录下的文件（不含子目录）
for file in dir_path.iterdir():
    if file.is_file():
        # print(file_path+file.name)
        audio = File(file_path+file.name)  
        if(get_format(file.name)=='m4a'):
            a.append(file.name)
            b.append(audio.tags.get("©nam", ["未知"])[0])
            c.append(audio.tags.get("©ART", ["未知"])[0])
            print(file.name+'---'+audio.tags.get("©nam", ["未知"])[0] if audio.tags else "无标签")
        if(get_format(file.name)=='ogg'):
            a.append(file.name)
            b.append(audio.tags.get("album", ["未知"])[0])
            c.append(audio.tags.get("artist", ["未知"])[0])
            print(file.name+'---'+audio.tags.get("album", ["未知"])[0] if audio.tags else "无标签")
# print(get_format('m4a'))

with open('./makeshift/music_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_ALL)
    writer.writerow(['name', 'title','author'])   # 表头
    writer.writerows(zip(a, b, c))          # 按行配对写入
