#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from playpanel_ui import *
import GL

class PlayPanel(QWidget, Ui_PlayPanelBase):

    def __init__(self, parent = None):
        QWidget(parent, Qt.Dialog)
        super(PlayPanel, self).__init__()
        self.cachedTickPosition = -1
        self.cachedTimePosition = -1
        self.cs                 = 0
        self.setupUi(self)
        self.setScore(0)

        self.playButton.setDefaultAction(GL.actions["play"])
        self.rewindButton.setDefaultAction(GL.actions["rewind"])

        self.connect(self.volumeSlider, SIGNAL("valueChanged(double,int)"), self.volumeChanged)
        self.connect(self.posSlider,    SIGNAL("sliderMoved(int)"), self.setPos)
        self.connect(self.tempoSlider,  SIGNAL("valueChanged(double,int)"), self.relTempoChanged)
        self.connect(self.swingStyle,   SIGNAL("currentIndexChanged(int)"), self.swingStyleChanged)

