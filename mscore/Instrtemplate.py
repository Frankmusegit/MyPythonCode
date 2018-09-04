#!/usr/bin/env python
#-*- coding:utf-8 -*-
import GL
from globals import *
from Xml import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtXml import *

class InstrumentGroup:
    def __init__(self):
        self.name = QString()
        self.extended = False
        self.instrumentTemplates = list()

class  MidiArticulation:
    def __init__(self):
        self.name = QString()
        self.velocity = 0
        self.gateTime = 0

class InstrumentTemplate:
    def __init__(self):
        self.staves             = 1
        self.clefIdx         = [CLEF.CLEF_G]
        self.staffLines      = [5]
        self.smallStaff      = False
        self.bracket            = BRACKET.NO_BRACKET
        self. minPitchA          = 0
        self.maxPitchA          = 127
        self.minPitchP          = 0
        self.maxPitchP          = 127
        self.useDrumset         = False
        self.drumset            = 0
        self.extended           = False

def searchTemplate(name):
    for g in GL.instrumentGroups:
        for it in g.instrumentTemplates:
            if it.trackName == name:
                return it
    return 0


def readInstrumentGroup(group, e):
    e = e.firstChildElement()
    while not e.isNull():
        tag = QString(e.tagName())
        if tag == "instrument":
            t = InstrumentTemplate()
            group.instrumentTemplates.append(t)
            t.read(e)
        elif tag == "ref":
            ttt = searchTemplate(e.text())
            if ttt:
                t = InstrumentTemplate(ttt)
                group.instrumentTemplates.append(t)
            else:
                print "instrument reference not found <%s>\n" %e.text().toAscii().data()
        else:
                  domError(e)
        e = e.nextSiblingElement()


def loadInstrumentTemplates(instrTemplates):
    qf = QFile(instrTemplates)
    if not qf.open(QIODevice.ReadOnly):
        return False
    doc = QDomDocument()
    line = 0
    column = 0
    err = QString()
    (rv, err, line, column) = doc.setContent(qf, False)
    docName = qf.fileName()
    qf.close()
    for g in GL.instrumentGroups:
        for t in g.instrumentTemplates:
            del(t)
        del(g)
    GL.instrumentGroups.clear()
    if not rv:
        s = QString()
        s.sprintf("error reading file %s at line %d column %d: %s\n",
               instrTemplates.toLatin1().data(), line, column, err.toLatin1().data())
        QMessageBox.critical(0, "Muse 3.0: Read Template File", s)
        return True
    e = doc.documentElement()
    while not e.isNull():
        if e.tagName() == "museScore":
            ee = e.firstChildElement()
            while not ee.isNull():
                tag = QString(ee.tagName())
                val = QString(ee.text())
                if tag == "instrument-group" or tag == "InstrumentGroup":
                    group = InstrumentGroup()
                    group.name = ee.attribute("name")
                    group.extended = ee.attribute("extended", "0").toInt()
                    readInstrumentGroup(group, ee)
                    GL.instrumentGroups.append(group)
                elif tag == "Articulation":
                    a = MidiArticulation()
                    a.read(ee)
                    GL.articulation.append(a)
                else:
                    domError(ee)
                ee = ee.nextSiblingElement()
        e = e.nextSiblingElement()
    return True

