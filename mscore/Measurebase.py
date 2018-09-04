#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from Element import *

class MeasureBase(Element):

    def __init__(self, score):
        Element.__init__(self, score)
        self._next = 0
        self._prev = 0
        self._lineBreak = False
        self._pageBreak = False
        self._dirty = True