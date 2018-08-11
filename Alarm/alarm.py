# alarm.py 
import RPi.GPIO as GPIO
import time
import libeep
while True:
        print "=== Attention -- Alarm Launched ==="
        libeep.beepAction (3,0.05,1)
        time.sleep(1)