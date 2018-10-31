#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# 参考サイト http://yura2.hateblo.jp/entry/2016/02/14/Raspberry_Pi%E3%81%A7%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E3%82%92%E6%8A%BC%E3%81%99%E3%81%A8%E9%9F%B3%E6%A5%BD%E3%82%92%E5%86%8D%E7%94%9F%E3%81%99%E3%82%8B
# https://teratail.com/questions/90652

from __future__ import print_function

import RPi.GPIO as GPIO
import os #ディレクトリの中を確認するためのもの
import time #ディレイ用
import random #ランダム再生用
import shlex    #文字列を読む(？)
import subprocess #サブプロセス管理
#import PlayMusic #playmusicのライブラリ(別ダウンロード)

# Pin Number
PIN = 19
is_playing = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
last_pin_status = 0

SONG_DIR = '/home/pi/デスクトップ/gpio_test/music_sw'
SONG_LIST = ['夏色の時間.mp3', 'メロディ.mp3']


def play_song():
    song = random.choice(SONG_LIST)
    song_path = os.path.join(SONG_DIR, song)
    command = 'aplay %s' % (song_path)
    print(command)
    subprocess.Popen(shlex.split(command)) #実行中にコンソールで入力したように使う

# def stop_song():


# try:
    while True:
        pin_status = GPIO.input(PIN)
        if pin_status == 1:
            play_song()
            if is_playing:    # 再生ステータスの検査
                stop_song()
            else:
                play_song()

            is_playing = not(is_playing)    # 再生ステータスの反転

        last_pin_status = pin_status
        time.sleep(0.1)

# except KeyboardInterrupt:
# GPIO.cleanup()
