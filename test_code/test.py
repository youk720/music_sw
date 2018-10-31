#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import RPi.GPIO as GPIO
import time

# Pin Number
PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    pin_status = GPIO.input(PIN)
    print(pin_status)
    time.sleep(0.1)

GPIO.cleanup()
