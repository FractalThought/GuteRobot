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
    gpio.setup(23, gpio.OUT)  # Left wheels forwards
    gpio.setup(24, gpio.OUT)  # Left wheels backwards
    gpio.setup(20, gpio.OUT)  # Right wheels forwards
    gpio.setup(21, gpio.OUT)  # Right wheels backwards


def forward():
    stop()
    gpio.output(23, True)  # Left wheels forward
    gpio.output(24, False)
    gpio.output(20, True)  # Right wheels forward
    gpio.output(21, False)


def backward():
    stop()
    gpio.output(23, False)
    gpio.output(24, True)  # Left wheels backwards
    gpio.output(20, False)
    gpio.output(21, True)  # Right wheels backwards


def right():
    stop()
    gpio.output(23, False)
    gpio.output(24, True)  # Left wheels backwards
    gpio.output(20, True)  # Right wheels forward
    gpio.output(21, False)


def left():
    stop()
    gpio.output(23, True)  # Left wheels forward
    gpio.output(24, False)
    gpio.output(20, False)
    gpio.output(21, True)  # Right wheels backwards


def stop():
    gpio.output(23, False)  # Left wheels forward
    gpio.output(24, False)
    gpio.output(20, False)
    gpio.output(21, False)  # Right wheels backwards


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
    if (action == "f"):
        forward()
    elif (action == "l"):
        left()
    elif (action == "r"):
        right()
    elif (action == "b"):
        backward()
    elif action == "s":
        stop()

    templateData = {
        'title': 'GuteRobot action',
        'action': action
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
