import threading
class a(threading.Thread):
    def run(self):
        for i in range(0,5):
            print(threading.currentThread)
t=a()
t1=a()
t2=a()
t3=a()
t.start()
t1.start()
t2.start()
t3.start()
