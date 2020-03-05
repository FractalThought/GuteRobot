'''

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
