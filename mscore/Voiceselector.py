#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Preferences import *
import GL

class VoiceButton(QToolButton):
    def __init__(self, v, parent = None):
        super( VoiceButton, self).__init__(parent)
        self.voice = v
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, preferences.selectColor[self.voice].light(170))
        pal.setColor(QPalette.Button, preferences.selectColor[self.voice].light(100))
        self.setPalette(pal)

    def paintEvent(self, e):
        p = QPainter(self)
        if self.isChecked():
            if self.isChecked():
                p.fillRect(e.rect(), self.palette().color(QPalette.Button))
            else:
                p.fillRect(e.rect(), self.palette().color(QPalette.Window))
            p.setPen(1)
            p.drawRect(0, 0, self.width()-1, self.height()-1)
        else:
            p.fillRect(e.rect(), self.palette().color(QPalette.Window))
        f = self.font()
        f.setPixelSize(preferences.iconHeight / 2)
        p.setFont(f)
        p.drawText(self.rect(), Qt.AlignCenter, QString("%1").arg(self.voice+1))

    def sizeHint(self):
        w = preferences.iconWidth / 2
        h = preferences.iconHeight / 2
        return QSize((w * 3)/2, h)


class VoiceSelector(QWidget):

    triggered = pyqtSignal(QAction)

    def __init__(self, parent = None):
        super(VoiceSelector, self).__init__(parent)
        vwl = QGridLayout()
        vwl.setSpacing(0)
        vwl.setContentsMargins(0, 0, 0, 0)

        sl2 = QStringList()
        sl2 << "voice-1" << "voice-3" << "voice-2" << "voice-4"
        v = [ 0, 2, 1, 3 ]
        vag = QActionGroup(self)
        vag.setExclusive(True)
        i = 0
        for s in sl2:
            a = GL.actions[s.toLatin1().data()]
            a.setCheckable(True)
            vag.addAction(a)
            tb = VoiceButton(v[i])
            tb.setDefaultAction(a)
            vwl.addWidget(tb, i/2, i%2, 1, 1)
            i = i + 1
        self.setLayout(vwl)
        vag.triggered.connect(self.triggered)
        #self.connect(vag, SIGNAL("triggered(QAction)"), self, SIGNAL("triggered(QAction)"))

