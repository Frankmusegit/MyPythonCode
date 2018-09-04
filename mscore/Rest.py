#!/usr/bin/env python
#-*- coding:utf-8 -*-
from ChordRest import *
from Sym import *

class Rest(ChordRest):
    def __init__(self, s = None):
        ChordRest.__init__(self, s)
        self.setOffsetType(OffsetType.OFFSET_SPATIUM)
        self._beamMode  = BeamMode.BEAM_NO
        self.dotline    = -1
        self._sym       = SymName.rest4Sym

    def isMovable(self):
        return True

    def type(self):
        return ElementType.REST

    def setMMWidth(self, val):
        self._mmWidth = val

    def mmWidth(self):
        return self._mmWidth