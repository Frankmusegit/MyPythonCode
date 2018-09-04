#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Duration import *

class ChordRest(DurationElement):
    def __init__(self, s):
        DurationElement.__init__(self, s)
        self._tuplet = 0
        self._ticks  = -1

    def type(self):
        return 0

    def segment(self):
        return self.parent()

    def  measure(self):
        return self.parent().parent()

    def setBeamMode(self,  m):
        self._beamMode = m

    def beamMode(self):
        return self._beamMode