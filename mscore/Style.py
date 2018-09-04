#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from globals import *
import GL
class TextStyle:
    def __init__(self, _name, _family, _size, _bold,  _italic, _underline, _ALIGN, _xoff=0, _yoff=0, _ot=OffsetType.OFFSET_SPATIUM, _rxoff=0, _ryoff=0, sd=False,\
                 fw=0.0, pw=0.0, fr=25, co=QColor(Qt.black), _circle=False,  _systemFlag=False, fg=QColor(Qt.black)):                                                                        
        self.name = _name
        self.family = _family
        self.size = _size
        self.bold = _bold
        self.italic = _italic
        self.underline = _underline
        self.align = _ALIGN
        self.xoff = _xoff
        self.yoff = _yoff
        self.ot = _ot
        self.rxoff = _rxoff
        self.ryoff = _ryoff
        self.sizeIsSpatiumDependent = sd
        self.frameWidth = fw
        self.paddingWidth = pw
        self.frameRound = fr
        self.frameColor = co
        self.circle = _circle
        self.systemFlag = _systemFlag
        self.foregroundColor = fg
        self.hasFrame = fw != 0.0
        self.offsetType = 0

    def font(self, _spatium):
        m = self.size
        f = QFont(self.family)
        f.setBold(self.bold)
        f.setItalic(self.italic)
        f.setUnderline(self.underline)
        if self.sizeIsSpatiumDependent:
            m *= _spatium / ( SPATIUM20 * GL.DPI)
        f.setPointSizeF(m)
        return f

class StyleType:
    
    def __init__(self, n, v):       
        self._name = n
        self._valueType = StyleValueType()
        self._valueType = v
        
styleTypes = [
      StyleType("staffUpperBorder",        StyleValueType.ST_SPATIUM),
      StyleType("staffLowerBorder",        StyleValueType.ST_SPATIUM),
      StyleType("staffDistance",           StyleValueType.ST_SPATIUM),
      StyleType("akkoladeDistance",        StyleValueType.ST_SPATIUM),
      StyleType("systemDistance",          StyleValueType.ST_SPATIUM),
      StyleType("lyricsDistance",          StyleValueType.ST_SPATIUM),
      StyleType("lyricsMinBottomDistance", StyleValueType.ST_SPATIUM),
      StyleType("systemFrameDistance",     StyleValueType.ST_SPATIUM), 
      StyleType("frameSystemDistance",     StyleValueType.ST_SPATIUM),  
      StyleType("minMeasureWidth",         StyleValueType.ST_SPATIUM),
      StyleType("barWidth",                StyleValueType.ST_SPATIUM),
      StyleType("doubleBarWidth",          StyleValueType.ST_SPATIUM),
      StyleType("endBarWidth",             StyleValueType.ST_SPATIUM),
      StyleType("doubleBarDistance",       StyleValueType.ST_SPATIUM),
      StyleType("endBarDistance",          StyleValueType.ST_SPATIUM),
      StyleType("repeatBarTips",           StyleValueType.ST_BOOL),
      StyleType("startBarlineSingle",      StyleValueType.ST_BOOL),
      StyleType("startBarlineMultiple",    StyleValueType.ST_BOOL),
      StyleType("bracketWidth",            StyleValueType.ST_SPATIUM), 
      StyleType("bracketDistance",         StyleValueType.ST_SPATIUM), 
      StyleType("clefLeftMargin",          StyleValueType.ST_SPATIUM),
      StyleType("keysigLeftMargin",        StyleValueType.ST_SPATIUM),
      StyleType("timesigLeftMargin",       StyleValueType.ST_SPATIUM),
      StyleType("clefKeyRightMargin",      StyleValueType.ST_SPATIUM),
      StyleType("clefBarlineDistance",     StyleValueType.ST_SPATIUM),
      StyleType("stemWidth",               StyleValueType.ST_SPATIUM),
      StyleType("shortenStem",             StyleValueType.ST_BOOL),       
      StyleType("shortStemProgression",    StyleValueType.ST_SPATIUM),     
      StyleType("shortestStem",            StyleValueType.ST_SPATIUM),
      StyleType("beginRepeatLeftMargin",   StyleValueType.ST_SPATIUM),
      StyleType("minNoteDistance",         StyleValueType.ST_SPATIUM),
      StyleType("barNoteDistance",         StyleValueType.ST_SPATIUM),
      StyleType("noteBarDistance",         StyleValueType.ST_SPATIUM),
      StyleType("measureSpacing",          StyleValueType.ST_DOUBLE),
      StyleType("staffLineWidth",          StyleValueType.ST_SPATIUM),
      StyleType("ledgerLineWidth",         StyleValueType.ST_SPATIUM),
      StyleType("akkoladeWidth",           StyleValueType.ST_SPATIUM),
      StyleType("accidentalDistance",      StyleValueType.ST_SPATIUM),
      StyleType("accidentalNoteDistance",  StyleValueType.ST_SPATIUM),
      StyleType("beamWidth",               StyleValueType.ST_SPATIUM),
      StyleType("beamDistance",            StyleValueType.ST_DOUBLE),        
      StyleType("beamMinLen",              StyleValueType.ST_SPATIUM),        
      StyleType("beamMinSlope",            StyleValueType.ST_DOUBLE),
      StyleType("beamMaxSlope",            StyleValueType.ST_DOUBLE),
      StyleType("maxBeamTicks",            StyleValueType.ST_INT),
      StyleType("dotNoteDistance",         StyleValueType.ST_SPATIUM),
      StyleType("dotRestDistance",         StyleValueType.ST_SPATIUM),
      StyleType("dotDotDistance",          StyleValueType.ST_SPATIUM),
      StyleType("propertyDistanceHead",    StyleValueType.ST_SPATIUM),  
      StyleType("propertyDistanceStem",    StyleValueType.ST_SPATIUM),     
      StyleType("propertyDistance",        StyleValueType.ST_SPATIUM),   
      StyleType("pageFillLimit",           StyleValueType.ST_DOUBLE), 
      StyleType("lastSystemFillLimit",     StyleValueType.ST_DOUBLE),
      StyleType("hairpinHeight",           StyleValueType.ST_SPATIUM),
      StyleType("hairpinContHeight",       StyleValueType.ST_SPATIUM),
      StyleType("hairpinWidth",            StyleValueType.ST_SPATIUM),
      StyleType("showPageNumber",          StyleValueType.ST_BOOL),
      StyleType("showPageNumberOne",       StyleValueType.ST_BOOL),
      StyleType("pageNumberOddEven",       StyleValueType.ST_BOOL),
      StyleType("showMeasureNumber",       StyleValueType.ST_BOOL),
      StyleType("showMeasureNumberOne",    StyleValueType.ST_BOOL),
      StyleType("measureNumberInterval",   StyleValueType.ST_INT),
      StyleType("measureNumberSystem",     StyleValueType.ST_BOOL),
      StyleType("measureNumberAllStaffs",  StyleValueType.ST_BOOL),
      StyleType("smallNoteMag",            StyleValueType.ST_DOUBLE),
      StyleType("graceNoteMag",            StyleValueType.ST_DOUBLE),
      StyleType("smallStaffMag",           StyleValueType.ST_DOUBLE),
      StyleType("smallClefMag",            StyleValueType.ST_DOUBLE),
      StyleType("genClef",                 StyleValueType.ST_BOOL),         
      StyleType("genKeysig",               StyleValueType.ST_BOOL),     
      StyleType("genTimesig",              StyleValueType.ST_BOOL),
      StyleType("genCourtesyTimesig",      StyleValueType.ST_BOOL),
      StyleType("genCourtesyKeysig",       StyleValueType.ST_BOOL),
      StyleType("useGermanNoteNames",      StyleValueType.ST_BOOL),
      StyleType("chordDescriptionFile",    StyleValueType.ST_STRING),
      StyleType("concertPitch",            StyleValueType.ST_BOOL),         
      StyleType("createMultiMeasureRests", StyleValueType.ST_BOOL),
      StyleType("minEmptyMeasures",        StyleValueType.ST_INT),      
      StyleType("minMMRestWidth",          StyleValueType.ST_SPATIUM),      
      StyleType("hideEmptyStaves",         StyleValueType.ST_BOOL),
      StyleType("stemDir1",                StyleValueType.ST_DIRECTION),
      StyleType("stemDir2",                StyleValueType.ST_DIRECTION),
      StyleType("stemDir3",                StyleValueType.ST_DIRECTION),
      StyleType("stemDir4",                StyleValueType.ST_DIRECTION),
      StyleType("gateTime",                StyleValueType.ST_INT),
      StyleType("tenutoGateTime",          StyleValueType.ST_INT),
      StyleType("staccatoGateTime",        StyleValueType.ST_INT),
      StyleType("slurGateTime",            StyleValueType.ST_INT),
      StyleType("UfermataAnchor",          StyleValueType.ST_INT),
      StyleType("DfermataAnchor",          StyleValueType.ST_INT),
      StyleType("UshortfermataAnchor",     StyleValueType.ST_INT),
      StyleType("DshortfermataAnchor",     StyleValueType.ST_INT),
      StyleType("UlongfermataAnchor",      StyleValueType.ST_INT),
      StyleType("DlongfermataAnchor",      StyleValueType.ST_INT),
      StyleType("UverylongfermataAnchor",  StyleValueType.ST_INT),
      StyleType("DverylongfermataAnchor",  StyleValueType.ST_INT),
      StyleType("ThumbAnchor",             StyleValueType.ST_INT),
      StyleType("SforzatoaccentAnchor",    StyleValueType.ST_INT),
      StyleType("EspressivoAnchor",        StyleValueType.ST_INT),
      StyleType("StaccatoAnchor",          StyleValueType.ST_INT),
      StyleType("UstaccatissimoAnchor",    StyleValueType.ST_INT),
      StyleType("DstaccatissimoAnchor",    StyleValueType.ST_INT),
      StyleType("TenutoAnchor",            StyleValueType.ST_INT),
      StyleType("UportatoAnchor",          StyleValueType.ST_INT),
      StyleType("DportatoAnchor",          StyleValueType.ST_INT),
      StyleType("UmarcatoAnchor",          StyleValueType.ST_INT),
      StyleType("DmarcatoAnchor",          StyleValueType.ST_INT),
      StyleType("OuvertAnchor",            StyleValueType.ST_INT),
      StyleType("PlusstopAnchor",          StyleValueType.ST_INT),
      StyleType("UpbowAnchor",             StyleValueType.ST_INT),
      StyleType("DownbowAnchor",           StyleValueType.ST_INT),
      StyleType("ReverseturnAnchor",       StyleValueType.ST_INT),
      StyleType("TurnAnchor",              StyleValueType.ST_INT),
      StyleType("TrillAnchor",             StyleValueType.ST_INT),
      StyleType("PrallAnchor",             StyleValueType.ST_INT),
      StyleType("MordentAnchor",           StyleValueType.ST_INT),
      StyleType("PrallPrallAnchor",        StyleValueType.ST_INT),
      StyleType("PrallMordentAnchor",      StyleValueType.ST_INT),
      StyleType("UpPrallAnchor",           StyleValueType.ST_INT),
      StyleType("DownPrallAnchor",         StyleValueType.ST_INT),
      StyleType("UpMordentAnchor",         StyleValueType.ST_INT),
      StyleType("DownMordentAnchor",       StyleValueType.ST_INT),
      StyleType("SnappizzicatorAnchor",    StyleValueType.ST_INT),
      StyleType("ArpeggioNoteDistance",    StyleValueType.ST_SPATIUM),
      StyleType("ArpeggioLineWidth",       StyleValueType.ST_SPATIUM),
      StyleType("ArpeggioHookLen",         StyleValueType.ST_SPATIUM),
      StyleType("FixMeasureNumbers",     StyleValueType.ST_INT),
      StyleType("FixMeasureWidth",       StyleValueType.ST_BOOL)
    ]

ff = QString("Times New Roman")
def MM(x):
    return x/INCH
OA = OffsetType.OFFSET_ABS
OS = OffsetType.OFFSET_SPATIUM
defaultTextStyleArray = [
      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Symbols1"), QString("MScore"), 20, False, False, False, AlignmentFlags.ALIGN_LEFT),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Symbols3"), QString("MScore"), 14, False, False, False, AlignmentFlags.ALIGN_LEFT),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Title"), ff, 24, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, 0, OA, 50, 0),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Subtitle"), ff, 14, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, MM(10), OA, 50, 0),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Composer"), ff, 12, False, False, False, AlignmentFlags.ALIGN_RIGHT | AlignmentFlags.ALIGN_BOTTOM, 0, 0, OA, 100, 100),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Poet"), ff, 12, False, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BOTTOM, 0, 0, OA, 0, 100),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Lyrics odd lines"), ff, 11, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, 7, OS, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Lyrics even lines"), ff, 11, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, 7, OS, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Fingering"), ff,  8, False, False, False, AlignmentFlags.ALIGN_CENTER, 0.0, 0.0, OA, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "InstrumentsLong"),   ff, 12, False, False, False, AlignmentFlags.ALIGN_RIGHT | AlignmentFlags.ALIGN_VCENTER, 0.0, 0.0, OA, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "InstrumentsShort"),   ff, 12, False, False, False, AlignmentFlags.ALIGN_RIGHT | AlignmentFlags.ALIGN_VCENTER, 0.0, 0.0, OA, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "InstrumentsExcerpt"), ff, 18, False, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BOTTOM, 0.0, 0.0, OA, 0, 100),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Dynamics"), ff, 12, False, True, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BASELINE, 0.0, 8.0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Technik"), ff, 12, False, True, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BASELINE, 0.0, -2.0, OS),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Tempo"), ff, 12, True, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BASELINE, 0, -4.0, OS, 0, 0, True, .0, .0, 0, Qt.black, False, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Metronome"), ff, 12, True, False, False, AlignmentFlags.ALIGN_LEFT),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Copyright"), ff, 8, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, MM(-15), OA, 50.0, 100.0),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Measure Number"), ff, 8, False, False, False, AlignmentFlags.ALIGN_CENTER | AlignmentFlags.ALIGN_BOTTOM, 0.0, 0.0, OS, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Page Number Odd"), ff, 12, False, False, False, AlignmentFlags.ALIGN_RIGHT | AlignmentFlags.ALIGN_BASELINE, MM(-10), MM(-10), OA, 100.0, 100.0),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Page Number Even"), ff, 12, False, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BASELINE, MM(10), MM(-10), OA, 0.0, 100.0),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Translator"), ff, 11, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_TOP, 0, 6),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Tuplets"), ff,  8, False, False, False, AlignmentFlags.ALIGN_CENTER, 0.0,  0.0, OS, 0.0, 0.0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "System"), ff,  10, False, False, False, AlignmentFlags.ALIGN_LEFT, 0, -4.0, OS, 0, 0, True, 0.0, 0.0, 25, Qt.black, False, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Staff"), ff,  10, False, False, False, AlignmentFlags.ALIGN_LEFT, 0, -4.0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Chordname"), ff,  12, False, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_BASELINE, 0, -4.0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Rehearsal Mark"), ff,  14, True, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_BASELINE, 0, -3.0, OS, 0, 0, True,\
        0.3, 1.0, 20, Qt.black, False, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Repeat Text"), ff,  12, False, False, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_BASELINE, 0, -2.0, OS, 100, 0, True,\
         0.0, 0.0, 25, Qt.black, False, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Volta"), ff, 11, True, False, False, AlignmentFlags.ALIGN_LEFT, 0.5, .0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Frame"), ff, 11, False, False, False, AlignmentFlags.ALIGN_LEFT, 0, 0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "TextLine"), ff,  12, False, False, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_VCENTER, 0, 0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Glissando"), ff, 8, False, True, False, AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_BASELINE, 0.0, 0.0, OS, 0, 0, True),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "String Number"), ff,  8, False, False, False,\
        AlignmentFlags.ALIGN_CENTER, 0, -5.0, OS, 100, 0, True, 0.2, -0.2, 0, Qt.black, True, False),

      TextStyle(QT_TRANSLATE_NOOP("MuseScore", "Ottava"), ff, 12, False, True, False, AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_VCENTER, 0.0, 0.0, OS, 0, 0, True)
]

class StyleVal:

    def __init__(self, t, val):
        self.idx = t
        self.v = val

class Spatium:

    def __init__(self, val):
        self._val = val

class Style(StyleVal):

    def __init__(self):
        
        self.values = [
            StyleVal(StyleIdx.ST_staffUpperBorder, Spatium(7.0)),
            StyleVal(StyleIdx.ST_staffLowerBorder, Spatium(7.0)),
            StyleVal(StyleIdx.ST_staffDistance, Spatium(6.5)),
            StyleVal(StyleIdx.ST_akkoladeDistance, Spatium(6.5)),
            StyleVal(StyleIdx.ST_systemDistance, Spatium(9.25)),
            StyleVal(StyleIdx.ST_lyricsDistance, Spatium(2)),
            StyleVal(StyleIdx.ST_lyricsMinBottomDistance, Spatium(2)),
            StyleVal(StyleIdx.ST_systemFrameDistance, Spatium(7.0)),
            StyleVal(StyleIdx.ST_frameSystemDistance, Spatium(1.0)),
            StyleVal(StyleIdx.ST_minMeasureWidth, Spatium(4.0)),
            StyleVal(StyleIdx.ST_barWidth, Spatium(0.16)),           
            StyleVal(StyleIdx.ST_doubleBarWidth, Spatium(0.16)),
            StyleVal(StyleIdx.ST_endBarWidth, Spatium(0.3)),         
            StyleVal(StyleIdx.ST_doubleBarDistance, Spatium(0.30)),
            StyleVal(StyleIdx.ST_endBarDistance, Spatium(0.30)),
            StyleVal(StyleIdx.ST_repeatBarTips, False),
            StyleVal(StyleIdx.ST_startBarlineSingle, False),
            StyleVal(StyleIdx.ST_startBarlineMultiple, True),
            StyleVal(StyleIdx.ST_bracketWidth, Spatium(0.35)),
            StyleVal(StyleIdx.ST_bracketDistance, Spatium(0.25)),
            StyleVal(StyleIdx.ST_clefLeftMargin, Spatium(0.5)),
            StyleVal(StyleIdx.ST_keysigLeftMargin, Spatium(0.5)),
            StyleVal(StyleIdx.ST_timesigLeftMargin, Spatium(0.5)),
            StyleVal(StyleIdx.ST_clefKeyRightMargin, Spatium(1.75)),
            StyleVal(StyleIdx.ST_clefBarlineDistance, Spatium(0.18)),  
            StyleVal(StyleIdx.ST_stemWidth, Spatium(0.13)),         
            StyleVal(StyleIdx.ST_shortenStem, True),
            StyleVal(StyleIdx.ST_shortStemProgression, Spatium(0.25)),
            StyleVal(StyleIdx.ST_shortestStem,Spatium(2.25)),
            StyleVal(StyleIdx.ST_beginRepeatLeftMargin,Spatium(1.0)),
            StyleVal(StyleIdx.ST_minNoteDistance,Spatium(0.4)),
            StyleVal(StyleIdx.ST_barNoteDistance,Spatium(1.2)),
            StyleVal(StyleIdx.ST_noteBarDistance,Spatium(1.0)),
            StyleVal(StyleIdx.ST_measureSpacing,1.2),
            StyleVal(StyleIdx.ST_staffLineWidth,Spatium(0.08)),  
            StyleVal(StyleIdx.ST_ledgerLineWidth,Spatium(0.12)),    
            StyleVal(StyleIdx.ST_akkoladeWidth,Spatium(1.6)),
            StyleVal(StyleIdx.ST_accidentalDistance,Spatium(0.22)),
            StyleVal(StyleIdx.ST_accidentalNoteDistance,Spatium(0.22)),
            StyleVal(StyleIdx.ST_beamWidth,Spatium(0.48)),
            StyleVal(StyleIdx.ST_beamDistance,0.5),
            StyleVal(StyleIdx.ST_beamMinLen,Spatium(1.25)),
            StyleVal(StyleIdx.ST_beamMinSlope,0.05),
            StyleVal(StyleIdx.ST_beamMaxSlope,0.2),
            StyleVal(StyleIdx.ST_maxBeamTicks, 480),
            StyleVal(StyleIdx.ST_dotNoteDistance,Spatium(0.35)),
            StyleVal(StyleIdx.ST_dotRestDistance,Spatium(0.25)),
            StyleVal(StyleIdx.ST_dotDotDistance,Spatium(0.5)),
            StyleVal(StyleIdx.ST_propertyDistanceHead,Spatium(1.0)),
            StyleVal(StyleIdx.ST_propertyDistanceStem,Spatium(0.5)),
            StyleVal(StyleIdx.ST_propertyDistance,Spatium(1.0)),
            StyleVal(StyleIdx.ST_pageFillLimit,0.7),
            StyleVal(StyleIdx.ST_lastSystemFillLimit,0.3),
            StyleVal(StyleIdx.ST_hairpinHeight,Spatium(1.2)),
            StyleVal(StyleIdx.ST_hairpinContHeight,Spatium(0.5)),
            StyleVal(StyleIdx.ST_hairpinWidth,Spatium(0.13)),
            StyleVal(StyleIdx.ST_showPageNumber,True),
            StyleVal(StyleIdx.ST_showPageNumberOne,False),
            StyleVal(StyleIdx.ST_pageNumberOddEven,True),
            StyleVal(StyleIdx.ST_showMeasureNumber,True),
            StyleVal(StyleIdx.ST_showMeasureNumberOne,False),
            StyleVal(StyleIdx.ST_measureNumberInterval,5),
            StyleVal(StyleIdx.ST_measureNumberSystem,True),
            StyleVal(StyleIdx.ST_measureNumberAllStaffs,False),
            StyleVal(StyleIdx.ST_smallNoteMag,0.7),
            StyleVal(StyleIdx.ST_graceNoteMag,0.7),
            StyleVal(StyleIdx.ST_smallStaffMag,0.7),
            StyleVal(StyleIdx.ST_smallClefMag,0.8),
            StyleVal(StyleIdx.ST_genClef,True),
            StyleVal(StyleIdx.ST_genKeysig,True),
            StyleVal(StyleIdx.ST_genTimesig,True),
            StyleVal(StyleIdx.ST_genCourtesyTimesig, True),
            StyleVal(StyleIdx.ST_genCourtesyKeysig, True),
            StyleVal(StyleIdx.ST_useGermanNoteNames, False),
            StyleVal(StyleIdx.ST_chordDescriptionFile, QString("stdchords.xml")),
            StyleVal(StyleIdx.ST_concertPitch, False),
            StyleVal(StyleIdx.ST_createMultiMeasureRests, False),
            StyleVal(StyleIdx.ST_minEmptyMeasures, 2),
            StyleVal(StyleIdx.ST_minMMRestWidth, Spatium(4)),
            StyleVal(StyleIdx.ST_hideEmptyStaves, False),
            StyleVal(StyleIdx.ST_stemDir1, Direction.UP),
            StyleVal(StyleIdx.ST_stemDir2, Direction.DOWN),
            StyleVal(StyleIdx.ST_stemDir3, Direction.UP),
            StyleVal(StyleIdx.ST_stemDir4, Direction.DOWN),
            StyleVal(StyleIdx.ST_gateTime, 100),
            StyleVal(StyleIdx.ST_tenutoGateTime, 100),
            StyleVal(StyleIdx.ST_staccatoGateTime, 50),
            StyleVal(StyleIdx.ST_slurGateTime, 100),
            StyleVal(StyleIdx.ST_UfermataAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DfermataAnchor, int(ArticulationAnchor.A_BOTTOM_STAFF)),
            StyleVal(StyleIdx.ST_UshortfermataAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DshortfermataAnchor, int(ArticulationAnchor.A_BOTTOM_STAFF)),
            StyleVal(StyleIdx.ST_UlongfermataAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DlongfermataAnchor, int(ArticulationAnchor.A_BOTTOM_STAFF)),
            StyleVal(StyleIdx.ST_UverylongfermataAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DverylongfermataAnchor, int(ArticulationAnchor.A_BOTTOM_STAFF)),
            StyleVal(StyleIdx.ST_ThumbAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_SforzatoaccentAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_EspressivoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_StaccatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_UstaccatissimoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_DstaccatissimoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_TenutoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_UportatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_DportatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_UmarcatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_DmarcatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_OuvertAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_PlusstopAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_UpbowAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DownbowAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_ReverseturnAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_TurnAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_TrillAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_PrallAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_MordentAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_PrallPrallAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_PrallMordentAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_UpPrallAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DownPrallAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_UpMordentAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_DownMordentAnchor, int(ArticulationAnchor.A_TOP_STAFF)),
            StyleVal(StyleIdx.ST_SnappizzicatoAnchor, int(ArticulationAnchor.A_CHORD)),
            StyleVal(StyleIdx.ST_ArpeggioNoteDistance, Spatium(.5)),
            StyleVal(StyleIdx.ST_ArpeggioLineWidth, Spatium(.18)),
            StyleVal(StyleIdx.ST_ArpeggioHookLen, Spatium(.8)),
            StyleVal(StyleIdx.ST_FixMeasureNumbers, 0),
            StyleVal(StyleIdx.ST_FixMeasureWidth, False)
            ]

defaultStyle = Style()

        
