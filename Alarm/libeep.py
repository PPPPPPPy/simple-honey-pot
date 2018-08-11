# GPIO Library
import RPi.GPIO as GPIO
import time
# Channel (Pin code)
PIN_NO = 12

GPIO.setmode(GPIO.BOARD)
# GPIO channel with "Source Input"
GPIO.setup(PIN_NO, GPIO.OUT)

def beep(seconds):
     GPIO.output(PIN_NO, GPIO.HIGH)
     time.sleep(seconds)
     GPIO.output(PIN_NO, GPIO.LOW)

def beepAction(secs, sleepsecs, times):
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)