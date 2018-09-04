#!/usr/bin/env python
#-*- coding:utf-8 -*-

from globals import *
import GL


class MidEvent:
      ME_NOTEOFF    = 0x80
      ME_NOTEON     = 0x90
      ME_POLYAFTER  = 0xa0
      ME_CONTROLLER = 0xb0
      ME_PROGRAM    = 0xc0
      ME_AFTERTOUCH = 0xd0
      ME_PITCHBEND  = 0xe0
      ME_SYSEX      = 0xf0
      ME_META       = 0xff
      ME_SONGPOS    = 0xf2
      ME_ENDSYSEX   = 0xf7
      ME_CLOCK      = 0xf8
      ME_START      = 0xfa
      ME_CONTINUE   = 0xfb
      ME_STOP       = 0xfc

      ME_NOTE       = 0x100
      ME_CHORD      = 0x101

class Seq(QObject):
    def __init__(self):
        super(Seq, self).__init__()
        self.running         = False
        self.playlistChanged = False
        self.cs              = 0
        self.cv              = 0
        self.events = dict()
        self.endTick  = 0
        self.state    = SEQ.STOP
        self.driver   = 0
        self.eventList = []
        if len(self.events.items()):
            self.playPos  = self.events.items()[0]

        self.playTime = 0.0
        self.startTime = 0.0
        self.curTick   = 0
        self.curUtick  = 0

        self.meterValue = [0.0, 0.0]
        self.meterPeakValue = [0.0, 0.0]
        self.peakTimer = [0, 0]

        self.heartBeatTimer = QTimer(self)
        self.connect(self.heartBeatTimer, SIGNAL("timeout()"), self, SLOT("heartBeat()"))
        self.heartBeatTimer.stop()

        self.noteTimer = QTimer(self)
        self.noteTimer.setSingleShot(True)
        self.connect(self.noteTimer, SIGNAL("timeout()"), self, SLOT("stopNotes()"))
        self.noteTimer.stop()
        self.driver = 0
        self.connect(self, SIGNAL("toGui(int)"), self, SLOT("seqMessage(int)"), Qt.QueuedConnection)

    def isRunning(self):
        return self.running

    def isPlaying(self):
        return self.state ==  SeqState.PLAY

    def isStopped(self):
        return self.state == SeqState.STOP

    def getEndTick(self):
        return self.endTick

    def isRealtime(self):
        return True

    def score(self):
        return self.cs

    def viewer(self):
        return self.cv

    def getDriver(self):
        return self.driver

    def stopWait(self):
        self.stop()
        mutex = QMutex()
        sleep = QWaitCondition()
        while self.state != SeqState.STOP:
            mutex.lock()
            sleep.wait(mutex, 100)
            mutex.unlock()

    def exit(self):
        if self.driver:
            if debugMode:
                print "Stop I/O\n"
            self.stopWait()
            del self.driver
            self.driver = 0
            
    def inputPorts(self):
        if self.driver:
            return self.driver.inputPorts()
        return list()

    def rewindStart(self):
        self.seek(0)

    def canStart(self):
        if not self.driver:
            return False
        if self.events.empty() or self.cs.playlistDirty() or self.playlistChanged:
            self.collectEvents()
        return (not self.events.empty() and self.endTick != 0)

    def start(self):
        if self.events.empty() or self.cs.playlistDirty() or self.playlistChanged:
            self.collectEvents()
        self.seek(self.cs.playPos())
        self.driver.startTransport()
      
    def stop(self):
        if not self.driver:
            return
        self.driver.stopTransport()
        if self.cv:
            self.cv.setCursorOn(False)
        if self.cs:
            self.cs.setLayoutAll(False)
            self.cs.setUpdateAll()
            self.cs.end()


    @pyqtSlot()
    def heartBeat(self):
        if self.state != SEQ.PLAY:
            return
        sc = GL.mscore.getSynthControl()
        if sc and self.driver and self.driver.getSynth():
            if ++self.peakTimer[0] >= peakHold:
                self.meterPeakValue[0] *= .7
            if ++self.peakTimer[1] >= peakHold:
                self.meterPeakValue[1] *= .7
                sc.setMeter(self.meterValue[0], self.meterValue[1], self.meterPeakValue[0], self.meterPeakValue[1])
        pp = GL.mscore.getPlayPanel()
        endTime = self.curTime() - self.startTime
        if pp:
            pp.heartBeat2(int(self.endTime))
        note = 0
        for (guiPos_key, guiPos_value) in self.events:
            f = self.cs.utick2utime(guiPos_key)
            if f >= endTime:
                break
            if guiPos_value.type() == MidEvent.ME_NOTEON:
                n = guiPos_value
                note1 = n.note()
                if n.velo():
                    note = note1
                    while note1:
                        note1.setSelected(True)
                        self.markedNotes.append(note1)
                        self.cs.addRefresh(note1.abbox())
                        if note1.tieFor():
                            note1 =  note1.tieFor().endNote()
                        else:
                            note1 = 0
            else:
                while note1:
                    note1.setSelected(False)
                    self.cs.addRefresh(note1.abbox())
                    self.markedNotes.removeOne(note1)
                    if note1.tieFor():
                        note1 =  note1.tieFor().endNote()
                    else:
                        note1 = 0
        if note:
            GL.mscore.currentScoreView().moveCursor(note.chord().segment(), -1)
            self.cv.adjustCanvasPosition(note, True)
            self.curTick  = note.chord().tick()
            self.curUtick = self.guiPos.key()
            if pp:
                pp.heartBeat(self.curTick, self.curUtick)
                GL.mscore.setPos(self.curTick)
        pre = GL.mscore.getPianorollEditor()
        if pre and pre.isVisible():
            pre.heartBeat(self)
        self.cs.end()

    @pyqtSlot()
    def stopNotes(self):
        for event in self.eventList:
            self.sendEvent(event)
        self.eventList.clear()

    @pyqtSlot(int)
    def seqMessage(self, msg):
        if msg == '0' :
            self.guiStop()
            self.heartBeatTimer.stop()
            if self.driver and self.driver.getSynth() and GL.mscore.getSynthControl():
                self.meterValue[0]     = .0
                self.meterValue[1]     = .0
                self.meterPeakValue[0] = .0
                self.meterPeakValue[1] = .0
                self.peakTimer[0]       = 0
                self.peakTimer[1]       = 0
                GL.mscore.getSynthControl().setMeter(0.0, 0.0, 0.0, 0.0)
        elif msg == '1':
            self.emit.started()
            self.heartBeatTimer.start(1000/guiRefresh)
        else:
            print "MScore::Seq:: unknown seq msg %d\n", msg

    def setScoreView(self, v):
        if self.cv !=v and self.cs:
            self.disconnect(self.cs, SIGNAL("selectionChanged(int)"), self.selectionChanged)
            self.markedNotes = list()
            self.stopWait()
            if v:
                self.cs = v.score()
            else:
                self.cs = 0
        self.cv = v
        if self.cv:
            self.cs = self.cv.score()
        else:
            self.cs = 0
        self.playlistChanged = True
        if self.cs:
            self.connect(self.cs, SIGNAL("selectionChanged(int)"), self.selectionChanged)
            self.initInstruments()

    def selectionChanged(self, mode):
        if self.cs == 0 or self.driver == 0:
            return
        tick = self.cs.pos()
        if tick == -1:
            return
        if (mode !=  SelState.SEL_LIST) or (self.state == SeqState.STOP):
            self.cs.setPlayPos(tick)
        else:
            self.seek(tick)


