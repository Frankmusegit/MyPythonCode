# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'palette.ui'
#
# Created: Fri Jul 03 14:12:08 2015
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

class Ui_PaletteProperties(object):
    def setupUi(self, PaletteProperties):
        PaletteProperties.setObjectName(_fromUtf8("PaletteProperties"))
        PaletteProperties.resize(298, 174)
        self.verticalLayout = QtGui.QVBoxLayout(PaletteProperties)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label = QtGui.QLabel(PaletteProperties)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.name = QtGui.QLineEdit(PaletteProperties)
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.name)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(PaletteProperties)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(PaletteProperties)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cellWidth = QtGui.QSpinBox(PaletteProperties)
        self.cellWidth.setMinimum(1)
        self.cellWidth.setMaximum(1000)
        self.cellWidth.setObjectName(_fromUtf8("cellWidth"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cellWidth)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_4 = QtGui.QLabel(PaletteProperties)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cellHeight = QtGui.QSpinBox(PaletteProperties)
        self.cellHeight.setMinimum(1)
        self.cellHeight.setMaximum(1000)
        self.cellHeight.setObjectName(_fromUtf8("cellHeight"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.cellHeight)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.showGrid = QtGui.QCheckBox(PaletteProperties)
        self.showGrid.setObjectName(_fromUtf8("showGrid"))
        self.verticalLayout.addWidget(self.showGrid)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.elementOffset = QtGui.QDoubleSpinBox(PaletteProperties)
        self.elementOffset.setObjectName(_fromUtf8("elementOffset"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.elementOffset)
        self.label_5 = QtGui.QLabel(PaletteProperties)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_6 = QtGui.QLabel(PaletteProperties)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.mag = QtGui.QDoubleSpinBox(PaletteProperties)
        self.mag.setMinimum(0.01)
        self.mag.setSingleStep(0.1)
        self.mag.setProperty("value", 1.0)
        self.mag.setObjectName(_fromUtf8("mag"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.mag)
        self.horizontalLayout_2.addLayout(self.formLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 107, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(PaletteProperties)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PaletteProperties)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PaletteProperties.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PaletteProperties.reject)
        QtCore.QMetaObject.connectSlotsByName(PaletteProperties)

    def retranslateUi(self, PaletteProperties):
        PaletteProperties.setWindowTitle(_translate("PaletteProperties", "MuseScore: Palette Properties", None))
        self.label.setText(_translate("PaletteProperties", "Name:", None))
        self.label_2.setText(_translate("PaletteProperties", "Cell Size:", None))
        self.label_3.setText(_translate("PaletteProperties", "w:", None))
        self.label_4.setText(_translate("PaletteProperties", "h:", None))
        self.showGrid.setText(_translate("PaletteProperties", "Show Grid", None))
        self.label_5.setText(_translate("PaletteProperties", "Element Offset", None))
        self.label_6.setText(_translate("PaletteProperties", "Scale:", None))

