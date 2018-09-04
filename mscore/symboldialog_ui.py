# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symboldialog.ui'
#
# Created: Mon Jul 06 19:51:11 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SymbolDialogBase(object):
    def setupUi(self, SymbolDialogBase):
        SymbolDialogBase.setObjectName(_fromUtf8("SymbolDialogBase"))
        SymbolDialogBase.resize(711, 532)
        self.vboxlayout = QtGui.QVBoxLayout(SymbolDialogBase)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.frame = QtGui.QFrame(SymbolDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.vboxlayout.addWidget(self.frame)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.systemFlag = QtGui.QCheckBox(SymbolDialogBase)
        self.systemFlag.setObjectName(_fromUtf8("systemFlag"))
        self.hboxlayout.addWidget(self.systemFlag)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(SymbolDialogBase)
        QtCore.QMetaObject.connectSlotsByName(SymbolDialogBase)

    def retranslateUi(self, SymbolDialogBase):
        SymbolDialogBase.setWindowTitle(_translate("SymbolDialogBase", "Form", None))
        self.systemFlag.setText(_translate("SymbolDialogBase", "System Flag", None))

