# SuperFastPython.com
# example of running a function in another thread
from time import sleep
from threading import Thread
 
# a custom function that blocks for a moment
def task(num, ar):
    # block for a moment
    sleep(1)
    # display a message
    if num == "2":
        sleep(1)
    print('This is from thread' + num)
    print("args is:" + ar)
 
# create a thread
thread = Thread(target=task, args=["1", "1s arg"])
thread2 = Thread(target=task, args=["2", "2s arg"])
# run the thread
thread.start()
thread2.start()