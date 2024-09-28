#variable scope 
'''
global_var=10

def outer_fun():
    outer_var=20    #local scope


    def inner_fun():
       inner_var=30  #nested local scope

       print(inner_var)
       print(outer_var)


    inner_fun()


print(global_var)
outer_fun()
'''

import time
import threading

def print_hello():
    print("hello")
    time.sleep(2)

def print_world():
    print("world")
    time.sleep(2)

thread1=threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_world)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("both finished")