#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class Tremolo(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._chord1 = 0
        self._chord2 = 0

    def type(self):
        return ElementType.TREMOLO

    def chord1(self):
        return self._chord1

    def chord2(self):
        return self._chord2

    def setChords(self, c1, c2):
        self._chord1 = c1
        self._chord2 = c2


    def twoNotes(self):
        return self.subtype() > 2
