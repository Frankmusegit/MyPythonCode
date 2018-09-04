#!/usr/bin/env python
#-*- coding:utf-8 -*-
from timedialog_ui import *
from Palette import *
from Timesig import *


TSIG_FOUR_FOUR  = 0x40000104
TSIG_ALLA_BREVE = 0x40002084


class TimeDialog(QWidget, Ui_TimeDialogBase):
    def __init__(self, p,  parent = None):
        QWidget(parent, Qt.Dialog | Qt.Window)
        super(TimeDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(self.tr("Muse 3.0: Time Signatures"))
        l = QVBoxLayout()
        self.frame.setLayout(l)
        self.sp = Palette()
        self.sp.setReadOnly(False)
        self.connect(self.sp, SIGNAL("changed()"), self.setDirty)

        timePalette = PaletteScrollArea(self.sp)
        policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        timePalette.setSizePolicy(policy)
        timePalette.setRestrictHeight(False)

        l.addWidget(timePalette)
        self.sp.setGrid(60, 60)

        self._dirty = False
        self.connect(self.addButton, SIGNAL("clicked()"), self.addClicked)

        if not useFactorySettings:
            f = QFile(GL.dataPath + "/" + "timesigs.xml")
            if f.exists() and self.sp.read(f):
                return
        a = TimeSig(GL.gscore)
        a.TimeSig2(2, 2)
        self.sp.append(a, "2/2")

        a = TimeSig(GL.gscore)
        a.TimeSig2(4, 2)
        self.sp.append(a, "2/4")

        a = TimeSig(GL.gscore)
        a.TimeSig2(4, 3)
        self.sp.append(a, "3/4")

        a = TimeSig(GL.gscore)
        a.TimeSig2(4, 4)
        self.sp.append(a, "4/4")

        a = TimeSig(GL.gscore)
        a.TimeSig2(4, 5)
        self.sp.append(a, "5/4")

        a = TimeSig(GL.gscore)
        a.TimeSig2(4, 6)
        self.sp.append(a, "6/4")

        a = TimeSig(GL.gscore)
        a.TimeSig2(8, 3)
        self.sp.append(a, "3/8")

        a = TimeSig(GL.gscore)
        a.TimeSig2(8, 6)
        self.sp.append(a, "6/8")

        a = TimeSig(GL.gscore)
        a.TimeSig2(8, 9)
        self.sp.append(a, "9/8")

        a = TimeSig(GL.gscore)
        a.TimeSig2(8, 12)
        self.sp.append(a, "12/8")

        a = TimeSig(GL.gscore)
        a.TimeSig1(TSIG_FOUR_FOUR)
        self.sp.append(a, self.tr("4/4 common time"))

        a = TimeSig(GL.gscore)
        a.TimeSig1(TSIG_ALLA_BREVE)
        self.sp.append(a, self.tr("2/2 alla breve"))

    def addClicked(self):
        ts = TimeSig(GL.gscore, self.n.value(), self.z1.value(), self.z2.value(), self.z3.value(), self.z4.value())
        self.sp.append(ts, "")
        self._dirty = True
