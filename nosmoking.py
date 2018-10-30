import subprocess
import time
import RPi.GPIO as GPIO

led = 2
led_2 = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

def sound():
    GPIO.output(led_2, GPIO.HIGH)
    subprocess.call("ffplay -nodisp -autoexit 禁煙voicetext_men.mp3", shell=True)
    GPIO.output(led_2, GPIO.LOW)

while True:
    GPIO.output(led, GPIO.LOW)
    sound()
    time.sleep(120)
