#EXERCICE 1
import threading
import time
t = int(input("Combien d'itération? : "))

def task(i):
    for j in range(t):
        print(f"Je suis la Thread {i}")
        time.sleep(1)


start = time.perf_counter()
l = int(input("Vous voulez combiez de thread? : "))
T = []
for i in range(l):
    T.append(threading.Thread(target=task, args=[i]))

for i in range(l):
    T[i].start()

for i in range(l):
    T[i].join()

end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")

#EXERCICE 2

def timer1(i):
    times = 7
    for n in range(times):
        print(f"Thread 1/{i} : {times}")
        time.sleep(1)
        times = times - 1 

def timer2(i):
    times = 5
    for n in range(times):
        print(f"Thread 2/{i} : {times}")
        time.sleep(1)
        times = times - 1 

start = time.perf_counter()

t1 = int(input("Vous voulez combiez de thread pour le timer 1 : "))
t2 = int(input("Vous voulez combiez de thread pour le timer 1 : "))
T1 = []
T2 = []
for i in range(t1):
    T1.append(threading.Thread(target=timer1, args=[i]))
for i in range(t2):
    T2.append(threading.Thread(target=timer2, args=[i]))

for i in range(t1):
    T1[i].start()
for i in range(t2):
    T2[i].start()

for i in range(t1):
    T1[i].join()
for i in range(t2):
    T2[i].join()


end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")
