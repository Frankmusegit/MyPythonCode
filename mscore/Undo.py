#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from PyQt4.QtCore import *

class UndoGroup(QObject):

    canUndoChanged = pyqtSignal(bool)
    canRedoChanged = pyqtSignal(bool)
    cleanChanged = pyqtSignal(bool)

    def __init__(self):
        super(UndoGroup, self).__init__()
        self._activeStack = 0
        self.group = list()

    def addStack(self, stack):
        stack.setGroup(self)
        self.group.append(stack)
        self.connect(stack, SIGNAL("canUndoChanged(bool)"), self.canUndoChanged)
        self.connect(stack, SIGNAL("canRedoChanged(bool)"), self.canRedoChanged)
        self.connect(stack, SIGNAL("cleanChanged(bool)"), self.cleanChanged)

class UndoStack(QObject):

    canUndoChanged = pyqtSignal(bool)
    anRedoChanged = pyqtSignal(bool)
    cleanChanged = pyqtSignal(bool)

    def __init__(self):
        super(UndoStack, self).__init__()
        self.group = 0
        self.curCmd = 0
        self.curIdx = 0
        self.cleanIdx = 0

    def active(self):
        return self.curCmd != 0

    def setGroup(self, g):
        self.group = g
