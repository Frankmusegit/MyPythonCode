#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Symbol import *
from Sym import *

class NoteHead(Symbol):
    def __init__(self, s):
        Symbol.__init__(self, s)

    def type(self):
        return ElementType.NOTEHEAD

noteHeads = (
      (    
      ( SymName.wholeheadSym,         SymName.halfheadSym,         SymName.quartheadSym,      SymName.brevisheadSym        ),
      ( SymName.wholecrossedheadSym,  SymName.halfcrossedheadSym,  SymName.crossedheadSym,    SymName.wholecrossedheadSym  ),
      ( SymName.wholediamondheadSym,  SymName.halfdiamondheadSym,  SymName.diamondheadSym,    SymName.wholediamondheadSym  ),
      ( SymName.s0triangleHeadSym,    SymName.d1triangleHeadSym,   SymName.d2triangleHeadSym, SymName.s0triangleHeadSym    ),
      ( SymName.s0miHeadSym,          SymName.s1miHeadSym,         SymName.s2miHeadSym,       -1                   ),
      ( SymName.wholeslashheadSym,    SymName.halfslashheadSym,    SymName.quartslashheadSym, SymName.wholeslashheadSym    ),
      ( SymName.xcircledheadSym,      SymName.xcircledheadSym,     SymName.xcircledheadSym,   SymName.xcircledheadSym      ),
      ( SymName.s0doHeadSym,          SymName.d1doHeadSym,         SymName.d2doHeadSym,       -1                   ),
      ( SymName.s0reHeadSym,          SymName.d1reHeadSym,         SymName.d2reHeadSym,       -1                   ),
      ( SymName.d0faHeadSym,          SymName.d1faHeadSym,         SymName.d2faHeadSym,       -1                   ),
      ( SymName.s0laHeadSym,          SymName.s1laHeadSym,         SymName.s2laHeadSym,       -1                   ),
      ( SymName.s0tiHeadSym,          SymName.d1tiHeadSym,         SymName.d2tiHeadSym,       -1                   ),
      ( SymName.s0solHeadSym,         SymName.s1solHeadSym,        SymName.s2solHeadSym,      -1                   ),
      ( SymName.wholeheadSym,         SymName.halfheadSym,         SymName.quartheadSym,      SymName.brevisheadaltSym     ),
      ),
      ( 
      ( SymName.wholeheadSym,         SymName.halfheadSym,         SymName.quartheadSym,      SymName.brevisheadSym        ),
      ( SymName.wholecrossedheadSym,  SymName.halfcrossedheadSym,  SymName.crossedheadSym,    SymName.wholecrossedheadSym  ),
      ( SymName.wholediamondheadSym,  SymName.halfdiamondheadSym,  SymName.diamondheadSym,    SymName.wholediamondheadSym  ),
      ( SymName.s0triangleHeadSym,    SymName.u1triangleHeadSym,   SymName.u2triangleHeadSym, SymName.s0triangleHeadSym    ),
      ( SymName.s0miHeadSym,          SymName.s1miHeadSym,         SymName.s2miHeadSym,       -1                   ),
      ( SymName.wholeslashheadSym,    SymName.halfslashheadSym,    SymName.quartslashheadSym, SymName.wholeslashheadSym    ),
      ( SymName.xcircledheadSym,      SymName.xcircledheadSym,     SymName.xcircledheadSym,   SymName.xcircledheadSym      ),
      ( SymName.s0doHeadSym,          SymName.u1doHeadSym,         SymName.u2doHeadSym,       -1                   ),
      ( SymName.s0reHeadSym,          SymName.u1reHeadSym,         SymName.u2reHeadSym,       -1                   ),
      ( SymName.u0faHeadSym,          SymName.u1faHeadSym,         SymName.u2faHeadSym,       -1                   ),
      ( SymName.s0laHeadSym,          SymName.s1laHeadSym,         SymName.s2laHeadSym,       -1                   ),
      ( SymName.s0tiHeadSym,          SymName.u1tiHeadSym,         SymName.u2tiHeadSym,       -1                   ),
      ( SymName.s0solHeadSym,         SymName.s1solHeadSym,        SymName.s2solHeadSym,      -1                   ),
      ( SymName.wholeheadSym,         SymName.halfheadSym,         SymName.quartheadSym,      SymName.brevisheadaltSym     ),
      )
      )

class Note(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self.dragMode           = False
        self._pitch             = 0
        self._ppitch            = 0
        self._tuning            = 0.0
        self._userAccidental    = AccidentalType.ACC_NONE
        self._accidental        = 0
        self._mirror            = False
        self._userMirror        = DirectionH.DH_AUTO
        self._line              = 0
        self._lineOffset        = 0
        self._tieFor            = 0
        self._tieBack           = 0
        self._tpc               = -1
        self._headGroup         = 0
        self._headType          = NoteHeadType.HEAD_AUTO

        self._hidden            = False
        self._subchannel        = 0

        self._veloType          = ValueType.AUTO_VAL
        self._velocity          = 80
        self._veloOffset        = 0

        self._onTimeType        = ValueType.AUTO_VAL
        self._onTimeOffset      = 0
        self._onTimeUserOffset  = 0

        self._offTimeType       = ValueType.AUTO_VAL
        self._offTimeOffset     = 0
        self._offTimeUserOffset = 0

    def type(self):
        return ElementType.NOTE

class ShadowNote(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._line = 1000
        self._headGroup = 0
        self._head      = 2

    def type(self):
        return ElementType.SHADOW_NOTE

    def line(self):
        return self._line

    def setLine(self, n):
        self._line = n

    def headGroup(self):
        return self._headGroup

    def setHead(self, val):
        self._head = val

    def head(self):
        return self._head
