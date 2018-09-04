# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertmeasuresdialog.UI'
#
# Created: Mon Mar 16 13:45:35 2015
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

class Ui_InsertMeasuresDialogBase(object):
    def setupUi(self, InsertMeasuresDialogBase):
        InsertMeasuresDialogBase.setObjectName(_fromUtf8("InsertMeasuresDialogBase"))
        InsertMeasuresDialogBase.resize(463, 191)
        self.verticalLayout_2 = QtGui.QVBoxLayout(InsertMeasuresDialogBase)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(InsertMeasuresDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/data/bg1.jpg")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(InsertMeasuresDialogBase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.insmeasures = QtGui.QSpinBox(InsertMeasuresDialogBase)
        self.insmeasures.setMinimum(1)
        self.insmeasures.setMaximum(1000)
        self.insmeasures.setObjectName(_fromUtf8("insmeasures"))
        self.hboxlayout.addWidget(self.insmeasures)
        self.label = QtGui.QLabel(InsertMeasuresDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.hboxlayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        spacerItem2 = QtGui.QSpacerItem(131, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(InsertMeasuresDialogBase)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout1.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(InsertMeasuresDialogBase)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout1.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(InsertMeasuresDialogBase)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), InsertMeasuresDialogBase.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), InsertMeasuresDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(InsertMeasuresDialogBase)

    def retranslateUi(self, InsertMeasuresDialogBase):
        InsertMeasuresDialogBase.setWindowTitle(_translate("InsertMeasuresDialogBase", "Mscore: Insert Measures", None))
        self.label_2.setText(_translate("InsertMeasuresDialogBase", "Insert empty measures:", None))
        self.label.setText(_translate("InsertMeasuresDialogBase", "Number of measures to insert", None))
        self.okButton.setText(_translate("InsertMeasuresDialogBase", "OK", None))
        self.cancelButton.setText(_translate("InsertMeasuresDialogBase", "Cancel", None))

#import mscore_rc
