#!usr/bin/python
#coding:utf-8

# 1 fork() 2 multiprocessing Process 3 multiprocessing Pool
# 1=======================================================================================
# fork()只在 Unix/Linux/Mac 有
# import os
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#---------------------------------------------------------------------------------------
'''
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''
# 2=======================================================================================
# from multiprocessing import Process
# from time import sleep
# import os
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#     sleep(2)
#     print('child process %s (%s) end' % (name, os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p0 = Process(target=run_proc, args=('test0',))
#     p1 = Process(target=run_proc, args=('test1',))
#     print('Child process will start.')
#     p0.start()
#     p1.start()
#     #p0.join()
#     #p1.join()
#     print('Child process end.')
#---------------------------------------------------------------------------------------
'''
Parent process 38628.
Child process will start.
Child process end.
Run child process test0 (30284)...
Run child process test1 (35316)...
child process test0 (30284) end
child process test1 (35316) end
'''
# 3=======================================================================================
from multiprocessing import Pool
from time import sleep
import os
#多进程执行的程序
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    sleep(2)
    print('child process %s (%s) end' % (name, os.getpid()))

if __name__=='__main__':
    #主进程-管理者|调度者
    print('Parent process %s.' % os.getpid())
    #进程池-并发工作者
    p = Pool(4)
    for i in range(6):
        p.apply_async(run_proc, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
#---------------------------------------------------------------------------------------
'''
Parent process 17688.
Waiting for all subprocesses done...
Run child process 0 (28080)...
Run child process 1 (37328)...
Run child process 2 (35624)...
Run child process 3 (36908)...
child process 0 (28080) end
Run child process 4 (28080)...
child process 1 (37328) end
Run child process 5 (37328)...
child process 2 (35624) end
child process 3 (36908) end
child process 4 (28080) end
child process 5 (37328) end
All subprocesses done.
'''
#===========================================================================================
