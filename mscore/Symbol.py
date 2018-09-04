#!/usr/bin/env python
#-*- coding:utf-8 -*-

from BSymbol import *

class Symbol(BSymbol):
    def __init__(self, s):
        BSymbol.__init__(self, s)
        self._sym = 0

    def type(self):
        return ElementType.SYMBOL

    def setSym(self, s):
        self._sym  = s

    def sym(self):
        return self._sym

    def baseLine(self):
        return 0.0