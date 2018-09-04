#!/usr/bin/env python

from Textline import *

class VoltaSegment(TextLineSegment):
    def __init__(self, s):
        TextLineSegment.__init__(self, s)

    def type(self):
        return ElementType.VOLTA_SEGMENT

    def clone(self):
        return VoltaSegment(self)

    def volta(self):
        return self.parent()

class Volta(TextLine):
    def __init__(self, s):
        TextLine.__init__(self, s)
        self.setLineWidth(Spatium(.18))
        self.setBeginText("1.", TEXT_STYLE.TEXT_STYLE_VOLTA)

        self.setBeginTextPlace(Placement.PLACE_BELOW)
        self.setContinueTextPlace(Placement.PLACE_BELOW)

        self.setOffsetType(OffsetType.OFFSET_SPATIUM)
        self.setBeginHook(True)
        self.setBeginHookHeight(Spatium(1.9))
        self.setYoff(-2.0)
        self.setEndHookHeight(Spatium(1.9))
        self.setAnchor(Anchor.ANCHOR_MEASURE)

    def type(self):
        return ElementType.VOLTA

    def clone(self):
        return Volta(self)

    def endings(self):
        return self._endings

    def setEndings(self, l):
        self._endings = l

    def setText(self, s):
        self.setBeginText(s, TEXT_STYLE.TEXT_STYLE_VOLTA);
