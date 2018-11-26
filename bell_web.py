# 各種ライブラリ導入
import subprocess
import RPi.GPIO as GPIO
import time

#参考サイト
#https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
#https://qiita.com/ktanaka117/items/596febd96a63ae1431f8
#
# スイッチピン定義
sw = 19

#GPIO各種設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# フラグ初期設定
on_status = True
off_status = True

# IPアドレス定義
ip = 'http://xxxxxx:tyyyyy'

# 念の為正常に動作を確認するためログ出す
print('\n' + "SW Start")

# While無限回し
while True:
    # GPIO値を代入
    pin_status = GPIO.input(sw)
    try:
        # 以下ONだった時の制御
        if pin_status == 1:
            # フラグがTrueの時のみ実行(重複処理防止のため)
            if on_status == True:
                #ONの反応をsubprocessでcurlをmac側へ叩く
                subprocess.Popen(['curl',
                                # 以下HTTPメソッド指定
                                 '-X',
                                 'POST',
                                 # 以下で上記で定義したIPアドレスを文字列へ代入
                                 '%s' % (ip),
                                 '-H',
                                 'Accept: application/json',
                                 # POSTフォーマットをJSONに指定
                                 '-H',
                                 'Content-type: application/json',
                                 # 以下Mac側へ送る値(データ)
                                 '-d',
                                 '{ "sw" : "True" }'])
                                 # TrueでMac側で流れるメロディを再生させる
                # フラグ管理(これにより重複を避ける)
                on_status = False
                off_status = True
        # 以下OFFの時の
        if pin_status == 0:
            # フラグがTrueの時のみ実行(重複処理防止のため)
            if off_status == True:
                #OFFの反応をsubprocessでcurlをmac側へ叩く
                subprocess.Popen(['curl',
                                # 以下HTTPメソッド指定
                                 '-X',
                                 'POST',
                                 # 以下で上記で定義したIPアドレスを文字列へ代入
                                 '%s' % (ip),
                                 '-H',
                                 'Accept: application/json',
                                 # POSTフォーマットをJSONに指定
                                 '-H',
                                 'Content-type: application/json',
                                 # 以下Mac側へ送る値(データ)
                                 '-d',
                                 '{ "sw" : "False" }'])
                                 # FalseでMac側で流れるメロディを止める
                # フラグ管理
                # これにより重複を避ける
                on_status = True
                off_status = False
    # Curl+Cで実行を止めた時に動かす処理
    except KeyboardInterrupt:
        # GPIOの終了処理
        GPIO.cleanup()
        # 終わったというログ出し(改行しないと読みにくい)
        print('\n' + "Over SW test")
