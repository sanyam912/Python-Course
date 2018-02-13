from threading import Event,_RLock
import threading
class a(threading.Thread):
    def run(self):
        r.wait(2)
        print(threading.currentThread().getName())
        r1.acquire()
        for i in range(0,5):
             print(threading.currentThread().getName(),i)
        r1.release()
threads=[]
r=Event()
r1=_RLock()
t=a()
t1=a()
t2=a()
t3=a()
t.setName('ab')
t1.setName('cd')
t2.setName('ef')
t3.setName('gh')
t.start()
t1.start()
t2.start()
t3.start()
threads.append(t)
threads.append(t1)
threads.append(t2)
threads.append(t3)
for i in threads:
    i.join()
