#coding=utf-8
import threading
from time import ctime,sleep

f = open('C:/Users/yuying/Desktop/1.txt','a')

def music(func):
    for i in range(2):
        a = "I was listening to %s. %s" %(func,ctime())
        print a
        sleep(1)
        f.write('music_%s\n'%i)

def move(func):
    for i in range(2):
        b = "I was at the %s! %s" %(func,ctime())
        print b
        sleep(5)
        f.write('move_%s\n'%i)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    # sleep(11)
    # join()方法，用于等待子线程终止后再执行父进程
    t.join()
    print "\nall over %s" %ctime()
    f.close()
