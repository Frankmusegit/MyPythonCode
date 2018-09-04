#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from Instrument import *
from Text import *

class Part(Instrument):

    def __init__(self, s):
        Instrument.__init__(self)
        self._longName  = TextC(s)
        self._longName.setSubtype(TEXT.TEXT_INSTRUMENT_LONG)
        self._longName.setTextStyle(TEXT_STYLE.TEXT_STYLE_INSTRUMENT_LONG)
        self._shortName = TextC(s)
        self._shortName.setSubtype(TEXT.TEXT_INSTRUMENT_SHORT)
        self._shortName.setTextStyle(TEXT_STYLE.TEXT_STYLE_INSTRUMENT_SHORT)
        self._score = s
        self._show  = True
        self._id = QString()
        self._staves = []

    def setId(self, s):
        self._id = s

    def staves(self):
        return self._staves
