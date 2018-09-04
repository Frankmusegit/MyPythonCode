#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from Scoreview import *

class ScoreTab(QWidget):

    currentScoreViewChanged = pyqtSignal(ScoreView)
    
    def __init__(self, sl, parent = None):
        super(ScoreTab, self).__init__(parent)
        self.scoreList = sl
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(0)
        layout.setMargin(2)
    
        self.tab = QTabBar()
        self.tab.setExpanding(False)
        self.tab.setSelectionBehaviorOnRemove(QTabBar.SelectRightTab)
        self.tab.setFocusPolicy(Qt.StrongFocus)
        self.stack = QStackedLayout()
        layout.addWidget(self.tab)
        layout.addLayout(self.stack)
        self.tab.setTabsClosable(True)

        self.connect(self.tab, SIGNAL("currentChanged(int)"), self, SLOT("setCurrent(int)"))
        self.connect(self.tab, SIGNAL("tabCloseRequested(int)"), self, SLOT("removeTab(int)"))

    def view(self, n):
        score = self.scoreList[n]
        for i in range (0, self.stack.count()):
            v = self.stack.widget(i)
            if v.score() == score:
                return v
        return 0

    @pyqtSlot(int)
    def setCurrent(self, n):
        print n
        if n == -1:
            self.currentScoreViewChanged.emit(0)
            return
        v = self.view(n)
        if not v:
            v = ScoreView()
            v.setScore(self.scoreList[n])
            self.stack.addWidget(v)
        self.stack.setCurrentWidget(v)
        self.currentScoreViewChanged.emit(v)

    @pyqtSlot(int)
    def removeTab(self, idx):
        score = self.tab.tabData(idx)
        for i in range(0, self.stack.count()):
            v = self.stack.widget(i)
            if v.score() == score:
                self.stack.takeAt(i)
                break

        cidx = self.currentIndex()
        self.tab.removeTab(idx)
        if cidx > idx:
            cidx -= 1
        self.setCurrentIndex(cidx)

    def currentIndex(self):
        return self.tab.currentIndex()

    def insertTab(self, idx, s):
        self.tab.insertTab(idx, s)
        self.tab.setTabData(idx, self.scoreList[idx])

    def setCurrentIndex(self, idx):
        if self.currentIndex() == idx:
            self.setCurrent(idx)
        else:
            self.tab.setCurrentIndex(idx)
        self.tab.setTabText(idx, self.tab.tabText(idx))

    def count(self):
        return len(self.scoreList)

