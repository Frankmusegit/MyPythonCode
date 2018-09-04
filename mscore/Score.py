#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from Undo import *
from Page import *
from Repeatlist import *
from Importxml import *
from Tempo import *
from Sig import *
from Bsp import *
from Input import *

class MeasureBaseList:
    def __init__(self):
        self._size = 0
        self._first = 0
        self._last = 0

    def first(self):
        return self._first
    def last(self):
        return self._last

class MidiMapping:
    def __init__(self):
        self.port = 0
        self.channel = 0
        self.part = 0
        self.articulation = 0

class MidiInputEvent:
    def __init__(self):
        self.pitch = 0
        self.chord = 0

class Position:
    def __init__(self):
        self.measure = 0
        self.tick = 0
        self.staffIdx = 0
        self.line = 0
        self.pos = QPointF()

class ImagePath:
    def __init__(self, p):
        self.path = p
        self._references = 0
        self._loaded = False
        self._buffer = QBuffer()

    def path(self):
        return self._path

    def buffer(self):
        return self._buffer

    def setLoaded(self, val):
        self._loaded = val

    def loaded(self):
        return self._loaded

    def setPath(self, val):
        self._path = val

    def isUsed(self):
        return self._references > 0

    def dereference(self):
        self._references = self._references - 1

    def reference(self):
        self._references = self._references + 1


class Score(QObject):

    selectionChanged = pyqtSignal(int)
    dirtyChanged = pyqtSignal(int)
    posChanged = pyqtSignal(int)
    updateAll = pyqtSignal()
    dataChanged = pyqtSignal(QRectF)
    layoutChanged = pyqtSignal()
    
    def setClean(self, val):
        self.val = not val
        if self._dirty != val:
            self._dirty = val
            self._playlistDirty = True
            self.dirtyChanged.emit(self)
        if self._dirty:
            self._autosaveDirty = True
            self._playlistDirty = True

    def __init__(self, s):
        super(Score, self).__init__()
        self._spatium = Preferences().spatium * GL.DPI
        self._pageFormat = PageFormat()
        self._paintDevice = 0
        self.bspTree = BspTree()
        self._needLayout     = False
        self.startLayout     = 0
        self._undo           =  UndoStack()
        self._repeatList     = RepeatList(self)
        self._style  = s
        self._swingRatio     = 0.0
        self._textStyles = list()
        for i in range(0, TEXT_STYLE.TEXT_STYLES):
            self._textStyles.append(GL.defaultTextStyles[i])
        self._parts = list()
        self._staves = list()
        self._mscVersion     = 110
        self._created        = False
        self._updateAll      = False
        self.layoutAll       = False
        self.keyState        = 0
        self._showInvisible  = True
        self._showFrames     = True
        self.editTempo       = 0
        self._printing       = False
        self._playlistDirty  = False
        self._autosaveDirty  = False
        self._dirty          = False
        self._saved          = False
        self._playPos        = 0
        self._fileDivision   = 480
        self._creditsRead    = False
        self._defaultsRead   = False
        self.rights          = 0
        self.info = QFileInfo()
        self._tempomap       = TempoMap()
        self._sigmap         = TimeSigMap()
        self._sigmap.add(0, Fraction(4, 4))
        self.curTick = 0
        self._measures = MeasureBaseList()
        self._gel = list()
        self._midiMapping = list()
        self._is = InputState()
        self.connect(self._undo, SIGNAL("cleanChanged()"), self.setClean)

    def noStaves(self):
        return self._staves.empty()

    def appendPart(self, p):
        self._parts.append(p)

    def staves(self):
        return self._staves

    def nstaves(self):
        return len(self._staves)

    def spatium(self):
        return self._spatium

    def first(self):
        return self._measures.first()

    def staffIdx(self, staff):
        return self._staves.index((staff, 0))

    def staff(self,  n):
        return self._staves[n]

    def getSelectedElement(self):
        return self._selection.element()

    def selection(self):
        return self._selection

    def deselectAll(self):
        self._selection.deselectAll()

    def updateSelection(self):
        self._selection.update()

    def setUpdateAll(self, v = True):
        self._updateAll = v

    def setLayoutAll(self, val):
        self.layoutAll = val

    def addRefresh(self, r):
        self.refresh = self.refresh | r

    def  parts(self):
        return self._parts

    def showInvisible(self):
        return self._showInvisible

    def showFrames(self):
        return self._showFrames

    def fileDivision(self, t):
        return (t * AL.division + self._fileDivision/2) / self._fileDivision

    def filePath(self):
        return self.info.filePath()

    def fileInfo(self):
        return self.info

    def name(self):
        return self.info.completeBaseName()

    def setName(self, s):
        self.info.setFile(s)

    def dirty(self):
        return self._dirty

    def setCreated(self, val):
        self._created = val

    def created(self):
        return self._created

    def setSaved(self, v):
        self._saved = v

    def Saved(self, ):
        return self._saved

    def printing(self):
        return self._printing

    def setAutosaveDirty(self, v):
        self._autosaveDirty = v

    def autosaveDirty(self):
        return self._autosaveDirty

    def  style(self):
        return self._style

    def setStyle(self, s):
        self._style = s

    def  playPos(self):
        return self._playPos

    def setPlayPos(self, val):
        self._playPos = val

    def noteEntryMode(self):
        return self._is.noteEntryMode

    def pageFormat(self):
        return self._pageFormat

    def inputTrack(self):
        return self._is.track

    def inputState(self):
        return self._is

    def setInputState(self, st):
        self._is = st

    def textStyle(self,idx):
        if idx < 0:
            return 0
        else:
            return self._textStyles[idx]

    def textStyles(self):
        return self._textStyles

    def mscVersion(self):
        return self._mscVersion

    def setMscVersion(self, v):
        self._mscVersion = v

    def programVersion(self):
        return self._programVersion

    def setProgramVersion(self, v):
        self._programVersion = v

    def sigmap(self):
        return self._sigmap

    def excerpts(self):
        return self._excerpts

    def measures(self):
        return self._measures

    def gel(self):
        return self._gel

    def midiMapping(self):
        return self._midiMapping

    def tempomap(self):
        return self._tempomap

    def swingRatio(self):
        return self._swingRatio

    def setSwingRatio(self, d):
        self._swingRatio = d

    def  movementNumber(self):
        return self._movementNumber

    def  movementTitle(self):
        return self._movementTitle

    def  workNumber(self):
        return self._workNumber

    def workTitle(self):
        return self._workTitle

    def source(self):
        return self._source

    def mxmlRights(self):
        return self._rights

    def creditsRead(self):
        return self._creditsRead

    def defaultsRead(self):
        return self._defaultsRead

    def setMovementNumber(self, s):
        self._movementNumber = s

    def setMovementTitle(self, s):
        self._movementTitle = s

    def setWorkNumber(self, s):
        self._workNumber = s

    def setWorkTitle(self, s):
        self._workTitle = s

    def setSource(self, s):
        self._source = s

    def setmxmlRights(self, s):
        self._rights = s

    def setCreditsRead(self, b):
        self._creditsRead = b

    def setDefaultsRead(self,  b):
        self._defaultsRead = b

    def addCreator(self, c):
        self._creators.append(c)

    def getCreator(self, i):
        return self._creators[i]

    def numberOfCreators(self):
        return len(self._creators)

    def undo(self):
        return self._undo

    def copyright(self):
        return self.rights

    def repeatList(self):
        return self._repeatList

    def layout(self):
        self._needLayout = True

    def pages(self):
        return self._pages

    def systems(self):
        return self._systems

    def needLayout(self):
        return self._needLayout

    def paintDevice(self):
        return self._paintDevice

    def items(self, r):
        return self.bspTree.items(r)

    def insertBsp(self, e):
        self. bspTree.insert(e)

    def removeBsp(self, e):
        self.bspTree.remove(e)

    def point(self, sp):
        return sp.val() * self._spatium

    def tmpName(self):
        return self._tmpName

    def setTmpName(self, s):
        self._tmpName = s

    def beams(self):
        return self._beams



    def setPadState(self):
        GL.actions["pad-rest"].setChecked(self._is.rest)
        GL.actions["pad-dot"].setChecked(self._is.duration().dots() == 1)
        GL.actions["pad-dotdot"].setChecked(self._is.duration().dots() == 2)
        GL.actions["note-longa"].setChecked(self._is.duration()  == DurationType.V_LONG)
        GL.actions["note-breve"].setChecked(self._is.duration()  == DurationType.V_BREVE)
        GL.actions["pad-note-1"].setChecked(self._is.duration()  == DurationType.V_WHOLE)
        GL.actions["pad-note-2"].setChecked(self._is.duration()  == DurationType.V_HALF)
        GL.actions["pad-note-4"].setChecked(self._is.duration()  == DurationType.V_QUARTER)
        GL.actions["pad-note-8"].setChecked(self._is.duration()  == DurationType.V_EIGHT)
        GL.actions["pad-note-16"].setChecked(self._is.duration() == DurationType.V_16TH)
        GL.actions["pad-note-32"].setChecked(self._is.duration() == DurationType.V_32ND)
        GL.actions["pad-note-64"].setChecked(self._is.duration() == DurationType.V_64TH)

        voice = self._is.voice()
        GL.actions["voice-1"].setChecked(voice == 0)
        GL.actions["voice-2"].setChecked(voice == 1)
        GL.actions["voice-3"].setChecked(voice == 2)
        GL.actions["voice-4"].setChecked(voice == 3)

        GL.actions["pad-acciaccatura"].setChecked(self._is.noteType == NoteType.NOTE_ACCIACCATURA)
        GL.actions["pad-appoggiatura"].setChecked(self._is.noteType == NoteType.NOTE_APPOGGIATURA)
        GL.actions["pad-grace4"].setChecked(self._is.noteType  == NoteType.NOTE_GRACE4)
        GL.actions["pad-grace16"].setChecked(self._is.noteType == NoteType.NOTE_GRACE16)
        GL.actions["pad-grace32"].setChecked(self._is.noteType == NoteType.NOTE_GRACE32)

        GL.actions["beam-start"].setChecked(self._is.beamMode == BeamMode.BEAM_BEGIN)
        GL.actions["beam-mid"].setChecked(self._is.beamMode   == BeamMode.BEAM_MID)
        GL.actions["no-beam"].setChecked(self._is.beamMode    == BeamMode.BEAM_NO)
        GL.actions["beam32"].setChecked(self._is.beamMode     == BeamMode.BEAM_BEGIN32)
        GL.actions["auto-beam"].setChecked(self._is.beamMode  == BeamMode.BEAM_AUTO)

        #GL.mscore.updateDrumset()

    def undo(self):
        return self._undo

    def styleB(self, idx):
        return self._style.values[idx].v

    def tick2measure(self, tick):
        mb = self.first()
        while mb:
            if mb.type() != ElementType.MEASURE:
                continue
            m = mb
            st = m.tick()
            l =  m.tickLen()
            if tick >= st and tick < (st+l):
                return m
            nmb = mb.next
            while nmb:
                if nmb.type() == ElementType.MEASURE:
                    break
                nmb = nmb.next()
            if nmb == 0:
                return m
            mb = mb.next()

        print "-tick2measure %d not found\n" %tick
        return 0

    def tick2segment(self, tick, first, st):
        m = self.tick2measure(tick)
        if  m == 0:
            print "   no segment for tick %d\n" %tick
            return 0
        segment = m.first(st)
        while segment:
            t1 = segment.tick()
            nsegment = segment.next(st)
            if nsegment:
                t2 = nsegment.tick()
            else:
                t2 = 2147483647
            if ((tick == t1) and first) or ((tick == t1) and (tick < t2)):
                return segment
            segment = nsegment
        return 0

    def loadCompressedMsc(self, name):
        ext = QString(".mscz")
        self.info.setFile(name)
        if self.info.suffix().isEmpty():
            name += ext
            self.info.setFile(name)

    def checkSlurs(self):
        for e in self._gel:
            if e.type() != ElementType.SLUR:
                continue
            s = e
            n1 = s.startElement()
            n2 = s.endElement()
            if n1 == 0 or n2 == 0 or  n1 == n2:
                print "unconnected slur: removing\n"
                if n1:
                    n1.removeSlurFor(s)
                    n1.removeSlurBack(s)
                if n1 == 0:
                    print "  start at %d(%d) not found\n" %(s.tick(), s.track())
                if n2 == 0:
                    print "  end at %d(%d) not found\n" %(s.tick2(), s.track2())
                if (n1 or n2) and (n1==n2):
                    print "  start == end\n"
                idx = self._gel.indexOf(s)
                self._gel.removeAt(idx)

    def checkTuplets(self):
        m = self.firstMeasure()
        while m:
            for t in m.tuplets():
                if t.elements().empty():
                    print "empty tuplet: removing\n"
                    m.tuplets.removeAll(t)
            m = m.nextMeasure()

    def connectTies(self):
        tracks = self.nstaves() * VOICES
        mb = self.first()
        while mb:
            if mb.type() != ElementType.MEASURE:
                continue
            m = mb
            s = m.first()
            while s:
                for i in range(0, tracks):
                    el = s.element(i)
                    if el == 0 or el.type != ElementType.CHORD:
                        continue
                        for n in el.notes():
                            tie = n.tieFor()
                            if not tie:
                                continue
                            nnote = self.searchTieNote(n, s, i)
                            if nnote == 0:
                                print "next note at %d(measure %d) voice %d for tie not found delete tie\n" %(n.chord().tick(),  m.no(), n.chord().voice() )
                                n.setTieFor(0)
                            else:
                                tie.setEndNote(nnote)
                                nnote.setTieBack(tie)
                s = s.next()
            mb = mb.next()

    def importMusicXml(self, name):
        lx = LoadMusicXml()
        if not lx.load(name):
            return False
        self.setSaved(False)
        musicxml = MusicXml(lx.doc())
        musicxml.import_(self)
        self.connectTies()
        self.layoutAll = True
        self._created = False
        return True

    def firstMeasure(self):
        mb = self._measures.first()
        while mb  and  mb.type() != ElementType.MEASURE:
            mb = mb.next()
        return mb

    def rebuildMidiMapping(self):
        #self._midiMapping.clear()
        port    = 0
        channel = 0
        idx     = 0
        for part in self._parts:
            drum = part.useDrumset()
            for k in range(0, len(part.channel())):
                a = part.channel1(k)
                mm = MidiMapping()
                if drum:
                    mm.port = port
                    mm.channel = 9
                else:
                    mm.port    = port
                    mm.channel = channel
                    if channel == 15:
                        channel = 0
                        port = port + 1
                    else:
                        channel = channel + 1
                        if channel == 9:
                            channel = channel + 1

    def addPage(self):
        page = Page(self)
        page.setNo(len(self._pages))
        self._pages.append(page)
        return page

    def doLayout(self):
        self._needLayout = False
        if len(self._staves) == 0 or self.first() == 0:
            self._pages = []
            page = self.addPage()
            page.layout()
            page.setNo(0)
            page.setPos(0.0, 0.0)

            r = page.abbox()
            self.bspTree.initialize(r, 0)
            return

        self.layoutStage1()
        self.layoutStage2()
        self.layoutStage3()

        self.curMeasure  = self.first()
        self.curSystem   = 0
        self.firstSystem = True
        self.curPage = 0
        while self.curMeasure:
            self.getCurPage()
            om = self.curMeasure
            if not self.layoutPage():
                break
            if self.curMeasure == om:
                print "empty page ?\n"
                break
            self.curPage = self.curPage + 1
        for beam in self. _beams:
            beam.layout()
        tracks = self.nstaves() * VOICES
        for track in range(0,tracks):
            segment = self.firstSegment()
            while segment:
                e = segment.element(track)
                if e and e.isChordRest():
                    cr = e
                    if cr.beam():
                        continue
                    cr.layoutStem()
                segment = segment.next1()
        m = self.firstMeasure()
        while m:
            m.layout2()
            m = m.nextMeasure()
        for el in self._gel:
            if el:
                el.layout()
        n = self._pages.size() - self.curPage
        for i in range(0, n):
           self._pages[i] = 0
        n = self._systems.size() - self.curSystem
        for i in range(0, n):
            self._systems[i] = 0
        self.rebuildBspTree()
        self.layoutChanged.emit()


    def updateChannel(self):
        staffIdx   = 0
        #alist = list()
        for part in self._parts:
            for i in range(0, len(part.staves())):
                alist = list()
                mb = self.first()
                while mb:
                    if mb.type() != MEASURE:
                        continue
                    m = mb
                    for e in m.el():
                        if e.type() != STAFF_TEXT or e.staffIdx() != staffIdx:
                            continue
                        st = e
                        an = QString(st.channelName())
                        if an.isEmpty():
                            continue
                        a = part.channelIdx(an)
                        if a != -1:
                            ar = ARec()
                            ar.tick = st.tick()
                            ar.channel = a
                            alist.append(ar)
                        else:
                            print "channel <%s> not found\n" %qPrintable(an)
                    mb = mb.next()

            s = self.tick2segment(0, False, 0)
            while s:
                track = staffIdx * VOICES
                while track < staffIdx*VOICES+VOICES:
                    if not s.element(track):
                        continue
                    e = s.element(track)
                    if e.type() != CHORD:
                        continue
                    c = e
                    sc = 0
                    for ar in alist:
                        if ar.tick > c.tick():
                            break
                        sc = ar.channel
                    for note in c.notes():
                        if note.hidden():
                            continue
                        if note.tieBack():
                            continue
                            note.setSubchannel(sc)
                    track = track + 1
                s = s.next1()
            staffIdx = staffIdx + 1

    def startCmd(self):
        self.layoutAll = True
        if self._undo.active():
            self._undo.beginMacro()
            self._undo.push(self.SaveState(self))


    def end(self):
        if self.layoutAll:
            self._updateAll  = True
            self._needLayout = True
            self.startLayout = 0
        elif self.startLayout:
            self._updateAll = True
            self._needLayout = True
        if self._needLayout:
            self.doLayout()
        if self._updateAll:
            self.updateAll.emit()
        else:
            d = self._spatium * .5
            self.refresh.adjust(-d, -d, 2 * d, 2 * d)
            self.dataChanged(self.refresh)
        self.refresh     = QRectF()
        self.layoutAll   = False
        self._updateAll  = False
        self.startLayout = 0
        if not self.noteEntryMode():
           self.setPadState()

    def endCmd(self):
        if not self._undo.active():
            self.end()
            return
        noUndo = self._undo.current().childCount() <= 1
        if not noUndo:
            self.setClean(noUndo)
        self.end()
        self._undo.endMacro(noUndo)


    def renumberMeasures(self):
        measureNo = 0
        measure = self.firstMeasure()
        while measure:
            measureNo = measureNo +  measure.noOffset()
            if not measure.irregular():
                measureNo = measureNo + 1
            measure = measure.nextMeasure()

    def read(self, name):
        self._mscVersion = 110
        self._saved      = False
        self.info.setFile(name)

        cs = self.info.suffix()
        csl = cs.toLower()

        if csl == "mscz":
            if not loadCompressedMsc(name):
                return False
        elif csl == "msc" or csl == "mscx":
            if not loadMsc(name):
                return False
        else:
            if not Preferences().importStyleFile.isEmpty():
                f = QFile(Preferences().importStyleFile)
                if f.open(QIODevice.ReadOnly):
                    loadStyle(f)

            if csl == "xml":
                if not self.importMusicXml(name):
                    return False
            elif csl == "mxl":
                if not importCompressedMusicXml(name):
                    return False
            elif csl == "mid" or csl == "midi" or csl == "kar":
                if not importMidi(name):
                    return False
            elif csl == "md":
                if not importMuseData(name):
                    return False
            elif csl == "ly":
                if not importLilypond(name):
                    return False
            elif csl == "mgu" or csl == "sgu":
                if not importBB(name):
                    return False
            elif csl == "cap":
                if not importCapella(name):
                    return False
                    connectSlurs()
            elif csl == "ove":
                if not importOve(name):
            	    return False				    
            elif csl == "bww":
                if not importBww(name):
                    return False
            else:
                print "unknown file suffix <%s>, name <%s>\n" %qPrintable(cs) %qPrintable(name)
                QMessageBox.critical(0, "MuseScore", self.tr("Can't open file. File extension \"%1\" not supported.").arg(cs))
                return False

        self.renumberMeasures()
        self.checkSlurs()
        self.checkTuplets()
        self.rebuildMidiMapping()
        self.updateChannel()
        #self.fixPpitch()

        GL.mscore.updateRecentScores(self)

        self.startCmd()
        self._needLayout = True
        self.endCmd()
        return True

