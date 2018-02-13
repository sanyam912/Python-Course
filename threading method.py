import threading
class a(threading.Thread):
    def run(self):
        for i in range(0,5):
            print(threading.currentThread(),i)
t=a()
t1=a()
t.start()
t.join()
print(t.isAlive())
t1.start()
