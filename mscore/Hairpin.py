#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Line import *

class Hairpin(SLine):
    def __init__(self, s):
        SLine.__init__(self, s)
        self.setOffsetType(OffsetType.OFFSET_SPATIUM)
        self.setYoff(8.0)

    def type(self):
        return ElementType.HAIRPIN