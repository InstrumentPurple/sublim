#!/usr/bin/python
import PySide6.QtWidgets as qt
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer,Slot
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt

import sys
import random
import os
import time

class window(qt.QWidget):
    def __init__(self, fpath:str, isRandom: str, isburst: str):
        super().__init__()
        self.isRand = (isRandom == "random")
        self.isBurst = (isburst == "burst")
        with open(fpath, 'r') as file:
            self.lines = file.readlines()

        self.cur = 0
        self.timeMs = 44 # adjust this if you want. 44 is at good timing tho. should be 34-50ms for it still to be subliminal

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

        self.tm.start()
        self.show()

    @Slot()
    def changeText(self ):
        rgot = random.randrange(0, 1000000)

        if rgot < 1000000/6: #one in six chance
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


if __name__=="__main__":
    app=qt.QApplication()

    if len(sys.argv) >= 3:
        if sys.argv[2] == "rb":
            win=window(sys.argv[1], "random", "burst")
            win.setMinimumSize(1600, 52)
        elif sys.argv[2] == "b":
            win=window(sys.argv[1], "", "burst")
            win.setMinimumSize(1600, 52)
        elif sys.argv[2] == "r":
            win=window(sys.argv[1], "random", "")
            win.setMinimumSize(1600, 52)
        elif sys.argv[2] == "c":
            win=consiousReinforcement(sys.argv[1], "random", "")
            win.setMinimumSize(1600, 52)
    elif len(sys.argv) == 2:
        win=window(sys.argv[1], "random", "burst")
        win.setMinimumSize(1600, 52)

    app.exec()
