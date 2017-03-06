import random
import time

angle = random.gauss(0, 1)

while True:
    print "Current angle: {}\nCorrection needed: {}\n".format(angle, -angle)
    angle -= angle
    print "Orientation after correction: {}\n".format(angle)
    time.sleep(2)
    angle = random.gauss(0,1)
