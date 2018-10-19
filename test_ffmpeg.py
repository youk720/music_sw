import pygame.mixer
import time
import RPi.GPIO as GPIO
import subprocess

sw = 19
led = 4
led_2 = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

# mixerモジュールの初期化
pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.mixer.init()
# メロディ音源の読み込み
pygame.mixer.music.load("./melody/夏色の時間.mp3")
# time.sleep(60)
while True:
    pin_status = GPIO.input(sw)
    time.sleep(0.2)
    # print(pin_status)
    if pin_status == 0:
        # GPIO.output(led, GPIO.LOW)
        # if 再生処理の有無
        if pygame.mixer.music.get_busy() == True:
            # していたら以下を実行
            # 再生の終了
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            GPIO.output(led, GPIO.LOW)
            # break
            time.sleep(1)
            GPIO.output(led_2, GPIO.HIGH)
            #戸閉放送用 補足:pygameだとメロディの方とごっちゃになるので別にmpg321を使用
            subprocess.call("ffplay -nodisp -autoexit 4_1.mp3", shell=True)
            GPIO.output(led_2, GPIO.LOW)
            # pygame.mixer.quit()
    elif pin_status == 1:
        print(pygame.mixer.music.get_pos())
        # GPIO.output(led, GPIO.HIGH)
        # if 再生処理の有無
        if pygame.mixer.music.get_busy() == False :
            # していなかったら以下を実行
            time.sleep(0.2)

            # 音楽再生、および再生回数の設定(-1はループ再生)
            pygame.mixer.music.play(-1)
            GPIO.output(led, GPIO.HIGH)
