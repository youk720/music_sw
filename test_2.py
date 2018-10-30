import time
import RPi.GPIO as GPIO
import subprocess
from mutagen.mp3 import MP3

sw = 19
led = 4
led_2 = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

melo_time = MP3("./melody/夏色の時間.mp3")
door_time = MP3("./4_1.mp3")

melo = print("wait")
bell = True
door_flg = True

while True:
    pin_status = GPIO.input(sw)
    time.sleep(0.2)
    # print(pin_status
    if pin_status == 1:
        GPIO.output(led_2, GPIO.HIGH)
        # print("06")
        if bell == True:
            melo = subprocess.Popen("ffplay -nodisp -autoexit ./melody/夏色の時間.mp3", shell=True)
            time.sleep(melo_time.info.length)
            melo.kill()
            print("kill")
            bell = True
            door_flg = True
        # melo.kill()
        # print("07")
    if pin_status == 0:
        try:
            if door_flg == True:
                bell = True
                door = subprocess.Popen("ffplay -nodisp -autoexit 4_1.mp3", shell=True)
                time.sleep(door_time.info.length)
                door.kill()
                print("kill")
                GPIO.output(led_2, GPIO.LOW)
                door_flg = False
        except:
            pass
