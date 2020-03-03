from flask import Flask, render_template
import RPi.GPIO as gpio
import time

# https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d

"""
23 and 24 to right side
20 and 21 to left side
"""


def init():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(23, gpio.OUT)  # Left wheels forwards
    gpio.setup(24, gpio.OUT)  # Left wheels backwards
    gpio.setup(20, gpio.OUT)  # Right wheels forwards
    gpio.setup(21, gpio.OUT)  # Right wheels backwards
    print("GPIO initialized")


def forward():
    stop()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(20, True)
    gpio.output(21, False)


def backward():
    stop()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(20, False)
    gpio.output(21, True)


def right():
    stop()
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(20, True)
    gpio.output(21, False)


def left():
    stop()
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(20, False)
    gpio.output(21, True)


def stop():
    gpio.output(23, False)
    gpio.output(24, False)
    gpio.output(20, False)
    gpio.output(21, False)


init()

app = Flask(__name__)
@app.route("/")
def index():
    templateData = {
        'title': 'GuteRobot'
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
        'title': 'GuteRobot action',
        'action': actionName
    }
    return render_template('action.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
