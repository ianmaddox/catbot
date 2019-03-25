import PiMotor
import time
import RPi.GPIO as GPIO

fast = 0.001
medium = 0.005
slow = 0.01

try:
    delay = fast
    steps = 128
    m1 = PiMotor.Stepper("STEPPER2")
    while True:
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

#        m1.backward(fast,   90)
#	m1.backward(medium, 30)
#	m1.backward(slow,   15)

except KeyboardInterrupt:
    GPIO.cleanup()

