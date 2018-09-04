#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Seq import *

PDPI = 0.0
DPI = 0.0
DPMM = 0.0
symbols = dict()
icons = dict()
shortcuts = dict()
defaultTextStyles = []
docName = QString()
dataPath = QString()
mscoreGlobalShare = QString("share\\")
mscore = 0
gscore = 0
seq = Seq()
recentScores = QStringList()
revision = QString()
instrumentGroups = list()
articulation = list()
actions = dict()


