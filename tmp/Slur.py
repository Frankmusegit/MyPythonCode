#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class SlurSegment(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._segmentType = LineSegmentType.SEGMENT_SINGLE
        self._system      = 0

    def type(self):
        return ElementType.SLUR_SEGMENT

    def isMovable(self):
        return True

    def isEditable(self):
        return True

    def slurTie(self):
        return self.parent()

class SlurTie(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._slurDirection = Direction.AUTO
        self.up             = True
        self._startElement  = 0
        self._endElement    = 0
        self._len           = 0
        self._lineType      = 0

    def isUp(self):
        return self.up

    def setUp(self, val):
        self.up = val

    def slurDirection(self):
        return self._slurDirection

    def setSlurDirection(self, d):
        self._slurDirection = d

    def slurSegments(self):
        return self.segments

    def setStartElement(self, e):
        self._startElement = e

    def setEndElement(self, e):
        self._endElement = e

    def startElement(self):
        return self._startElement

    def endElement(self):
        return self._endElement

    def setLen(self, v):
        self._len = v

    def lineType(self):
        return self._lineType

    def setLineType(self, val):
        self._lineType = val

class Slur(SlurTie):
    def __init__(self, s):
        SlurTie.__init__(self, s)
        self.setTick(0)
        self._tick2  = 0
        self._track2 = 0

    def type(self):
        return ElementType.SLUR

    def tick2(self):
        return self._tick2

    def track2(self):
        return self._track2

    def staffIdx2(self):
        return self._track2 / VOICES

    def etTrack2(self, val):
        self._track2 = val

    def id(self):
        return self._id

    def setId(self, i):
        self._id = i

class Tie(SlurTie):
    def __init__(self, s):
        SlurTie.__init__(self, s)

    def type(self):
        return ElementType.TIE


