# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cellproperties.ui'
#
# Created: Fri Jul 03 14:18:12 2015
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

class Ui_PaletteCellProperties(object):
    def setupUi(self, PaletteCellProperties):
        PaletteCellProperties.setObjectName(_fromUtf8("PaletteCellProperties"))
        PaletteCellProperties.resize(396, 118)
        self.horizontalLayout = QtGui.QHBoxLayout(PaletteCellProperties)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(PaletteCellProperties)
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
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(PaletteCellProperties)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.xoffset = QtGui.QSpinBox(self.groupBox)
        self.xoffset.setMinimum(-1000)
        self.xoffset.setMaximum(1000)
        self.xoffset.setObjectName(_fromUtf8("xoffset"))
        self.horizontalLayout_2.addWidget(self.xoffset)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.yoffset = QtGui.QSpinBox(self.groupBox)
        self.yoffset.setMinimum(-1000)
        self.yoffset.setMaximum(1000)
        self.yoffset.setObjectName(_fromUtf8("yoffset"))
        self.horizontalLayout_2.addWidget(self.yoffset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(PaletteCellProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(PaletteCellProperties)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PaletteCellProperties.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PaletteCellProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(PaletteCellProperties)

    def retranslateUi(self, PaletteCellProperties):
        PaletteCellProperties.setWindowTitle(_translate("PaletteCellProperties", "Chord Properties", None))
        self.groupBox.setTitle(_translate("PaletteCellProperties", "Palette Cell Properties", None))
        self.label.setText(_translate("PaletteCellProperties", "Content Offset", None))
        self.label_2.setText(_translate("PaletteCellProperties", "x:", None))
        self.label_4.setText(_translate("PaletteCellProperties", "y:", None))

#import mscore_rc
