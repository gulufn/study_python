import re
import csv
import urllib.request
from bs4 import BeautifulSoup
import csv
import sys, io
import time
from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

content=''
with open('./asses/DOC/english_v.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# print(type(content))

a = re.sub(r'[^A-Za-z0-9 ]', '', content)  #只保留英文字母、数字、空格
# print(a)

b = re.split(r'\d+', a)   #以数字为分隔符，切片
del b[0]
# print(b)

c=[]
for i in b:
    c.append(i.strip())      # 去掉字符串首尾的空格
# print(c)
# print(len(c))

obj={}
url=f"https://dict.youdao.com/result?word={c[0]}&lang=en"
print(url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    for i in range(0,299):
        url=f"https://dict.youdao.com/result?word={c[i]}&lang=en"
        if(i<0):
            continue
        if(i==2):
            break
        page.goto(url, wait_until='domcontentloaded', timeout=20000)  # 等待网络加载完成networkidle
        page.click('.more span.unfold')   # 找到 class 为 more 的元素，再在它内部找到 class 为 unfold 的 <span> 元素
        page.wait_for_timeout(500)        # 强制等待 500 毫秒
        content = page.content()          # 返回当前页面的完整 HTML 源码

        soup = BeautifulSoup(content, 'html.parser')
        div_content = soup.find('div', class_='simple dict-module')
        li=div_content.find('li',class_='word-exp')
        obj['单词']=c[i]
        obj['词性']=li.find_all('span')[0].text
        obj['意思']=li.find_all('span')[1].text

        ff=div_content.find('ul',class_='word-wfs-less')
        obj['单三']=ff.find_all('li')[0].find_all('span')[-1].text
        obj['现在分词']=ff.find_all('li')[1].find_all('span')[-1].text
        obj['过去式']=ff.find_all('li')[2].find_all('span')[-1].text
        obj['过去分词']=ff.find_all('li')[3].find_all('span')[-1].text
        # print(obj)

        duanyu = soup.find('ul', class_='trans-container')
        danci = [a.text for a in duanyu.find_all('a', class_='point')]
        yisi = [a.text for a in duanyu.find_all('span', class_='phr_trans')]
        # print(danci)
        
        # 字典类型追加写入csv
        with open('./makeshift/words.csv', 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['单词', '词性', '意思','单三','现在分词','过去式','过去分词']
            writer = csv.DictWriter(f,fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
            writer.writerow(obj)
        with open('./makeshift/duanyu.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            # 先写表头
            writer.writerow(['短语', '解释'])
            # 使用zip将多个列表按行组合
            rows = zip(danci,yisi)
            for row in rows:
                writer.writerow(row)
    browser.close()