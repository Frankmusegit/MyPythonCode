#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *

class Glissando(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._text = "gliss."
        self._showText = True
        self._spatium = self.spatium()
        self.line = 0
        self.setSize(QSizeF(self._spatium * 2, self._spatium * 4))

    def type(self):
        return ElementType.GLISSANDO

    def isMovable(self):
        return False

    def text(self):
        return self._text

    def setText(self, t):
        self._text = t

    def showText(self):
        return self._showText

    def setShowText(self, v):
        self._showText = v

    def setSize(self, s):
        self.line = QLineF(0.0, s.height(), s.width(), 0.0)