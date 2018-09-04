#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class DurationElement(Element):
    def __init__(self, s):
        Element.__init__(self, s)

    def measure(self):
        return self.parent()

    def setTuplet(self, t):
        self._tuplet = t

    def tuplet(self):
        return self._tuplet

    def beam(self):
        return 0

    def tickLen(self):
        return self.ticks()
