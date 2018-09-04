#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Line import *

class TrillSegment(LineSegment):
    def __init__(self, s):
        LineSegment.__init__(self, s)

    def trill(self):
        return self.parent()

    def type(self):
        return ElementType.TRILL_SEGMENT

class Trill(SLine):
    def __init__(self, s):
        SLine.__init__(self, s)

    def type(self):
        return ElementType.TRILL
