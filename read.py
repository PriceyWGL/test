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
print "Press 1 to Clock in"
print "Press 2 to Clock out"

def NFCReadIn():

    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    else:
        print "Card not detected"
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        now = datetime.datetime.now()
        print "you clocked in at:"
        print now
		
def NFCReadOut():

    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    else:
        print "Card not detected"
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        now = datetime.datetime.now()
        print "you clocked out at:"
        print now

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    inkey = raw_input()
    if inkey == "1":
        print "Clocking In - Please Present Card"
        time.sleep(3)
        NFCRead()
    elif inkey == "2":
        print "Clocking Out - Please Present Card"
        time.sleep(3)
        NFCReadIn()
    else:
        print "Please select 1 to clock in"