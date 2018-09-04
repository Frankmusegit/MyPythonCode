#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from File import *
from Xml import *
from part import *
import Score
import AL
from Timesig import *

def stringToInt(s):
    res = 0
    str = s
    if s.endsWith(".0"):
        str = s.left(s.size() - 2)
    (res, ok) = str.toInt()
    return (res, ok)

def determineTimeSig(beats, beatType, timeSymbol = QString()):
    st = 0
    bts = [0,0,0,0]
    btp = 0
    if beats == "2" and beatType == "2" and timeSymbol == "cut":
        st = TSIG.TSIG_ALLA_BREVE
    elif beats == "4" and beatType == "4" and timeSymbol == "common":
        st = TSIG.TSIG_FOUR_FOUR
    else:
        if not timeSymbol.isEmpty():
            print "ImportMusicXml: time symbol <%s> not recognized with beats=%s and beat-type=%s\n"\
            %(timeSymbol.toAscii().data(), beats.toAscii().data(), beatType.toAscii().data())
            btp = beatType.toInt()
            list = beats.split("+") 
            for i in range(0, len(list)):
                bts[i] = list.at(i).toInt()
            if btp and (bts[0] or bts[1] or bts[2] or bts[3]):
                ts = TimeSig(0)
                ts.TimeSig2(btp, bts[0], bts[1], bts[2], bts[3])
                st = ts.subtype()
    return st

def calcTicks(text, divisions):
    (ok, val) = stringToInt(text)
    if not ok:
        print "MusicXml-Import: bad duration value: <%s>\n" %text.toAscii().data()
    if val == 0:
        val = 1
        val = val * AL.division / divisions
    return val

def moveTick(tick,  maxtick, lastLen, divisions, e):
    if e.tagName() == "forward":
        ee = e.firstChildElement()
        while not ee.isNull():
            if ee.tagName() == "duration":
                val = calcTicks(ee.text(), divisions)
                tick += val
                if tick > maxtick:
                    maxtick = tick
                    lastLen = val
                elif ee.tagName() == "voice":
                    pass
                elif ee.tagName() == "staff":
                    pass
                else:
                    domError(ee)
            ee = ee.nextSiblingElement()
    elif e.tagName() == "backup":
        ee = e.firstChildElement()
        while not ee.isNull():
            if ee.tagName() == "duration":
                val = calcTicks(ee.text(), divisions)
                tick -= val
                lastLen = val
            else:
                domError(ee)
            ee = ee.nextSiblingElement()
    elif e.tagName() == "note":
        grace   = False
        ticks = 0
        ee = e.firstChildElement()
        while not ee.isNull():
            tag = QString(ee.tagName())
            if tag == "grace":
                grace = True
            elif tag == "duration":
                ticks = calcTicks(ee.text(), divisions)
            ee = ee.nextSiblingElement()
        if not grace:
            lastLen = ticks
            tick += ticks
            if tick > maxtick:
                maxtick = tick



def determineMeasureLength(e, ml):
    #print "measurelength ml size %d\n" %len(ml)
    divisions = -1
    tick = 0
    maxtick = 0
    prevmaxtick = 0
    lastLen = 0
    measureNr = 0
    result = True
    beats = QString()
    beatType = QString()
    timeSigLen = -1
    e = e.firstChildElement()
    while not e.isNull():
        if e.tagName() == "measure":
            ee = e.firstChildElement()
            while not ee.isNull():
                if ee.tagName() == "attributes":
                    eee = ee.firstChildElement()
                    while not eee.isNull():
                        if eee.tagName() == "divisions":
                            (divisions, ok) = stringToInt(eee.text())
                            if not ok or divisions <= 0:
                                print "MusicXml-Import: bad divisions value: <%s>\n" %eee.text().toAscii().data()
                            #print "measurelength divisions %d\n" %divisions
                        elif eee.tagName() == "time":
                            eeee = eee.firstChildElement()
                            while not eeee.isNull():
                                if eeee.tagName() == "beats":
                                    beats = eeee.text()
                                elif eeee.tagName() == "beat-type":
                                    beatType = eeee.text()
                                elif eeee.tagName() == "senza-misura":
                                    pass
                                else:
                                    domError(eeee)
                                eeee = eeee.nextSiblingElement()
                            if beats != "" and beatType != "":
                                st = determineTimeSig(beats, beatType)
                                #print "measurelength beats %s beattype %s st %d" %(beats.toAscii().data(), beatType.toAscii().data(), st)
                                if st:
                                    ts = TimeSig(0)
                                    ts.TimeSig1(st)
                                    timeSigLen = ts.getSig().ticks()
                                    print " fraction %s len %d" %((ts.getSig().print_()).toAscii().data(), timeSigLen)
                        eee = eee.nextSiblingElement()

                if divisions > 0:
                    result = True
                    if ee.tagName() == "note":
                        chord = False
                        grace = False
                        eee = ee.firstChildElement()
                        while not eee.isNull():
                            if eee.tagName() == "chord":
                                chord = True
                            elif eee.tagName() == "grace":
                                grace = True
                            eee = eee.nextSiblingElement()
                        if chord and not grace:
                            tick -= lastLen
                            moveTick(tick, maxtick, lastLen, divisions, ee)
                    elif ee.tagName() == "backup":
                        moveTick(tick, maxtick, lastLen, divisions, ee)
                    elif ee.tagName() == "forward":
                        moveTick(tick, maxtick, lastLen, divisions, ee)
                else:
                    result = False
                ee = ee.nextSiblingElement()

            length = maxtick - prevmaxtick
            correctedLength = length
            if length % (AL.division/8) != 0:
                correctedLength = ((length / (AL.division/8)) + 1) * (AL.division/8)
            if correctedLength <= 0 and timeSigLen > 0:
                correctedLength = timeSigLen
                #debug
                #print "measurelength measure %d tick %d maxtick %d length %d corr length %d\n" %(measureNr + 1, tick, maxtick, length, correctedLength)
                length = correctedLength
                if len(ml) < measureNr + 1:
                    ml.append(length)
                else:
                    if length > ml[measureNr]:
                        ml[measureNr] = length
            prevmaxtick = maxtick
            tick = maxtick
            measureNr = measureNr + 1
        e = e.nextSiblingElement()
    #print "measurelength ml size %d res %d\n" %(len(ml), result)
    for i in range(0, len(ml)):
        print "measurelength ml[%d] %d\n" %(i + 1, ml[i])
    return result



class MusicXml:

    def __init__(self, d):
        self.doc = d
        self.maxLyrics = 0
        self.lastVolta = 0;
        self.beamMode = BeamMode.BEAM_NO
        self.score = Score.Score(defaultStyle)
        self.measureLength = list()
        
    def scorePartwise(self, ee):
        #e = QDomElement()
        e = ee
        while not e.isNull():
            if e.tagName() == "part":
                id_ = e.attribute(QString("id"))
                if id_ == "":
                    print "MusicXML import: part without id\n"
                else:
                    part = Part(self.score)
                    part.setId(id_)
                    self.score.appendPart(part)
                    staff = Staff()
                    staff.Staff1(self.score, part, 0)
                    part.staves().append(staff)
                    self.score.staves().append(staff)
                    self.tuplets = [0, 0, 0, 0]
                    #print "measurelength part '%s'\n" %id_.toAscii().data()
                    if not determineMeasureLength(e, self.measureLength):
                        print "MusicXML import: could not determine measure length for part '%s'\n" %id_.toAscii().data()
            e = e.nextSiblingElement()

    def import_(self, s):
        #tupletAssert()
        self.score  = s
        self.tie    = 0
        self.slur = [0, 0, 0, 0, 0, 0]
        self.bracket = [0, 0, 0, 0, 0, 0, 0, 0]
        self.dashes = [0, 0, 0, 0, 0, 0, 0, 0]
        self.ottava = 0
        self.trill = 0
        self.pedal = 0
        self.tremStart = 0
        e = self.doc.documentElement()
        while not e.isNull():
            if e.tagName() == "score-partwise":
                self.scorePartwise(e.firstChildElement())
            else:
                domError(e)
            e = e.nextSiblingElement()



class LoadMusicXml(LoadFile):

    def __init__(self):
        LoadFile.__init__(self)
        self._doc = QDomDocument()

    def load(self,name):
        if name.isEmpty():
            return False
        fp = QFile(name)
        if not fp.open(QIODevice.ReadOnly):
            p = QWidget()
            QMessageBox.warning(p, p.tr("file not found:"), name, QString(), QString(), QString(), 0, 1)
            return False
        if not self.loader(fp):
            p = QWidget()
            QMessageBox.warning(p, p.tr("load failed:"), self.error, QString(), QWidget().tr("Quit"), QString(), 0, 1)
            fp.close()
            return False
        fp.close()
        return True
    
    def doc(self):
        return self._doc


    def loader(self, qf):

        (ok, err, line, column) = self._doc.setContent(qf, False)
        if not ok :       
            col = QString()
            ln = QString()
            col.setNum(column)
            ln.setNum(line)
            self.error = err + "\n at line " + ln + " column " + col
            return False
        GL.docName = qf.fileName()
        return True
    


    
