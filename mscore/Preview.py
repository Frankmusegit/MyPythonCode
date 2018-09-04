#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PagePreview(QWidget):
    def __init__(self, parent = None):
        super(PagePreview, self).__init__(parent)
        self.setAttribute(Qt.WA_NoBackground)
        self._score  = 0
