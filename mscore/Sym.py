#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Preferences import *
import GL
from Xml import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtXml import *

def symToHtml(s, leftMargin):
    leftMargin = int((leftMargin * GL.PDPI) / GL.DPI)
    size    = s.font().pixelSize() * 72.0 / GL.DPI
    family = s.font().family()
    return QString(
      "<data>"
        "<html>"
          "<head>"
            "<meta name=\"qrichtext\" content=\"1\" >"
            "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf8\" />"
            "<style type=\"text/css\">"
              "p, li { white-space: pre-wrap; }"
              "</style>"
            "</head>"
          "<body style=\" font-family:'%1'; font-size:%2pt;\">"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:%3px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                "&#%4;"
              "</p>"
            "</body>"
          "</html>"
      "</data>").arg(family).arg(size).arg(leftMargin).arg(s.code().unicode())

def symToHtml1(s1, s2, leftMargin):
    leftMargin = (leftMargin * GL.PDPI) / GL.DPI

    f        = s1.font()
    size    = s1.font().pixelSize() * 72.0 / GL.DPI
    family = f.family()

    return QString(
      "<data>"
        "<html>"
          "<head>"
            "<meta name=\"qrichtext\" content=\"1\" >"
            "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf8\" />"
            "<style type=\"text/css\">"
              "p, li { white-space: pre-wrap; }"
              "</style>"
            "</head>"
          "<body style=\" font-family:'%1'; font-size:%2pt;\">"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:%3px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                "&#%4;&#%5;"
              "</p>"
            "</body>"
          "</html>"
      "</data>").arg(family).arg(size).arg(leftMargin).arg(s1.code().unicode()).arg(s2.code().unicode())

class SymName:
    clefEightSym =	0
    clefOneSym =	1
    clefFiveSym =	2
    wholerestSym =	3
    halfrestSym =	4
    outsidewholerestSym =	5
    outsidehalfrestSym =	6
    longarestSym =	7
    breverestSym =	8
    rest4Sym =	9
    rest8Sym =	10
    clasquartrestSym =	11
    rest16Sym =	12
    rest32Sym =	13
    rest64Sym =	14
    rest128Sym =	15
    rest_M3 =	16
    varcodaSym =	17
    brackettipsRightUp =	18
    brackettipsRightDown =	19
    brackettipsLeftUp =	20
    brackettipsLeftDown =	21
    zeroSym =	22
    oneSym =	23
    twoSym =	24
    threeSym =	25
    fourSym =	26
    fiveSym =	27
    sixSym =	28
    sevenSym =	29
    eightSym =	30
    nineSym =	31
    sharpSym =	32
    sharpArrowUpSym =	33
    sharpArrowDownSym =	34
    sharpArrowBothSym =	35
    sharpslashSym =	36
    sharpslash2Sym =	37
    sharpslash3Sym =	38
    sharpslash4Sym =	39
    naturalSym =	40
    naturalArrowUpSym =	41
    naturalArrowDownSym =	42
    naturalArrowBothSym =	43
    flatSym =	44
    flatArrowUpSym =	45
    flatArrowDownSym =	46
    flatArrowBothSym =	47
    flatslashSym =	48
    flatslash2Sym =	49
    mirroredflat2Sym =	50
    mirroredflatSym =	51
    mirroredflatslashSym =	52
    flatflatSym =	53
    flatflatslashSym =	54
    sharpsharpSym =	55
    soriSym =	56
    koronSym =	57
    rightparenSym =	58
    leftparenSym =	59
    dotSym =	60
    longaupSym =	61
    longadownSym =	62
    brevisheadSym =	63
    brevisdoubleheadSym =	64
    wholeheadSym =	65
    halfheadSym =	66
    quartheadSym =	67
    wholediamondheadSym =	68
    halfdiamondheadSym =	69
    diamondheadSym =	70
    s0triangleHeadSym =	71
    d1triangleHeadSym =	72
    u1triangleHeadSym =	73
    u2triangleHeadSym =	74
    d2triangleHeadSym =	75
    wholeslashheadSym =	76
    halfslashheadSym =	77
    quartslashheadSym =	78
    wholecrossedheadSym =	79
    halfcrossedheadSym =	80
    crossedheadSym =	81
    xcircledheadSym =	82
    s0doHeadSym =	83
    d1doHeadSym =	84
    u1doHeadSym =	85
    d2doHeadSym =	86
    u2doHeadSym =	87
    s0reHeadSym =	88
    u1reHeadSym =	89
    d1reHeadSym =	90
    u2reHeadSym =	91
    d2reHeadSym =	92
    s0miHeadSym =	93
    s1miHeadSym =	94
    s2miHeadSym =	95
    u0faHeadSym =	96
    d0faHeadSym =	97
    u1faHeadSym =	98
    d1faHeadSym =	99
    u2faHeadSym =	100
    d2faHeadSym =	101
    s0laHeadSym =	102
    s1laHeadSym =	103
    s2laHeadSym =	104
    s0tiHeadSym =	105
    u1tiHeadSym =	106
    d1tiHeadSym =	107
    u2tiHeadSym =	108
    d2tiHeadSym =	109
    s0solHeadSym =	110
    s1solHeadSym =	111
    s2solHeadSym =	112
    ufermataSym =	113
    dfermataSym =	114
    snappizzicatoSym =	115
    thumbSym =	116
    ushortfermataSym =	117
    dshortfermataSym =	118
    ulongfermataSym =	119
    dlongfermataSym =	120
    uverylongfermataSym =	121
    dverylongfermataSym =	122
    sforzatoaccentSym =	123
    esprSym =	124
    staccatoSym =	125
    ustaccatissimoSym =	126
    dstaccatissimoSym =	127
    tenutoSym =	128
    uportatoSym =	129
    dportatoSym =	130
    umarcatoSym =	131
    dmarcatoSym =	132
    ouvertSym =	133
    plusstopSym =	134
    upbowSym =	135
    downbowSym =	136
    reverseturnSym =	137
    turnSym =	138
    trillSym =	139
    upedalheelSym =	140
    dpedalheelSym =	141
    upedaltoeSym =	142
    dpedaltoeSym =	143
    flageoletSym =	144
    segnoSym =	145
    codaSym =	146
    rcommaSym =	147
    lcommaSym =	148
    arpeggioSym =	149
    trillelementSym =	150
    arpeggioarrowdownSym =	151
    arpeggioarrowupSym =	152
    trilelementSym =	153
    prallSym =	154
    mordentSym =	155
    prallprallSym =	156
    prallmordentSym =	157
    upprallSym =	158
    downprallSym =	159
    upmordentSym =	160
    downmordentSym =	161
    lineprallSym =	162
    pralldownSym =	163
    prallupSym =	164
    caesuraCurvedSym =	165
    caesuraStraight =	166
    eighthflagSym =	167
    sixteenthflagSym =	168
    thirtysecondflagSym =	169
    sixtyfourthflagSym =	170
    flag128Sym =	171
    deighthflagSym =	172
    gracedashSym =	173
    dgracedashSym =	174
    dsixteenthflagSym =	175
    dthirtysecondflagSym =	176
    dsixtyfourthflagSym =	177
    dflag128Sym =	178
    altoclefSym =	179
    caltoclefSym =	180
    bassclefSym =	181
    cbassclefSym =	182
    trebleclefSym =	183
    ctrebleclefSym =	184
    percussionclefSym =	185
    cpercussionclefSym =	186
    tabclefSym =	187
    ctabclefSym =	188
    fourfourmeterSym =	189
    allabreveSym =	190
    pedalasteriskSym =	191
    pedaldashSym =	192
    pedaldotSym =	193
    pedalPSym =	194
    pedaldSym =	195
    pedaleSym =	196
    pedalPedSym =	197
    accDiscantSym =	198
    accDotSym =	199
    accFreebaseSym =	200
    accStdbaseSym =	201
    accBayanbaseSym =	202
    accOldEESym =	203
    letterfSym =	204
    lettermSym =	205
    letterpSym =	206
    letterrSym =	207
    lettersSym =	208
    letterzSym =	209
    plusSym =	210
    note2Sym =	211
    note4Sym =	212
    note8Sym =	213
    note16Sym =	214
    note32Sym =	215
    note64Sym =	216
    dotdotSym =	217
    longaupaltSym =	218
    longadownaltSym =	219
    brevisheadaltSym =	220
    timesigcdotSym =	221
    timesigoSym =	222
    timesigocutSym =	223
    timesigodotSym =	224
    lastSym =	225

lilypondNames = {
SymName.wholerestSym:         [ QT_TRANSLATE_NOOP("symbol", "whole rest"),           "rests.0" ],
SymName.halfrestSym:          [ QT_TRANSLATE_NOOP("symbol", "half rest"),            "rests.1" ],
SymName.outsidewholerestSym:  [ QT_TRANSLATE_NOOP("symbol", "outside whole rest"),   "rests.0o" ],
SymName.outsidehalfrestSym:   [ QT_TRANSLATE_NOOP("symbol", "outside half rest"),    "rests.1o" ],
SymName.rest_M3:              [ QT_TRANSLATE_NOOP("symbol", "rest M3"),              "rests.M3" ],
SymName.breverestSym:         [ QT_TRANSLATE_NOOP("symbol", "breve rest"),           "rests.M1" ],
SymName.longarestSym:         [ QT_TRANSLATE_NOOP("symbol", "longa rest"),           "rests.M2" ],
SymName.rest4Sym:             [ QT_TRANSLATE_NOOP("symbol", "quart rest"),           "rests.2" ],
SymName.clasquartrestSym:     [ QT_TRANSLATE_NOOP("symbol", "clas quart rest"),      "rests.2classical" ],
SymName.rest8Sym:             [ QT_TRANSLATE_NOOP("symbol", "eight rest"),           "rests.3" ],
SymName.rest16Sym:            [ QT_TRANSLATE_NOOP("symbol", "16' rest"),             "rests.4" ],
SymName.rest32Sym:            [ QT_TRANSLATE_NOOP("symbol", "32' rest"),             "rests.5" ],
SymName.rest64Sym:            [ QT_TRANSLATE_NOOP("symbol", "64' rest"),             "rests.6" ],
SymName.rest128Sym:           [ QT_TRANSLATE_NOOP("symbol", "128' rest"),            "rests.7" ],
SymName.sharpSym:             [ QT_TRANSLATE_NOOP("symbol", "sharp"),                "accidentals.sharp" ],
SymName.sharpArrowUpSym:      [ QT_TRANSLATE_NOOP("symbol", "sharp arrow up"),       "accidentals.sharp.arrowup" ],
SymName.sharpArrowDownSym:    [ QT_TRANSLATE_NOOP("symbol", "sharp arrow both"),     "accidentals.sharp.arrowdown" ],
SymName.sharpArrowBothSym:    [ QT_TRANSLATE_NOOP("symbol", "sharp arrow both"),     "accidentals.sharp.arrowboth" ],
SymName.sharpslashSym:        [ QT_TRANSLATE_NOOP("symbol", "sharp slash"),          "accidentals.sharp.slashslash.stem" ],
SymName.sharpslash2Sym:       [ QT_TRANSLATE_NOOP("symbol", "sharp slash2"),         "accidentals.sharp.slashslashslash.stemstem" ],
SymName.sharpslash3Sym:       [ QT_TRANSLATE_NOOP("symbol", "sharp slash3"),         "accidentals.sharp.slashslashslash.stem" ],
SymName.sharpslash4Sym:       [ QT_TRANSLATE_NOOP("symbol", "sharp slash4"),         "accidentals.sharp.slashslash.stemstemstem" ],
SymName.naturalSym:           [ QT_TRANSLATE_NOOP("symbol", "natural"),              "accidentals.natural" ],
SymName.naturalArrowUpSym:    [ QT_TRANSLATE_NOOP("symbol", "natural arrow up"),     "accidentals.natural.arrowup" ],
SymName.naturalArrowDownSym:  [ QT_TRANSLATE_NOOP("symbol", "natural arrow down"),   "accidentals.natural.arrowdown" ],
SymName.naturalArrowBothSym:  [ QT_TRANSLATE_NOOP("symbol", "natural arrow both"),   "accidentals.natural.arrowboth" ],
SymName.flatSym:              [ QT_TRANSLATE_NOOP("symbol", "flat"),                 "accidentals.flat" ],
SymName.flatArrowUpSym:       [ QT_TRANSLATE_NOOP("symbol", "flat arrow up"),        "accidentals.flat.arrowup" ],
SymName.flatArrowDownSym:     [ QT_TRANSLATE_NOOP("symbol", "flat arrow both"),      "accidentals.flat.arrowdown" ],
SymName.flatArrowBothSym:     [ QT_TRANSLATE_NOOP("symbol", "flat arrow both"),      "accidentals.flat.arrowboth" ],
SymName.flatslashSym:         [ QT_TRANSLATE_NOOP("symbol", "flat slash"),           "accidentals.flat.slash" ],
SymName.flatslash2Sym:        [ QT_TRANSLATE_NOOP("symbol", "flat slash2"),          "accidentals.flat.slashslash" ],
SymName.mirroredflat2Sym:     [ QT_TRANSLATE_NOOP("symbol", "mirrored flat2"),       "accidentals.mirroredflat.flat" ],
SymName.mirroredflatSym:      [ QT_TRANSLATE_NOOP("symbol", "mirrored flat"),        "accidentals.mirroredflat" ],
SymName.mirroredflatslashSym: [ QT_TRANSLATE_NOOP("symbol", "mirrored flat slash"),  "accidentals.mirroredflat.backslash" ],
SymName.flatflatSym:          [ QT_TRANSLATE_NOOP("symbol", "flat flat"),            "accidentals.flatflat" ],
SymName.flatflatslashSym:     [ QT_TRANSLATE_NOOP("symbol", "flat flat slash"),      "accidentals.flatflat.slash" ],
SymName.sharpsharpSym:        [ QT_TRANSLATE_NOOP("symbol", "sharp sharp"),          "accidentals.doublesharp" ],
SymName.soriSym:              [ QT_TRANSLATE_NOOP("symbol", "sori"),                 "accidentals.sori" ],
SymName.koronSym:             [ QT_TRANSLATE_NOOP("symbol", "koron"),                "accidentals.koron" ],
SymName.rightparenSym:        [ QT_TRANSLATE_NOOP("symbol", "right parenthesis"),    "accidentals.rightparen" ],
SymName.leftparenSym:         [ QT_TRANSLATE_NOOP("symbol", "left parenthesis"),     "accidentals.leftparen" ],
SymName.dotSym:               [ QT_TRANSLATE_NOOP("symbol", "dot"),                  "dots.dot" ],
SymName.longaupSym:           [ QT_TRANSLATE_NOOP("symbol", "longa up"),             "noteheads.uM2" ],
SymName.longadownSym:         [ QT_TRANSLATE_NOOP("symbol", "longa down"),           "noteheads.dM2" ],
SymName.brevisheadSym:        [ QT_TRANSLATE_NOOP("symbol", "brevis head"),          "noteheads.sM1" ],
SymName.brevisdoubleheadSym:  [ QT_TRANSLATE_NOOP("symbol", "brevis double head"),   "noteheads.sM1double" ],
SymName.wholeheadSym:         [ QT_TRANSLATE_NOOP("symbol", "whole head"),           "noteheads.s0" ],
SymName.halfheadSym:          [ QT_TRANSLATE_NOOP("symbol", "half head"),            "noteheads.s1" ],
SymName.quartheadSym:         [ QT_TRANSLATE_NOOP("symbol", "quart head"),           "noteheads.s2" ],
SymName.wholediamondheadSym:  [ QT_TRANSLATE_NOOP("symbol", "whole diamond head"),   "noteheads.s0diamond" ],
SymName.halfdiamondheadSym:   [ QT_TRANSLATE_NOOP("symbol", "half diamond head"),    "noteheads.s1diamond" ],
SymName.diamondheadSym:       [ QT_TRANSLATE_NOOP("symbol", "diamond head"),         "noteheads.s2diamond" ],
SymName.s0triangleHeadSym:    [ QT_TRANSLATE_NOOP("symbol", "whole triangle head"),  "noteheads.s0triangle" ],
SymName.d1triangleHeadSym:    [ QT_TRANSLATE_NOOP("symbol", "down half triangle head"), "noteheads.d1triangle" ],
SymName.u1triangleHeadSym:    [ QT_TRANSLATE_NOOP("symbol", "up half triangle head"), "noteheads.u1triangle" ],
SymName.u2triangleHeadSym:    [ QT_TRANSLATE_NOOP("symbol", "up quart triangle head"), "noteheads.u2triangle" ],
SymName.d2triangleHeadSym:    [ QT_TRANSLATE_NOOP("symbol", "down quart triangle head"), "noteheads.d2triangle" ],
SymName.wholeslashheadSym:    [ QT_TRANSLATE_NOOP("symbol", "whole slash head"),     "noteheads.s0slash" ],
SymName.halfslashheadSym:     [ QT_TRANSLATE_NOOP("symbol", "half slash head"),      "noteheads.s1slash" ],
SymName.quartslashheadSym:    [ QT_TRANSLATE_NOOP("symbol", "quart slash head"),     "noteheads.s2slash" ],
SymName.wholecrossedheadSym:  [ QT_TRANSLATE_NOOP("symbol", "whole cross head"),     "noteheads.s0cross" ],
SymName.halfcrossedheadSym:   [ QT_TRANSLATE_NOOP("symbol", "half cross head"),      "noteheads.s1cross" ],
SymName.crossedheadSym:       [ QT_TRANSLATE_NOOP("symbol", "cross head"),           "noteheads.s2cross" ],
SymName.xcircledheadSym:      [ QT_TRANSLATE_NOOP("symbol", "x circle head"),        "noteheads.s2xcircle" ],
SymName.s0doHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s0do head"),            "noteheads.s0do" ],
SymName.d1doHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d1do head"),            "noteheads.d1do" ],
SymName.u1doHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u1do head"),            "noteheads.u1do" ],
SymName.d2doHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d2do head"),            "noteheads.d2do" ],
SymName.u2doHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u2do head"),            "noteheads.u2do" ],
SymName.s0reHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s0re head"),            "noteheads.s0re" ],
SymName.u1reHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u1re head"),            "noteheads.u1re" ],
SymName.d1reHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d1re head"),            "noteheads.d1re" ],
SymName.u2reHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u2re head"),            "noteheads.u2re" ],
SymName.d2reHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d2re head"),            "noteheads.d2re" ],
SymName.s0miHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s0mi head"),            "noteheads.s0mi" ],
SymName.s1miHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s1mi head"),            "noteheads.s1mi" ],
SymName.s2miHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s2mi head"),            "noteheads.s2mi" ],
SymName.u0faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u0fa head"),            "noteheads.u0fa" ],
SymName.d0faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d0fa head"),            "noteheads.d0fa" ],
SymName.u1faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u1fa head"),            "noteheads.u1fa" ],
SymName.d1faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d1fa head"),            "noteheads.d1fa" ],
SymName.u2faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u2fa head"),            "noteheads.u2fa" ],
SymName.d2faHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d2fa head"),            "noteheads.d2fa" ],
SymName.s0laHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s0la head"),            "noteheads.s0la" ],
SymName.s1laHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s1la head"),            "noteheads.s1la" ],
SymName.s2laHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s2la head"),            "noteheads.s2la" ],
SymName.s0tiHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "s0ti head"),            "noteheads.s0ti" ],
SymName.u1tiHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u1ti head"),            "noteheads.u1ti" ],
SymName.d1tiHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d1ti head"),            "noteheads.d1ti" ],
SymName.u2tiHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "u2ti head"),            "noteheads.u2ti" ],
SymName.d2tiHeadSym:          [ QT_TRANSLATE_NOOP("symbol", "d2ti head"),            "noteheads.d2ti" ],
SymName.s0solHeadSym:         [ QT_TRANSLATE_NOOP("symbol", "s0sol head"),           "noteheads.s0sol" ],
SymName.s1solHeadSym:         [ QT_TRANSLATE_NOOP("symbol", "s1sol head"),           "noteheads.s1sol" ],
SymName.s2solHeadSym:         [ QT_TRANSLATE_NOOP("symbol", "s2sol head"),           "noteheads.s2sol" ],
SymName.ufermataSym:          [ QT_TRANSLATE_NOOP("symbol", "ufermata"),             "scripts.ufermata" ],
SymName.dfermataSym:          [ QT_TRANSLATE_NOOP("symbol", "dfermata"),             "scripts.dfermata" ],
SymName.snappizzicatoSym:     [ QT_TRANSLATE_NOOP("symbol", "snappizzicato"),        "scripts.snappizzicato" ],
SymName.ushortfermataSym:     [ QT_TRANSLATE_NOOP("symbol", "ushortfermata"),        "scripts.ushortfermata" ],
SymName.dshortfermataSym:     [ QT_TRANSLATE_NOOP("symbol", "dshortfermata"),        "scripts.dshortfermata" ],
SymName.ulongfermataSym:      [ QT_TRANSLATE_NOOP("symbol", "ulongfermata"),         "scripts.ulongfermata" ],
SymName.dlongfermataSym:      [ QT_TRANSLATE_NOOP("symbol", "dlongfermata"),         "scripts.dlongfermata" ],
SymName.uverylongfermataSym:  [ QT_TRANSLATE_NOOP("symbol", "uverylongfermata"),     "scripts.uverylongfermata" ],
SymName.dverylongfermataSym:  [ QT_TRANSLATE_NOOP("symbol", "dverylongfermata"),     "scripts.dverylongfermata" ],
SymName.thumbSym:             [ QT_TRANSLATE_NOOP("symbol", "thumb"),                "scripts.thumb" ],
SymName.sforzatoaccentSym:    [ QT_TRANSLATE_NOOP("symbol", "sforza to accent"),     "scripts.sforzato" ],
SymName.esprSym:              [ QT_TRANSLATE_NOOP("symbol", "espressivo"),           "scripts.espr" ],
SymName.staccatoSym:          [ QT_TRANSLATE_NOOP("symbol", "staccato"),             "scripts.staccato" ],
SymName.ustaccatissimoSym:    [ QT_TRANSLATE_NOOP("symbol", "ustaccatissimo"),       "scripts.ustaccatissimo" ],
SymName.dstaccatissimoSym:    [ QT_TRANSLATE_NOOP("symbol", "dstaccatissimo"),       "scripts.dstaccatissimo" ],
SymName.tenutoSym:            [ QT_TRANSLATE_NOOP("symbol", "tenuto"),               "scripts.tenuto" ],
SymName.uportatoSym:          [ QT_TRANSLATE_NOOP("symbol", "uportato"),             "scripts.uportato" ],
SymName.dportatoSym:          [ QT_TRANSLATE_NOOP("symbol", "dportato"),             "scripts.dportato" ],
SymName.umarcatoSym:          [ QT_TRANSLATE_NOOP("symbol", "umarcato"),             "scripts.umarcato" ],
SymName.dmarcatoSym:          [ QT_TRANSLATE_NOOP("symbol", "dmarcato"),             "scripts.dmarcato" ],
SymName.ouvertSym:            [ QT_TRANSLATE_NOOP("symbol", "ouvert"),               "scripts.open" ],
SymName.plusstopSym:          [ QT_TRANSLATE_NOOP("symbol", "plus stop"),            "scripts.stopped" ],
SymName.upbowSym:             [ QT_TRANSLATE_NOOP("symbol", "up bow"),               "scripts.upbow" ],
SymName.downbowSym:           [ QT_TRANSLATE_NOOP("symbol", "down bow"),             "scripts.downbow" ],
SymName.reverseturnSym:       [ QT_TRANSLATE_NOOP("symbol", "reverse turn"),         "scripts.reverseturn" ],
SymName.turnSym:              [ QT_TRANSLATE_NOOP("symbol", "turn"),                 "scripts.turn"        ],
SymName.trillSym:             [ QT_TRANSLATE_NOOP("symbol", "trill"),                "scripts.trill"       ],
SymName.upedalheelSym:        [ QT_TRANSLATE_NOOP("symbol", "upedal heel"),          "scripts.upedalheel"  ],
SymName.dpedalheelSym:        [ QT_TRANSLATE_NOOP("symbol", "dpedalheel"),          "scripts.dpedalheel"  ],
SymName.upedaltoeSym:         [ QT_TRANSLATE_NOOP("symbol", "upedal toe"),           "scripts.upedaltoe"   ],
SymName.dpedaltoeSym:         [ QT_TRANSLATE_NOOP("symbol", "dpedal toe"),           "scripts.dpedaltoe"   ],
SymName.flageoletSym:         [ QT_TRANSLATE_NOOP("symbol", "flageolet"),            "scripts.flageolet"   ],
SymName.segnoSym:             [ QT_TRANSLATE_NOOP("symbol", "segno"),                "scripts.segno"       ],
SymName.codaSym:              [ QT_TRANSLATE_NOOP("symbol", "coda"),                 "scripts.coda"        ],
SymName.varcodaSym:           [ QT_TRANSLATE_NOOP("symbol", "varied coda"),          "scripts.varcoda"     ],
SymName.rcommaSym:            [ QT_TRANSLATE_NOOP("symbol", "rcomma"),               "scripts.rcomma"      ],
SymName.lcommaSym:            [ QT_TRANSLATE_NOOP("symbol", "lcomma"),               "scripts.lcomma"      ],
SymName.arpeggioSym:          [ QT_TRANSLATE_NOOP("symbol", "arpeggio"),             "scripts.arpeggio" ],
SymName.trillelementSym:      [ QT_TRANSLATE_NOOP("symbol", "trillelement"),         "scripts.trill_element" ],
SymName.arpeggioarrowdownSym: [ QT_TRANSLATE_NOOP("symbol", "arpeggio arrow down"),  "scripts.arpeggio.arrow.M1" ],
SymName.arpeggioarrowupSym:   [ QT_TRANSLATE_NOOP("symbol", "arpeggio arrow up"),    "scripts.arpeggio.arrow.1" ],
SymName.trilelementSym:       [ QT_TRANSLATE_NOOP("symbol", "trill element"),        "scripts.trilelement" ],
SymName.prallSym:             [ QT_TRANSLATE_NOOP("symbol", "prall"),                "scripts.prall" ],
SymName.mordentSym:           [ QT_TRANSLATE_NOOP("symbol", "mordent"),              "scripts.mordent" ],
SymName.prallprallSym:        [ QT_TRANSLATE_NOOP("symbol", "prall prall"),          "scripts.prallprall" ],
SymName.prallmordentSym:      [ QT_TRANSLATE_NOOP("symbol", "prall mordent"),        "scripts.prallmordent" ],
SymName.upprallSym:           [ QT_TRANSLATE_NOOP("symbol", "up prall"),             "scripts.upprall" ],
SymName.upmordentSym:         [ QT_TRANSLATE_NOOP("symbol", "up mordent"),           "scripts.upmordent" ],
SymName.pralldownSym:         [ QT_TRANSLATE_NOOP("symbol", "prall down"),           "scripts.pralldown" ],
SymName.downprallSym:         [ QT_TRANSLATE_NOOP("symbol", "down prall"),           "scripts.downprall" ],
SymName.downmordentSym:       [ QT_TRANSLATE_NOOP("symbol", "down mordent"),         "scripts.downmordent" ],
SymName.prallupSym:           [ QT_TRANSLATE_NOOP("symbol", "prall up"),             "scripts.prallup" ],
SymName.lineprallSym:         [ QT_TRANSLATE_NOOP("symbol", "line prall"),           "scripts.lineprall" ],
SymName.caesuraCurvedSym:     [ QT_TRANSLATE_NOOP("symbol", "caesura curved"),       "scripts.caesura.curved" ],
SymName.caesuraStraight:      [ QT_TRANSLATE_NOOP("symbol", "caesura straight"),     "scripts.caesura.straight" ],
SymName.eighthflagSym:        [ QT_TRANSLATE_NOOP("symbol", "eight flag"),           "flags.u3" ],
SymName.sixteenthflagSym:     [ QT_TRANSLATE_NOOP("symbol", "sixteenth flag"),       "flags.u4" ],
SymName.thirtysecondflagSym:  [ QT_TRANSLATE_NOOP("symbol", "thirtysecond flag"),    "flags.u5" ],
SymName.sixtyfourthflagSym:   [ QT_TRANSLATE_NOOP("symbol", "sixtyfour flag"),       "flags.u6" ],
SymName.flag128Sym:           [ QT_TRANSLATE_NOOP("symbol", "128flag"),              "flags.u7" ],
SymName.deighthflagSym:       [ QT_TRANSLATE_NOOP("symbol", "deight flag"),          "flags.d3" ],
SymName.gracedashSym:         [ QT_TRANSLATE_NOOP("symbol", "grace dash"),           "flags.ugrace" ],
SymName.dgracedashSym:        [ QT_TRANSLATE_NOOP("symbol", "dgrace dash"),          "flags.dgrace" ],
SymName.dsixteenthflagSym:    [ QT_TRANSLATE_NOOP("symbol", "dsixteenth flag"),      "flags.d4" ],
SymName.dthirtysecondflagSym: [ QT_TRANSLATE_NOOP("symbol", "dthirtysecond flag"),   "flags.d5" ],
SymName.dsixtyfourthflagSym:  [ QT_TRANSLATE_NOOP("symbol", "dsixtyfourth flag"),    "flags.d6" ],
SymName.dflag128Sym:          [ QT_TRANSLATE_NOOP("symbol", "d128flag"),             "flags.d7" ],
SymName.altoclefSym:          [ QT_TRANSLATE_NOOP("symbol", "alto clef"),            "clefs.C" ],
SymName.caltoclefSym:         [ QT_TRANSLATE_NOOP("symbol", "calto clef"),           "clefs.C_change" ],
SymName.bassclefSym:          [ QT_TRANSLATE_NOOP("symbol", "bass clef"),            "clefs.F" ],
SymName.cbassclefSym:         [ QT_TRANSLATE_NOOP("symbol", "cbass clef"),           "clefs.F_change" ],
SymName.trebleclefSym:        [ QT_TRANSLATE_NOOP("symbol", "trebleclef"),           "clefs.G" ],
SymName.ctrebleclefSym:       [ QT_TRANSLATE_NOOP("symbol", "ctrebleclef"),          "clefs.G_change" ],
SymName.percussionclefSym:    [ QT_TRANSLATE_NOOP("symbol", "percussion clef"),      "clefs.percussion" ],
SymName.cpercussionclefSym:   [ QT_TRANSLATE_NOOP("symbol", "cpercussion clef"),     "clefs.percussion_change" ],
SymName.tabclefSym:           [ QT_TRANSLATE_NOOP("symbol", "tab clef"),             "clefs.tab" ],
SymName.ctabclefSym:          [ QT_TRANSLATE_NOOP("symbol", "ctab clef"),            "clefs.tab_change" ],
SymName.fourfourmeterSym:     [ QT_TRANSLATE_NOOP("symbol", "four four meter"),      "timesig.C44" ],
SymName.allabreveSym:         [ QT_TRANSLATE_NOOP("symbol", "allabreve"),            "timesig.C22" ],
SymName.pedalasteriskSym:     [ QT_TRANSLATE_NOOP("symbol", "pedalasterisk"),        "pedal.*" ],
SymName.pedaldashSym:         [ QT_TRANSLATE_NOOP("symbol", "pedaldash"),            "pedal.M" ],
SymName.pedaldotSym:          [ QT_TRANSLATE_NOOP("symbol", "pedaldot"),             "pedal.." ],
SymName.pedalPSym:            [ QT_TRANSLATE_NOOP("symbol", "pedalP"),               "pedal.P" ],
SymName.pedaldSym:            [ QT_TRANSLATE_NOOP("symbol", "pedald"),               "pedal.d" ],
SymName.pedaleSym:            [ QT_TRANSLATE_NOOP("symbol", "pedale"),               "pedal.e" ],
SymName.pedalPedSym:          [ QT_TRANSLATE_NOOP("symbol", "pedal ped"),            "pedal.Ped" ],
SymName.brackettipsRightUp:   [ QT_TRANSLATE_NOOP("symbol", "bracket tips up"),      "brackettips.uright"     ],
SymName.brackettipsRightDown: [ QT_TRANSLATE_NOOP("symbol", "bracket tips down"),    "brackettips.dright"     ],
SymName.brackettipsLeftUp:    [ QT_TRANSLATE_NOOP("symbol", "bracket tips left up"), "brackettips.uleft"      ],
SymName.brackettipsLeftDown:  [ QT_TRANSLATE_NOOP("symbol", "bracket tips left down"), "brackettips.dleft"      ],
SymName.accDotSym:            [ QT_TRANSLATE_NOOP("symbol", "acc dot"),              "accordion.accDot"       ],
SymName.accFreebaseSym:       [ QT_TRANSLATE_NOOP("symbol", "acc freebase"),         "accordion.accFreebase"  ],
SymName.accStdbaseSym:        [ QT_TRANSLATE_NOOP("symbol", "acc stdbase"),          "accordion.accStdbase"   ],
SymName.accBayanbaseSym:      [ QT_TRANSLATE_NOOP("symbol", "acc bayanbase"),        "accordion.accBayanbase" ],
SymName.accOldEESym:          [ QT_TRANSLATE_NOOP("symbol", "acc old ee"),           "accordion.accOldEE"     ],
SymName.accDiscantSym:        [ QT_TRANSLATE_NOOP("symbol", "acc discant"),          "accordion.accDiscant"   ],
SymName.zeroSym:              [ QT_TRANSLATE_NOOP("symbol", "zero"),                 "zero" ],
SymName.oneSym:               [ QT_TRANSLATE_NOOP("symbol", "one"),                  "one" ],
SymName.twoSym:               [ QT_TRANSLATE_NOOP("symbol", "two"),                  "two" ],
SymName.threeSym:             [ QT_TRANSLATE_NOOP("symbol", "three"),                "three" ],
SymName.fourSym:              [ QT_TRANSLATE_NOOP("symbol", "four"),                 "four" ],
SymName.fiveSym:              [ QT_TRANSLATE_NOOP("symbol", "five"),                 "five" ],
SymName.sixSym:               [ QT_TRANSLATE_NOOP("symbol", "six"),                  "six" ],
SymName.sevenSym:             [ QT_TRANSLATE_NOOP("symbol", "seven"),                "seven" ],
SymName.eightSym:             [ QT_TRANSLATE_NOOP("symbol", "eight"),                "eight" ],
SymName.nineSym:              [ QT_TRANSLATE_NOOP("symbol", "nine"),                 "nine" ],
SymName.plusSym:              [ QT_TRANSLATE_NOOP("symbol", "plus"),                 "plus" ],
SymName.letterzSym:           [ QT_TRANSLATE_NOOP("symbol", "z"),                    "z" ],
SymName.letterfSym:           [ QT_TRANSLATE_NOOP("symbol", "f"),                    "f" ],
SymName.lettersSym:           [ QT_TRANSLATE_NOOP("symbol", "s"),                    "s" ],
SymName.letterpSym:           [ QT_TRANSLATE_NOOP("symbol", "p"),                    "p" ],
SymName.lettermSym:           [ QT_TRANSLATE_NOOP("symbol", "m"),                    "m" ],
SymName.letterrSym:           [ QT_TRANSLATE_NOOP("symbol", "r"),                    "r" ],
SymName.longaupaltSym:        [ QT_TRANSLATE_NOOP("symbol", "longa up alt"),         "noteheads.uM2alt" ],
SymName.longadownaltSym:      [ QT_TRANSLATE_NOOP("symbol", "longa down alt"),       "noteheads.dM2alt" ],
SymName.brevisheadaltSym:     [ QT_TRANSLATE_NOOP("symbol", "brevis head alt"),      "noteheads.sM1alt" ],
SymName.timesigcdotSym:       [ QT_TRANSLATE_NOOP("symbol", "time sig C dot"),       "timesig.Cdot" ],
SymName.timesigoSym:          [ QT_TRANSLATE_NOOP("symbol", "time sig O"),           "timesig.O" ],
SymName.timesigocutSym:       [ QT_TRANSLATE_NOOP("symbol", "time sig O cut"),       "timesig.Ocut" ],
SymName.timesigodotSym:       [ QT_TRANSLATE_NOOP("symbol", "time sig O dot"),       "timesig.Odot" ]
}

class SymbolType:
    SYMBOL_UNKNOWN = 0
    SYMBOL_COPYRIGHT = 1
    SYMBOL_FRACTION = 2
    
class SymCode:
    
     def __init__(self, c, id, t=0, Type=SymbolType.SYMBOL_UNKNOWN, show=True):
         self.code = QChar(c)
         self.fontId = id
         self.text = t
         self.Type = Type
         self.show = show

pSymbols = [
      SymCode(0xe10e, 1),\
      SymCode(0xe10c, 1),\
      SymCode(0xe10d, 1),\
      SymCode(0xe104, 1),\
      SymCode(0xe105, 1),\
      SymCode(0xe106, 1),\
      SymCode(0xe107, 1),\
      SymCode(0xe108, 1),\
      SymCode(0xe109, 1),\
      SymCode(0xe10a, 1),\
      SymCode(0xe10b, 1),\
      SymCode(0xe167, 1),\
      SymCode(0xe168, 1),\
      SymCode(0xe169, 1),\
      SymCode(0, 0),\
      SymCode(0xa9,   -1, "(C)", SymbolType.SYMBOL_COPYRIGHT),\
      SymCode(0x00c0, -1),\
      SymCode(0x00c1, -1),\
      SymCode(0x00c2, -1),\
      SymCode(0x00c3, -1),\
      SymCode(0x00c4, -1),\
      SymCode(0x00c5, -1),\
      SymCode(0x00c6, -1),\
      SymCode(0x00c7, -1),\
      SymCode(0x00c8, -1),\
      SymCode(0x00c9, -1),\
      SymCode(0x00ca, -1),\
      SymCode(0x00cb, -1),\
      SymCode(0x00cc, -1),\
      SymCode(0x00cd, -1),\
      SymCode(0x00ce, -1),\
      SymCode(0x00cf, -1),\
      SymCode(0x00d0, -1),\
      SymCode(0x00d1, -1),\
      SymCode(0x00d2, -1),\
      SymCode(0x00d3, -1),\
      SymCode(0x00d4, -1),\
      SymCode(0x00d5, -1),\
      SymCode(0x00d6, -1),\
      SymCode(0x00d7, -1),\
      SymCode(0x00d8, -1),\
      SymCode(0x00d9, -1),\
      SymCode(0x00da, -1),\
      SymCode(0x00db, -1),\
      SymCode(0x00dc, -1),\
      SymCode(0x00dd, -1),\
      SymCode(0x00de, -1),\
      SymCode(0x00df, -1),\
      SymCode(0x0108, -1),\
      SymCode(0x011c, -1),\
      SymCode(0x0124, -1),\
      SymCode(0x0134, -1),\
      SymCode(0x015c, -1),\
      SymCode(0x016c, -1),\
      SymCode(0x00e0, -1),\
      SymCode(0x00e1, -1),\
      SymCode(0x00e2, -1),\
      SymCode(0x00e3, -1),\
      SymCode(0x00e4, -1),\
      SymCode(0x00e5, -1),\
      SymCode(0x00e6, -1),\
      SymCode(0x00e7, -1),\
      SymCode(0x00e8, -1),\
      SymCode(0x00e9, -1),\
      SymCode(0x00ea, -1),\
      SymCode(0x00eb, -1),\
      SymCode(0x00ec, -1),\
      SymCode(0x00ed, -1),\
      SymCode(0x00ee, -1),\
      SymCode(0x00ef, -1),\
      SymCode(0x00f0, -1),\
      SymCode(0x00f1, -1),\
      SymCode(0x00f2, -1),\
      SymCode(0x00f3, -1),\
      SymCode(0x00f4, -1),\
      SymCode(0x00f5, -1),\
      SymCode(0x00f6, -1),\
      SymCode(0x00f7, -1),\
      SymCode(0x00f8, -1),\
      SymCode(0x00f9, -1),\
      SymCode(0x00fa, -1),\
      SymCode(0x00fb, -1),\
      SymCode(0x00fc, -1),\
      SymCode(0x00fd, -1),\
      SymCode(0x00fe, -1),\
      SymCode(0x00ff, -1),\
      SymCode(0x0109, -1),\
      SymCode(0x011d, -1),\
      SymCode(0x0125, -1),\
      SymCode(0x0135, -1),\
      SymCode(0x015d, -1),\
      SymCode(0x016d, -1),\
      SymCode(0x00BC, -1, "1/4", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x00BD, -1, "1/2", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x00BE, -1, "3/4", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2153, -1, "1/3", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2154, -1, "2/3", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2155, -1, "1/5", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2156, -1, "2/5", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2157, -1, "3/5", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2158, -1, "4/5", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x2159, -1, "1/6", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x215A, -1, "5/6", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x215B, -1, "1/8", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x215C, -1, "3/8", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x215D, -1, "5/8", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x215E, -1, "7/8", SymbolType.SYMBOL_FRACTION),\
      SymCode(0x35c, -1),\
      SymCode(0x361, -1),\
      SymCode(0x0152, -1),\
      SymCode(0x0153, -1),\
      SymCode(-1, -1)\
]

charReplaceMap = {}

def fontId2font(fontId):
    _font = QFont()
    size = int(20.0 * GL.DPI / PPI)
    if fontId == 0:
        _font.setFamily("MScore")
        _font.setStyleStrategy(QFont.NoFontMerging)
    elif fontId == 1:
        _font.setFamily("MScore1")
    elif fontId == 2:
        _font.setFamily("Times New Roman")
        _font.setStyleStrategy(QFont.NoFontMerging)
        size = int(8 * GL.DPI / PPI)
    else:
        print"illegal font id %d\n"  %fontId
        exit(1)
    _font.setPixelSize(size)
    return _font



class Sym:
    
                  
     def __init__(self, name, c, fid, ax = 0.0, ay = 0.0):
         self._code = QChar(c)
         self.fontId = fid
         self._name = name
         self._font = fontId2font(self.fontId)
         self._bbox = QRectF()
         self._attach = ax* GL.DPI/PPI, ay * GL.DPI/PPI
         fm = QFontMetricsF(self._font)
         if fm.inFont(self._code) == False and name != 0:
             print "Sym: character 0x%x(%d) <%s> are not in font <%s>\n" %(self._code.unicode(),c, self._name, self._font.family().toAscii().data())
         self.w = fm.width(self._code)
         self._bbox = fm.boundingRect(self._code)
         self.createTextLayout()
         
     def init2(self, name, c, fid, a, b):
         self._code = QChar(c)
         self.fontId = fid
         self._name = name
         self._font = fontId2font(self.fontId)
         self._bbox = QRectF()
         s = GL.DPI/PPI
         aa = QRectF()
         bb = QRectF()
         aa = a
         bb = b
         self._bbox.setRect(bb.x() * s, bb.y() * s, bb.width() * s, bb.height() * s)
         self._attach = aa * s
         self.w = self._bbox.width()
         self.createTextLayout()


     def name(self):
         return self._name
     def setName(self, s ):
         self._name = s
     def height(self, mag):
         return self._bbox.height() * mag
     def width(self, mag):
         return self.w  *mag
     def attach(self, mag):
         return self._attach * mag
     def code(self):
         return self._code
     def getFontId(self):
         return self.fontId
     def setFontId(self, v):
         self.fontId = v
         return self.fontId
     def font(self):
         return self._font
     def setAttach(self, r):
         self._attach = r
     def isValid(self):
         return self.tl != 0



     def createTextLayout(self):
         self.tl = QTextLayout(QString(self._code), self._font)
         self.tl.beginLayout()
         l = QTextLine(self.tl.createLine())
         l.setNumColumns(1)
         l.setPosition(QPointF(0.0, -l.ascent()))
         self.tl.endLayout()
         self.tl.setCacheEnabled(True)

     def findSymbol(self, code, fontId):
         s = Sym()
         for s in range(0, len(GL.symbols)):
             if (s.code() == code) and (s.getFontId() == fontId):
                 return s
         return 0

     def bbox(self, mag):
         return QRectF(self._bbox.x() * mag, self._bbox.y() * mag, self._bbox.width() * mag, self._bbox.height() * mag)

     def draw(self, painter, mag, x, y):
         p = QPainter()
         p = painter
         imag = 1.0 / mag
         p.scale(mag, mag)
         self.tl.draw(p, QPointF(x * imag, y * imag))
         p.scale(imag, imag)
         
     '''def draw(painter, mag, x, y, n):
         p = QPainter()
         p = painter
         imag = 1.0 / mag
         p.scale(mag, mag)
         p.setFont(self._font)
         p.drawText(x * imag, y * imag, QString(n, self._code))
         p.scale(imag, imag)'''

def initSymbols():
    GL.symbols = {
        SymName.clefEightSym: Sym(QT_TRANSLATE_NOOP("symbol", "clef eight"),                 0x38, 2),
        SymName.clefOneSym:   Sym(QT_TRANSLATE_NOOP("symbol", "clef one"),                   0x31, 2),
        SymName.clefFiveSym:  Sym(QT_TRANSLATE_NOOP("symbol", "clef five"),                  0x35, 2),
        SymName.letterfSym:   Sym(QT_TRANSLATE_NOOP("symbol", "f"),                          0x66, 1),
        SymName.lettermSym:   Sym(QT_TRANSLATE_NOOP("symbol", "m"),                          0x6d, 1),
        SymName.letterpSym:   Sym(QT_TRANSLATE_NOOP("symbol", "p"),                          0x70, 1),
        SymName.letterrSym:   Sym(QT_TRANSLATE_NOOP("symbol", "r"),                          0x72, 1),
        SymName.lettersSym:   Sym(QT_TRANSLATE_NOOP("symbol", "s"),                          0x73, 1),
        SymName.letterzSym:   Sym(QT_TRANSLATE_NOOP("symbol", "z"),                          0x7a, 1),
        # used for GUI:
        SymName.note2Sym:     Sym(QT_TRANSLATE_NOOP("symbol", "note 1/2"),   0xe104, 1),
        SymName.note4Sym:     Sym(QT_TRANSLATE_NOOP("symbol", "note 1/4"),   0xe105, 1),
        SymName.note8Sym:     Sym(QT_TRANSLATE_NOOP("symbol", "note 1/8"),   0xe106, 1),
        SymName.note16Sym:    Sym(QT_TRANSLATE_NOOP("symbol", "note 1/16"),  0xe107, 1),
        SymName.note32Sym:    Sym(QT_TRANSLATE_NOOP("symbol", "note 1/32"),  0xe108, 1),
        SymName.note64Sym:    Sym(QT_TRANSLATE_NOOP("symbol", "note 1/64"),  0xe109, 1),
        SymName.dotdotSym:    Sym(QT_TRANSLATE_NOOP("symbol", "dot dot"),    0xe10b, 1)
        }
    
    lnhash = dict()
    for i, j in lilypondNames.items():
        lnhash[j[1]] = i
    f = QFile("data\symbols.xml")
    if not f.open(QFile.ReadOnly):
        print "cannot open symbols file\n", f.errorString()
        exit(1)
    doc = QDomDocument()
    errorMsg = QString()    
    (result, errorMsg, errorLine, errorColumn) = doc.setContent(f, False)
    if result == False:
        error = QString()
        error.sprintf("error reading style file %s at line %d column %d: %s\n", f.fileName().toLatin1().data(), errorLine, errorColumn, errorMsg.toLatin1().data())
        QMessageBox.warning(0, QWidget.tr("Muse: Load font symbols failed:"), error, QString.null, QWidget.tr("Quit"), QString.null, 0, 1)
        return
    f.close()
    docName = f.fileName()
    e = doc.documentElement()
    while not e.isNull():
        if e.tagName() == "museScore":
            ee = e.firstChildElement()
            while not ee.isNull():
                if ee.tagName() == "Glyph":
                    name = QString()
                    code = -1
                    p = QPointF()
                    b = QRectF ()
                    eee = ee.firstChildElement()
                    while not eee.isNull():
                        tag = QString(eee.tagName())
                        val = QString(eee.text())
                        if tag == "name":
                            name = val
                        elif tag == "code":
                            (code, ok) = val.mid(2).toInt(16)
                            if ok == False:
                                print"cannot read code\n"
                        elif tag == "attach":
                            p = readPoint(eee)
                        elif tag == "bbox":
                            b = readRectF(eee)
                        else:
                            domError(eee)
                        eee = eee.nextSiblingElement()
                    if code == -1:
                        print"no code for glyph <%s>\n" %name.toAscii().data()
                    if lnhash.has_key(unicode(name)):
                        idx = lnhash[unicode(name)]
                        if idx > 0:
                            GL.symbols[idx] = Sym(name, code, 0)
                            GL.symbols[idx].init2(name, code, 0, p, b)
                        elif idx == 0:
                            print "symbol <%s> not found\n" %name.toAscii().data()
                else:
                    domError(ee)
                ee = ee.nextSiblingElement()
        else:
            domError(e)
        e = e.nextSiblingElement()
    for i, j in lilypondNames.items():
        idx = i
        if idx != -1 :
            GL.symbols[idx].setName(j[0])
    global charReplaceMap       
    if len(charReplaceMap) == 0 :
        for i in range(0, len(pSymbols)):
            if (pSymbols[i].code == 0 or pSymbols[i].text == 0):
                continue
            charReplaceMap[pSymbols[i].text] =  pSymbols[i]

