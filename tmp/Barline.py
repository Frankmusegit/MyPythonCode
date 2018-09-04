#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *

class BarLine(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self.setSubtype(BarType.NORMAL_BAR)
        self._span = 1
        self.yoff  = 0.0
        self.setHeight(4.0 * self.spatium())

    def type(self):
        return ElementType.BAR_LINE