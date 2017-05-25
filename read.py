#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import sys
import time
import datetime
import urllib2
import urllib

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

def readNfc():
    reading = True
    while reading:
        MIFAREReader = MFRC522.MFRC522()

        #while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        #if status == MIFAREReader.MI_OK:
        #    print("Card detected")

        (status,backData) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            #print ("Card Number: "+str(backData[0])+","+str(backData[1])+","+str(backData[2])+","+str(backData[3])+","+str(backData[4]))
            MIFAREReader.AntennaOff()
            reading=False
            return str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])

def readNfc(action):
    if(action==55):#7 - Incomming
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        now = datetime.datetime.now()
        print now

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getOneKey():
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        return ord(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

def main():
    GPIO.cleanup()
    try:
        initGpio()
        display.init()
        while True:
            #display.lcdWriteSecondLine("Choose an action...")
            #global displayTime
            #displayTime=true
            #Start new thread to show curent datetime on display
            # and wait for user input on keyboard
            #thr = thread.start_new_thread(printDateToDisplay, ())
            a = getOneKey()
            #displayTime=False
            if 47 < a < 58:
                readNfc(a)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
    GPIO.cleanup()