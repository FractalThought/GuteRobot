'''

https://flask.palletsprojects.com/en/1.1.x/appcontext/

https://diegoquintanav.github.io/flask-contexts.html

http://kronosapiens.github.io/blog/2014/08/14/understanding-contexts-in-flask.html

from flask import g

def get_robot():
    if 'robot' not in g:
        g.robot = activate_robot()

    return g.robot

# @app.teardown_appcontext
# def teardown_db():
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()



https://realpython.com/async-io-python/

Use a singleton thread that is stopped and started by the server
The thread is started and the process is started by sending a request with the data for the instructions

arrayOfTasks

request(data)
    add data to an arrayOfTasks
    while(arrayOfTasks.length > 0)
        await RunTask(arrayOfTasks[0])
        remove arrayOfTasks[0] from arrayOfTasks

async RunTask(task)
    DoRunTask(task.type)
    delay task.delay
    return

What it won't be able to do:
Send the status of the robot
Queue up tasks over multiple requests

'''

# https://www.tutorialspoint.com/python/python_multithreading.htm
# https://dzone.com/articles/python-thread-part-1
# https://www.geeksforgeeks.org/multithreading-python-set-1/

import threading
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
