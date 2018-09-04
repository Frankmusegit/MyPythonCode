#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Event:

    def __init__(self, t = 0):
        self._type   = t
        self._data   = 0
        self._note   = 0
        self._tuning = 0.0
        self._ontime = -1
        self._channel = 0
        self._noquantOntime = 0
        
    def noquantOntime(self):
        return self._noquantOntime

    def setNoquantOntime(self, v):
        self._noquantOntime = v

    def noquantDuration(self):
        return self._noquantDuration

    def setNoquantDuration(self, v):
        self._noquantDuration = v

    def type(self):
        return self._type

    def setType(self, v):
        self._type = v

    def ontime(self):
        return self._ontime

    def  setOntime(self, v):
        self._ontime = v

    def channel(self):
        return self._channel

    def setChannel(self, c):
        self._channel = c

    def dataA(self):
        return self._a

    def dataB(self):
        return self._b

    def setDataA(self, v):
        self._a = v

    def setDataB(self, v):
        self._b = v

    def pitch(self):
        return self._a

    def setPitch(self, v ):
        self._a = v

    def  velo(self):
        return self._b

    def setVelo(self, v):
        self._b = v

    def controller(self):
        return self._a

    def setController(self, val):
        self._a = val

    def value(self):
        return self._b

    def setValue(self, v):
        self._b = v

    def duration(self):
        return self._duration

    def setDuration(self, v) :
        self._duration = v

    def voice(self):
        return self._voice

    def setVoice(self, val):
        self._voice = val

    def offtime(self):
        return self.ontime() + self._duration

    def notes(self):
        return self._notes

    def data(self):
        return self._data

    def setData(self, d):
        self._data = d

    def len(self):
        return self._len

    def setLen(self, l):
        self._len = l

    def metaType(self):
        return self._metaType

    def setMetaType(self, v):
        self._metaType = v

    def tpc(self):
        return self._tpc

    def setTpc(self, v):
        self._tpc = v

    def note(self):
        return self._note

    def setNote(self, v):
        self._note = v

    def tuning(self):
        return self._tuning

    def setTuning(self, v):
        self._tuning = v
