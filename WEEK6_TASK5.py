import threading
import time

def print_even():
    for i in range(0, 10, 2):
        print(f"Even: {i}")
        time.sleep(0.5)

def print_odd():
    for i in range(1, 10, 2):
        print(f"Odd: {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()
