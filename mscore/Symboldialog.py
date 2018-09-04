#!/usr/bin/env python
#-*- coding:utf-8 -*-
from symboldialog_ui import *
from Palette import *
from Sym import *

class SymbolDialog(QWidget, Ui_SymbolDialogBase):

    def __init__(self, parent = None):
        QWidget(parent, Qt.Dialog | Qt.Window)
        super(SymbolDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(self.tr("Muse 3.0: Symbols"))
        l = QVBoxLayout()
        self.frame.setLayout(l)
        sa = QScrollArea()
        l.addWidget(sa)

        self.createSymbolPalette()
        self.sp =  Palette()
        self.sp.setAcceptDrops(False)
        self.sp.setDrawGrid(True)
        self.sp.setSelectable(True)

        self.connect(self.sp, SIGNAL("changed()"), self.setDirty)
        self.connect(self.systemFlag, SIGNAL("stateChanged(int)"), self.systemFlagChanged)

        sa.setWidget(self.sp)

    def createSymbolPalette(self):
        self.sp = Palette()
        for i  in range(0, SymName.lastSym):
            self.sp.append(i)


    def setDirty(self):
        preferences.dirty = True

    def systemFlagChanged(self, state):
        sysFlag = False
        if state == Qt.Checked:
            sysFlag = True
        for i in range(0, len(self.sp)):
            e = self.sp.element(i)
            if e:
                e.setSystemFlag(sysFlag)
