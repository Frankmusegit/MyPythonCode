#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Text import *

class Dyn:
    def __init__(self, velo, t):
        self.velocity = velo
        self.tag = t

dynList = [
      Dyn( -1,  "other-dynamics"),
      Dyn(  1,  "pppppp"),
      Dyn(  5,  "ppppp"),
      Dyn( 10,  "pppp"),
      Dyn( 16,  "ppp"),
      Dyn( 33,  "pp"),
      Dyn( 49,  "p"),
      Dyn( 64,  "mp"),
      Dyn( 80,  "mf"),
      Dyn( 96,  "f"),
      Dyn(112,  "ff"),
      Dyn(126,  "fff"),
      Dyn(127,  "ffff"),
      Dyn(127,  "fffff"),
      Dyn(127,  "ffffff"),
      Dyn( -1,  "fp"),
      Dyn( -1,  "sf"),
      Dyn( -1,  "sfz"),
      Dyn( -1,  "sff"),
      Dyn( -1,  "sffz"),
      Dyn( -1,  "sfp"),
      Dyn( -1,  "sfpp"),
      Dyn( -1,  "rfz"),
      Dyn( -1,  "rf"),
      Dyn( -1,  "fz"),
      Dyn( -1,  "m"),
      Dyn( -1,  "r"),
      Dyn( -1,  "s"),
      Dyn( -1,  "z")
      ]

class Dynamic(Text):

    def __init__(self, s):
        Text.__init__(self, s)
        self._velocity = -1
        self.setTextStyle(TEXT_STYLE.TEXT_STYLE_DYNAMICS)
        self._dynType  = DynamicType.DYNAMIC_PART

    def type(self):
        return ElementType.DYNAMIC

    def measure(self):
        return self.parent()

    def isMovable(self):
        return True

    def isEditable(self):
        return True

    def dynType(self):
        return self._dynType

    def setDynType(self, t):
        self._dynType = t

    def subtypeName(self):
        return dynList[self.subtype()].tag

    def setSubtype1(self, tag):
        for i in range(0, len(dynList)):
            if dynList[i].tag == tag:
                self.setSubtype(i)
                return
        Element.setSubtype(0)
        self.setText(tag)

    def setSubtype(self, idx):
        Element().setSubtype(idx)
        if idx:
            Element().setSubtype(idx)
            self.doc().clear()
            cursor = QTextCursor(self.doc())
            cursor.movePosition(QTextCursor.Start)
            tf = cursor.charFormat()
            ts = self.score().textStyle(TEXT_STYLE.TEXT_STYLE_DYNAMICS)
            size = ts.size
            m = size
            if ts.sizeIsSpatiumDependent:
                m = m * (self.score().spatium() / (SPATIUM20 * GL.DPI))
            m = m * self.mag()

            font = QFont("MScore1")
            font.setPointSize(m)
            font.setKerning(True)
            tf.setFont(font)
            tf.setProperty(QTextFormat.FontKerning, True)
            #tf.setProperty(QTextFormat::FontLetterSpacing, 100)
            cursor.setBlockCharFormat(tf)
            cursor.insertText(dynList[idx].tag)
            