import threading
import os, io, base64, time, socket, picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
camera.exposure_mode = 'sports'
print('Camera initialized')

while 1:
    start = time.time()
    camera.capture('/tmp/snap.jpg')
    finish = start - time.time()
    print finish
    print 'Picture Taken!'

