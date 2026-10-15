import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
from utils import Utils


folder_path = r"C:/Users/gulu/Videos/电视剧/果宝特攻1/"  # 改成你的路径


n=1
for filename in os.listdir(folder_path):
    if(Utils.get_format(filename)=='mp4'):
        old_path = os.path.join(folder_path, filename)
    # print(filename)
        print(old_path)
    
        # 只处理文件，跳过文件夹
        if os.path.isfile(old_path):
            new_name = f"tv_{n:04d}_video_1080p.{Utils.get_format(filename)}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"{filename} -> {new_name}")
        n=n+1