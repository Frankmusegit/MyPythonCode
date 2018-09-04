#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *

class Segment(Element):
    def __init__(self, s):
        Element.__init__(self, s)

    def type(self):
        return ElementType.SEGMENT

    def next(self):
        return self._next

    def setNext(self, e):
        self._next = e

    def prev(self):
        return self._prev

    def setPrev(self, e):
        self._prev = e
