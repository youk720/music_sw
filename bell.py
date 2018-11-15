import time
import RPi.GPIO as GPIO
import subprocess
# 音楽の時間の長さを測るためのもの:下のページも参照を
# https://mutagen.readthedocs.io/en/latest/user/gettingstarted.html
from mutagen.mp3 import MP3

# 各種ピンを指定
sw = 19
led = 3
led_2 = 4

# GPIO関連設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

door_time = MP3("./吹上_1ドア.mp3")
# 時間カスタム設定用(ネットのリンクから再生時)
# door_time = 7

# フラグやメロディの初期定義
melo = print("wait")
now_door = 0
bell = True
door_flg = False
door_play = True

# ここから無限ループ開始
while True:
    # スイッチの状態を代入
    pin_status = GPIO.input(sw)
    # print(pin_status

    #スイッチがONの場合
    if pin_status == 1:
        # ベルのフラグの正負で以下を
        # 先にメロディが流れ終わるまで一回だけ実行
        if bell == True:
            GPIO.output(led_2, GPIO.HIGH)
            #メロディ再生(↓はローカルファイル内での実行時)
            # melo = subprocess.Popen("exec " + "ffplay -nodisp -autoexit -loop 0 /home/pi/デスクトップ/gpio_test/music_sw/melody/summer_night_v1_Ab.mp3", shell=True)
            melo = subprocess.Popen("exec " + "ffplay -nodisp -autoexit -loop 0 /home/pi/デスクトップ/gpio_test/music_sw/melody/HANDS-大きな手から小さな手へ-verA.mp3", shell=True)
            #メロディ再生(↓はネットからのリンクで再生:この場合、上記のメロディ時間を設定してください)
            # melo = subprocess.Popen("exec " + "ffplay -loop 0 -nodisp -autoexit https://youk720.github.io/melo_work/melo/see%20you%20again.mp3", shell=True)
            # フラグを指定
            bell = False
            door_flg = True
        else:
            #pass
            if now_door != 0:
               GPIO.output(led, GPIO.LOW)
               door.terminate()
    #スイッチがOFFの場合
    if pin_status == 0:
        try:
             # ベルのフラグの正負で以下を
             # 先に流れた放送が終わった後一回だけ実行
            if door_flg == True:
                GPIO.output(led_2, GPIO.LOW)
                melo.terminate()
                bell = True
                if door_play == False:
                    door.terminate()
                    door_play = True
                GPIO.output(led, GPIO.HIGH)
                # メロディ再生(↓はローカルファイル内での実行時)
                door = subprocess.Popen("exec " + "ffplay -nodisp -autoexit 吹上_1ドア.mp3", shell=True)
                # メロディ再生(↓はネットからのリンクで再生:この場合、上記のメロディ時間を設定してください)
                # door = subprocess.Popen("exec " + "ffplay -nodisp -autoexit https://youk720.github.io/melo_work/melo/saki/10.mp3", shell=True)
                #door = subprocess.Popen("exec " + "ffplay -nodisp -autoexit https://youk720.github.io/melo_work/sound/%E3%83%88%E3%82%99%E3%82%A2%E3%81%8B%E3%82%99%E9%96%89%E3%81%BE%E3%82%8A%E3%81%BE%E3%81%99%E6%89%8B%E8%8D%B7%E7%89%A9.mp3", shell=True)
                # 開始した時間を記録
                door_start = time.time()
                door_flg = False
                door_play = False
            else:
                now_door = time.time() - door_start
                # ローカルから時間を定義する場合
                if now_door > door_time.info.length or now_door == door_time.info.length:
                # 時間カスタム設定用(ネットのリンクから再生時)
                # if now_door > door_time:
                    # ドア流れ終わったらキル
                    door.terminate()
                    GPIO.output(led, GPIO.LOW)
        except:
            pass
