import time
# 导入多进程模块
import multiprocessing
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os


def p1(n, lock):
    total=0
    for i in range(n):
        total=total+i
    # print(total)
    with lock:                 # 同一时刻只有一个进程能进来
        print(f"进程{os.getpid()}计算结果为：{total}")
    return total

    
if __name__ == '__main__':
    #记录开始时间
    start_time = time.time()
    print(start_time)
    #设置运行次数
    n=1000
    # 进程锁
    lock = multiprocessing.Lock()


    # 用逻辑核心数减半，或者直接查物理核心数
    num_procs = os.cpu_count() // 2   # 粗略估算物理核心
    print(f"逻辑核心数: {os.cpu_count()}, 物理核心数: {num_procs}")
    # 创建进程列表
    procs = []
    for _ in range(2):
        p = multiprocessing.Process(target=p1, args=(n, lock,))
        p.start()                # 进程已经在运行了，不用等运行结果，继续执行下一行代码
        procs.append(p)          # 将进程对象添加到列表中

    for p in procs:
        print(f"{p}")
        p.join()                 # 等待进程结束，阻塞主进程，直到所有子进程结束
        
        
    end_time = time.time()
    #记录结束时间
    print(end_time)
    print(f"耗时{end_time-start_time}秒")


