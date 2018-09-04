#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Textline import *
from Sym import *

class Pedal(TextLine):
    def __init__(self, s):
        TextLine.__init__(self, s)
        self.setBeginSymbol(SymName.pedalPedSym)
        self.setEndHook(True)
        self.setEndHookHeight(Spatium(-1.5))

