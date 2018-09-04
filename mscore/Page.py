#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from Text import *


class PaperSize:
    def __init__(self, s, n, wi, hi):
        self.qtsize = s
        self.name = n
        self.w = wi
        self.h = hi
def MM(x):
    return x/INCH

paperSizes = [
      PaperSize(QPrinter.A4,      "A4",        MM(210),  MM(297)),
      PaperSize(QPrinter.B5,      "B5",        MM(176),  MM(250)),
      PaperSize(QPrinter.Letter,  "Letter",    8.5,      11),
      PaperSize(QPrinter.Legal,   "Legal",     8.5,      14),
      PaperSize(QPrinter.Executive,"Executive",7.5,      10),
      PaperSize(QPrinter.A0,      "A0",        MM(841),  MM(1189)),
      PaperSize(QPrinter.A1,      "A1",        MM(594),  MM(841)),
      PaperSize(QPrinter.A2,      "A2",        MM(420),  MM(594)),
      PaperSize(QPrinter.A3,      "A3",        MM(297),  MM(420)),
      PaperSize(QPrinter.A5,      "A5",        MM(148),  MM(210)),
      PaperSize(QPrinter.A6,      "A6",        MM(105),  MM(148)),
      PaperSize(QPrinter.A7,      "A7",        MM(74),   MM(105)),
      PaperSize(QPrinter.A8,      "A8",        MM(52),   MM(74)),
      PaperSize(QPrinter.A9,      "A9",        MM(37),   MM(52)),
      PaperSize(QPrinter.B0,      "B0",        MM(1000), MM(1414)),
      PaperSize(QPrinter.B1,      "B1",        MM(707),  MM(1000)),
      PaperSize(QPrinter.B10,     "B10",       MM(31),   MM(44)),
      PaperSize(QPrinter.B2,      "B2",        MM(500),  MM(707)),
      PaperSize(QPrinter.B3,      "B3",        MM(353),  MM(500)),
      PaperSize(QPrinter.B4,      "B4",        MM(250),  MM(353)),
      PaperSize(QPrinter.B5,      "B5",        MM(125),  MM(176)),
      PaperSize(QPrinter.B6,      "B6",        MM(88),   MM(125)),
      PaperSize(QPrinter.B7,      "B7",        MM(62),   MM(88)),
      PaperSize(QPrinter.B8,      "B8",        MM(44),   MM(62)),
      PaperSize(QPrinter.B9,      "B9",        MM(163),  MM(229)),
      PaperSize(QPrinter.Comm10E, "Comm10E",   MM(105),  MM(241)),
      PaperSize(QPrinter.DLE,     "DLE",       MM(110),  MM(220)),
      PaperSize(QPrinter.Folio,   "Folio",     MM(210),  MM(330)),
      PaperSize(QPrinter.Ledger,  "Ledger",    MM(432),  MM(279)),
      PaperSize(QPrinter.Tabloid, "Tabloid",   MM(279),  MM(432)),
      PaperSize(QPrinter.Custom,  "Custom",    MM(210),  MM(297)),
      PaperSize(QPrinter.A4, 0, 0, 0  )
    ]

class PageFormat:

    def __init__(self):
        self.size = Preferences().paperSize
        self._width = Preferences().paperWidth
        self._height = Preferences().paperHeight
        self.evenLeftMargin = 10.0 / INCH
        self.evenRightMargin = 10.0 / INCH
        self.evenTopMargin = 10.0 / INCH
        self.evenBottomMargin = 20.0 / INCH
        self.oddLeftMargin = 10.0 / INCH
        self.oddRightMargin = 10.0 / INCH
        self.oddTopMargin = 10.0 / INCH
        self.oddBottomMargin = 20.0 / INCH
        self.landscape = Preferences().landscape
        self.twosided = Preferences().twosided
        self._pageOffset = 0

    def width(self):
        global paperSizes
        if paperSizes[self.size].qtsize == QPrinter.Custom:
            if self.landscape:
                return self._height
            else:
                return self._width
        if self.landscape:
            return paperSizes[self.size].h
        else:
            return paperSizes[self.size].w

    def height(self):
        global paperSizes
        if paperSizes[self.size].qtsize == QPrinter.Custom:
            if self.landscape:
                return self._width
            else:
                return self._height
        if self.landscape:
            return paperSizes[self.size].w
        else:
            return paperSizes[self.size].h

class Page(Element):

    def __init__(self, s):
        Element.__init__(self, s)
        self._systems = list()
        self._no = 0
        self._pageNo = 0
        self._copyright = 0

    def setNo(self, n):
        self._no = n

    def no(self):
        return self._no

    def loWidth(self):
        return self.score().pageFormat().width() * GL.DPI

    def loHeight(self):
        return self.score().pageFormat().height() * GL.DPI

    def score(self):
        return self._score

    def layout(self):
        self.setbbox(QRectF(0.0, 0.0, self.loWidth(), self.loHeight()))
        n = self.no() + 1 + self._score.pageFormat()._pageOffset
        if self.score().styleB( StyleIdx.ST_showPageNumber) and (self.no() > 0 or self.score().styleB( StyleIdx.ST_showPageNumberOne)):
            if n & 1:
               subtype =  TEXT.TEXT_PAGE_NUMBER_ODD
            else:
                subtype = TEXT.TEXT_PAGE_NUMBER_EVEN
            if n & 1:
                style  = TEXT.TEXT_STYLE_PAGE_NUMBER_ODD
            else:
                style  = TEXT.TEXT_STYLE_PAGE_NUMBER_EVEN
            if self._pageNo == 0:
                self._pageNo = Text(self.score())
                self._pageNo.setParent(self)
            if subtype != self._pageNo.subtype():
                self._pageNo.setSubtype(subtype)
                self._pageNo.setTextStyle(style)
            s = QString("%1").arg(n)
            if self._pageNo.getText() != s:
                self._pageNo.setText(s)
                self._pageNo.layout()
        else:
            self._pageNo = 0

        if self._score.rights:
            if self._copyright == 0:
                self._copyright = TextC(self._score.rights)
                self._copyright.setParent(self)
                self._copyright.setTextStyle(TEXT.TEXT_STYLE_COPYRIGHT)
                self._copyright.layout()
        else:
                self._copyright = 0

