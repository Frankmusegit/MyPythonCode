#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Navigator(QFrame):

    def __init__(self):
        super(Navigator, self).__init__()
        #self.setAttribute(Qt.WA_NoBackground)
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)
        self._score = 0
        self._cv = 0
        self.viewRect = QRect()
        self.startMove = QPoint()
        self.moving = False
        self.pm = QPixmap()
        self.redraw = False
        self.matrix = QTransform() 
