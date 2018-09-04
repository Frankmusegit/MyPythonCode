#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from PyQt4.QtCore import *

class Channel:

    def __init__(self):
        self.name = QString()

class Instrument:

    def __init__(self):
        self._channel = []
        a = Channel()
        a.name  = "normal"
        self._channel.append(a)

        self._minPitchA          = 0
        self._maxPitchA          = 127
        self._minPitchP          = 0
        self._maxPitchP          = 127
        self._drumset            = 0
        self._useDrumset         = False

    def useDrumset(self):
        return self._useDrumset

    def channel(self):
        return self._channel

    def channel1(self,idx):
        return self._channel[idx]