#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from Element import *

class ClefInfo:
    def __init__(self, sign, line, octChng, yOffset, pitchOffset, lines, name):
        self.sign = sign
        self.line = line
        self.octChng = octChng
        self.yOffset = yOffset
        self.pitchOffset = pitchOffset
        self.lines = lines
        self.name = name

clefTable = [
      ClefInfo("G",   2,  0,   0, 45, [ 0, 3, -1, 2, 5, 1, 4 , 4, 1,  5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Treble clef")),
      ClefInfo("G",   2,  1,   7, 52, [ 0, 3, -1, 2, 5, 1, 4, 4, 1,  5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Treble clef 8va")),
      ClefInfo("G",   2,  2,  14, 59, [ 0, 3, -1, 2, 5, 1, 4, 4, 1,  5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Treble clef 15ma")),
      ClefInfo("G",   2, -1,  -7, 38, [ 0, 3, -1, 2, 5, 1, 4, 4, 1,  5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Treble clef 8vb")),
      ClefInfo("F",   4,  0, -12, 33, [ 2, 5, 1, 4, 7, 3, 6, 6, 3, 7, 4, 8, 5, 9 ], QT_TRANSLATE_NOOP("clefTable", "Bass clef")),
      ClefInfo("F",   4, -1, -19, 26, [ 2, 5, 1, 4, 7, 3, 6, 6, 3, 7, 4, 8, 5, 9 ], QT_TRANSLATE_NOOP("clefTable", "Bass clef 8vb")),
      ClefInfo("F",   4, -2, -26, 19, [ 2, 5, 1, 4, 7, 3, 6, 6, 3, 7, 4, 8, 5, 9 ], QT_TRANSLATE_NOOP("clefTable", "Bass clef 15mb")),
      ClefInfo("F",   3,  0, -10, 35, [ 4, 0, 3, -1, 2, 5, 1, 1, 5, 2, 6, 3, 7, 4 ], QT_TRANSLATE_NOOP("clefTable", "Baritone clef (F clef)")),
      ClefInfo("F",   5,  0, -14, 31, [ 0, 3, -1, 2, 5, 1, 4 , 4, 1,  5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Subbass clef") ),
      ClefInfo("C",   1,  0,  -2, 43, [ 5, 1, 4, 0, 3, -1, 2, 2, -1, 3, 0, 4, 1, 5 ], QT_TRANSLATE_NOOP("clefTable", "Soprano clef")),
      ClefInfo("C",   2,  0,  -4, 41, [ 3, 6, 2, 5, 1, 4, 0, 0, 4, 1, 5, 2, 6, 3 ], QT_TRANSLATE_NOOP("clefTable", "Mezzo-soprano clef")),
      ClefInfo("C",   3,  0,  -6, 39, [ 1, 4, 0, 3, 6, 2, 5, 5, 2, 6, 3, 7, 4, 8 ], QT_TRANSLATE_NOOP("clefTable", "Alto clef")),
      ClefInfo( "C",   4,  0,  -8, 37, [ 6, 2, 5, 1, 4, 0, 3, 3, 0, 4, 1, 5, 2, 6 ], QT_TRANSLATE_NOOP("clefTable", "Tenor clef")),
      ClefInfo( "TAB", 5,  0,   0,  0, [ 0, 3, -1, 2, 5, 1, 4, 4, 1, 5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Tablature")),
      ClefInfo("percussion", 2,  0,   0, 45, [ 0, 3, -1, 2, 5, 1, 4, 4, 1, 5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Percussion")),
      ClefInfo("C",   5,  0, -10, 35, [ 4, 0, 3, -1, 2, 5, 1, 1, 5, 2, 6, 3, 7, 4 ], QT_TRANSLATE_NOOP("clefTable", "Baritone clef (C clef)")),
      ClefInfo("G",   1,  0,   2, 47, [ 2, 5, 1, 4, 0, 3, -1, 6, 3, 7, 4, 1, 5, 2 ], QT_TRANSLATE_NOOP("clefTable", "French violin clef")),
      ClefInfo( "F",   4,  1, -5, 40, [ 2, 5, 1, 4, 7, 3, 6, 6, 3, 7, 4, 8, 5, 9 ], QT_TRANSLATE_NOOP("clefTable", "Bass clef 8va")),
      ClefInfo("F",   4,  2,  2, 47,  [ 2, 5, 1, 4, 7, 3, 6, 6, 3, 7, 4, 8, 5, 9 ], QT_TRANSLATE_NOOP("clefTable", "Bass clef 15ma")),
      ClefInfo( "percussion", 2,  0,   0, 45, [ 0, 3, -1, 2, 5, 1, 4, 4, 1, 5, 2, 6, 3, 7 ], QT_TRANSLATE_NOOP("clefTable", "Percussion"))
      ]

class Clef(Compound):

    def __init__(self, s):
        Compound.__init__(self, s)
        self._small = False

    def Clef1(self, i):
        self.setSubtype(i)

    def type(self):
        return ElementType.CLEF

class ClefList:

    def __init__(self):
        self.t = 0
        
