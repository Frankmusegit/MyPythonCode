#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Rest import *
from Text import *
from Sym import *

class RepeatMeasure(Rest):
    def __init__(self, s ):
        Rest.__init__(self, s)

    def type(self):
        return ElementType.REPEAT_MEASURE

    def bbox(self):
        return self._bbox

class Marker(Text):
    def __init__(self, s ):
        Text.__init__(self, s)
        self.setSubtype(TEXT.TEXT_REPEAT)
        self.setTextStyle(TEXT_STYLE.TEXT_STYLE_REPEAT)

    def type(self):
        return ElementType.MARKER

    def label(self):
        return self._label

    def setLabel(self, s):
        self._label = s

    def setMarkerType(self, t):
        if t == MARKER.MARKER_SEGNO:
            self.setHtml(symToHtml(GL.symbols[SymName.segnoSym], 0))
            self.setLabel("segno")
            self._reloff.rx = 0.0
        elif MARKER.MARKER_CODA:
            self.setHtml(symToHtml(GL.symbols[SymName.codaSym], 0))
            self.setLabel("codab")
            self._reloff.rx = 0.0
        elif MARKER.MARKER_VARCODA:
            self.setHtml(symToHtml(GL.symbols[SymName.varcodaSym], 0))
            self.setLabel("varcoda")
            self._reloff.rx = 0.0
        elif MARKER.MARKER_CODETTA:
            self.setHtml(symToHtml1(GL.symbols[SymName.codaSym], GL.symbols[SymName.codaSym], 0))
            self.setLabel("codetta")
            self._reloff.rx = 0.0
        elif MARKER.MARKER_FINE:
            self.setText("Fine")
            self.setLabel("fine")
            self._reloff.rx = 100.0
        elif MARKER.MARKER_TOCODA:
            self.setText("To Coda")
            self.setLabel("coda")
            self._reloff.rx = 100.0
        elif MARKER.MARKER_USER:
            pass
        else:
            print "unknown marker type %d\n" %t

      
class Jump(Text):
    def __init__(self, s ):
        Text.__init__(self, s)
        self.setSubtype(TEXT.TEXT_REPEAT)
        self.setTextStyle(TEXT_STYLE.TEXT_STYLE_REPEAT)

    def type(self):
        return ElementType.JUMP

    def jumpTo(self):
        return self._jumpTo

    def playUntil(self):
        return self._playUntil

    def continueAt(self):
        return self._continueAt

    def setJumpTo(self, s):
        self._jumpTo = s

    def setPlayUntil(self, s):
        self._playUntil = s

    def setContinueAt(self, s):
        self._continueAt = s

    def setJumpType(self, t):
        if t == JUMP.JUMP_DC:
            self.setText("D.C.")
            self.setJumpTo("start")
            self.setPlayUntil("end")
        elif JUMP.JUMP_DC_AL_FINE:
            self.setText("D.C. al Fine")
            self.setJumpTo("start")
            self.setPlayUntil("fine")
        elif JUMP.JUMP_DC_AL_CODA:
            self.setText("D.C. al Coda")
            self.setJumpTo("start")
            self.setPlayUntil("coda")
            self.setContinueAt("codab")
        elif JUMP.JUMP_DS_AL_CODA:
            self.setText("D.S. al Coda")
            self.setJumpTo("segno")
            self.setPlayUntil("coda")
            self.setContinueAt("codab")
        elif JUMP.JUMP_DS_AL_FINE:
            self.setText("D.S. al Fine")
            self.setJumpTo("segno")
            self.setPlayUntil("fine")
        elif JUMP.JUMP_DS:
            self.setText("D.S.")
            self.setJumpTo("segno")
            self.setPlayUntil("end")
        elif JUMP.JUMP_USER:
            pass
        else:
            print "unknown jump type\n"

