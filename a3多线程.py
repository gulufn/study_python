import time
# 导入多线程模块
import threading
import sys
sys.stdout.reconfigure(encoding='utf-8')

def p1(n):
    total = 0
    for i in range(n):
        total = total + i
    print(f"线程{threading.current_thread().name}计算结果为：{total}")
    return total

if __name__ == '__main__':
    start_time = time.time()
    print(start_time)
    #设置运行次数
    n=1000000

    # 创建线程列表
    threads = []
    for _ in range(6):
        t = threading.Thread(target=p1, args=(n,))
        t.start()                # 线程已经在运行了，不用等运行结果，继续执行下一行代码
        threads.append(t)          # 将线程对象添加到列表中

    for t in threads:
        print(f"线程：{t}")
        t.join()                 # 等待线程结束，阻塞主进程，直到所有子线程结束

    end_time = time.time()
    print(end_time)
    print(f"{end_time - start_time}")