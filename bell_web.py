import subprocess
import RPi.GPIO as GPIO
import time

#参考サイト
#https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script
#https://qiita.com/ktanaka117/items/596febd96a63ae1431f8
#

sw = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
on_status = True
off_status = True

while True:
    pin_status = GPIO.input(sw)

    try:
        if pin_status == 1:
        #ONの反応をsubprocessでcurlをmac側へ叩く
            if on_status == True:
                subprocess.Popen(['curl',
                                 '-X',
                                 'POST',
                                 'IP',
                                 '-H',
                                 'Accept: application/json',
                                 '-H',
                                 'Content-type: application/json',
                                 '-d',
                                 '{ "sw" : "True" }'])
                on_status = False
                off_status = True
        if pin_status == 0:
            #OFFの反応をsubprocessでcurlをmac側へ叩く
            # subprocess.Popen('curl -X POST http://10.3.100.209:3000 -H "Accept: application/json" -H "Content-type: application/json" -d '{ "sw" : "False" }'', shell=True)
            if off_status == True:

                subprocess.Popen(['curl',
                                 '-X',
                                 'POST',
                                 'IP',
                                 '-H',
                                 'Accept: application/json',
                                 '-H',
                                 'Content-type: application/json',
                                 '-d',
                                 '{ "sw" : "False" }'])
                on_status = True
                off_status = False
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('\n' + "Over SW test")
