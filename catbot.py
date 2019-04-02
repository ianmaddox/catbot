#!/usr/bin/env python

import struct
import PiMotor
import time
import RPi.GPIO as GPIO


def tail():
    fast = 0.001
    medium = 0.005
    slow = 0.01
    loops = 1
    print("Tail")
    try:
        delay = fast
        steps = 128
        m1 = PiMotor.Stepper("STEPPER2")
        while loops > 0:
            speed = medium
            fadeSteps = 0
            while fadeSteps < 5:
                m1.forward(speed, fadeSteps * 3)
                speed = speed - 0.001
                fadeSteps = fadeSteps + 1

            speed = fast
            fadeSteps = 5
            while fadeSteps > 0:
                m1.forward(speed, fadeSteps * 3)
                speed = speed + 0.001
                fadeSteps = fadeSteps - 1

    #backward
            speed = medium
            fadeSteps = 0
            while fadeSteps < 5:
                m1.backward(speed, fadeSteps * 3)
                speed = speed - 0.001
                fadeSteps = fadeSteps + 1

            speed = fast
            fadeSteps = 5
            while fadeSteps > 0:
                m1.backward(speed, fadeSteps * 3)
                speed = speed + 0.001
                fadeSteps = fadeSteps - 1

            loops = loops - 1
            if loops > 0
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

def up():
    print("Fwd")

def down():
    print("Back")

def left():
    print("Left")

def right():
    print("Right")

def joy(argument):
    switcher = {
        163841: up,
        163839: down,
        16941057: left,
        16941055: right,
        16842753: tail
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()

infile_path = "/dev/input/js0"
EVENT_SIZE = struct.calcsize("llHHI")
file = open(infile_path, "rb")
event = file.read(EVENT_SIZE)
while event:
    #print(struct.unpack("llHHI", event))
    (tv_sec, tv_usec, type, code, value) = struct.unpack("llHHI", event)
    joy(value)
    event = file.read(EVENT_SIZE)

