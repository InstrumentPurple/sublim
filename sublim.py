#!/usr/bin/python
import PySide6.QtWidgets as qt
from PySide6.QtGui import QFont, QCloseEvent
from PySide6.QtCore import QTimer,Slot
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt

from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl

import sys
import random
import os
import time
import datetime

million = 1000000

class windowBase(qt.QWidget):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__()
        self.isRand = (isRandom == "random")
        self.isBurst = (isburst == "burst")
        with open(fpath, 'r') as file:
            self.lines = file.readlines()

        self.cur = 0
        self.timeMs = 44 # adjust this if you want. 44 is at good timing tho. should be 34-50ms for it still to be subliminal

        self.startedTime = datetime.datetime.now()
        self.timeFile = open("./rectime.txt", "a")
        self.timeFile.write(self.startedTime.strftime("date %Y-%m-%d %I:%M:%S %p\n"))


        self.tm = QTimer()
        self.tm.setInterval(self.timeMs)

        self.tm.timeout.connect(self.changeText)

        self.layout = qt.QGridLayout()
        self.setLayout(self.layout)


        self.text = qt.QLabel()
        self.text.setAlignment(Qt.AlignHCenter)
        self.font  = QFont("Arial", 60)
        self.text.setFont(self.font)

        self.layout.addWidget(self.text,0,0)
        self.setMinimumSize(1600, 120)
        self.adjustSize()
        self.tm.start()
        self.show()


    def closeEvent(self, event: QCloseEvent):
        delta = datetime.datetime.now() - self.startedTime
        seconds = delta.total_seconds()
        self.timeFile.write(str(seconds) + " seconds\n")
        self.timeFile.close()

        event.accept()


class window(windowBase):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__(fpath, isRandom, isburst)
        self.burstWaitMin = 3000
        self.burstWaitMax = 5500

    @Slot()
    def changeText(self):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            QTest.qWait(random.randrange(self.burstWaitMin ,self.burstWaitMax))

        self.cur += 1


class consiousReinforcement(windowBase):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__(fpath, isRandom, isburst)

        self.readable = False
        self.burstWaitMin = 3000
        self.burstWaitMax = 5500
        self.readableWait = 2500

    @Slot()
    def changeText(self):
        rgot = random.randrange(0, million)

        if rgot < million/6: #one in six chance
            self.readable=True
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        if self.readable:
            QTest.qWait(self.readableWait)
            self.readable=False
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            QTest.qWait(random.randrange(self.burstWaitMin,self.burstWaitMax))

        self.cur += 1




class surpriser(windowBase):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__(fpath, isRandom, isburst)
        self.burstWaitMin = 4000
        self.burstWaitMax = 35000
        self.randMsgWaitMin = 5000
        self.randMsgWaitMax = 10000
        self.oneInProb = 4.5

    @Slot()
    def changeText(self):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        rnd = random.randrange(0,million)
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            if rnd < million / self.oneInProb:
                QTest.qWait(random.randrange(self.randMsgWaitMin,self.randMsgWaitMax))
                self.text.setText(self.lines[random.randrange(0, len(self.lines))])
                QTest.qWait(self.timeMs)
                self.text.setText("")
            QTest.qWait(random.randrange(self.burstWaitMin,self.burstWaitMax))


        self.cur += 1



class surpriserBird(windowBase):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__(fpath, isRandom, isburst)

        self.burstsWithoutBirds = 0
        self.burstWithoutMax = 8.0
        self.oneInProb = 5.3

        self.burstWaitMin = 6000
        self.burstWaitMax = 20000
        self.randMsgWaitMin = 5000
        self.randMsgWaitMax = 10000
        self.randMsgDelay = 100

        birdPaths = ["./bird1.wav","./bird2.wav", "./bird3.wav", "./bird4.wav"]
        self.sounds = [QSoundEffect(),QSoundEffect(),QSoundEffect(),QSoundEffect()]
        i = 0
        for p in birdPaths:
            self.sounds[i].setSource(QUrl.fromLocalFile(p))
            self.sounds[i].setVolume(0.8)
            i += 1


    @Slot()
    def changeText(self):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        rnd = random.randrange(0,million)
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")

            if self.burstsWithoutBirds >= self.burstWithoutMax: # been damn long enough just play one now
                self.playOneShowOne()
            elif rnd < million / self.oneInProb:
                self.playOneShowOne()
            else:
                self.burstsWithoutBirds += 1
            QTest.qWait(random.randrange(self.burstWaitMin,self.burstWaitMax))


        self.cur += 1

    def playOneShowOne(self):
        QTest.qWait(random.randrange(self.randMsgWaitMin,self.randMsgWaitMax))
        random.choice(self.sounds).play()
        QTest.qWait(self.randMsgDelay)
        self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        QTest.qWait(self.timeMs)
        self.text.setText("")


if __name__=="__main__":
    app=qt.QApplication()

    if len(sys.argv) >= 3:
        if sys.argv[2] == "rb":
            win=window(sys.argv[1], "random", "burst")
        elif sys.argv[2] == "b":
            win=window(sys.argv[1], "", "burst")
        elif sys.argv[2] == "r":
            win=window(sys.argv[1], "random", "")
        elif sys.argv[2] == "c":
            win=consiousReinforcement(sys.argv[1], "random", "")
        elif sys.argv[2] == "s":
            win=surpriser(sys.argv[1], "random", "burst")
        elif sys.argv[2] == "bird":
            win=surpriserBird(sys.argv[1], "random", "burst")
    elif len(sys.argv) == 2:
        win=window(sys.argv[1], "", "")
    else:
        print("USAGE: python ./sublim.py [text file] [r|b|rb|c|s|bird]")
        quit()

    app.exec()
