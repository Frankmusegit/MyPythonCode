#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *

class LayoutBreak(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._reloff.rx = 100.0
        self.setXoff(-1.0)
        self.setYoff(-2.0)
        self.setOffsetType(OffsetType.OFFSET_SPATIUM)
        self.setAlign(AlignmentFlags.ALIGN_RIGHT | AlignmentFlags.ALIGN_BOTTOM)

    def type(self):
        return ElementType.LAYOUT_BREAK