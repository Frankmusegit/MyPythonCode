#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Line import *
from Spatium import *
from Text import *

class TextLineSegment(LineSegment):
    def __init__(self, s):
        LineSegment.__init__(self, s)
        self._text = 0

    def clone(self):
        return TextLineSegment(self, None)

    def type(self):
        return ElementType.TEXTLINE_SEGMENT

    def textLine(self):
        return self.parent()

    def text(self):
        return self._text

class TextLine(SLine):
    def __init__(self, s):
        SLine.__init__(self, s)
        self._beginText         = 0
        self._continueText      = 0
        self._beginHookHeight   = Spatium(1.5)
        self._endHookHeight     =  Spatium(1.5)
        self._beginHook         = False
        self._endHook           = False

        self._lineWidth         = Spatium(0.15)
        self._lineStyle         = Qt.SolidLine
        self._beginTextPlace    = Placement.PLACE_LEFT
        self._continueTextPlace = Placement.PLACE_LEFT
        self._lineColor         = Qt.black
        self._mxmlOff2          = 0
        self._beginSymbol       = -1
        self._continueSymbol    = -1
        self._endSymbol         = -1

    def clone(self):
        return TextLine(self)

    def type(self):
        return ElementType.TEXTLINE

    def beginHook(self):
        return self._beginHook

    def endHook(self):
        return self._endHook

    def setBeginHook(self, v):
        self._beginHook = v

    def setEndHook(self, v):
        self._endHook = v

    def  beginText(self):
        return self._beginText

    def continueText(self):
        return self._continueText

    def beginTextPlace(self):
        return self._beginTextPlace

    def setBeginTextPlace(self, p):
        self._beginTextPlace = p

    def continueTextPlace(self):
        return self._continueTextPlace

    def setContinueTextPlace(self, p):
        self._continueTextPlace = p

    def setBeginSymbol(self, v):
        self._beginSymbol = v

    def setContinueSymbol(self, v):
        self._continueSymbol = v

    def setEndSymbol(self, v):
        self._endSymbol = v

    def setBeginHookHeight(self, v):
        self._beginHookHeight = v

    def setEndHookHeight(self,  v):
        self._endHookHeight = v

    def beginHookHeight(self):
        return self._beginHookHeight

    def endHookHeight(self):
        return self._endHookHeight

    def lineWidth(self):
        return self._lineWidth

    def lineColor(self):
        return self._lineColor

    def lineStyle(self):
        return self._lineStyle

    def setLineWidth(self, v):
        self._lineWidth = v

    def setLineColor(self, v):
        self._lineColor = v

    def setLineStyle(self, v):
        self._lineStyle = v

    def beginSymbol(self):
        return self._beginSymbol

    def continueSymbol(self):
        return self._continueSymbol

    def endSymbol(self):
        return self._endSymbol

    def beginSymbolOffset(self):
        return self._beginSymbolOffset

    def continueSymbolOffset(self):
        return self._continueSymbolOffset

    def endSymbolOffset(self):
        return self._endSymbolOffset

    def setBeginSymbolOffset(self, v):
        self._beginSymbolOffset = v

    def setContinueSymbolOffset(self, v):
        self._continueSymbolOffset = v

    def setEndSymbolOffset(self, v):
        self._endSymbolOffset = v

    def setMxmlOff2(self,  v):
        self._mxmlOff2 = v

    def mxmlOff2(self):
        return self._mxmlOff2

    def setBeginText(self, s, textStyle):
        if not self._beginText:
            self._beginText = TextC(self.score())
            self._beginText.setSubtype(TEXT.TEXT_TEXTLINE)
            self._beginText.setTextStyle(textStyle)
            self._beginText.setParent(self)
        self._beginText.setText(s)

    def setBeginText1(self, v):
        del self._beginText
        self._beginText = v

