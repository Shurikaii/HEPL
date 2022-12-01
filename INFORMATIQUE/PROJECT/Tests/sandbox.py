from threading import Thread
import time

def getvalue():
    n = 0
    while True:
        time.sleep(1)
        n = n + 1
        print(n)
        
def hourra():
    while True:
        time.sleep(5.1)
        print("Hourra!")
        

threadlist = []

threadlist.append(Thread(target=getvalue))
threadlist.append(Thread(target=hourra))

for t in threadlist:
    t.start()
for t in threadlist:
    t.join()