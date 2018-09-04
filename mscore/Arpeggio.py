#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class Arpeggio(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self.setHeight(self.spatium() * 4)

    def isMovable(self):
        return True

    def type(self):
        return ElementType.ARPEGGIO

    def isEditable(self):
        return True

    def setHeight(self, h):
        self._height = h
