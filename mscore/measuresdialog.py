# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measuresdialog.UI'
#
# Created: Mon Mar 16 13:46:27 2015
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

class Ui_MeasuresDialogBase(object):
    def setupUi(self, MeasuresDialogBase):
        MeasuresDialogBase.setObjectName(_fromUtf8("MeasuresDialogBase"))
        MeasuresDialogBase.resize(400, 112)
        self.vboxlayout = QtGui.QVBoxLayout(MeasuresDialogBase)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(MeasuresDialogBase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.vboxlayout.addWidget(self.label_2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(MeasuresDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.measures = QtGui.QSpinBox(MeasuresDialogBase)
        self.measures.setMaximum(1000)
        self.measures.setMinimum(1)
        self.measures.setObjectName(_fromUtf8("measures"))
        self.hboxlayout.addWidget(self.measures)
        self.vboxlayout.addLayout(self.hboxlayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        spacerItem2 = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(MeasuresDialogBase)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout1.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(MeasuresDialogBase)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(MeasuresDialogBase)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MeasuresDialogBase.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MeasuresDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MeasuresDialogBase)

    def retranslateUi(self, MeasuresDialogBase):
        MeasuresDialogBase.setWindowTitle(_translate("MeasuresDialogBase", "Mscore: Append Measures", None))
        self.label_2.setText(_translate("MeasuresDialogBase", "Append empty measures:", None))
        self.label.setText(_translate("MeasuresDialogBase", "Number of measures to append", None))
        self.okButton.setText(_translate("MeasuresDialogBase", "OK", None))
        self.cancelButton.setText(_translate("MeasuresDialogBase", "Cancel", None))

