

import RPi.GPIO as GPIO
import time
import os
import shlex    #文字列を読む(？)
import subprocess

sw = 19
led = 4
wait = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        pin_status = GPIO.input(sw)
        # print(pin_status)

        if pin_status == 1:
            GPIO.output(led, GPIO.HIGH)
        elif pin_status == 0:
            GPIO.output(led, GPIO.LOW)

except KeyboardInterrupt:
 GPIO.cleanup()
