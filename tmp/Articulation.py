#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Symbol import *
from Sym import *
from Accidental import *

class ArticulationInfo:
    def __init__(self, sym, name, relVelocity, relGateTime):
        self.sym = sym
        self.name = name
        self.relVelocity = relVelocity
        self.relGateTime = relGateTime



class Articulation(Symbol):
    def __init__(self, s):
        Symbol.__init__(self, s)
        self.articulationList = [
      ArticulationInfo( SymName.ufermataSym,       QT_TRANSLATE_NOOP("articulation", "ufermata"),        100, 100  ),
      ArticulationInfo( SymName.dfermataSym,       QT_TRANSLATE_NOOP("articulation", "dfermata"),        100, 100  ),
      ArticulationInfo( SymName.ushortfermataSym,    QT_TRANSLATE_NOOP("articulation", "ushortfermata"),    100, 100  ),
      ArticulationInfo( SymName.dshortfermataSym,    QT_TRANSLATE_NOOP("articulation", "dshortfermata"),    100, 100  ),
      ArticulationInfo( SymName.ulongfermataSym,     QT_TRANSLATE_NOOP("articulation", "ulongfermata"),     100, 100  ),
      ArticulationInfo( SymName.dlongfermataSym,     QT_TRANSLATE_NOOP("articulation", "dlongfermata"),     100, 100  ),
      ArticulationInfo( SymName.uverylongfermataSym, QT_TRANSLATE_NOOP("articulation", "uverylongfermata"), 100, 100  ),
      ArticulationInfo( SymName.dverylongfermataSym, QT_TRANSLATE_NOOP("articulation", "dverylongfermata"), 100, 100  ),
      ArticulationInfo( SymName.thumbSym,          QT_TRANSLATE_NOOP("articulation", "thumb"),           100, 100  ),
      ArticulationInfo( SymName.sforzatoaccentSym, QT_TRANSLATE_NOOP("articulation", "sforzato"),        120, 100  ),
      ArticulationInfo( SymName.esprSym,           QT_TRANSLATE_NOOP("articulation", "espressivo"),      100, 100  ),
      ArticulationInfo( SymName.staccatoSym,       QT_TRANSLATE_NOOP("articulation", "staccato"),        100,  50  ),
      ArticulationInfo( SymName.ustaccatissimoSym, QT_TRANSLATE_NOOP("articulation", "ustaccatissimo"),  100, 100  ),
      ArticulationInfo( SymName.dstaccatissimoSym, QT_TRANSLATE_NOOP("articulation", "dstaccatissimo"),  100, 100  ),
      ArticulationInfo( SymName.tenutoSym,         QT_TRANSLATE_NOOP("articulation", "tenuto"),          100, 100  ),
      ArticulationInfo( SymName.uportatoSym,       QT_TRANSLATE_NOOP("articulation", "uportato"),        100, 100  ),
      ArticulationInfo( SymName.dportatoSym,       QT_TRANSLATE_NOOP("articulation", "dportato"),        100, 100  ),
      ArticulationInfo( SymName.umarcatoSym,       QT_TRANSLATE_NOOP("articulation", "umarcato"),        110, 100  ),
      ArticulationInfo( SymName.dmarcatoSym,       QT_TRANSLATE_NOOP("articulation", "dmarcato"),        110, 100  ),
      ArticulationInfo( SymName.ouvertSym,         QT_TRANSLATE_NOOP("articulation", "ouvert"),          100, 100  ),
      ArticulationInfo( SymName.plusstopSym,       QT_TRANSLATE_NOOP("articulation", "plusstop"),        100, 100  ),
      ArticulationInfo( SymName.upbowSym,          QT_TRANSLATE_NOOP("articulation", "upbow"),           100, 100  ),
      ArticulationInfo( SymName.downbowSym,        QT_TRANSLATE_NOOP("articulation", "downbow"),         100, 100  ),
      ArticulationInfo( SymName.reverseturnSym,    QT_TRANSLATE_NOOP("articulation", "reverseturn"),     100, 100  ),
      ArticulationInfo( SymName.turnSym,           QT_TRANSLATE_NOOP("articulation", "turn"),            100, 100  ),
      ArticulationInfo( SymName.trillSym,          QT_TRANSLATE_NOOP("articulation", "trill"),           100, 100  ),
      ArticulationInfo( SymName.prallSym,          QT_TRANSLATE_NOOP("articulation", "prall"),           100, 100  ),
      ArticulationInfo( SymName.mordentSym,        QT_TRANSLATE_NOOP("articulation", "mordent"),         100, 100  ),
      ArticulationInfo( SymName.prallprallSym,     QT_TRANSLATE_NOOP("articulation", "prallprall"),      100, 100  ),
      ArticulationInfo( SymName.prallmordentSym,   QT_TRANSLATE_NOOP("articulation", "prallmordent"),    100, 100  ),
      ArticulationInfo( SymName.upprallSym,        QT_TRANSLATE_NOOP("articulation", "upprall"),         100, 100  ),
	  ArticulationInfo( SymName.downprallSym,      QT_TRANSLATE_NOOP("articulation", "downprall"),       100, 100  ),
	  ArticulationInfo( SymName.upmordentSym,      QT_TRANSLATE_NOOP("articulation", "upmordent"),       100, 100  ),
	  ArticulationInfo( SymName.downmordentSym,    QT_TRANSLATE_NOOP("articulation", "downmordent"),     100, 100  ),
      ArticulationInfo( SymName.snappizzicatoSym,  QT_TRANSLATE_NOOP("articulation", "snappizzicato"),   100, 100  )
	]

    def isMovable(self):
        return True

    def type(self):
        return ElementType.ARTICULATION

    def name(self):
        return self.articulationList[self.subtype()].name

    def relGateTime(self):
        return self.articulationList[self.subtype()].relGateTime

    def relVelocity(self):
        return self.articulationList[self.subtype()].relVelocity

    def chordRest(self):
        return self.parent()

    def anchor(self):
        return self._anchor

    def setAnchor(self, v):
        self._anchor = v

    def channelName(self):
        return self._channelName

    def setChannelName(self, s):
        self._channelName = s

    def subtypeName(self):
        return self.articulationList[self.subtype()].name


