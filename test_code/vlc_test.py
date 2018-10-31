import time
# import RPi.GPIO as GPIO
# import subprocess
import vlc

p = vlc.MediaPlayer()  # 直接コンストラクタに下記のメディアのパスを渡しても良い
p.set_mrl("./meody/熊谷市歌A.mp3")  # 'http://foo.bar/buzz.mp3'とかでもイケる
p.play()  # この時点でバックグラウンドで音が流れる スリープ中も音は流れる
