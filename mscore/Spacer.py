#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *
from Spatium import *

class Spacer(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._space = Spatium(0)

    def type(self):
        return ElementType.SPACER

    def setSpace(self, sp):
        self._space = sp

    def getSpace(self):
        return self._space

    def isEditable(self):
        return True