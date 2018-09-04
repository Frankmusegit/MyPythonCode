#!/usr/bin/env python

from Element import *

class LineSegment(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._segmentType = LineSegmentType.SEGMENT_SINGLE
        self._system = 0

    def isMovable(self):
        return True

    def isEditable(self):
        return True

    def line(self):
        return self.parent()

    def userOff2(self):
        return self._userOff2

    def setUserOff2(self, o):
        self._userOff2 = o

    def setUserXoffset2(self, x):
        self._userOff2.setX(x)

    def setPos2(self, p):
        self._p2 = p

    def setXpos2(self, x):
        self._p2.setX(x)

    def setLineSegmentType(self, s):
        self. _segmentType = s

    def segmentType(self):
        return self._segmentType

    def setSystem(self, s):
        self._system = s


class SLine(Element):

    def __init__(self, s):
        Element.__init__(self, s)
        self.setTick(0)
        self._tick2 = 0
        self._diagonal = False
        self._anchor = Anchor.ANCHOR_SEGMENT
        self.segments = list()

    def setLen(self, l):
        if len(self.segments) == 0:
            self.add(self.createLineSegment())
        s = self.segments[0]
        s.setPos1(QPointF())
        s.setPos2(QPointF(l, 0))

    def tick2(self):
        return self._tick2

    def lineSegments(self):
        return self.segments

    def diagonal(self):
        return self._diagonal

    def setDiagonal(self, v):
        self._diagonal = v

    def anchor(self):
        return self._anchor

    def setAnchor(self, a):
        self._anchor = a

    def add(self, e):
        e.setParent(self)
        self.segments.append(e)

    def createLineSegment(self):
        return LineSegment(None)

