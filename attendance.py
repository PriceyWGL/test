#!/usr/bin/python

import nfc

import sys
import tty
import termios
import logging

import thread
import time

import RPi.GPIO as GPIO

#Enable debug logging into log
DEBUG=True
#Enable printing informations to std. output
VERBOSE=True

class Actions:
    incomming=1
    outcomming=2
    breakstart=3
    breakend=4

if(DEBUG):
    logging.basicConfig(format='%(asctime)s %(message)s',filename='attendance.log', level=logging.DEBUG)

def debug(message):
    logging.debug(message)

def onScreen(message):
    if(VERBOSE):
        print(message)

def read():
    #ledRedOn()
    cardId=nfc.readNfc()
    #beep()
    #ledRedOff()
    return cardId

def readNfc(action):
    if(action==55):#7 - Incomming
        print "Logging In..."
        print "Swipe your tag"
        cardId=read()
    time.sleep(1)



#Backing up the input attributes, so we can change it for reading single
#character without hitting enter  each time
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getOneKey():
    try:
        tty.setcbreak(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        return ord(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


displayTime=True
def printDateToDisplay():
    while True:
        #Display current time on display, until global variable is set
        if displayTime!=True:
            thread.exit()
        display.lcdWriteFirstLine(time.strftime("%d.%m. %H:%M:%S", time.localtime()))
        onScreen(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
        time.sleep(1)