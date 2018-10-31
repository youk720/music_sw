import time
import RPi.GPIO as GPIO
import subprocess
# 音楽の時間の長さを測るためのもの:下のページも参照を
# https://mutagen.readthedocs.io/en/latest/user/gettingstarted.html
from mutagen.mp3 import MP3

# 各種ピンを指定
sw = 19
led = 4
led_2 = 3

# GPIO関連設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

# メロディ & 放送時間定義
melo_time = MP3("./melody/farewell_D#m.mp3")
# 時間カスタム設定用(ネットのリンクから再生時)
#melo_time = 9
#door_time = MP3("./2_ドア.mp3")
# 時間カスタム設定用(ネットのリンクから再生時)
door_time = 6

# フラグやメロディの初期定義
melo = print("wait")
bell = True
door_flg = False

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
            melo = subprocess.Popen("ffplay -nodisp -autoexit melody/farewell_D#m.mp3", shell=True)
            #メロディ再生(↓はネットからのリンクで再生:この場合、上記のメロディ時間を設定してください)
            #melo = subprocess.Popen("ffplay -nodisp -autoexit https://youk720.github.io/melo_work/melo/%E6%B5%B7%E5%B2%B8%E9%80%9A%E3%82%8AV1.mp3", shell=True)
            # フラグを指定
            bell = False
            door_flg = True
            # 鳴らしはじめの時間(秒数)を記録させる
            melo_start = time.time()
        else:
            # 現在の時間(秒数)が melo_time.info.length よりも多くなる場合 melo.kill させる
            now_time = time.time() - melo_start
            # ローカルから時間を定義する場合
            if now_time > melo_time.info.length or now_time == melo_time.info.length:
            # 時間カスタム設定用(ネットのリンクから再生時)
            #if now_time > melo_time:
                melo.kill()
                print("kill_melo")
                bell = True
    #スイッチがOFFの場合
    if pin_status == 0:
        try:
             # ベルのフラグの正負で以下を
             # 先に流れた放送が終わった後一回だけ実行
            if door_flg == True:
                GPIO.output(led, GPIO.HIGH)
                # メロディ再生(↓はローカルファイル内での実行時)
                #door = subprocess.Popen("ffplay -nodisp -autoexit 2_ドア.mp3", shell=True)
                # メロディ再生(↓はネットからのリンクで再生:この場合、上記のメロディ時間を設定してください)
                door = subprocess.Popen("ffplay -nodisp -autoexit https://youk720.github.io/melo_work/melo/saki/7_%E6%9C%AA%E6%9B%B4%E6%96%B0voss.mp3", shell=True)
                # 開始した時間を記録
                door_start = time.time()
                door_flg = False
            else:
                now_door = time.time() - door_start
                # ローカルから時間を定義する場合
                #if now_door > door_time.info.length or now_door == door_time.info.length:
                # 時間カスタム設定用(ネットのリンクから再生時)
                if now_door > door_time:
                    # ドア流れ終わったらキル
                    door.kill()
                    GPIO.output(led, GPIO.LOW)
                now_time = time.time() - melo_start
                # ローカルから時間を定義する場合
                if now_time > melo_time.info.length or now_time == melo_time.info.length:
               # 時間カスタム設定用(ネットのリンクから再生時)
                #if now_time > melo_time:
                    melo.kill()
                    bell = True
                    GPIO.output(led_2, GPIO.LOW)
        except:
            pass
