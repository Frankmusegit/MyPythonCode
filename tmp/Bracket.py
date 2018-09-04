#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *
from Spatium import *

class Bracket(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self.h2       = 3.5 * self.spatium()
        self._span    = 1
        self._column   = 0
        self.yoff     = 0.0

    def type(self):
        return ElementType.BRACKET

    def span(self):
        return self._span

    def setSpan(self, val):
        self._span = val

    def level(self):
        return self._column

    def setLevel(self, v):
        self._column = v

    def system(self):
        return self.parent()

    def isEditable(self):
        return True