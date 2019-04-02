#!/usr/bin/env python

import struct
import PiMotor
import time
import RPi.GPIO as GPIO

gospeed = 50
golen = 0.5
turnspeed = 25
turnlen = 0.5

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
motorAll = PiMotor.LinkedMotors(m1,m2)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

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
            al.on()
            ar.on()

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
            al.off()
            ar.off()
    #backward
            af.on()
            ab.on()
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
            if loops > 0:
                time.sleep(1)
            af.off()
            ab.off()
    except KeyboardInterrupt:
        GPIO.cleanup()

def stop():
    print("Stop")
    motorAll.stop()
    ab.off()
    af.off()
    al.off()
    ar.off()

def up():
    print("Fwd")
    af.on()
    motorAll.forward(gospeed)
    time.sleep(golen)
    motorAll.stop()
    af.off()

def down():
    print("Back")
    ab.on()
    motorAll.reverse(gospeed)
    time.sleep(golen)
    motorAll.stop()
    ab.off()

def left():
    print("Left")
    al.on()
    m1.forward(turnspeed)
    m2.reverse(turnspeed)
    time.sleep(turnlen)
    motorAll.stop()
    al.off()


def right():
    print("Right")
    ar.on()
    m2.forward(turnspeed)
    m1.reverse(turnspeed)
    time.sleep(turnlen)
    motorAll.stop()
    ar.off()

def joy(argument):
    switcher = {
        163841:   up,
        163839:   down,
        16941057: left,
        16941055: right,
        16842753: tail,
        65537:    stop
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()



stop()
infile_path = "/dev/input/js0"
EVENT_SIZE = struct.calcsize("llHHI")
file = open(infile_path, "rb")
event = file.read(EVENT_SIZE)
while event:
    #print(struct.unpack("llHHI", event))
    (tv_sec, tv_usec, type, code, value) = struct.unpack("llHHI", event)
    joy(value)
    event = file.read(EVENT_SIZE)

