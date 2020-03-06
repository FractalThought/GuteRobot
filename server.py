from flask import Flask, render_template, request
import robotcontroller as robot
import RPi.GPIO as gpio
import time
import threading

# https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

leftWheelsForwards = 23
leftWheelsBackwards = 24
rightWheelsForwards = 20
rightWheelsBackwards = 21


def LeftWheels(direction):
    forwards = True
    if(direction == "backwards"):
        forwards = False
    gpio.output(leftWheelsForwards, forwards)
    gpio.output(leftWheelsBackwards, not forwards)
    print("Left wheels going " + direction)


def RightWheels(direction):
    forwards = True
    if(direction == "backwards"):
        forwards = False
    gpio.output(rightWheelsForwards, forwards)
    gpio.output(rightWheelsBackwards, not forwards)
    print("Right wheels going " + direction)


def init():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(leftWheelsForwards, gpio.OUT)  # Left wheels forwards
    gpio.setup(leftWheelsBackwards, gpio.OUT)  # Left wheels backwards
    gpio.setup(rightWheelsForwards, gpio.OUT)  # Right wheels forwards
    gpio.setup(rightWheelsBackwards, gpio.OUT)  # Right wheels backwards
    print("GPIO initialized")


def forward():
    stop()
    RightWheels("forwards")
    LeftWheels("forwards")


def backward():
    stop()
    RightWheels("backwards")
    LeftWheels("backwards")


def right():
    stop()
    RightWheels("backwards")
    LeftWheels("forwards")


def left():
    stop()
    RightWheels("forwards")
    LeftWheels("backwards")


def stop():
    gpio.output(leftWheelsForwards, False)
    gpio.output(leftWheelsBackwards, False)
    gpio.output(rightWheelsForwards, False)
    gpio.output(rightWheelsBackwards, False)


# Run the Init-function to initialize the GPIO
init()

app = Flask(__name__)
@app.route("/")
def index():
    templateData = {
        'title': 'GuteRobot'
    }
    return render_template('index.html', **templateData)


@app.route('/', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()

    templateData = {
        'title': "lol"
    }
    return render_template('index.html', **templateData)


@app.route("/<action>")
def action(action):
    actionName = ""
    if (action == "f"):
        forward()
        actionName = "forward"
    elif (action == "l"):
        left()
        actionName = "left"
    elif (action == "r"):
        right()
        actionName = "right"
    elif (action == "b"):
        backward()
        actionName = "backward"
    elif action == "s":
        stop()

    templateData = {
        'title': actionName
    }
    return render_template('action.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
