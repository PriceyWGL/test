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
        #onScreen("Logging In...")
        #display.lcdWriteFirstLine("Prichod...")
        #display.lcdWriteSecondLine("Swipe your Card")
        print "Logging In..."
        print "Swipe your tag"
        cardId=read()
        logging.info("Incomming - %s",cardId)
        #name = mysql.insertReading(cardId,Actions.incomming)
        #display.lcdWriteSecondLine(name)
    if(action==57):#9 - outcomming
        #onScreen("...")
        #display.lcdWriteFirstLine("Logging out...")
        #display.lcdWriteSecondLine("Swipe your Card")
        cardId=read()
        logging.info("Outcomming - %s",cardId)
        #name = mysql.insertReading(cardId,Actions.outcomming)
        #display.lcdWriteSecondLine(name)
    if(action==49):#1 - break start
       # onScreen("Zacatek pauzy...")
        #display.lcdWriteFirstLine("Pauza zacatek...")
        #display.lcdWriteSecondLine("Swipe your Card")
        cardId=read()
        logging.info("Break start - %s",cardId)
        #name = mysql.insertReading(cardId,Actions.breakstart)
       # display.lcdWriteSecondLine(name)
    if(action==51):#3 - break end
       # onScreen("Konec pauzy...")
        #display.lcdWriteFirstLine("Pauza konec...")
        #display.lcdWriteSecondLine("Swipe your Card")
        cardId=read()
        logging.info("Break end - %s",cardId)
        #name = mysql.insertReading(cardId,Actions.breakend)
        #display.lcdWriteSecondLine(name)

    #Sleep a little, so the information about last action on display is readable by humans
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