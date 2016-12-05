#!usr/bin/python
#coding:utf-8

import time, threading
# 新线程执行的代码------------------------------------------------------
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    time.sleep(0.5)
    print('thread %s ended.' % threading.current_thread().name)
#-------------------------------------------------------------------------
print('thread %s is running...' % threading.current_thread().name)
t0 = threading.Thread(target=loop)#name='LoopThread'
t1 = threading.Thread(target=loop)#name='LoopThread'
t0.start()
t1.start()
t0.join()
t1.join()
print('thread %s ended.' % threading.current_thread().name)
'''
thread MainThread is running...
thread Thread-1 is running...
thread Thread-2 is running...
thread Thread-1 ended.
thread Thread-2 ended.
thread MainThread ended
'''
#===================================================================
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(10):
        lock.acquire()
        change_it(n)
        lock.release()

t3 = threading.Thread(target=run_thread, args=(5,))
t4 = threading.Thread(target=run_thread, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print(balance)#0
#=================================================================
# 创建全局锁 Thread_Local 对象:
LOCK = threading.local()
def hello_student():
    # 获取当前线程关联的student:
    std = LOCK.student
    print('hello %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    # 绑定ThreadLocal的student:
    LOCK.student = name
    hello_student()
t5 = threading.Thread(target= process_thread, args=('student_A',))
t6 = threading.Thread(target= process_thread, args=('student_B',))
t5.start()
t6.start()
t5.join()
t6.join()
'''
hello student_A (in Thread-5)
hello student_B (in Thread-6)
'''
#=====================================================================
