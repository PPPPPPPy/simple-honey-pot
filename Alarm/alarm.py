# alarm.py 
import RPi.GPIO as GPIO
import time
import libeep
while True:
        print "=== Attention -- Alarm Launched ==="
        libeep.beepAction (3,0.05,1)
        time.sleep(1)
   

''' # Latest Version
# alarm.py
import RPi.GPIO as GPIO
import time
import libeep

libeep.beepAction (2,0.05,1)
time.sleep(1)
while True:
        print "=== Attention -- Alarm Launched ==="
        libeep.beepAction (1,0.05,1)
        time.sleep(1)
'''
