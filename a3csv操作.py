import csv
# 引号策略
# csv.QUOTE_MINIMAL   # 默认，只在必要时加引号
# csv.QUOTE_ALL       # 所有字段都加引号
# csv.QUOTE_NONNUMERIC# 非数字加引号
# csv.QUOTE_NONE      # 不加引号
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("读取CSV文件--------------------------------------------------")
# 读取CSV文件,设置分隔符为逗号，跳过表头
with open('./asses/DOC/test_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f,delimiter=',')
    # reader 是一个迭代器对象
    next(reader)    #跳过表头
    for row in reader:
        print(row)   # row 是一个列表，如 ['A', '1', 'Apple']
print("字典类型读取CSV文件--------------------------------------------------")
# 字典类型读取CSV文件，按列名取值
with open('./asses/DOC/test_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)          # 有序字典，如 {'字母': 'A', '数字': '1', '水果': 'Apple'}
        print(row['水果'])   # 按列名取值
print("读取CSV文件，取表头--------------------------------------------------")
# 读取CSV文件，取表头
with open('./asses/DOC/test_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)   # 取第一行
    print(header)           # ['字母', '数字', '水果']
print("读取CSV文件，全部加载到内存--------------------------------------------------")
# 读取CSV文件，全部加载到内存
with open('./asses/DOC/test_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)     # 转成列表，全部加载到内存
    print(rows)             # [['字母', '数字', '水果'], ['A', '1', 'Apple'], ['B', '2', 'Banana'], ['C', '3', 'Cherry'], ['D', '4', 'Date']]
print("列表写入CSV文件========================================================")
# 列表写入CSV文件,并添加引号策略,指定引号为单引号，设置换行符
a=["name","age","sex"]
b=["bob","18","Y"]
c=["alice","19","X"]
v=[]
v.append(b)
v.append(c)
with open('./makeshift/output0.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f,quoting=csv.QUOTE_ALL,quotechar="'",lineterminator='\r\n')
    writer.writerow(a)          # 写一行
    writer.writerows(v)         # 写多行
print("字典写入csv文件--------------------------------------------------")
# 字典写入csv文件
a={}
a['name']='bob'
a['age']='18'
a['sex']='Y'
b={'name': 'alice', 'age': '19', 'sex': 'X'}
c={'name': 'Helen', 'age': '21', 'sex': 'X'}
d=[]
d.append(a)
d.append(b)
print(d)
with open('./makeshift/output1.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'age', 'sex']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()          # 自动写表头
    writer.writerow(c)              #写一行
    writer.writerows(d)             # 写多行
print("字典类型追加写入csv--------------------------------------------------")
a={'name': 'LiHua', 'age': '25', 'sex': 'Y'}
# 字典类型追加写入csv
with open('./makeshift/output1.csv', 'a', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'age', 'sex']
    writer = csv.DictWriter(f, fieldnames=fieldnames)      
    writer.writerow(a)
print("列表类型追加写入csv--------------------------------------------------")
a=['Li,hua','25','Y']
with open('./makeshift/output1.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(a)

print("多列表按列合并写入csv--------------------------------------------------")
# 多列表按列合并写入csv
list1 = ['A', 'B', 'C', 'D']
list2 = [1, 2, 3, 4]
list3 = ['Apple', 'Banana', 'Cherry', 'Pear']
# 写入CSV
with open('./makeshift/output2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
     # 先写表头
    writer.writerow(['字母', '数字', '水果'])
    # 使用zip将多个列表按行组合
    rows = zip(list1, list2, list3)
    for row in rows:
        writer.writerow(row)

