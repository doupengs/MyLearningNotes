#!/usr/bin/python
#coding:utf-8

# task_master.py
# 服务器端，往任务队列中放任务后，从结果队列中获取结果

import time
import queue
from multiprocessing.managers import BaseManager
# from multiprocessing import freeze_support   # 不用加也可以正常启动服务器
"""
当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始
的task_queue进行操作，那样就绕过了QueueManager的封装，
必须通过manager.get_task_queue()获得的Queue接口添加。
"""

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

# 注册到网络register
def start_server():
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    # register内不要使用lambda，否则win7运行出错
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000，设置验证码'abc'
    # win7 需要写ip地址
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放20个任务进去
    for i in range(1,21):
        print('Put task %d: calculate %d + %d = ?' % (i,i,i))
        time.sleep(0.1)
        task.put(i)
    # 从result队列读取结果
    print('Try get results...')
    # 服务器已经准备好接收数据，故开始启动task_worker.py
    while True:
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('result queue is empty.')
            break
    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    # freeze_support()      # 注释掉也可以正常运行
    start_server()
