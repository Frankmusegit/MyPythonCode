#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Preview import *

from pagesettings_ui import Ui_PageSettingsBase

class PageSettings(QDialog, Ui_PageSettingsBase):
    def __init__(self, parent = None):
        super(PageSettings, self).__init__(parent = None)
        self.setupUi(self)
        self.setModal(True)
        self.preview = PagePreview()
        ppLayout = QHBoxLayout()
        ppLayout.addWidget(self.preview)
        self.previewGroup.setLayout(ppLayout)

        mmUnit = True

        if mmUnit:
            self.mmButton.setChecked(True)
        else:
            self.inchButton.setChecked(True)
        self.connect(self.mmButton, SIGNAL("clicked()"), self.mmClicked)
        self.connect(self.inchButton, SIGNAL("clicked()"), self.inchClicked)
        self.connect(self.buttonApply, SIGNAL("clicked()"), self.apply)
        self.connect(self.buttonOk, SIGNAL("clicked()"), self.ok)
        self.connect(self.landscape, SIGNAL("toggled(bool)"), self.landscapeToggled)
        self.connect(self.twosided, SIGNAL("toggled(bool)"), self.twosidedToggled)
        self.connect(self.pageHeight, SIGNAL("valueChanged(double)"), self.pageHeightChanged)
        self.connect(self.pageWidth,  SIGNAL("valueChanged(double)"), self.pageWidthChanged)


