#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-                                                                            

from Score import *
import Actions
from Style import *
from Updatechecker import *
from Undo import *
from Navigator import *
from Scoretab import *
import Voiceselector
from Barline import *
from Magbox import *
from Palette import *
from Hairpin import *
from Volta import *
from Ottava import *
from Pedal import *
from Keysig import *
from Bracket import *
from Breath import *
from Repeat import *
from Tremolo import *
from Glissando import *
from Arpeggio import *
from Icons import *
from Trill import *
from Clef import *
from Accidental import *
from Articulation import *
from Dynamics import *
from Layoutbreak import *
from Playpanel import *
from Spacer import *
from Slur import *
from Pagesettings import *
from Instrtemplate import *
from aboutbox import Ui_AboutBox
from insertmeasuresdialog import Ui_InsertMeasuresDialogBase
from measuresdialog import Ui_MeasuresDialogBase
from Symboldialog import *
from Timedialog import *

def setMscoreLocale(localeName):
    translatorList = []
    for t in translatorList:
        qApp.removeTranslator(t)

    if localeName.toLower() == "system":
        localeName = QLocale.system().name()

    translator = QTranslator()
    lp = QString(GL.mscoreGlobalShare + "locale\\" + QString("mscore_") + localeName)
    if not translator.load(lp):
        print "load translator <%s> failed\n" %lp.toAscii().data()
    else:
        qApp.installTranslator(translator)
        translatorList.append(translator)

    resourceDir = GL.mscoreGlobalShare + "locale\\"
    qtTranslator = QTranslator()
    if qtTranslator.load(QLatin1String("qt_") + localeName, resourceDir):
        qApp.installTranslator(qtTranslator)
        translatorList.append(qtTranslator)

def initShortcuts():
    for i in range(0, len(Actions.sc)):
        if Actions.sc[i].xml == 0:
            break
        GL.shortcuts[Actions.sc[i].xml] = Actions.sc[i]

def setDefaultStyle():
    for i in range(0, TEXT_STYLE.TEXT_STYLES):
        GL.defaultTextStyles.append(defaultTextStyleArray[i])



class AboutBoxDialog(QDialog, Ui_AboutBox):
    
    def __init__(self):                                                                        
        super(AboutBoxDialog, self).__init__()                                                 
        self.setupUi(self)                                                                     
        self.revisionLabel.setText(self.tr("Revision: %1").arg(GL.revision))

class InsertMeasuresDialog(QDialog, Ui_InsertMeasuresDialogBase):                                
                                                                                                                                                                                                  
    def __init__(self):                                                                        
        super(InsertMeasuresDialog, self).__init__()                                         
        self.setupUi(self)                                                                   
                                                                                                 
    def slotAccept(self):                                                                      
        n = self.insmeasures.value()                                                         
        if GL.mscore.currentScore():
            GL.mscore.currentScore().cmdInsertMeasures(n)

class MeasuresDialog(QDialog, Ui_MeasuresDialogBase):                                            
                                                                                                                                                                                                 
    def __init__(self):                                                                        
        super(MeasuresDialog, self).__init__()                                               
        self.setupUi(self)                                                                   
                                                                                                 
    def slotAccept(self):                                                                      
        n = self.insmeasures.value()                                                         
        if GL.mscore.currentScore():
            GL.mscore.currentScore().cmdAppendMeasures(n)

class NoteButton(QToolButton):                                                                   
                                                                                                 
    def __init__(self):                                                                        
        super(NoteButton, self).__init__()                                                   
                                                                                                 
    def sizeHint(self):                                                                        
        w = Preferences().noteEntryIconWidth                                                   
        h = Preferences().noteEntryIconHeight
        return QSize(w, h)

class MuseScore(QMainWindow):
                                                                                                 
    def __init__(self, parent=None):                                                                      
        super(MuseScore, self).__init__(parent)
        self._sstate =  SS.STATE_INIT
        self.setIconSize(QSize(Preferences().iconWidth, Preferences().iconHeight))               
        self.setWindowTitle(QString("Muse 3.0"))                                                 
        self.ucheck = UpdateChecker()                                                           
        self.setAcceptDrops(True)                                                                
        self._undoGroup = UndoGroup()                                                           
        self.scoreList = list()
        self.dataPath = QString()
        self.cs = 0
        self.cv = 0                                                                              
        self.layout = 0                                                                          
        self.splitter = 0                                                                        
        self.tab1 = 0                                                                            
        self.tab2 = 0                                                                            
        self.navigator = 0                                                                       
        self.mainWindow = QSplitter()
        self.menuDisplay = 0                                                                     
        self.openRecent = 0                                                                      
        self.mag = 0                                                                             
        self.playId = QAction(None)
        self._progressBar = 0                                                                    
        self.preferenceDialog = 0                                                                
        self.cpitchTools = 0                                                                     
        self.fileTools = QToolBar()
        self.transportTools = 0                                                                  
        self.entryTools = 0                                                                      
        self._textTools = 0                                                                      
        self.voiceTools = 0                                                                      
        self._webPage = 0                                                                        
        self.instrList = 0                                                                       
        self.measuresDialog = 0                                                                  
        self.insertMeasuresDialog = 0                                                            
        self._fileMenu = 0                                                                       
        self.menuEdit = 0                                                                        
        self.menuNotes = 0                                                                       
        self.menuLayout = 0                                                                      
        self.menuStyle = 0                                                                       
        self.searchDialog = 0                                                                    
        self.searchCombo = 0                                                                     
        self.networkManager = 0                                                                  
        self.playPanel = 0                                                                       
        self.iledit = 0                                                                          
        self.synthControl = 0                                                                    
        self.inspector = 0                                                                       
        self.measureListEdit = 0                                                                 
        self.pageSettings = 0                                                                    
        self.symbolDialog = 0                                                                    
        self.clefPalette = 0                                                                     
        self.keyPalette = 0                                                                      
        self.keyEditor = 0                                                                       
        self.chordStyleEditor = 0                                                                
        self.timePalette = 0                                                                     
        self.linePalette = 0                                                                     
        self.bracketPalette = 0                                                                  
        self.barPalette = 0                                                                      
        self.fingeringPalette = 0                                                                
        self.noteAttributesPalette = 0                                                           
        self.accidentalsPalette = 0                                                              
        self.dynamicsPalette = 0                                                                 
        self.layoutBreakPalette = 0                                                              
        self._statusBar = 0                                                                      
        self._modeText = 0                                                                       
        self._positionLabel = 0                                                                  
        self.newWizard = 0                                                                       
        self.paletteBox = 0                                                                      
        self.drumPalette = 0                                                                     
        self.drumset = 0                                                                         
        self._midiinEnabled = True                                                               
        self._speakerEnabled = True                                                              
        self.lastOpenPath = Preferences().workingDirectory                                       
        self.plugins = 0                                                                         
        self.pluginPath = 0                                                                      
        self.autoSaveTimer = QTimer()
        self.pluginMapper = 0                                                                    
        self.pianorollEditor = 0                                                                 
        self._splitScreen = False                                                                
        self._horizontalSplit = True
        self.rev = 0
        self.initUI()

    def closeEvent(self, ev):
        #unloadPlugins()
        removeList = list()
        for score in self.scoreList:
            if score.created() and not score.dirty():
                removeList.append(score)
            else:
                if self.checkDirty(score):
                    ev.ignore()
                    return
                if score.created() and score.dirty():
                    removeList.append(score)
        for score in self.scoreList:
            self.scoreList.remove(score)
      
        self.writeSessionFile(True)
        for score in self.scoreList:
            if not score.tmpName().isEmpty():
                f = QFile(score.tmpName())
                f.remove()
        settings = QSettings()

        for i in range(0, RECENT_LIST_SIZE):
            pass
            #settings.setValue(QString("recent-%1").arg(i), GL.recentScores[i])

        settings.setValue("scores", len(self.scoreList))
        if self.cs != 0:
            curScore = self.scoreList.index(self.cs)
        else:
            curScore = -1
        settings.setValue("currentScore", curScore)

        idx = 0
        for s in self.scoreList:
            settings.setValue(QString("score-%1").arg(idx), s.fileInfo().absoluteFilePath())
            idx = idx + 1

        settings.setValue("lastSaveCopyDirectory", self.lastSaveCopyDirectory)
        settings.setValue("lastSaveDirectory", self.lastSaveDirectory)

        if self.synthControl:
            self.synthControl.updatePreferences()

        self.writeSettings()
        if self.inspector:
            self.inspector.writeSettings()
        GL.seq.stopWait()

        GL.seq.exit()
        ev.accept()
        if preferences.dirty:
            preferences.write()
        qApp.quit()

    def dragEnterEvent(self, event):
        data = event.mimeData()
        if data.hasUrls():
            ul = event.mimeData().urls()
            for u in ul:
                if u.scheme() == "file":
                    fi = QFileInfo(u.toLocalFile())
                    event.acceptProposedAction()
                    
    def dropEvent(self, event):
        data = event.mimeData()
        if data.hasUrls():
            view = -1
            for u in event.mimeData().urls():
                if u.scheme() == "file":
                    score = Score(defaultStyle)
                    if score.read(u.toLocalFile()):
                        view = self.appendScore(score)
                    else:
                        del score

            if view != -1:
                self.setCurrentScoreView(view)
            event.acceptProposedAction()





    def getShortcut(self,id):
        s = GL.shortcuts[id]
        if s == 0 :
            print "internal error: shortcut <%s> not found\n" %id
            return 0
        return s

    def getAction(self, id):
        s = self.getShortcut(id)
        if s == 0 :
            return 0
        else:
            a = QAction(s.xml, self)
            s.action  = a
            a.setData(s.xml)
            if s.key != 0:
                a.setShortcut(s.key)
            else :
                a.setShortcuts(s.standardKey)
            a.setShortcutContext(s.context)
            if s.help != 0:
                a.setToolTip(s.help)
                a.setWhatsThis(s.help)
            else:
                a.setToolTip(s.descr)
                a.setWhatsThis(s.descr)
            if s.standardKey != QKeySequence.UnknownKey:
                kl = QKeySequence(a.shortcuts())
                if len(kl)!= 0:
                    s = QString(a.toolTip())
                    s += " ("
                    for i in range (0, kl.size()):
                        if i:
                            s += ","
                            s += kl[i].toString(QKeySequence.NativeText)
                    s += ")"
                    a.setToolTip(s)
            elif s.key != 0:
                a.setToolTip(a.toolTip() + "(" + s.key.toString(QKeySequence.NativeText) + ")" )
            if s.text != 0:
                a.setText(s.text)
            if s.icon != -1:
                a.setIcon(GL.icons[s.icon])
        return s.action

    def setDrumPalette(self, p):
        self.drumPalette = p

    def setNormalState(self):
        self.changeState(SS.STATE_NORMAL)

    def setEditState(self):
        self.changeState(SS.STATE_EDIT)

    def setNoteEntryState(self):
        self.changeState(SS.STATE_NOTE_ENTRY)

    def setPlayState(self):
        self.changeState(SS.STATE_PLAY)

    def setSearchState(self):
        self.changeState(SS.STATE_SEARCH)

    def fileMenu(self):
        return self._fileMenu

    def getPlayPanel(self):
        return self.playPanel

    def currentScore(self):
        return self.cs

    def noScore(self):
        return self.scoreList.isEmpty()

    def  setDrumPalette(self, p):
        self.drumPalette = p

    def getSynthControl(self):
        return self.synthControl

    def getPianorollEditor(self):
        return self.pianorollEditor

    def currentScoreView(self):
        return self.cv

    def splitScreen(self):
        return self._splitScreen

    def setRevision(self, r):
        self.rev = r

    def state(self):
        return self._sstate

    def revision(self):
        return self.rev

    def  version(self):
        return VERSION

    def checkForUpdate(self):
        if self.ucheck:
            self.ucheck.check(self.revision(), self.sender() != 0)

    def magChanged(self, idx):
        if self.cv:
            self.cv.setMag(idx, self.mag.getMag(self.cv))

    def about(self):
        ab = AboutBoxDialog()
        ab.show()
        ab.exec_()

    def writeSettings(self):
        settings = QSettings()
        settings.beginGroup("MainWindow")
        settings.setValue("size", self.size())
        settings.setValue("pos", self.pos())
        settings.setValue("maximized", self.isMaximized())
        settings.setValue("showPanel", self.paletteBox and self.paletteBox.isVisible())
        settings.setValue("state", self.saveState())
        settings.setValue("splitScreen", self._splitScreen)
        settings.setValue("inspectorSplitter", self.mainWindow.saveState())
        if self._splitScreen:
            settings.setValue("split", self._horizontalSplit)
            settings.setValue("splitter", self.splitter.saveState())
        settings.endGroup()
        if self.paletteBox and self.paletteBox.dirty():
            dir = QDir()
            dir.mkpath(GL.dataPath)
            self.paletteBox.write(GL.dataPath + "/mscore-palette.xml")
        if self.timePalette and self.timePalette.dirty():
            self.timePalette.save()
        if self.keyEditor and self.keyEditor.dirty():
            self.keyEditor.save()
        if self.chordStyleEditor:
            self.chordStyleEditor.save()

    def checkDirty(self, s):
        if s.dirty():
            n = QMessageBox.warning(self, "MuseScore",
               self.tr("Save changes to the score \"%1\"\n"
               "before closing?").arg(s.name()),
               QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
               QMessageBox.Save)
            if n == QMessageBox.Save:
                if s.isSavable():
                    if not s.saveFile(False):
                        return True
                    else:
                        if not s.saveAs(False):
                            return True
            elif n == QMessageBox.Cancel:
                return True
        return False

    def loadFile(self):
        fn = QFileDialog.getOpenFileName(
        self,
        self.tr("Muse: Load Score"),
        self.lastOpenPath,
        #self.tr("All Supported Files (*.mscz *.mscx *.msc *.xml *.mxl *.mid *.midi *.kar *.md *.mgu *.MGU *.sgu *.SGU *.cap *.ove *.bww)")+
        #self.tr("MuseScore Files (*.mscz *.mscx *.msc)")+
        self.tr("MusicXML Files (*.xml *.mxl)"))
        #self.tr("MIDI Files (*.mid *.midi *.kar)")+
        #self.tr("Muse Data Files (*.md)")+
        #self.tr("Capella Files (*.cap)")+
        #self.tr("Bagpipe Music Writer Files (*.bww)")+
        #self.tr("BB Files <experimental> (*.mgu *.MGU *.sgu *.SGU)")+
        #self.tr("Overture Files <experimental> (*.ove)"))
        self.openScore(fn)

    def dirtyChanged(self, score):
        idx = self.scoreList.indexOf(score)
        if idx == -1:
            print "score not in list\n"
            return
        label = QString(score.name())
        if score.dirty():
            label = label + "*"
        self.tab1.setTabText(idx, label)
        self.tab2.setTabText(idx, label)

    def selectionChanged(self, state):
        GL.actions["cut"].setEnabled(state)
        GL.actions["copy"].setEnabled(state)

    def setPos(self, t):
        if self.cs == 0 or t < 0:
            return
        s = self.cs.sigmap()
        (bar, beat, tick) = s.tickValues(t)
        self._positionLabel.setText(self.tr("Bar %1 Beat %2.%3") .arg(bar + 1,  3, 10, QLatin1Char(' ')) .arg(beat + 1, 2, 10, QLatin1Char(' ')).arg(tick,     3, 10, QLatin1Char('0')))

    def appendScore(self, score):
        self.connect(score, SIGNAL("dirtyChanged(PyQt_PyObject)"),  self.dirtyChanged)
        self.connect(score, SIGNAL("selectionChanged(int)"), self.selectionChanged)
        self.connect(score, SIGNAL("posChanged(int)"), self.setPos)

        index = len(self.scoreList)
        for i in range(0, len(self.scoreList)):
            if self.scoreList[i].filePath() == score.filePath():
                self.removeTab(i)
                index = i
                break
        self.scoreList.insert(index, score)
        self.tab1.blockSignals(True)
        self.tab2.blockSignals(True)
        self.tab1.insertTab(index, score.name())
        self.tab2.insertTab(index, score.name())
        self._undoGroup.addStack(score.undo())
        self.tab1.blockSignals(False)
        self.tab2.blockSignals(False)
        return index


    def writeSessionFile(self, cleanExit):
        print "write session file\n"
        dir = QDir()
        dir.mkpath(GL.dataPath)
        f = QFile(GL.dataPath + "\session")
        if not f.open(QIODevice.WriteOnly):
            print "cannot create session file <%s>\n" %f.fileName().toAscii().data()
            return
        xml = Xml(f)
        xml.header()
        xml.stag("muse 3.0 version=\"" "1.0" "\"")
        if cleanExit:
             xml.tagE("clean")
        else:
            xml.tagE("dirty")
        for score in self.scoreList:
            xml.stag("Score")
            xml.tag("created", score.created())
            xml.tag("dirty", score.dirty())
            if score.tmpName().isEmpty():
                xml.tag("path", score.fileInfo().absoluteFilePath())
            else:
                xml.tag("name", score.fileInfo().absoluteFilePath())
                xml.tag("path", score.tmpName())
            xml.etag()
        tab = 0
        idx = 0
        for i in range(0, self.tab1.count()):
            v = self.tab1.view(i)
            if v:
                if v == self.cv:
                    tab = 0
                    idx = i
                xml.stag("ScoreView")
                xml.tag("tab", tab)
                xml.tag("idx", i)
                if v.magIdx() == MAG.MAG_FREE:
                    xml.tag("mag", v.mag())
                else:
                    xml.tag("magIdx", v.magIdx())
                    xml.tag("x",   v.xoffset() / GL.DPMM)
                    xml.tag("y",   v.yoffset() / GL.DPMM)
                    xml.etag()
        if self.splitScreen():
            for i in range(0, self.tab2.count()):
                v = self.tab2.view(i)
                if v:
                    if v  == self.cv:
                        tab = 1
                        idx = i
                    xml.stag("ScoreView")
                    xml.tag("tab", 1)
                    xml.tag("idx", i)
                    if v.magIdx() == MAG.MAG_FREE:
                        xml.tag("mag", v.mag())
                    else:
                        xml.tag("magIdx", v.magIdx())
                    xml.tag("x",   v.xoffset() / GL.DPMM)
                    xml.tag("y",   v.yoffset() / GL.DPMM)
                    xml.etag()
        xml.tag2("tab", tab)
        xml.tag2("idx", idx)
        xml.etag()
        f.close()
        if cleanExit:
            pass


    def openScore(self, fn):
        if fn.isEmpty():
            return
        score = Score(defaultStyle)
        if score.read(fn):
            self.setCurrentScoreView(self.appendScore(score))
            self.lastOpenPath = score.fileInfo().path()
            self.writeSessionFile(False)

    def saveFile(self):
        self.setWindowTitle("Muse 3.0: " + self.cs.name())
        idx = self.scoreList.indexOf(self.cs)
        self.tab1.setTabText(idx, self.cs.name())
        self.tab2.setTabText(idx, self.cs.name())
        tmp = self.cs.tmpName()
        if not tmp.isEmpty():
            f = QFile(tmp)
            if not f.remove():
                print "cannot remove temporary file <%s>\n" %f.fileName().toAscii().data()
                self.cs.setTmpName("")
        self.writeSessionFile(False)

    def clipboardChanged(self):
        ms = QApplication.clipboard().mimeData()
        if ms == 0:
            return
        formats = ms.formats()

        flag = ms.hasFormat(mimeSymbolFormat) or ms.hasFormat(mimeStaffListFormat) or ms.hasFormat(mimeSymbolListFormat) or ms.hasText()
        GL.actions["paste"].setEnabled(flag)


    def updateRecentScores(self, score):
        path = score.fileInfo().absoluteFilePath()
        GL.recentScores.removeAll(path)
        GL.recentScores.prepend(path)

    def changeState(self, val):
        if self._sstate == val:
            return
        for v, s in GL.shortcuts.items():
            if not s.action:
                continue
            if s.xml =="undo":
                s.action.setEnabled((s.state & val) and self._undoGroup.canUndo())
            elif s.xml == "redo":
                s.action.setEnabled((s.state & val) and self._undoGroup.canRedo())
            elif s.xml =="cut":
                s.action.setEnabled(self.cs and self.cs.selection().state())
            elif s.xml =="copy":
                  s.action.setEnabled(self.cs and self.cs.selection().state())
            elif s.xml == "synth-control":
                if self.seq:
                    driver = self.seq.getDriver()
                else:
                    driver = 0
                s.action.setEnabled(driver and driver.getSynth())
            else:
                s.action.setEnabled(s.state & val)
            if val == SS.STATE_DISABLED:
                names = ["file-open", "file-new", "quit"]
                for p in names:
                    if p == s.xml:
                        s.action.setEnabled(True)
        if val != SS.STATE_SEARCH and self.searchDialog:
            self.searchDialog.hide()

        enable = val != SS.STATE_DISABLED
        ol = self.menuBar().children()
        for o in ol:
            menu = o
            if not menu:
                continue
            s = QString(menu.objectName())
            if s == "File" or s == "Help" or s == "Edit":
                continue
            menu.setEnabled(enable)
        if self.paletteBox:
            self.paletteBox.setEnabled(enable)
        self.transportTools.setEnabled(enable and not self.noSeq)
        self.cpitchTools.setEnabled(enable)
        self.mag.setEnabled(enable)
        self.entryTools.setEnabled(enable)

        if val == SS.STATE_DISABLED:
            self._modeText.setText(self.tr("no score"))
            self._modeText.show()
            if self.inspector:
                self.inspector.hide()
        elif val== SS.STATE_NORMAL:
            self._modeText.hide()
            if self.searchDialog:
                self.searchDialog.hide()
        elif val == SS.STATE_NOTE_ENTRY:
            self._modeText.setText(self.tr("note entry mode"))
            self._modeText.show()
        elif val == SS.STATE_EDIT:
            self._modeText.setText(self.tr("edit mode"))
            self._modeText.show()
        elif val == SS.STATE_PLAY:
            self._modeText.setText(self.tr("play"))
            self._modeText.show()
        elif val == SS.STATE_SEARCH:
            if self.searchDialog == 0:
                self.searchDialog = QWidget()
                self.searchDialog.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
                searchDialogLayout = QHBoxLayout()
                self.searchDialog.setLayout(searchDialogLayout)
                self.layout.insertWidget(2, self.searchDialog)

                searchExit = QToolButton()
                searchExit.setIcon(QIcon("data\cancel.png"))
                self.connect(searchExit, SIGNAL("clicked()"), self.endSearch)
                searchDialogLayout.addWidget(searchExit)

                searchDialogLayout.addWidget(QLabel(self.tr("Go To: ")))
                self.searchCombo = QLineEdit()
                self.searchCombo.setInputMask("0000")
                searchDialogLayout.addWidget(self.searchCombo)

                searchDialogLayout.addStretch(10)
                self.searchDialog.hide()

                self.connect(self.searchCombo, SIGNAL("textChanged(QString)"), self.searchTextChanged)
                self.connect(self.searchCombo, SIGNAL("returnPressed()"), self.endSearch)
            self.searchCombo.clear()
            self.searchCombo.setFocus()
            self.searchDialog.show()
            self._modeText.setText(self.tr("Search"))
            self._modeText.show()
        else:
             print "MuseScore.setState: illegal state %d\n" %val

        a = GL.actions["note-input"]
        a.setChecked(val == SS.STATE_NOTE_ENTRY)
        self._sstate = val

## meunu function

    def drumPaletteSelected(self, idx):
        if self.cs == 0:
            return
        padState = self.cs.inputState()
        ds          = padState.drumset()
        if ds == 0:
            return
        i = 0
        for pitch in range(0, 128):
            if not self.drumset.isValid(pitch):
                continue
            if i == idx:
                padState.setDrumNote(pitch)
                padState.track    = (padState.track / VOICES) * VOICES + ds.voice(pitch)
                self.cs.setPadState()
                break
            i = i+1


    def showPalette(self, visible):
        act = GL.actions["toggle-palette"]
        if self.paletteBox == 0:
            self.paletteBox = PaletteBox(self)

            self.connect(self.paletteBox, SIGNAL("paletteVisible(bool)"), act.setChecked)
            self.addDockWidget(Qt.LeftDockWidgetArea, self.paletteBox)

            f = QFile(GL.dataPath + "/" + "mscore-palette.xml")
            if preferences.firstStart12:
                f.remove()
                preferences.firstStart12 = False
                preferences.dirty  = True

            if not useFactorySettings:
                if f.exists():
                    if self.paletteBox.read(f):
                        self.paletteBox.setShown(visible)
                        act.setChecked(visible)
                        return


            notePalette = Palette()
            notePalette.setName(self.tr("Grace Notes"))
            notePalette.setGrid(27, 40)
            notePalette.setDrawGrid(True)

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_ACCIACCATURA)
            ik.setAction(GL.actions["pad-acciaccatura"])
            notePalette.append1(ik, self.tr("Acciaccatura"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_APPOGGIATURA)
            ik.setAction(GL.actions["pad-appoggiatura"])
            notePalette.append1(ik, self.tr("Appoggiatura"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_GRACE4)
            ik.setAction(GL.actions["pad-grace4"])
            notePalette.append1(ik, self.tr("Quarter grace note"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_GRACE16)
            ik.setAction(GL.actions["pad-grace16"])
            notePalette.append1(ik, self.tr("16th grace note"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_GRACE32)
            ik.setAction(GL.actions["pad-grace32"])
            notePalette.append1(ik, self.tr("32nd grace note"))

            self.paletteBox.addPalette(notePalette)


            drumPalette = Palette()
            drumPalette.setName(self.tr("Drums"))
            drumPalette.setMag(0.8)
            drumPalette.setSelectable(True)
            drumPalette.setGrid(42, 60)
            drumPalette.setDrumPalette(True)

            self.paletteBox.addPalette(drumPalette)


            sp = Palette()
            sp.setName(self.tr("Clefs"))
            sp.setMag(0.8)
            sp.setGrid(33, 60)
            sp.setYOffset(1.0)
            clefs = [ 0, 1, 2, 3, 16, 9, 10, 11, 12, 15, 4, 17, 18, 5, 6, 7, 8, 14, 13 ]

            for i in range(0, 19):
                j = clefs[i]
                k = Clef(GL.gscore)
                k.Clef1(j)
                sp.append1(k, qApp.translate("clefTable", clefTable[j].name))
            self.paletteBox.addPalette(sp)


            sp = Palette()
            sp.setName(self.tr("Key Signatures"))
            sp.setMag(0.8)
            sp.setGrid(56, 45)
            sp.setYOffset(6.0)

            for i in range(0, 7):
                k = KeySig(GL.gscore)
                k.setSubtype(i+1)
                sp.append1(k, qApp.translate("MuseScore", keyNames[i*2]))
            for i in range(-7, 0):
                k = KeySig(GL.gscore)
                k.setSubtype(i & 0xff)
                sp.append1(k, qApp.translate("MuseScore", keyNames[(7 + i) * 2 + 1]))
            k = KeySig(GL.gscore)
            k.setSubtype(0)
            sp.append1(k, qApp.translate("MuseScore", keyNames[14]))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Time Signatures"))
            sp.setMag(.8)
            sp.setGrid(42, 38)

            a = TimeSig(GL.gscore)
            a.TimeSig2(2, 2)
            sp.append1(a, "2/2")

            a = TimeSig(GL.gscore)
            a.TimeSig2(4, 2)
            sp.append1(a, "2/4")

            a = TimeSig(GL.gscore)
            a.TimeSig2(4, 3)
            sp.append1(a, "3/4")

            a = TimeSig(GL.gscore)
            a.TimeSig2(4, 4)
            sp.append1(a, "4/4")

            a = TimeSig(GL.gscore)
            a.TimeSig2(4, 5)
            sp.append1(a, "5/4")

            a = TimeSig(GL.gscore)
            a.TimeSig2(4, 6)
            sp.append1(a, "6/4")

            a = TimeSig(GL.gscore)
            a.TimeSig2(8, 3)
            sp.append1(a, "3/8")

            a = TimeSig(GL.gscore)
            a.TimeSig2(8, 6)
            sp.append1(a, "6/8")

            a = TimeSig(GL.gscore)
            a.TimeSig2(8, 9)
            sp.append1(a, "9/8")

            a = TimeSig(GL.gscore)
            a.TimeSig2(8, 12)
            sp.append1(a, "12/8")

            a = TimeSig(GL.gscore)
            a.TimeSig1(TSIG_FOUR_FOUR)
            sp.append1(a, self.tr("4/4 common time"))

            a = TimeSig(GL.gscore)
            a.TimeSig1(TSIG_ALLA_BREVE)
            sp.append1(a, self.tr("2/2 alla breve"))
            self.paletteBox.addPalette(sp)


            sp = Palette()
            sp.setName(self.tr("Barlines"))
            sp.setMag(0.8)
            sp.setGrid(42, 38)

            t = {  BarType.NORMAL_BAR:       QT_TR_NOOP("Normal"),
                   BarType.BROKEN_BAR:       QT_TR_NOOP("Dashed"),
                   BarType.END_BAR:          QT_TR_NOOP("End Bar"),
                   BarType.DOUBLE_BAR:       QT_TR_NOOP("Double Bar"),
                   BarType.START_REPEAT:     QT_TR_NOOP("Start Repeat"),
                   BarType.END_REPEAT:       QT_TR_NOOP("End Repeat"),
                   BarType.END_START_REPEAT: QT_TR_NOOP("End-Start Repeat")
                  }
            for (type, name) in t.items():
                b  = BarLine(GL.gscore)
                b.setSubtype(type)
                sp.append1(b, self.tr(name))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Lines"))
            sp.setMag(.8)
            sp.setGrid(84, 23)

            l = GL.gscore.spatium() * 7

            slur = Slur(GL.gscore)
            slur.setLen(l)
            slur.setId(0)
            sp.append1(slur, self.tr("Slur"))

            hairpin0 = Hairpin(GL.gscore)
            hairpin0.setLen(l)
            hairpin0.setSubtype(0)
            sp.append1(hairpin0, self.tr("Crescendo"))

            hairpin1 = Hairpin(GL.gscore)
            hairpin1.setLen(l)
            hairpin1.setSubtype(1)
            sp.append1(hairpin1, self.tr("Diminuendo"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setSubtype(VOLTA.VOLTA_CLOSED)
            volta.setText("1.")
            il = list()
            il.append(1)
            volta.setEndings(il)
            sp.append1(volta, self.tr("Prima volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setSubtype(VOLTA.VOLTA_CLOSED)
            volta.setText("2.")
            il = []
            il.append(2)
            volta.setEndings(il)
            sp.append1(volta, self.tr("Seconda volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setSubtype(VOLTA.VOLTA_CLOSED)
            volta.setText("3.")
            il = []
            il.append(3)
            volta.setEndings(il)
            sp.append1(volta, self.tr("Terza volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setSubtype(VOLTA.VOLTA_OPEN)
            volta.setText("2.")
            il = []
            il.append(2)
            volta.setEndings(il)
            sp.append1(volta, self.tr("Seconda volta 2"))

            ottava = Ottava(GL.gscore)
            ottava.setLen(l)
            ottava.setSubtype(0)
            sp.append1(ottava, self.tr("8va"))

            ottava = Ottava(GL.gscore)
            ottava.setLen(l)
            ottava.setSubtype(1)
            sp.append1(ottava, self.tr("15ma"))

            ottava = Ottava(GL.gscore)
            ottava.setLen(l)
            ottava.setSubtype(2)
            sp.append1(ottava, self.tr("8vb"))

            ottava = Ottava(GL.gscore)
            ottava.setLen(l)
            ottava.setSubtype(3)
            sp.append1(ottava, self.tr("15mb"))

            pedal = Pedal(GL.gscore)
            pedal.setLen(l)
            sp.append1(pedal, self.tr("pedal"))

            trill = Trill(GL.gscore)
            trill.setLen(l)
            sp.append1(trill, self.tr("Trill line"))

            textLine = TextLine(GL.gscore)
            textLine.setLen(l)
            textLine.setBeginText1("VII")
            textLine.setEndHook(True)
            textLine.setEndHookHeight(Spatium(1.5))
            sp.append1(textLine, self.tr("Text line"))

            line = TextLine(GL.gscore)
            line.setLen(l)
            line.setDiagonal(True)
            sp.append1(line, self.tr("Line"))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Arpeggio && Glissando"))
            sp.setGrid(27, 60)

            for i in range(0, 4):
                a = Arpeggio(GL.gscore)
                a.setSubtype(i)
                sp.append1(a, self.tr("Arpeggio"))

            for i in range(0, 2):
                a = Glissando(GL.gscore)
                a.setSubtype(i)
                sp.append1(a, self.tr("Glissando"))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Breath && Pauses"))
            sp.setGrid(42, 40)

            for i in range(0, 4):
                a = Breath(GL.gscore)
                a.setSubtype(i)
                if i < 2:
                    sp.append1(a, self.tr("Breath"))
                else:
                    sp.append1(a, self.tr("Caesura"))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Brackets"))
            sp.setMag(0.7)
            sp.setGrid(42, 60)

            b1 = Bracket(GL.gscore)
            b1.setSubtype(BRACKET.BRACKET_NORMAL)
            b2 = Bracket(GL.gscore)
            b2.setSubtype(BRACKET.BRACKET_AKKOLADE)
            #b1.setHeight(_spatium * 7)
            #b2.setHeight(_spatium * 7)

            sp.append1(b1, self.tr("Bracket"))
            sp.append1(b2, self.tr("Akkolade"))

            self.paletteBox.addPalette(sp)

            nn = ArticulationIdx.ARTICULATIONS
            sp = Palette()
            sp.setName(self.tr("Articulations && Ornaments"))
            sp.setGrid(42, 25)

            for i in range(0, nn):
                s = Articulation(GL.gscore)
                s.setSubtype(i)
                sp.append1(s, qApp.translate("articulation", s.subtypeName()))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Accidentals"))
            sp.setGrid(33, 36)

            for i in range(AccidentalType.ACC_SHARP, AccidentalType.ACC_END):
                s = Accidental(GL.gscore)
                s.setSubtype(i)
                sp.append1(s, qApp.translate("accidental", s.subtypeUserName()))
            ab = AccidentalBracket(GL.gscore)
            ab.setSubtype(0)
            sp.append1(ab, qApp.translate("Accidental", "round bracket"))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Dynamics"))
            sp.setMag(.8)
            sp.setGrid(42, 28)
            #sp.setYOffset(-12.0)

            dynS = [ "ppp", "pp", "p", "mp", "mf", "f", "ff", "fff"]
            for i in range(0, len(dynS)):
                dynamic = Dynamic(GL.gscore)
                dynamic.setSubtype1(dynS[i])
                sp.append1(dynamic, dynamic.subtypeName())
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Fingering"))
            sp.setMag(1.5)
            sp.setGrid(28, 30)
            sp.setDrawGrid(True)

            finger = ["0", "1", "2", "3", "4", "5", "p", "i", "m", "a", "c"]
            for i in range(0, len(finger)):
                k = Text(GL.gscore)
                k.setSubtype(TEXT.TEXT_FINGERING)
                k.setTextStyle(TEXT_STYLE.TEXT_STYLE_FINGERING)
                k.setText(QString(finger[i]))
                sp.append1(k, self.tr("Fingering %1").arg(finger[i]))
            stringnumber = ["0", "1", "2", "3", "4", "5", "6"]
            for i in range(0, len(stringnumber)):
                k = Text(GL.gscore)
                k.setSubtype(TEXT.TEXT_STRING_NUMBER)
                k.setTextStyle(TEXT_STYLE.TEXT_STYLE_STRING_NUMBER)
                k.setText(QString(stringnumber[i]))
                sp.append1(k, self.tr("String number %1").arg(stringnumber[i]))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Note Heads"))
            sp.setMag(1.3)
            sp.setGrid(33, 36)
            sp.setDrawGrid(True)
            for i in range(0, NoteHeadGroup.HEAD_GROUPS):
                sym = noteHeads[0][i][1]
                if i == NoteHeadGroup.HEAD_BREVIS_ALT:
                    sym = noteHeads[0][i][3]
                nh = NoteHead(GL.gscore)
                nh.setSym(sym)
                sp.append1(nh, qApp.translate("symbol", GL.symbols[sym].name()))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Tremolo"))
            sp.setGrid(27, 40)
            sp.setDrawGrid(True)
            tremoloName = [
                  QT_TR_NOOP("1 through stem"),
                  QT_TR_NOOP("2 through stem"),
                  QT_TR_NOOP("3 through stem"),
                  QT_TR_NOOP("1 between notes"),
                  QT_TR_NOOP("2 between notes"),
                  QT_TR_NOOP("3 between notes")
                  ]

            for i in range(0, 6):
                tremolo = Tremolo(GL.gscore)
                tremolo.setSubtype(i)
                sp.append1(tremolo, self.tr(tremoloName[i]))
            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Repeats"))
            sp.setMag(0.65)
            sp.setGrid(84, 28)
            sp.setDrawGrid(True)

            rm = RepeatMeasure(GL.gscore)
            sp.append1(rm, self.tr("Repeat measure sign"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_SEGNO)
            sp.append1(mk, self.tr("Segno"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_CODA)
            sp.append1(mk, self.tr("Coda"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_VARCODA)
            sp.append1(mk, self.tr("Varied coda"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_CODETTA)
            sp.append1(mk, self.tr("Codetta"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_FINE)
            sp.append1(mk, self.tr("Fine"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DC)
            sp.append1(jp, self.tr("Da Capo"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DC_AL_FINE)
            sp.append1(jp, self.tr("Da Capo al Fine"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DC_AL_CODA)
            sp.append1(jp, self.tr("Da Capo al Coda"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DS_AL_CODA)
            sp.append1(jp, self.tr("D.S al Coda"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DS_AL_FINE)
            sp.append1(jp, self.tr("D.S al Fine"))

            jp = Jump(GL.gscore)
            jp.setJumpType(JUMP.JUMP_DS)
            sp.append1(jp, self.tr("D.S"))

            mk = Marker(GL.gscore)
            mk.setMarkerType(MARKER.MARKER_TOCODA)
            sp.append1(mk, self.tr("To Coda"))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Breaks && Spacer"))
            sp.setMag(.7)
            sp.setGrid(42, 36)
            sp.setDrawGrid(True)

            lb = LayoutBreak(GL.gscore)
            lb.setSubtype(LAYOUT.LAYOUT_BREAK_LINE)
            sp.append1(lb, self.tr("Line break"))

            lb = LayoutBreak(GL.gscore)
            lb.setSubtype(LAYOUT.LAYOUT_BREAK_PAGE)
            sp.append1(lb, self.tr("Page break"))

            spacer = Spacer(GL.gscore)
            spacer.setSpace(Spatium(3))
            sp.append1(spacer, self.tr("Staff spacer"))

            self.paletteBox.addPalette(sp)


            sp = Palette()
            sp.setName(self.tr("Beam Properties"))
            sp.setGrid(27, 40)
            sp.setDrawGrid(True)

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_SBEAM)
            ik.setAction(GL.actions["beam-start"])
            sp.append1(ik, self.tr("Start beam"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_MBEAM)
            ik.setAction(GL.actions["beam-mid"])
            sp.append1(ik, self.tr("Middle of beam"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_NBEAM)
            ik.setAction(GL.actions["no-beam"])
            sp.append1(ik, self.tr("No beam"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_BEAM32)
            ik.setAction(GL.actions["beam32"])
            sp.append1(ik, self.tr("Start subbeam"))

            ik = Icon(GL.gscore)
            ik.setSubtype(IconNames1.ICON_AUTOBEAM)
            ik.setAction(GL.actions["auto-beam"])
            sp.append1(ik, self.tr("Auto beam"))

            self.paletteBox.addPalette(sp)

            sp = Palette()
            sp.setName(self.tr("Symbols"))
            sp.setGrid(42, 45)
            sp.setDrawGrid(True)

            sp.append(SymName.accDiscantSym)
            sp.append(SymName.accDotSym)
            sp.append(SymName.accFreebaseSym)
            sp.append(SymName.accStdbaseSym)
            sp.append(SymName.accBayanbaseSym)
            sp.append(SymName.accOldEESym)

            self.paletteBox.addPalette(sp)

        self.paletteBox.setShown(visible)
        act.setChecked(visible)

    def symbolMenu(self):
        if self.symbolDialog == 0:
            self.symbolDialog = SymbolDialog(self)
        self.symbolDialog.show()
        self.symbolDialog.raise_()
        
    def clefMenu(self):
        if self.clefPalette == 0:
            sp = Palette()
            sp.setGrid(60, 80)
            sp.resize(360, 400)
            clefPalette = PaletteScrollArea(sp)
            clefPalette.setRestrictHeight(False)
            clefPalette.setWindowTitle(self.tr("Muse 3.0: Clefs"))
            for i in range(0, CLEF.CLEF_MAX):
                k = Clef(GL.gscore)
                k.Clef1(i)
                sp.append(k, qApp.translate("clefTable", clefTable[i].name))
        self.clefPalette.show()
        self.clefPalette.raise_()


    def barMenu(self):
        if self.barPalette == 0:
            sp = Palette()
            sp.resize(300, 200)
            self.barPalette = PaletteScrollArea(sp, 0)
            self.barPalette.setRestrictHeight(False)
            self.barPalette.setWindowTitle(self.tr("Muse 3.0: Barlines"))
            self.sp.setGrid(42, 38)
            t= {  BarType.NORMAL_BAR:       QT_TR_NOOP("Normal"),
                  BarType.BROKEN_BAR:      QT_TR_NOOP("Dashed"),
                  BarType.END_BAR:          QT_TR_NOOP("End Bar"),
                  BarType.DOUBLE_BAR:       QT_TR_NOOP("Double Bar"),
                  BarType.START_REPEAT:     QT_TR_NOOP("Start Repeat"),
                  BarType.END_REPEAT:       QT_TR_NOOP("End Repeat"),
                  BarType.END_START_REPEAT: QT_TR_NOOP("End-Start Repeat")
                  }
            for key, value in t.items():
                b  = BarLine(GL.gscore)
                b.setHeight(4 * GL.gscore.spatium())
                b.setSubtype(key)
                self.sp.append(b, self.tr(t[key]))
        self.barPalette.show()
        self.barPalette.raise_()

    def timeMenu(self):
        if self.timePalette == 0:
            self.timePalette = TimeDialog(self)
        self.timePalette.show()
        self.timePalette.raise_()


    def lineMenu(self):
        if self.linePalette == 0:
            sp = Palette()
            sp.resize(400, 300)
            self.linePalette = PaletteScrollArea(sp)
            self.linePalette.setRestrictHeight(False)
            self.linePalette.setWindowTitle(self.tr("Muse 3.0: Lines"))
            sp.setGrid(100, 30)

            l = GL.gscore.spatium() * 8

            gabel0 = Hairpin(GL.gscore)
            gabel0.setSubtype(0)
            gabel0.setLen(l)
            sp.append(gabel0, self.tr("Crescendo"))

            gabel1 = Hairpin(GL.gscore)
            gabel1.setSubtype(1)
            gabel1.setLen(l)
            sp.append(gabel1, self.tr("Diminuendo"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setText("1.")
            il = list()
            il.append(1)
            volta.setEndings(il)
            volta.setSubtype(Volta.VOLTA_CLOSED)

            sp.append(volta, self.tr("Prima volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setText("2.")
            il.clear()
            il.append(2)
            volta.setEndings(il)
            volta.setSubtype(Volta.VOLTA_CLOSED)
            sp.append(volta, self.tr("Seconda volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setText("3.")
            il.clear()
            il.append(3)
            volta.setEndings(il)
            volta.setSubtype(Volta.VOLTA_CLOSED)
            sp.append(volta, self.tr("Terza volta"))

            volta = Volta(GL.gscore)
            volta.setLen(l)
            volta.setText("2.")
            il.clear()
            il.append(2)
            volta.setEndings(il)
            volta.setSubtype(VOLTA.VOLTA_OPEN)
            sp.append(volta, self.tr("Seconda volta"))

            ottava = Ottava(GL.gscore)
            ottava.setSubtype(0)
            ottava.setLen(l)
            sp.append(ottava, self.tr("8va"))

            ottava = Ottava(GL.gscore)
            ottava.setSubtype(1)
            ottava.setLen(l)
            sp.append(ottava, self.tr("15ma"))

            ottava = Ottava(GL.gscore)
            ottava.setSubtype(2)
            ottava.setLen(l)
            sp.append(ottava, self.tr("8vb"))

            ottava = Ottava(GL.gscore)
            ottava.setSubtype(3)
            ottava.setLen(l)
            sp.append(ottava, self.tr("15mb"))

            pedal = Pedal(GL.gscore)
            pedal.setLen(l)
            sp.append(pedal, self.tr("Pedal"))

            trill = Trill(GL.gscore)
            trill.setLen(l)
            sp.append(trill, self.tr("Trill line"))

            textLine = TextLine(GL.gscore)
            textLine.setLen(l)
            textLine.setBeginText("VII")
            sp.append(textLine, self.tr("Text line"))
            textLine.setEndHook(True)
            textLine.setEndHookHeight(Spatium(1.5))

            line = TextLine(GL.gscore)
            line.setLen(l)
            line.setDiagonal(True)
            sp.append(line, self.tr("Line"))
        self.linePalette.show()
        self.linePalette.raise_()

    def bracketMenu(self):
        if self.bracketPalette == 0:
            sp = Palette()
            self.bracketPalette = PaletteScrollArea(sp)
            self.bracketPalette.setRestrictHeight(False)
            self.bracketPalette.setWindowTitle(self.tr("Muse 3.0: Brackets"))
            sp.setGrid(40, 80)

            self._spatium = GL.gscore.spatium()
            b1 = Bracket(GL.gscore)
            b1.setSubtype(BRACKET.BRACKET_NORMAL)
            b2 = Bracket(GL.gscore)
            b2.setSubtype(BRACKET.BRACKET_AKKOLADE)
            b1.setHeight(self._spatium * 7)
            b2.setHeight(self._spatium * 7)

            sp.append(b1, self.tr("Bracket"))
            sp.append(b2, self.tr("Akkolade"))

        self.bracketPalette.show()
        self.bracketPalette.raise_()

    def noteAttributesMenu(self):
        if self.noteAttributesPalette == 0:
            sp = Palette()
            sp.resize(400, 300)
            self.noteAttributesPalette = PaletteScrollArea(sp)
            self.noteAttributesPalette.setRestrictHeight(False)
            self.noteAttributesPalette.setWindowTitle(self.tr("Muse 3.0: Articulations & Ornaments"))
            nn = ArticulationIdx.ARTICULATIONS
            sp.setGrid(42, 30)

            for i in range(0, nn):
                s = Articulation(GL.gscore)
                s.setSubtype(i)
                sp.append(s, qApp.translate("articulation", s.subtypeName().toAscii().data()))
        self.noteAttributesPalette.show()
        self.noteAttributesPalette.raise_()

    def accidentalsMenu(self):
        if self.accidentalsPalette == 0:
            sp = Palette()
            sp.resize(400, 300)
            self.accidentalsPalette = PaletteScrollArea(sp)
            self.accidentalsPalette.setRestrictHeight(False)
            self.accidentalsPalette.setWindowTitle(self.tr("Muse 3.0: Accidentals"))
            sp.setGrid(40, 50)

            for i in range(AccidentalType.ACC_SHARP, AccidentalType.ACC_END):
                s = Accidental(GL.gscore)
                s.setSubtype(i)
                sp.append(s, qApp.translate("accidental", s.subtypeUserName()))
            ab = AccidentalBracket(GL.gscore)
            ab.setSubtype(0)
            sp.append(ab, qApp.translate("Accidental", "round bracket"))
        self.accidentalsPalette.show()
        self.accidentalsPalette.raise_()

    def dynamicsMenu(self):
        if self.dynamicsPalette == 0:
            sp = Palette()
            self.dynamicsPalette = PaletteScrollArea(sp)
            self.dynamicsPalette.setRestrictHeight(False)
            self.dynamicsPalette.setWindowTitle(self.tr("Muse 3.0: Dynamics"))
            sp.setGrid(90, 40)
            sp.resize(300, 200)

            for i in range(0, 27):
                dynamic = Dynamic(GL.gscore)
                dynamic.setSubtype(dynList[i + 1].tag)
                sp.append(dynamic, dynamic.subtypeName())

                expr = [
                  "crescendo", "diminuendo", "dolce", "espressivo",
                  "legato", "leggiero", "marcato", "mero", "molto"
                  ]
            for i in expr:
                d = Dynamic(GL.gscore)
                d.setSubtype(expr[i])
                sp.append(d,  expr[i])
        self.dynamicsPalette.show()
        self.dynamicsPalette.raise_()

    def fingeringMenu(self):
        if self.fingeringPalette == 0:
            sp = Palette()
            sp.setMag(1.5)
            sp.resize(300, 200)
            self.fingeringPalette = PaletteScrollArea(sp)
            self.fingeringPalette.setRestrictHeight(False)
            self.fingeringPalette.setWindowTitle(self.tr("Muse 3.0: Fingering"))
            sp.setGrid(28, 30)
            finger = ['0', '1', '2', '3', '4', '5', 'p', 'i', 'm', 'a', 'c']
            k = Text()

            for i in range(0, len(finger)):
                k = Text(GL.gscore)
                k.setSubtype(TEXT.TEXT_FINGERING)
                k.setTextStyle(TEXT.TEXT_STYLE_FINGERING)
                k.setText(QString(finger[i]))
                sp.append(k, self.tr("Fingering %1").arg(finger[i]))
            stringnumber = ['0', '1', '2', '3', '4', '5', '6']
            for i in range(0, len(stringnumber)):
                k = Text(GL.gscore)
                k.setSubtype(TEXT.TEXT_STRING_NUMBER)
                k.setTextStyle(TEXT.TEXT_STYLE_STRING_NUMBER)
                k.setText(QString(stringnumber[i]))
                sp.append(k, self.tr("String number %1").arg(stringnumber[i]))
        self.fingeringPalette.show()
        self.fingeringPalette.raise_()

    def showLayoutBreakPalette(self):
        if self.layoutBreakPalette == 0:
            sp = Palette()
            self.layoutBreakPalette = PaletteScrollArea(sp)
            self.layoutBreakPalette.setRestrictHeight(False)
            self.layoutBreakPalette.setWindowTitle(self.tr("Muse 3.0: Breaks & Spacer"))
            sp.setGrid(80, 80)
            sp.resize(240,80)
            lb = LayoutBreak(GL.gscore)
            lb.setSubtype(LAYOUT.LAYOUT_BREAK_LINE)
            sp.append(lb, self.tr("Line break"))
            lb = LayoutBreak(GL.gscore)
            lb.setSubtype(LAYOUT.LAYOUT_BREAK_PAGE)
            sp.append(lb, self.tr("Page break"))
            spacer = Spacer(GL.gscore)
            spacer.setSpace(Spatium(3))
            sp.append(spacer, self.tr("Staff spacer"))
        self.layoutBreakPalette.show()
        self.layoutBreakPalette.raise_()

    def updateDrumset(self):
        if (self.cs == 0 or self.paletteBox == 0 or self.drumPalette == 0):
            return

        _spatium = GL.gscore.spatium()
        padState = self.cs.inputState()
        ds        = padState.drumset()
        if ds != self.drumset:
            self.drumset = ds
            self.drumPalette.clear()
            if self.drumset:
                drumInstruments = 0
                for pitch in range(0, 128):
                    if self.drumset.isValid(pitch):
                        drumInstruments = drumInstruments + 1
                i = 0
                for pitch in range(0, 128):
                    if not self.drumset.isValid(pitch):
                        continue
                        line      = ds.line(pitch)
                        noteHead  = ds.noteHead(pitch)
                        voice     = ds.voice(pitch)
                        dir = ds.stemDirection(pitch)
                        if dir == Direction.UP:
                            up = True
                        elif dir == Direction.DOWN:
                            up = False
                        else:
                            up = line > 4

                        chord = Chord(GL.gscore)
                        chord.setDuration(DurationType.V_QUARTER)
                        chord.setStemDirection(dir)
                        chord.setTrack(voice)
                        note = Note(GL.gscore)
                        note.setParent(chord)
                        note.setTrack(voice)
                        note.setPitch(pitch)
                        note.setTpcFromPitch()
                        note.setLine(line)
                        note.setPos(0.0, _spatium * .5 * line)
                        note.setHeadGroup(noteHead)
                        chord.add(note)
                        stem = Stem(GL.gscore)
                        if up:
                           stem.setLen(-3.0) * _spatium
                        else:
                            stem.setLen(3.0) * _spatium
                        chord.setStem(stem)
                        stem.setPos(note.stemPos(up))
                        drumPalette.append(chord, qApp.translate("drumset", drumset.name(pitch).toAscii().data()))
                        i = i + 1
        if self.drumset:
            i = 0
            self.drumPalette.setSelected(-1)
            for pitch in range(0, 128):
                if self.drumset.isValid(pitch):
                    if pitch == padState.drumNote():
                        self.drumPalette.setSelected(i)
                        break
                    i = i + 1
        self.drumPalette.update()

    def drumPaletteSelected(self, idx):
        if self.cs == 0:
            return
        padState = self.cs.inputState()
        ds          = padState.drumset()
        if ds == 0:
            return
        i = 0
        for pitch in range(0, 128):
            if not self.drumset.isValid(pitch):
                continue
            if i == idx:
                padState.setDrumNote(pitch)
                padState.track    = (padState.track / VOICES) * VOICES + ds.voice(pitch)
                self.cs.setPadState()
                break
            i = i + 1


    def setCurrentScoreView(self, idx):
        self.setCurrentView(0, idx)

    def setCurrentView(self, tabIdx, idx):
        if idx == -1:
            self.setCurrentScoreView2(ScoreView())
        else:
            if tabIdx:
                self.tab2.setCurrentIndex(idx)
            else:
                self.tab1.setCurrentIndex(idx)

    def setCurrentScoreView2(self, view):
        self.cv = view
        if view:
            self.cs = view.score()
            view.setFocusRect()
        else:
            self.cs = 0
        if GL.seq:
            GL.seq.setScoreView(self.cv)
        if self.playPanel:
            self.playPanel.setScore(self.cs)
        if self.iledit:
            self.iledit.updateAll(self.cs)
        if self.cs == 0:
            self.changeState(SS.STATE_DISABLED)
            self._undoGroup.setActiveStack(0)
            self.setWindowTitle("Muse 3.0")
            if self.navigator:
                self.navigator.setScore(0)
            return

        self._undoGroup.setActiveStack(self.cs.undo())
        self.view.setFocus(Qt.OtherFocusReason)

        GL.actions["file-save"].setEnabled(self.cs.isSavable())
        GL.actions["show-invisible"].setChecked(self.cs.showInvisible())
        GL.actions["show-frames"].setChecked(self.cs.showFrames())
        if view.magIdx() == MAG.MAG_FREE:
            self.mag.setMag(view.mag())
        else:
            self.mag.setMagIdx(view.magIdx())

        self.setWindowTitle("Muse 3.0: " + self.cs.name())

        a = GL.actions["concert-pitch"]
        a.setChecked(self.cs.styleB(StyleIdx.ST_concertPitch))

        self.setPos(self.cs.inputPos())
        self._statusBar.showMessage(self.cs.filePath(), 2000)
        if self.navigator:
            self.navigator.setScore(self.cv)

    def genCreateMenu(self, parent):
        popup = QMenu(self.tr("&Create"), parent)
        popup.setObjectName("Create")
        popup.addAction(GL.actions["instruments"])

        measures = popup.addMenu(self.tr("Measures"))
        measures.addAction(GL.actions["append-measure"])
        measures.addAction(GL.actions["append-measures"])
        measures.addAction(GL.actions["insert-measure"])
        measures.addAction(GL.actions["insert-measures"])
        measures.addAction(GL.actions["insert-hbox"])
        measures.addAction(GL.actions["insert-vbox"])
        measures.addAction(GL.actions["append-hbox"])
        measures.addAction(GL.actions["append-vbox"])

        popup.addAction(self.tr("Barlines..."),        self.barMenu)
        popup.addAction(GL.actions["clefs"])
        popup.addAction(GL.actions["keys"])
        popup.addAction(GL.actions["times"])
        popup.addAction(self.tr("&Lines..."),          self.lineMenu)
        popup.addAction(self.tr("Brackets..."), self.bracketMenu)
        popup.addAction(self.tr("Articulations && Ornaments..."), self.noteAttributesMenu)
        popup.addAction(self.tr("Accidentals..."),     self.accidentalsMenu)

        text = popup.addMenu(self.tr("Text"))
        text.addAction(GL.actions["title-text"])
        text.addAction(GL.actions["subtitle-text"])
        text.addAction(GL.actions["composer-text"])
        text.addAction(GL.actions["poet-text"])
        text.addAction(GL.actions["copyright-text"])
        text.addSeparator()
        text.addAction(GL.actions["system-text"])
        text.addAction(GL.actions["staff-text"])
        text.addAction(GL.actions["chord-text"])
        text.addAction(GL.actions["rehearsalmark-text"])
        text.addSeparator()
        text.addAction(GL.actions["lyrics"])
        text.addAction(GL.actions["fingering"])
        text.addAction(GL.actions["dynamics"])
        text.addAction(GL.actions["tempo"])

        popup.addAction(GL.actions["symbols"])
        return popup

    def showPageSettings(self):
        if not self.cs:
            return
        if self.pageSettings == 0:
            self.pageSettings = PageSettings()
        self.pageSettings.setScore(self.cs)
        self.pageSettings.show()
        self.pageSettings.raise_()

    def seqStarted(self):
        self.cv.setCursorOn(True)
        self.cs.end()

    def seqStopped(self):
        self.cs.setLayoutAll(False)
        self.cs.setUpdateAll()
        self.cs.end()

    def autoSaveTimerTimeout(self):
        sessionChanged = False
        for s in self.scoreList:
            if s.autosaveDirty():
                tmp = QString(s.tmpName())
                if not tmp.isEmpty():
                    fi = QFileInfo(tmp)
                    self.cs.saveCompressedFile(fi, True)
                else:
                    dir = QDir()
                    dir.mkpath(GL.dataPath)
                    tf = QTemporaryFile(GL.dataPath + "\scXXXXXX.mscz")
                    tf.setAutoRemove(False)
                    if not tf.open():
                        print "autoSaveTimerTimeout(): create temporary file failed\n"
                        return
                    s.setTmpName(tf.fileName())
                    info = QFileInfo(tf.fileName())
                    s.saveCompressedFile(tf, info, True)
                    tf.close()
                    sessionChanged = True
                    s.setAutosaveDirty(False)
        if sessionChanged:
            self.writeSessionFile(False)
        if preferences.autoSave:
            t = preferences.autoSaveTime * 60 * 1000
            self.autoSaveTimer.start(t)

    def cmd(self, a):
        print a.text()
        lastCmd = QAction(None)
        cmd = a.data().toString()
        sc = self.getShortcut(cmd.toAscii().data())
        if sc == 0:
            print "Muse.cmd(): unknown action <%s>\n" %cmd.toAscii().data()
            return
        if self.cs and sc.state and self._sstate:
            QMessageBox.warning(0,
               QWidget.tr("Muse: invalid command"),
               QString("command %1 not valid in current state").arg(cmd),
               QString.null, QWidget.tr("Quit"), QString.null, 0, 1)
            return
        if cmd == "repeat-cmd":
            a = lastCmd
            if a == 0:
                return
            cmd = a.data().toString()
        else:
            lastCmd = a
        if cmd == "instruments":
            self.editInstrList()
            if self.iledit:
                self.iledit.updateAll(self.cs)
        elif cmd == "clefs":
            self.clefMenu()
        elif cmd == "keys":
            self.showKeyEditor()
        elif cmd == "symbols":
            self.symbolMenu()
        elif cmd == "times":
            self.timeMenu()
        elif cmd == "dynamics":
            self.dynamicsMenu()
        elif cmd == "file-open":
            self.loadFile()
        elif cmd == "file-save":
            self.saveFile()
        elif cmd == "file-reload":
            if self.cs and not self.cs.created() and not self.checkDirty(self.cs):
                if self.cv.editMode():
                    self.cv.postCmd("escape")
                    qApp.processEvents()
                score = Score(defaultStyle)
                score.read(self.cs.filePath())
                self.cs.setDirty(False)
                self.setCurrentScoreView(self.appendScore(score))
        elif cmd == "file-close":
            self.closeScore(self.cs)
        elif cmd == "file-save-as":
            if self.cs:
                self.cs.saveAs(False)
        elif cmd == "file-save-a-copy":
            if self.cs:
                self.cs.saveAs(True)
        elif cmd == "file-new":
            self.newFile()
        elif cmd == "quit":
            self.close()
        elif cmd == "fingering":
            self.fingeringMenu()
        elif cmd == "toggle-statusbar":
            Preferences().showStatusBar = a.isChecked()
            self._statusBar.setShown(Preferences().showStatusBar)
            Preferences().write()
        elif cmd == "append-measures":
            self.cmdAppendMeasures()
        elif cmd == "insert-measures":
            self.cmdInsertMeasures()
        elif cmd == "inspector":
            self.startInspector()
        elif cmd == "script-debug":
            self.scriptDebug = a.isChecked()
        elif cmd == "backspace":
            self.undo()
        elif cmd == "zoomin":
            self.incMag()
        elif cmd == "zoomout":
            self.decMag()
        elif cmd == "midi-on":
            self.midiinToggled(a.isChecked())
        elif cmd == "sound-on":
            self.speakerToggled(a.isChecked())
        elif cmd == "undo":
            self.undo()
        elif cmd == "redo":
            self.redo()
        elif cmd == "toggle-palette":
            self.showPalette(a.isChecked())
        elif cmd == "toggle-playpanel":
            self.showPlayPanel(a.isChecked())
        elif cmd == "toggle-navigator":
            self.showNavigator(a.isChecked())
        elif cmd == "toggle-mixer":
            self.showMixer(a.isChecked())
        elif cmd == "synth-control":
            self.showSynthControl(a.isChecked())
        elif cmd == "musescore-connect":
            self.showWebPanel(a.isChecked())
        elif cmd == "show-keys":
            pass
        elif cmd == "toggle-transport":
            self.transportTools.setVisible(not self.transportTools.isVisible())
        elif cmd == "toggle-noteinput":
            self.entryTools.setVisible(not self.entryTools.isVisible())
        elif cmd == "local-help":
            self.helpBrowser()
        elif cmd == "follow":
            Preferences().followSong = a.isChecked()
        elif cmd == "split-h":
            self.splitWindow(True)
        elif cmd == "split-v":
            self.splitWindow(False)
        elif cmd == "edit-harmony":
            self.editChordStyle()
        elif cmd == "parts":
            self.startExcerptsDialog()
        elif cmd == "next-score":
            self.gotoNextScore()
        elif cmd == "previous-score":
            self.gotoPreviousScore()
        else:
            if self.cv:
                self.cv.setFocus()
                self.cv.cmd(a)
            else:
                print "unknown cmd <%s>\n" %cmd.toAscii().data()

    def midiinToggled(self, val):
        self._midiinEnabled = val

    def startPreferenceDialog(self):
        if not self.preferenceDialog:
            self.preferenceDialog = PreferenceDialog(self)
            self.connect(self.preferenceDialog, SIGNAL("preferencesChanged()"), self.preferencesChanged)
        self.preferenceDialog.show()

    def preferencesChanged(self):
        for i in range(0, self.tab1.count()):
            canvas = self.tab1.view(i)
            if canvas == 0:
                continue
            if preferences.bgUseColor:
                canvas.setBackground(preferences.bgColor)
            else:
                pm = QPixmap(preferences.bgWallpaper)
                canvas.setBackground(pm)
            if preferences.fgUseColor:
                canvas.setForeground(preferences.fgColor)
            else:
                pm = QPixmap(preferences.fgWallpaper)
                if pm == 0 or pm.isNull():
                    print"no valid pixmap %s\n" %preferences.fgWallpaper.toLatin1().data()
                    canvas.setForeground(pm)
        for i in range(0, self.tab2.count()):
            canvas = self.tab2.view(i)
            if canvas == 0:
                continue
            if preferences.bgUseColor:
                canvas.setBackground(preferences.bgColor)
            else:
                pm = QPixmap(preferences.bgWallpaper)
                canvas.setBackground(pm)
            if preferences.fgUseColor:
                canvas.setForeground(preferences.fgColor)
            else:
                pm = QPixmap(preferences.fgWallpaper)
                if pm == 0 or pm.isNull():
                    print "no valid pixmap %s\n" %preferences.fgWallpaper.toLatin1().data()
                    canvas.setForeground(pm)
        self.transportTools.setEnabled(not noSeq)
        self.playId.setEnabled(not noSeq)

        GL.actions["midi-on"].setEnabled(preferences.enableMidiInput)
        self._statusBar.setShown(preferences.showStatusBar)

    def loadScoreList(self):
        if useFactorySettings:
            return
        s = QSettings()
        for i in range(0, RECENT_LIST_SIZE-1):
            path = QString(s.value(QString("recent-%1").arg(i),"").toString())
            if not path.isEmpty() and QFileInfo(path).exists():
                GL.recentScores.removeAll(path)
                GL.recentScores.prepend(path)

    def startAutoSave(self):
        if preferences.autoSave:
            t = preferences.autoSaveTime * 60 * 1000
            self.autoSaveTimer.start(t)
        else:
            self.autoSaveTimer.stop()


    def showPlayPanel(self, visible):
        if noSeq:
            return
        if self.playPanel == 0:
            if not visible:
                return
            self.playPanel = PlayPanel(self)
            self.connect(self.playPanel, SIGNAL("volChange(float)"), GL.seq, SLOT("setMasterVolume(float)"))
            self.connect(self.playPanel, SIGNAL("relTempoChanged(float,int)"),GL.seq, SLOT("setRelTempo(double)"))
            self.connect(self.playPanel, SIGNAL("posChange(int)"),      GL.seq, SLOT("seek(int)"))
            self.connect(self.playPanel, SIGNAL("closed()"),                 SLOT("closePlayPanel()"))
            self.connect(GL.seq,       SIGNAL("masterVolumeChanged(float)"), self.playPanel, SLOT("setVolume(float)"))

            self.playPanel.setVolume(GL.seq.masterVolume())
            self.playPanel.setScore(self.cs)
        self.playPanel.setVisible(visible)
        self.playId.setChecked(visible)



    def selectScore(self, action):
        a = action.data().toString()
        if not a.isEmpty():
            score = Score(defaultStyle)
            if score.read(a):
                self.setCurrentScoreView(self.appendScore(score))

    def openRecentMenu(self):
        self.openRecent.clear()
        for s in GL.recentScores:
            if s.isEmpty():
                break
            action = self.openRecent.addAction(s)
            action.setData(s)


    def speakerToggled(self, val):
        self._speakerEnabled = val

    def initUI(self):
        self.lastSaveCopyDirectory = ''
        self.lastSaveDirectory = ''
        self._positionLabel = QLabel()
        self._positionLabel.setText("001:01:000")
        self._positionLabel.setAutoFillBackground(True)
        p = QPalette(self._positionLabel.palette())
        p.setColor(QPalette.Window, QColor(176, 190, 242))
        self._positionLabel.setPalette(p)

        self._modeText = QLabel()
        self._modeText.setAutoFillBackground(True)
        p.setColor(QPalette.Window, QColor(176, 190, 242))
        self._modeText.setPalette(p)

        self._statusBar = QStatusBar()
        self._statusBar.addPermanentWidget(self._modeText, 0)
        self._statusBar.addPermanentWidget(self._positionLabel, 0)
        self.setStatusBar(self._statusBar)
        self._progressBar = 0


        ag = QActionGroup(self)
        ag.setExclusive(False)
        for s in GL.shortcuts:
            a = self.getAction(s)
            GL.actions[s] = a
            ag.addAction(a)
        ag.triggered.connect(self.cmd)
        self.addActions(ag.actions())

        mainWindow = QSplitter()
        mainWindow.setOrientation(Qt.Vertical)
        mlayout = QVBoxLayout()
        mlayout.setMargin(0)
        mlayout.setSpacing(0)
        mainWindow.setLayout(mlayout)

        mainScore = QWidget()
        mainScore.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout = QVBoxLayout()
        self.layout.setMargin(0)
        self.layout.setSpacing(0)
        mainScore.setLayout(self.layout)
        mainWindow.addWidget(mainScore)
        self.navigator = Navigator()
        self.navigator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainWindow.addWidget(self.navigator)
        self.navigator.setShown(Preferences().showNavigator)
        sizes = [500, 100]
        mainWindow.setSizes(sizes)

        self.splitter = QSplitter()

        self.tab1 = ScoreTab(self.scoreList)
        self.tab1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.connect(self.tab1, SIGNAL("currentScoreViewChanged(PyQt_PyObject)"), self.setCurrentScoreView)
        self.connect(self.tab1, SIGNAL("tabCloseRequested(int)"), self.tab1.removeTab)

        self.tab2 = ScoreTab(self.scoreList)
        self.tab2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.connect(self.tab2, SIGNAL("currentScoreViewChanged(PyQt_PyObject)"), self.setCurrentScoreView)
        self.connect(self.tab2, SIGNAL("tabCloseRequested(int)"), self.tab2.removeTab)

        self.splitter.addWidget(self.tab1)
        self.splitter.addWidget(self.tab2)
        self.tab2.setVisible(False)
        self.layout.addWidget(self.splitter)
        self.searchDialog = 0

        a = GL.actions["midi-on"]
        a.triggered.connect(self.midiinToggled)
        a.setCheckable(True)
        a.setEnabled(Preferences().enableMidiInput)
        a.triggered.emit(a.isChecked())
        a.setChecked(self._midiinEnabled)

        a = GL.actions["sound-on"]
        a.triggered.connect(self.speakerToggled)
        a.setCheckable(True)
        a.setEnabled(Preferences().playNotes)
        a.triggered.emit(a.isChecked())
        a.setChecked(self._speakerEnabled)

        GL.actions["play"].setCheckable(True)
        #getAction("pause").setCheckable(True)
        a = GL.actions["repeat"]
        a.setCheckable(True)
        a.setChecked(True)

        self.fileTools = self.addToolBar(self.tr("File Operations"))
        self.fileTools.setObjectName("file-operations")
        self.fileTools.addAction(GL.actions["file-new"])
        self.fileTools.addAction(GL.actions["file-open"])
        self.fileTools.addAction(GL.actions["file-save"])
        self.fileTools.addAction(GL.actions["print"])
        self.fileTools.addAction(GL.actions["musescore-connect"])

        self.fileTools.addSeparator()

        a = GL.actions["undo"]
        a.setEnabled(False)
        self.connect(self._undoGroup, SIGNAL("canUndoChanged(bool)"), a, SLOT("setEnabled(bool)"))
        self.fileTools.addAction(a)

        a = GL.actions["redo"]
        a.setEnabled(False)
        self.connect(self._undoGroup, SIGNAL("canRedoChanged(bool)"), a, SLOT("setEnabled(bool)"))
        self.fileTools.addAction(a)
        self.fileTools.addSeparator()

        self.transportTools = self.addToolBar(self.tr("Transport Tools"))
        self.transportTools.setObjectName("transport-tools")
        self.transportTools.addAction(GL.actions["sound-on"])
        self.transportTools.addAction(GL.actions["midi-on"])
        self.transportTools.addSeparator()
        self.transportTools.addAction(GL.actions["rewind"])
        self.transportTools.addAction(GL.actions["play"])
        self.transportTools.addSeparator()
        GL.actions["repeat"].setChecked(Preferences().playRepeats)
        self.transportTools.addAction(GL.actions["repeat"])


        mag = MagBox()
        self.connect(mag, SIGNAL("magChanged(int)"), self.magChanged)
        self.fileTools.addWidget(mag)
        self.addToolBarBreak()

        self.cpitchTools = self.addToolBar(self.tr("Concert Pitch"))
        self.cpitchTools.setObjectName("pitch-tools")
        self.cpitchTools.addAction(GL.actions["concert-pitch"])

        self.entryTools = self.addToolBar(self.tr("Note Entry"))
        self.entryTools.setObjectName("entry-tools")
        self.entryTools.setIconSize(QSize(Preferences().noteEntryIconWidth, Preferences().noteEntryIconHeight))

        a = GL.actions["note-input"]
        a.setCheckable(True)
        self.entryTools.addAction(a)

        sl1 = [QString("pad-note-64"), QString("pad-note-32"), QString("pad-note-16"), QString("pad-note-8"), QString("pad-note-4"),\
               QString("pad-note-2"), QString("note-breve"), QString("note-longa"), QString("pad-dot"),\
               QString("pad-dotdot"), QString("tie"), QString("pad-rest")]

        for s in sl1:
            nb = NoteButton()
            a = GL.actions[s.toAscii().data()]
            if s != "tie":
                a.setCheckable(True)
            nb.setDefaultAction(a)
            self.entryTools.addWidget(nb)
            if s == "tie" or s == "pad-rest":
                self.entryTools.addSeparator()

        sl2 = [QString( "sharp2"), QString("sharp"), QString( "nat"), QString("flat"), QString("flat2")]

        for s in sl2:
            nb = NoteButton()
            a = GL.actions[s.toAscii().data()]
            nb.setDefaultAction(a)
            self.entryTools.addWidget(nb)

        sl3 = [QString( "pad-appoggiatura"), QString("pad-acciaccatura"), QString( "pad-grace4"), QString("pad-grace16"), QString("pad-grace32"),\
               QString("beam-start"), QString("beam-mid"), QString("no-beam"), QString("beam32"), QString("auto-beam"),\
               QString("show-invisible"), QString("show-frames")]

        for s in sl3:
            a = GL.actions[s.toLatin1().data()]
            a.setCheckable(True)

        a = GL.actions["flip"]
        self.entryTools.addAction(a)
        self.entryTools.addSeparator()
        vw = Voiceselector.VoiceSelector()
        self.entryTools.addWidget(vw)
        vw.triggered.connect(self.cmd)

        mb = self.menuBar()
        self._fileMenu = mb.addMenu(self.tr("&File"))
        self._fileMenu.setObjectName("File")

        self._fileMenu.addAction(GL.actions["file-new"])
        self._fileMenu.addAction(GL.actions["file-open"])
        self.openRecent = self._fileMenu.addMenu(GL.icons[IconNames2.fileOpen_ICON], self.tr("Open &Recent"))
        self.connect(self.openRecent, SIGNAL("aboutToShow()"), self.openRecentMenu)
        self.connect(self.openRecent, SIGNAL("triggered()"), self.selectScore)
        self._fileMenu.addSeparator()

        self._fileMenu.addAction(GL.actions["file-save"])
        self._fileMenu.addAction(GL.actions["file-save-as"])
        self._fileMenu.addAction(GL.actions["file-save-a-copy"])
        self._fileMenu.addSeparator()
        self._fileMenu.addAction(GL.actions["file-reload"])
        self._fileMenu.addSeparator()
        self._fileMenu.addAction(GL.actions["file-close"])

        self._fileMenu.addSeparator()
        self._fileMenu.addAction(GL.actions["parts"])
        self._fileMenu.addAction(GL.actions["print"])
        self._fileMenu.addSeparator()
        self._fileMenu.addAction(GL.actions["quit"])

        self.menuEdit = mb.addMenu(self.tr("&Edit"))
        self.menuEdit.setObjectName("Edit")
        self.menuEdit.addAction(GL.actions["undo"])
        self.menuEdit.addAction(GL.actions["redo"])

        self.menuEdit.addSeparator()

        self.menuEdit.addAction(GL.actions["cut"])
        self.menuEdit.addAction(GL.actions["copy"])
        a = GL.actions["paste"]
        a.setEnabled(False)
        self.menuEdit.addAction(a)
        self.selectionChanged(0)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(GL.actions["select-all"])
        self.menuEdit.addAction(GL.actions["find"])
        self.menuEdit.addSeparator()

        self.menuEdit.addAction(GL.actions["delete-measures"])
        self.menuEdit.addSeparator()

        menuVoices = QMenu(self.tr("Voices"))
        menuVoices.addAction(GL.actions["voice-x12"])
        menuVoices.addAction(GL.actions["voice-x13"])
        menuVoices.addAction(GL.actions["voice-x14"])
        menuVoices.addAction(GL.actions["voice-x23"])
        menuVoices.addAction(GL.actions["voice-x24"])
        menuVoices.addAction(GL.actions["voice-x34"])
        self.menuEdit.addMenu(menuVoices)

        self.menuEdit.addSeparator()
        self.menuEdit.addAction(GL.actions["edit-meta"])
        self.menuEdit.addAction(GL.actions["inspector"])
        self.menuEdit.addSeparator()
        pref = self.menuEdit.addAction(self.tr("Preferences..."), self.startPreferenceDialog)
        pref.setMenuRole(QAction.PreferencesRole)

        menuCreate = self.genCreateMenu(mb)
        mb.setObjectName("Create")
        mb.addMenu(menuCreate)

        self.menuNotes = mb.addMenu(qApp.translate("MenuNotes", "&Notes"))
        self.menuNotes.setObjectName("Notes")
        self.menuNotes.addAction(GL.actions["note-input"])
        self.menuNotes.addAction(GL.actions["pitch-spell"])
        self.menuNotes.addSeparator()

        menuAddPitch = QMenu(self.tr("Add Note"))
        lst = {0:'c', 1:'d', 2:'e', 3:'f', 4:'g', 5:'a', 6:'b'}
        for i in lst:
            tmp = "note-" + lst[i]
            a = GL.actions[tmp]
            menuAddPitch.addAction(a)
        self.menuNotes.addMenu(menuAddPitch)

        for i in lst:
            tmp = "chord-" + lst[i]
            a = GL.actions[tmp]
            menuAddPitch.addAction(a)

        menuAddInterval = QMenu(self.tr("Add Interval"))
        for i in range(1,10):
            tmp = "interval" + str(i)
            a = GL.actions[tmp]
            menuAddInterval.addAction(a)

        menuAddInterval.addSeparator()
        for i in range(2,10):
            tmp = "interval-" + str(i)
            a = GL.actions[tmp]
            menuAddInterval.addAction(a)
        self.menuNotes.addMenu(menuAddInterval)

        menuNtole = QMenu(self.tr("Tuplets"))
        menuNtole.addAction(GL.actions["duplet"])
        menuNtole.addAction(GL.actions["triplet"])
        menuNtole.addAction(GL.actions["quadruplet"])
        menuNtole.addAction(GL.actions["quintuplet"])
        menuNtole.addAction(GL.actions["sextuplet"])
        menuNtole.addAction(GL.actions["septuplet"])
        menuNtole.addAction(GL.actions["octuplet"])
        menuNtole.addAction(GL.actions["nonuplet"])
        menuNtole.addAction(GL.actions["tuplet-dialog"])
        self.menuNotes.addMenu(menuNtole)

        self.menuNotes.addSeparator()
        self.menuNotes.addAction(GL.actions["transpose"])
        a = GL.actions["concert-pitch"]
        a.setCheckable(True)
        self.menuNotes.addAction(a)

        self.menuLayout = mb.addMenu(self.tr("&Layout"))
        self.menuLayout.setObjectName("Layout")

        self.menuLayout.addAction(self.tr("Page Settings..."), self.showPageSettings)

        self.menuLayout.addAction(GL.actions["reset-positions"])
        self.menuLayout.addAction(GL.actions["stretch+"])
        self.menuLayout.addAction(GL.actions["stretch-"])

        self.menuLayout.addAction(GL.actions["reset-stretch"])
        self.menuLayout.addAction(GL.actions["reset-beammode"])
        self.menuLayout.addAction(self.tr("Breaks && Spacer..."), self.showLayoutBreakPalette)

        self.menuStyle = mb.addMenu(self.tr("&Style"))
        self.menuStyle.setObjectName("Style")
        self.menuStyle.addAction(GL.actions["edit-style"])
        self.menuStyle.addAction(GL.actions["edit-text-style"])
        self.menuStyle.addAction(GL.actions["edit-harmony"])
        self.menuStyle.addSeparator()
        self.menuStyle.addAction(GL.actions["load-style"])
        self.menuStyle.addAction(GL.actions["save-style"])

        self.menuDisplay = mb.addMenu(self.tr("&Display"))
        self.menuDisplay.setObjectName("Display")

        a = GL.actions["toggle-palette"]
        a.setCheckable(True)
        self.menuDisplay.addAction(a)

        playId = GL.actions["toggle-playpanel"]
        playId.setCheckable(True)
        self.menuDisplay.addAction(playId)

        a = GL.actions["toggle-navigator"]
        a.setCheckable(True)
        a.setChecked(Preferences().showNavigator)
        self.menuDisplay.addAction(a)

        a = GL.actions["toggle-mixer"]
        a.setCheckable(True)
        self.menuDisplay.addAction(a)

        a = GL.actions["synth-control"]
        a.setCheckable(True)
        self.menuDisplay.addAction(a)

        a = GL.actions["musescore-connect"]
        a.setCheckable(True)
        self.menuDisplay.addAction(a)

        self.menuDisplay.addSeparator()
        self.menuDisplay.addAction(GL.actions["zoomin"])
        self.menuDisplay.addAction(GL.actions["zoomout"])
        self.menuDisplay.addSeparator()

        a = GL.actions["toggle-transport"]
        a.setCheckable(True)
        a.setChecked(self.transportTools.isVisible())
        self.menuDisplay.addAction(a)

        a = GL.actions["toggle-noteinput"]
        a.setCheckable(True)
        a.setChecked(True)
        self.menuDisplay.addAction(a)

        a = GL.actions["toggle-statusbar"]
        a.setCheckable(True)
        a.setChecked(True)
        self.menuDisplay.addAction(a)

        self.menuDisplay.addSeparator()
        a = GL.actions["split-h"]
        a.setCheckable(True)
        a.setChecked(False)
        self.menuDisplay.addAction(a)
        a = GL.actions["split-v"]
        a.setCheckable(True)
        a.setChecked(False)
        self.menuDisplay.addAction(a)

        self.menuDisplay.addSeparator()
        self.menuDisplay.addAction(GL.actions["show-invisible"])
        self.menuDisplay.addAction(GL.actions["show-frames"])

        mb.addSeparator()
        self.menuHelp = mb.addMenu(self.tr("&Help"))
        self.menuHelp.setObjectName("Help")

        self.menuHelp.addAction(GL.actions["local-help"])
        #self.menuHelp.addAction(self.tr("Online Handbook"), self.helpBrowser1)
        self.menuHelp.addSeparator()
        a = QAction("&About", self, statusTip="Show About box")
        a.triggered.connect(self.about)
        self.menuHelp.addAction(a)
        self.menuHelp.addAction(self.tr("&About"), self.about)
        self.menuHelp.addAction(self.tr("Check for Update"), self.checkForUpdate)
        self.menuHelp.addSeparator()

        self.setCentralWidget(mainWindow)

        loadInstrumentTemplates(preferences.instrumentList)
        self.preferencesChanged()
        if GL.seq:
            self.connect(GL.seq, SIGNAL("started()"), self.seqStarted)
            self.connect(GL.seq, SIGNAL("stopped()"), self.seqStopped)
        self.loadScoreList()

        self.showPlayPanel(Preferences().showPlayPanel)

        cb = QApplication.clipboard()
        self.connect(cb, SIGNAL("dataChanged()"), self.clipboardChanged)
        self.connect(cb, SIGNAL("selectionChanged()"), self.clipboardChanged)
        autoSaveTimer = QTimer(self)
        autoSaveTimer.setSingleShot(True)
        self.connect(autoSaveTimer, SIGNAL("timeout()"), self.autoSaveTimerTimeout)
        #initOsc()
        self.startAutoSave()






