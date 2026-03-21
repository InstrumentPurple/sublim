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

class window(qt.QWidget):
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
        self.timeFile.write(self.startedTime.strftime("date %Y-%m-%d\n"))


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
        self.setMinimumSize(1600, 52)
        self.tm.start()
        self.show()

    @Slot()
    def changeText(self ):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            QTest.qWait(random.randrange(3000,5500))

        self.cur += 1

    def closeEvent(self, event: QCloseEvent):
        delta = datetime.datetime.now() - self.startedTime
        seconds = delta.total_seconds()
        self.timeFile.write(str(seconds) + " seconds\n")
        self.timeFile.close()

        event.accept()


class consiousReinforcement(qt.QWidget):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__()
        self.isRand = (isRandom == "random")
        self.isBurst = (isburst == "burst")
        with open(fpath, 'r') as file:
            self.lines = file.readlines()

        self.readable = False

        self.cur = 0
        self.timeMs = 44 # adjust this if you want. 44 is at good timing tho. should be 34-50ms for it still to be subliminal

        self.startedTime = datetime.datetime.now()
        self.timeFile = open("./rectime.txt", "a")
        self.timeFile.write(self.startedTime.strftime("date %Y-%m-%d\n"))


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
        self.setMinimumSize(1600, 52)
        self.tm.start()
        self.show()

    @Slot()
    def changeText(self ):
        rgot = random.randrange(0, million)

        if rgot < million/6: #one in six chance
            self.readable=True
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        if self.readable:
            QTest.qWait(2500)
            self.readable=False
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            QTest.qWait(random.randrange(3000,5500))

        self.cur += 1

    def closeEvent(self, event: QCloseEvent):
        delta = datetime.datetime.now() - self.startedTime
        seconds = delta.total_seconds()
        self.timeFile.write(str(seconds) + " seconds\n")
        self.timeFile.close()

        event.accept()




class surpriser(qt.QWidget):
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
        self.timeFile.write(self.startedTime.strftime("date %Y-%m-%d\n"))

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
        self.setMinimumSize(1600, 52)
        self.tm.start()
        self.show()

    @Slot()
    def changeText(self ):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        rnd = random.randrange(0,million)
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")
            if rnd < million / 4.5:
                QTest.qWait(random.randrange(5000,10000))
                self.text.setText(self.lines[random.randrange(0, len(self.lines))])
                QTest.qWait(self.timeMs)
                self.text.setText("")
            QTest.qWait(random.randrange(4000,35000))


        self.cur += 1

    def closeEvent(self, event: QCloseEvent):
        delta = datetime.datetime.now() - self.startedTime
        seconds = delta.total_seconds()
        self.timeFile.write(str(seconds) + " seconds\n")
        self.timeFile.close()

        event.accept()





class surpriserBird(qt.QWidget):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__()
        self.isRand = (isRandom == "random")
        self.isBurst = (isburst == "burst")
        with open(fpath, 'r') as file:
            self.lines = file.readlines()

        self.burstsWithoutBirds = 0
        self.cur = 0
        self.timeMs = 44 # adjust this if you want. 44 is at good timing tho. should be 34-50ms for it still to be subliminal

        self.startedTime = datetime.datetime.now()
        self.timeFile = open("./rectime.txt", "a")
        self.timeFile.write(self.startedTime.strftime("date %Y-%m-%d\n"))

        self.tm = QTimer()
        self.tm.setInterval(self.timeMs)

        self.tm.timeout.connect(self.changeText)

        self.layout = qt.QGridLayout()
        self.setLayout(self.layout)

        self.text = qt.QLabel()
        self.text.setAlignment(Qt.AlignHCenter)
        self.font = QFont("Arial", 60)
        self.text.setFont(self.font)


        birdPaths = ["./bird1.wav","./bird2.wav", "./bird3.wav", "./bird4.wav"]
        self.sounds = [QSoundEffect(),QSoundEffect(),QSoundEffect(),QSoundEffect()]
        i = 0
        for p in birdPaths:
            self.sounds[i].setSource(QUrl.fromLocalFile(p))
            self.sounds[i].setVolume(0.8)
            i += 1

        self.layout.addWidget(self.text,0,0)
        self.setMinimumSize(1600, 52)
        self.tm.start()
        self.show()

    @Slot()
    def changeText(self ):
        if self.isRand:
            self.text.setText(self.lines[random.randrange(0, len(self.lines))])
        else:
            self.text.setText(self.lines[self.cur % len(self.lines)])

        rnd = random.randrange(0,million)
        if self.isBurst and (self.cur % len(self.lines) == 0):
            QTest.qWait(self.timeMs)
            self.text.setText("")

            if self.burstsWithoutBirds >= 9.0: # been damn long enough just play one now
                QTest.qWait(random.randrange(5000,14000))
                random.choice(self.sounds).play()
                QTest.qWait(100)
                self.text.setText(self.lines[random.randrange(0, len(self.lines))])
                QTest.qWait(self.timeMs)
                self.text.setText("")
                self.burstsWithoutBirds = 0
            elif rnd < million / 6.0:
                QTest.qWait(random.randrange(5000,14000))
                random.choice(self.sounds).play()
                QTest.qWait(100)
                self.text.setText(self.lines[random.randrange(0, len(self.lines))])
                QTest.qWait(self.timeMs)
                self.text.setText("")
            else:
                self.burstsWithoutBirds += 1
            QTest.qWait(random.randrange(6000,20000))


        self.cur += 1


    def closeEvent(self, event: QCloseEvent):
        delta = datetime.datetime.now() - self.startedTime
        seconds = delta.total_seconds()
        self.timeFile.write(str(seconds) + " seconds\n")
        self.timeFile.close()

        event.accept()



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
        print("USAGE: python ./sublim.py [text file] [options]")
        quit()

    app.exec()
