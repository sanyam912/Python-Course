import _thread

def a1(threadName):
    for i in range(0,5):
        print(threadName,i)
def a2(threadName):
    for i in range(0,5):
        print(threadName,i)
_thread.start_new_thread(a1,("Thread1",))
_thread.start_new_thread(a2,("Thread2",))
_thread.start_new_thread(a1,("Thread3",))
