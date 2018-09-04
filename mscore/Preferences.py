#!/usr/bin/env python
import sys,os
from globals import *
import GL
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Updatechecker import *
from prefsdialog import Ui_PrefsDialogBase

def appStyleSheet():
      fff = QFont()
      if Preferences().applicationFont.isEmpty():
            fff = QApplication.font()
      else:
            fff.fromString(Preferences().applicationFont)
      return QString(
      "* { font-size: %1pt font-family: \"%2\"}\n"
      "PlayPanel QLabel#posLabel   { font-size: 28pt font-family: \"San Serif\" }\n"
      "PlayPanel QLabel#timeLabel      { font-size: 28pt font-family: \"San Serif\" }\n"
      "SynthControl QLabel#titleLabel  { font-size: 24pt font-family: \"San Serif\" }\n"
      "ChordEdit QLabel#chordLabel { font-size: 24pt font-family: \"San Serif\" }\n"
      "PlayPanel QLabel#tempoLabel { font-size: 10pt font-family: \"San Serif\" }\n"
      "PlayPanel QLabel#relTempo   { font-size: 10pt font-family: \"San Serif\" }\n"
      "AboutBoxDialog QLabel#titleLabel { font-size: 28pt  }\n").arg(fff.pointSize()).arg(fff.family())


class Preferences:
    def __init__(self):
        self.bgUseColor         = True
        self.fgUseColor         = False
        self.bgWallpaper        = QString()
        self.fgWallpaper        = "data\paper5.png"
        self.fgColor = QColor()
        self.fgColor.setRgb(255, 255, 255)
        self.bgColor = QColor()
        self.bgColor.setRgb(0x76, 0x76, 0x6e)
        color0 = QColor()
        color0.setRgb(0, 0, 255)
        color1 = QColor()
        color1.setRgb(0, 150, 0)
        color2 = QColor()
        color2.setRgb(230, 180, 50)
        color3 = QColor()
        color3.setRgb(200, 0, 200)
        self.selectColor = [color0, color1, color2, color3]
        self.dropColor      = Qt.red
        self.defaultColor   = Qt.black
        self.enableMidiInput    = True
        self.playNotes          = True
        self.lPort              = ""
        self.rPort              = ""
        self.showNavigator      = True
        self.showPlayPanel      = False
        self.showWebPanel       = True
        self.showStatusBar      = True
        self.useAlsaAudio       = False
        self.useJackAudio       = False
        self.usePortaudioAudio  = True
        self.useJackMidi        = False
        self.alsaDevice         = "default"
        self.alsaSampleRate     = 48000
        self.alsaPeriodSize     = 1024
        self.alsaFragments      = 3
        self.portaudioDevice    = -1
        self.portMidiInput      = ""
        self.midiPorts          = 2
        self.rememberLastMidiConnections = True
        self.layoutBreakColor         = Qt.green
        self.antialiasedDrawing       = True
        self.sessionStart             = SessionStart.SCORE_SESSION
        self.startScore               = "data\Reunion_Example.xml"
        self.workingDirectory         = QDesktopServices.storageLocation(QDesktopServices.DocumentsLocation)
        self.showSplashScreen         = True
        self.rewind = MidiRemote().Type              = -1
        self.play = MidiRemote().Type                = -1
        self.stop = MidiRemote().Type                = -1
        self.len1 = MidiRemote().Type                = -1
        self.len2 = MidiRemote().Type                = -1
        self.len4 = MidiRemote().Type                = -1
        self.len8 = MidiRemote().Type                = -1
        self.len16 = MidiRemote().Type               = -1
        self.len32 = MidiRemote().Type               = -1
        self.len3 = MidiRemote().Type                = -1
        self.len6 = MidiRemote().Type                = -1
        self.len12 = MidiRemote().Type               = -1
        self.len24 = MidiRemote().Type               = -1
        self.midiExpandRepeats        = True
        self.playRepeats              = True
        self.instrumentList           = "data\instruments.xml"

        self.alternateNoteEntryMethod = False
        self.proximity                = 6
        self.autoSave                 = True
        self.autoSaveTime             = 2      # minutes
        self.pngScreenShot            = False
        self.language                 = "system"
        self.iconWidth                = 24
        self.iconHeight               = 24
        self.noteEntryIconWidth       = ICON_WIDTH
        self.noteEntryIconHeight      = ICON_HEIGHT
        self.applicationFont          = QString()
        self.style                    = QString()

        self.replaceCopyrightSymbol  = True
        self.replaceFractions        = True

        self.paperSize               = QPrinter.A4     # default paper size
        self.paperWidth              = 1.0
        self.paperHeight             = 1.0
        self.landscape               = False
        self.twosided                = True
        self.spatium                 = SPATIUM20
        self.tuning                  = 440.0
        self.masterGain              = 0.3
        self.chorusGain              = 0.0
        self.reverbGain              = 0.0
        self.reverbRoomSize          = 0.5
        self.reverbDamp              = 0.5
        self.reverbWidth             = 1.0

        self.importStyleFile = QString()
        self.defaultPlayDuration     = 300      # ms
        self.warnPitchRange          = True
        self.followSong              = True
        self.importCharset           = "GBK"
      
        self.useOsc                  = False
        self.oscPort                 = 5282

        self.checkUpdateStartup      = 0     
        self.firstStartWeb = True
        self.firstStart12 = True
        self.dirty = False
        self.soundFont = 0
        
    def write(self):
        self.dirty = False
        s = QSettings()

        s.setValue("bgUseColor",         self.bgUseColor)
        s.setValue("fgUseColor",         self.fgUseColor)
        s.setValue("bgWallpaper",        self.bgWallpaper)
        s.setValue("fgWallpaper",        self.fgWallpaper)
        s.setValue("fgColor",            self.fgColor)
        s.setValue("bgColor",            self.bgColor)

        s.setValue("selectColor1",       self.selectColor[0])
        s.setValue("selectColor2",       self.selectColor[1])
        s.setValue("selectColor3",       self.selectColor[2])
        s.setValue("selectColor4",       self.selectColor[3])
        s.setValue("dropColor",          self.dropColor)
        s.setValue("defaultColor",       self.defaultColor)
        s.setValue("enableMidiInput",    self.enableMidiInput)
        s.setValue("playNotes",          self.playNotes)

        s.setValue("soundFont",          self.soundFont)
        s.setValue("lPort",              self.lPort)
        s.setValue("rPort",              self.rPort)
        s.setValue("showNavigator",      self.showNavigator)
        s.setValue("showPlayPanel",      self.showPlayPanel)
        s.setValue("showWebPanel",       self.showWebPanel)
        s.setValue("showStatusBar",      self.showStatusBar)

        s.setValue("useAlsaAudio",       self.useAlsaAudio)
        s.setValue("useJackAudio",       self.useJackAudio)
        s.setValue("useJackMidi",        self.useJackMidi)
        s.setValue("usePortaudioAudio",  self.usePortaudioAudio)
        s.setValue("midiPorts",          self.midiPorts)
        s.setValue("rememberLastMidiConnections", self.rememberLastMidiConnections)

        s.setValue("alsaDevice",         self.alsaDevice)
        s.setValue("alsaSampleRate",     self.alsaSampleRate)
        s.setValue("alsaPeriodSize",     self.alsaPeriodSize)
        s.setValue("alsaFragments",      self.alsaFragments)
        s.setValue("portaudioDevice",    self.portaudioDevice)
        s.setValue("portMidiInput",   self.portMidiInput)

        s.setValue("layoutBreakColor",   self.layoutBreakColor)
        s.setValue("antialiasedDrawing", self.antialiasedDrawing)
        if self.sessionStart == SessionStart.EMPTY_SESSION:
            s.setValue("sessionStart", "empty")
        elif self.sessionStart == SessionStart.LAST_SESSION:
            s.setValue("sessionStart", "last")
        elif self.sessionStart == SessionStart.NEW_SESSION:
            s.setValue("sessionStart", "new")
        elif self.sessionStart == SessionStart.SCORE_SESSION:
            s.setValue("sessionStart", "score")
        s.setValue("startScore",         self.startScore)
        s.setValue("workingDirectory",   self.workingDirectory)
        #s.setValue("lastSaveDirectory",  lastSaveDirectory)
        #s.setValue("lastSaveCopyDirectory",  lastSaveCopyDirectory)
        s.setValue("showSplashScreen",   self.showSplashScreen)

        s.setValue("midiExpandRepeats",  self.midiExpandRepeats)
        s.setValue("playRepeats",        self.playRepeats)
        s.setValue("instrumentList", self.instrumentList)

        s.setValue("alternateNoteEntry", self.alternateNoteEntryMethod)
        s.setValue("proximity",          self.proximity)
        s.setValue("autoSave",           self.autoSave)
        s.setValue("autoSaveTime",       self.autoSaveTime)
        s.setValue("pngScreenShot",      self.pngScreenShot)
        s.setValue("language",           self.language)
        s.setValue("iconHeight",          self.iconHeight)
        s.setValue("iconWidth",           self.iconWidth)
        s.setValue("noteEntryIconHeight", self.noteEntryIconHeight)
        s.setValue("noteEntryIconWidth",  self.noteEntryIconWidth)
        s.setValue("applicationFont", self.applicationFont)
        s.setValue("style", self.style)

        s.setValue("replaceFractions", self.replaceFractions)
        s.setValue("replaceCopyrightSymbol", self.replaceCopyrightSymbol)
        s.setValue("paperSize", self.paperSize)
        s.setValue("paperWidth", self.paperWidth)
        s.setValue("paperHeight", self.paperHeight)
        s.setValue("landscape", self.landscape)
        s.setValue("twosided", self.twosided)
        s.setValue("spatium", self.spatium)
        s.setValue("tuning", self.tuning)
        s.setValue("masterGain", self.masterGain)
        s.setValue("chorusGain", self.chorusGain)
        s.setValue("reverbGain", self.reverbGain)
        s.setValue("reverbRoomSize", self.reverbRoomSize)
        s.setValue("reverbDamp", self.reverbDamp)
        s.setValue("reverbWidth", self.reverbWidth)

        s.setValue("defaultPlayDuration", self.defaultPlayDuration)
        s.setValue("importStyleFile", self.importStyleFile)
        s.setValue("importCharset", self.importCharset)
        s.setValue("warnPitchRange", self.warnPitchRange)
        s.setValue("followSong", self.followSong)
      
        s.setValue("firstStartWeb", self.firstStartWeb)
        s.setValue("firstStart12", False)

        s.setValue("checkUpdateStartup", self.checkUpdateStartup)

        self.writeShortcuts()
      
    def read(self):
        s = QSettings ()

        self.bgUseColor      = s.value("bgUseColor", True).toBool()
        self.fgUseColor      = s.value("fgUseColor", False).toBool()
        self.bgWallpaper     = s.value("bgWallpaper").toString()
        self.fgWallpaper     = s.value("fgWallpaper", ":/data/paper5.png").toString()
        self.fgColor         = s.value("fgColor", QColor(255, 255, 255)).value<QColor>()
        self.bgColor         = s.value("bgColor", QColor(0x76, 0x76, 0x6e)).value<QColor>()

        self.selectColor[0]  = s.value("selectColor1", QColor(Qt.blue)).value<QColor>()
        self.selectColor[1]  = s.value("selectColor2", QColor(0, 150, 0)).value<QColor>()
        self.selectColor[2]  = s.value("selectColor3", QColor(230, 180, 50)).value<QColor>()
        self.selectColor[3]  = s.value("selectColor4", QColor(200, 0, 200)).value<QColor>()

        self.defaultColor    = s.value("defaultColor", QColor(Qt.black)).value<QColor>()
        self.dropColor       = s.value("dropColor",    QColor(Qt.red)).value<QColor>()

        self.enableMidiInput = s.value("enableMidiInput", True).toBool()
        self.playNotes       = s.value("playNotes", True).toBool()
        self.lPort           = s.value("lPort").toString()
        self.rPort           = s.value("rPort").toString()
        self.defaultSoundfont = GL.mscoreGlobalShare+"sound/TimGM6mb.sf2"
        self.soundFont       = s.value("soundFont", self.defaultSoundfont).toString()
        if self.soundFont == ":/data/piano1.sf2":
            self.soundFont = self.defaultSoundfont
        self.showNavigator   = s.value("showNavigator", True).toBool()
        self.showStatusBar   = s.value("showStatusBar", True).toBool()
        self.showPlayPanel   = s.value("showPlayPanel", False).toBool()
        self.showWebPanel    = s.value("showWebPanel", True).toBool()


        self.useAlsaAudio       = s.value("useAlsaAudio", False).toBool()
        self.useJackAudio       = s.value("useJackAudio", False).toBool()
        self.useJackMidi        = s.value("useJackMidi",  False).toBool()
        self.usePortaudioAudio  = s.value("usePortaudioAudio", True).toBool()

        self.alsaDevice         = s.value("alsaDevice", "default").toString()
        self.alsaSampleRate     = s.value("alsaSampleRate", 48000).toInt()
        self.alsaPeriodSize     = s.value("alsaPeriodSize", 1024).toInt()
        self.alsaFragments      = s.value("alsaFragments", 3).toInt()
        self.portaudioDevice    = s.value("portaudioDevice", -1).toInt()
        self.portMidiInput      = s.value("portMidiInput", "").toString()
        self.layoutBreakColor   = s.value("layoutBreakColor", QColor(Qt.green)).value<QColor>()
        self.antialiasedDrawing = s.value("antialiasedDrawing", True).toBool()

        path = QDesktopServices.storageLocation(QDesktopServices.DocumentsLocation)
        self.workingDirectory   = s.value("workingDirectory", path).toString()

        self.showSplashScreen         = s.value("showSplashScreen", True).toBool()
        self.midiExpandRepeats        = s.value("midiExpandRepeats", True).toBool()
        self.playRepeats              = s.value("playRepeats", True).toBool()
        self.alternateNoteEntryMethod = s.value("alternateNoteEntry", False).toBool()
        self.midiPorts                = s.value("midiPorts", 2).toInt()
        self.rememberLastMidiConnections = s.value("rememberLastMidiConnections", True).toBool()
        self.proximity                = s.value("proximity", 6).toInt()
        self.autoSave                 = s.value("autoSave", True).toBool()
        self.autoSaveTime             = s.value("autoSaveTime", 2).toInt()
        self.pngScreenShot            = s.value("pngScreenShot", False).toBool()
        self.language                 = s.value("language", "system").toString()
        self.iconHeight               = s.value("iconHeight", 24).toInt()
        self.iconWidth                = s.value("iconHeight", 24).toInt()
        self.noteEntryIconHeight      = s.value("noteEntryIconHeight", ICON_HEIGHT).toInt()
        self.noteEntryIconWidth       = s.value("noteEntryIconWidth", ICON_WIDTH).toInt()
        self.applicationFont          = s.value("applicationFont", "").toString()
        self.style                    = s.value("style", "").toString()

        self.replaceFractions = s.value("replaceFractions", True).toBool()
        self.replaceCopyrightSymbol = s.value("replaceCopyrightSymbol", True).toBool()
        self.paperSize              = QPrinter.PageSize(s.value("paperSize", QPrinter.A4).toInt())
        self.paperWidth             = s.value("paperWidth", 1.0).toDouble()
        self.paperHeight            = s.value("paperHeight", 1.0).toDouble()
        self.landscape              = s.value("landscape", False).toBool()
        self.twosided               = s.value("twosided", True).toBool()
        self.spatium                = s.value("spatium", SPATIUM20).toDouble()
        self.tuning                 = s.value("tuning", 440.0).toDouble()
        self.masterGain             = s.value("masterGain", 0.3).toDouble()
        self.chorusGain             = s.value("chorusGain", 0.0).toDouble()
        self.reverbGain             = s.value("reverbGain", 0.0).toDouble()
        self.reverbRoomSize         = s.value("reverbRoomSize", 0.5).toDouble()
        self.reverbDamp             = s.value("reverbDamp", 0.5).toDouble()
        self.reverbWidth            = s.value("reverbWidth", 1.0).toDouble()

        self.defaultPlayDuration    = s.value("defaultPlayDuration", 300).toInt()
        self.importStyleFile        = s.value("importStyleFile", "").toString()
        self.importCharset          = s.value("importCharset", "GBK").toString()
        self.warnPitchRange         = s.value("warnPitchRange", True).toBool()
        self.followSong             = s.value("followSong", True).toBool()
      
        self.firstStartWeb = s.value("firstStartWeb", True).toBool()
        self.firstStart12 = s.value("firstStart12", True).toBool()

        self.checkUpdateStartup = s.value("checkUpdateStartup", UpdateChecker.defaultPeriod()).toInt()
        if self.checkUpdateStartup == 0:
            checkUpdateStartup = UpdateChecker.defaultPeriod()

        ss = QString(s.value("sessionStart", "score").toString())
        if ss == "last":
            self.sessionStart = SessionStart.LAST_SESSION
        elif ss == "new":
            self.sessionStart = SessionStart.NEW_SESSION
        elif ss == "score":
            self.sessionStart = SessionStart.SCORE_SESSION
        elif ss == "empty":
            self.sessionStart = SessionStart.EMPTY_SESSION

        self.startScore     = s.value("startScore", "data/Reunion_Example.mscz").toString()
        if self.startScore == "data/Promenade_Example.mscx":
            self.startScore = ":/data/Reunion_Example.mscz"
        self.instrumentList = s.value("instrumentList", ":/data/instruments.xml").toString()

        self.readShortcuts()

preferences = Preferences()

class PreferenceDialog(QDialog, Ui_PrefsDialogBase):
    def __init__(self, parent = None):
        super(PreferenceDialog, self).__init__(parent)
        self.setupUi(self)
        self.shortcutsChanged        = False
        self.jackDriver.setEnabled(False)
        self.alsaDriver.setEnabled(False)
        self.portaudioDriver.setEnabled(False)
        self.portmidiDriverInput.setVisible(False)

        fgButtons = QButtonGroup(self)
        fgButtons.setExclusive(True)
        fgButtons.addButton(self.fgColorButton)
        fgButtons.addButton(self.fgWallpaperButton)
        self.connect(self.fgColorButton, SIGNAL("toggled(bool)"), self.fgClicked)
        bgButtons = QButtonGroup(self)
        bgButtons.setExclusive(True)
        bgButtons.addButton(self.bgColorButton)
        bgButtons.addButton(self.bgWallpaperButton)
        self.updateValues(preferences)

        self.connect(self.buttonBox, SIGNAL("clicked(QAbstractButton)"), self.buttonBoxClicked)
        self.connect(self.fgWallpaperSelect,  SIGNAL("clicked()"), self.selectFgWallpaper)
        self.connect(self.bgWallpaperSelect,  SIGNAL("clicked()"), self.selectBgWallpaper)
        self.connect(self.workingDirectoryButton, SIGNAL("clicked()"), self.selectWorkingDirectory)
        self.connect(self.instrumentListButton,   SIGNAL("clicked()"), self.selectInstrumentList)
        self.connect(self.startWithButton,        SIGNAL("clicked()"), self.selectStartWith)
        self.connect(self.shortcutList, SIGNAL("itemActivated(QTreeWidgetItem, int)"), self.defineShortcutClicked)
        self.connect(self.resetShortcut, SIGNAL("clicked()"), self.resetShortcutClicked)
        self.connect(self.clearShortcut, SIGNAL("clicked()"), self.clearShortcutClicked)
        self.connect(self.defineShortcut, SIGNAL("clicked()"), self.defineShortcutClicked)
        self.connect(self.resetToDefault, SIGNAL("clicked()"), self.resetAllValues)

        self.connect(self.paperHeight, SIGNAL("valueChanged(double)"), self.paperSizeChanged)
        self.connect(self.paperWidth,  SIGNAL("valueChanged(double)"), self.paperSizeChanged)
        self.connect(self.pageGroup,   SIGNAL("activated(int)"), self.pageFormatSelected)
        self.connect(self.landscape,   SIGNAL("toggled(bool)"), self.landscapeToggled)

        self.connect(self.styleFileButton, SIGNAL("clicked()"), self.styleFileButtonClicked)
