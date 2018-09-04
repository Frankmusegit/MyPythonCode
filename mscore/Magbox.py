#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *


class MagValidator(QValidator):

    def __init__(self, parent = None):
        super(MagValidator, self).__init__(parent)

class MagBox(QComboBox):

    def __init__(self, parent = None):
        super(MagBox, self).__init__(parent)

    def indexChanged(self, idx):
        self.magChanged(idx)