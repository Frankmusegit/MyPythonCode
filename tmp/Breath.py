#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class Breath(Element):
    def __init__(self, s):
        Element.__init__(self, s)

    def segment(self):
        return self.parent()

    def type(self):
        return ElementType.BREATH

    def isMovable(self):
        return True