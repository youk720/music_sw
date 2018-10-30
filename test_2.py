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

melo_time = MP3("./melody/farewell_D#m.mp3")
# 時間カスタム設定用
#melo_time = 9
#door_time = MP3("./2_ドア.mp3")
# 時間カスタム設定用
door_time = 6

melo = print("wait")
bell = True
door_flg = False

while True:
    pin_status = GPIO.input(sw)
    # print(pin_status
    if pin_status == 1:
        # print("06")
        if bell == True:
            GPIO.output(led_2, GPIO.HIGH)
            melo = subprocess.Popen("ffplay -nodisp -autoexit melody/farewell_D#m.mp3", shell=True)
            #melo = subprocess.Popen("ffplay -nodisp -autoexit https://youk720.github.io/melo_work/melo/%E6%B5%B7%E5%B2%B8%E9%80%9A%E3%82%8AV1.mp3", shell=True)
            bell = False
            door_flg = True
            # 鳴らしはじめの時間(秒数)を記録させる
            melo_start = time.time()
        else:
            # 現在の時間(秒数)が melo_time.info.length よりも多くなる場合 melo.kill させる
            now_time = time.time() - melo_start
            if now_time > melo_time.info.length or now_time == melo_time.info.length:
            # 時間カスタム設定用
            #if now_time > melo_time:
                melo.kill()
                print("kill_melo")
                bell = True
    if pin_status == 0:
        try:
            if door_flg == True:
                GPIO.output(led, GPIO.HIGH)
                #door = subprocess.Popen("ffplay -nodisp -autoexit 2_ドア.mp3", shell=True)
                door = subprocess.Popen("ffplay -nodisp -autoexit https://youk720.github.io/melo_work/melo/saki/7_%E6%9C%AA%E6%9B%B4%E6%96%B0voss.mp3", shell=True)
                door_start = time.time()
                door_flg = False
            else:
                now_door = time.time() - door_start
                #if now_door > door_time.info.length or now_door == door_time.info.length:
                # 時間カスタム設定用
                if now_door > door_time:
                    door.kill()
                    GPIO.output(led, GPIO.LOW)
                now_time = time.time() - melo_start
                if now_time > melo_time.info.length or now_time == melo_time.info.length:
               # 時間カスタム設定用
                #if now_time > melo_time:
                    melo.kill()
                    bell = True
                    GPIO.output(led_2, GPIO.LOW)
        except:
            pass
