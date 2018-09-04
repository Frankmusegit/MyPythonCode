#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Element import *
from Sym import *

class Acc:
    def __init__(self, t, n, o, o2, s):
        self.tag = t
        self.name = n
        self.offset = o
        self.centOffset = o2
        self.sym = s

accList = [
      Acc("none",                QT_TRANSLATE_NOOP("accidental", "none"),                0, 0, -1),
      Acc("sharp",               QT_TRANSLATE_NOOP("accidental", "sharp"),               1, 0, SymName.sharpSym),
      Acc("flat",                QT_TRANSLATE_NOOP("accidental", "flat"),               -1, 0, SymName.flatSym),
      Acc("double sharp",        QT_TRANSLATE_NOOP("accidental", "double sharp"),        2, 0, SymName.sharpsharpSym),
      Acc("double flat",         QT_TRANSLATE_NOOP("accidental", "double flat"),        -2, 0, SymName.flatflatSym),
      Acc("natural",             QT_TRANSLATE_NOOP("accidental", "natural"),             0, 0, SymName.naturalSym),

      Acc("flat-slash",          QT_TRANSLATE_NOOP("accidental", "flat-slash"),          0, 0, SymName.flatslashSym),
      Acc("flat-slash2",         QT_TRANSLATE_NOOP("accidental", "flat-slash2"),         0, 0, SymName.flatslash2Sym),
      Acc("mirrored-flat2",      QT_TRANSLATE_NOOP("accidental", "mirrored-flat2"),      0, 0, SymName.mirroredflat2Sym),
      Acc("mirrored-flat",       QT_TRANSLATE_NOOP("accidental", "mirrored-flat"),       0, 0, SymName.mirroredflatSym),
      Acc("mirrored-flat-slash", QT_TRANSLATE_NOOP("accidental", "mirrored-flat-slash"), 0, 0, SymName.mirroredflatslashSym),
      Acc("flat-flat-slash",     QT_TRANSLATE_NOOP("accidental", "flat-flat-slash"),     0, 0, SymName.flatflatslashSym),

      Acc("sharp-slash",         QT_TRANSLATE_NOOP("accidental", "sharp-slash"),         0, 0, SymName.sharpslashSym),
      Acc("sharp-slash2",        QT_TRANSLATE_NOOP("accidental", "sharp-slash2"),        0, 0, SymName.sharpslash2Sym),
      Acc("sharp-slash3",        QT_TRANSLATE_NOOP("accidental", "sharp-slash3"),        0, 0, SymName.sharpslash3Sym),
      Acc("sharp-slash4",        QT_TRANSLATE_NOOP("accidental", "sharp-slash4"),        0, 0, SymName.sharpslash4Sym),

      Acc("sharp arrow up",      QT_TRANSLATE_NOOP("accidental", "sharp arrow up"),      0, 0, SymName.sharpArrowUpSym),
      Acc("sharp arrow down",    QT_TRANSLATE_NOOP("accidental", "sharp arrow down"),    0, 0, SymName.sharpArrowDownSym),
      Acc("sharp arrow both",    QT_TRANSLATE_NOOP("accidental", "sharp arrow both"),    0, 0, SymName.sharpArrowBothSym),
      Acc("flat arrow up",       QT_TRANSLATE_NOOP("accidental", "flat arrow up"),       0, 0, SymName.flatArrowUpSym),
      Acc("flat arrow down",     QT_TRANSLATE_NOOP("accidental", "flat arrow down"),     0, 0, SymName.flatArrowDownSym),
      Acc("flat arrow both",     QT_TRANSLATE_NOOP("accidental", "flat arrow both"),     0, 0, SymName.flatArrowBothSym),
      Acc("natural arrow up",    QT_TRANSLATE_NOOP("accidental", "natural arrow up"),    0, 0, SymName.naturalArrowUpSym),
      Acc("natural arrow down",  QT_TRANSLATE_NOOP("accidental", "natural arrow down"),  0, 0, SymName.naturalArrowDownSym),
      Acc("natural arrow both",  QT_TRANSLATE_NOOP("accidental", "natural arrow both"),  0, 0, SymName.naturalArrowBothSym),
      Acc("sori",                QT_TRANSLATE_NOOP("accidental", "sori"),                0, 0, SymName.soriSym),
      Acc("koron",               QT_TRANSLATE_NOOP("accidental", "koron"),               0, 0, SymName.koronSym)
      ]

class Accidental(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._hasBracket = False

    def type(self):
        return ElementType.ACCIDENTAL

    def subtypeUserName(self):
        return accList[self.subtype()].name

    def note(self):
        return self.parent()

    def hasBracket(self):
        return self._hasBracket

    def setHasBracket(self, val):
        self._hasBracket = val

class AccidentalBracket(Compound):
    def __init__(self, s):
        Compound.__init__(self, s)

    def type(self):
        return ElementType.ACCIDENTAL_BRACKET