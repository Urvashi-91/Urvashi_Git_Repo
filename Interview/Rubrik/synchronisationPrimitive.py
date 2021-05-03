'''
We do so by using synchronization primitives. These are simple software mechanisms that ensure
your threads run in a harmonious manner with each other.
'''
'''
LOCK: acquire() release()
'''
# lock_tut.py
from threading import Lock, Thread

lock = Lock()
g = 0


def add_one():
    """
    Just used for demonstration. It's bad to use the 'global'
    statement in general.
    """

    global g
    lock.acquire()
    g += 1
    lock.release()


def add_two():
    global g
    lock.acquire()
    g += 2
    lock.release()


threads = []
for func in [add_one, add_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    """
    Waits for threads to complete before moving on with the main
    script.
    """
    thread.join()

print(g)


'''
RLOCK: re-entrant Lock, prevent unwanted Locking
'''
#rlock_tut.py
import threading

num = 0
lock = Threading.Lock()

lock.acquire()
num += 1
lock.acquire() # This will block.
num += 2
lock.release()


# With RLock, that problem doesn't happen.
lock = Threading.RLock()

lock.acquire()
num += 3
lock.acquire() # This won't block.
num += 4
lock.release()
lock.release() # You need to call release once for each call to acquire.

'''
Semaphores: advanced counter
acquire() release()
'''

#semaphores_tut.py
import random, time
from threading import BoundedSemaphore, Thread
max_items = 5
"""
Consider 'container' as a container, of course, with a capacity of 5
items. Defaults to 1 item if 'max_items' is passed.
"""
container = BoundedSemaphore(max_items)
def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, skipping.")
def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        """
        In the following if statement we disable the default
        blocking behaviour by passing False for the blocking flag.
        """
        if container.acquire(False):
            print("Consumed an item.")
        else:
            print("Empty, skipping.")
threads = []
nloops = random.randrange(3, 6)
print("Starting with %s items." % max_items)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops, nloops+max_items+2),)))
for thread in threads:  # Starts all the threads.
    thread.start()
for thread in threads:  # Waits for threads to complete before moving on with the main script.
    thread.join()
print("All done.")


'''
Event: Event synchronization primitive acts as a simple communicator between threads.
set() clear()
wait()
'''
#event_tut.py
import random, time
from threading import Event, Thread

event = Event()

def waiter(event, nloops):
    for i in range(nloops):
    print("%s. Waiting for the flag to be set." % (i+1))
    event.wait() # Blocks until the flag becomes true.
    print("Wait complete at:", time.ctime())
    event.clear() # Resets the flag.
    print()

def setter(event, nloops):
    for i in range(nloops):
    time.sleep(random.randrange(2, 5)) # Sleeps for some time.
    event.set()

threads = []
nloops = random.randrange(3, 6)

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print("All done.")

'''
Conditions:used to notify() other threads about a change in the state of the program.'''
#condition_tut.py
import random, time
from threading import Condition, Thread
"""
'condition' variable will be used to represent the availability of a produced
item.
"""
condition = Condition()
box = []
def producer(box, nitems):
    for i in range(nitems):
        time.sleep(random.randrange(2, 5))  # Sleeps for some time.
        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # Puts an item into box for consumption.
        condition.notify()  # Notifies the consumer about the availability.
        print("Produced:", num)
        condition.release()
def consumer(box, nitems):
    for i in range(nitems):
        condition.acquire()
        condition.wait()  # Blocks until an item is available for consumption.
        print("%s: Acquired: %s" % (time.ctime(), box.pop()))
        condition.release()
threads = []
"""
'nloops' is the number of times an item will be produced and
consumed.
"""
nloops = random.randrange(3, 6)
for func in [producer, consumer]:
    threads.append(Thread(target=func, args=(box, nloops)))
    threads[-1].start()  # Starts the thread.
for thread in threads:
    """Waits for the threads to complete before moving on
       with the main script.
    """
    thread.join()
print("All done.")

'''
Barriers: simple synchronization primitive which can be used by different threads to wait for each other.
'''
# barrier_tut.py
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num = 4
# 4 threads will need to pass this barrier to get released.
b = Barrier(num)
names = ["Harsh", "Lokesh", "George", "Iqbal"]


def player():
    name = names.pop()
    sleep(randrange(2, 5))
    print("%s reached the barrier at: %s" % (name, ctime()))
    b.wait()


threads = []
print("Race starts now…")

for i in range(num):
    threads.append(Thread(target=player))
    threads[-1].start()
"""
Following loop enables waiting for the threads to complete before moving on with the main script.
"""
for thread in threads:
    thread.join()
print()
print("Race over!")