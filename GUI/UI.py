# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(380, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.sBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.sBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.sBox.setObjectName("sBox")
        self.gridLayout.addWidget(self.sBox, 0, 1, 1, 1)
        self.sCombo = QtWidgets.QComboBox(self.centralwidget)
        self.sCombo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sCombo.setObjectName("sCombo")
        self.sCombo.addItem("")
        self.sCombo.addItem("")
        self.gridLayout.addWidget(self.sCombo, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.epsilonBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.epsilonBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.epsilonBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.epsilonBox.setObjectName("epsilonBox")
        self.gridLayout.addWidget(self.epsilonBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.rBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.rBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.rBox.setObjectName("rBox")
        self.gridLayout.addWidget(self.rBox, 2, 1, 1, 1)
        self.rCombo = QtWidgets.QComboBox(self.centralwidget)
        self.rCombo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.rCombo.setObjectName("rCombo")
        self.rCombo.addItem("")
        self.rCombo.addItem("")
        self.rCombo.addItem("")
        self.gridLayout.addWidget(self.rCombo, 2, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.uBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.uBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.uBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.uBox.setObjectName("uBox")
        self.gridLayout.addWidget(self.uBox, 3, 1, 1, 1)
        self.uCombo = QtWidgets.QComboBox(self.centralwidget)
        self.uCombo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.uCombo.setObjectName("uCombo")
        self.uCombo.addItem("")
        self.uCombo.addItem("")
        self.gridLayout.addWidget(self.uCombo, 3, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.u0Box = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.u0Box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.u0Box.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.u0Box.setObjectName("u0Box")
        self.gridLayout.addWidget(self.u0Box, 4, 1, 1, 1)
        self.u0Combo = QtWidgets.QComboBox(self.centralwidget)
        self.u0Combo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.u0Combo.setObjectName("u0Combo")
        self.u0Combo.addItem("")
        self.u0Combo.addItem("")
        self.gridLayout.addWidget(self.u0Combo, 4, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.timpBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timpBox.setMinimumSize(QtCore.QSize(80, 0))
        self.timpBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.timpBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.timpBox.setObjectName("timpBox")
        self.gridLayout.addWidget(self.timpBox, 5, 1, 1, 1)
        self.timpCombo = QtWidgets.QComboBox(self.centralwidget)
        self.timpCombo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timpCombo.setObjectName("timpCombo")
        self.timpCombo.addItem("")
        self.timpCombo.addItem("")
        self.timpCombo.addItem("")
        self.timpCombo.addItem("")
        self.gridLayout.addWidget(self.timpCombo, 5, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 9, 3, 1, 1)
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setObjectName("calculate_btn")
        self.gridLayout.addWidget(self.calculate_btn, 6, 0, 1, 4)
        self.answer_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.answer_label.setFont(font)
        self.answer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.answer_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.answer_label.setLineWidth(2)
        self.answer_label.setTextFormat(QtCore.Qt.RichText)
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setObjectName("answer_label")
        self.gridLayout.addWidget(self.answer_label, 8, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 28))
        self.menubar.setObjectName("menubar")
        self.menuFailas = QtWidgets.QMenu(self.menubar)
        self.menuFailas.setObjectName("menuFailas")
        MainWindow.setMenuBar(self.menubar)
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.menuFailas.addAction(self.exit_action)
        self.menubar.addAction(self.menuFailas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Thickness"))
        self.label.setText(_translate("MainWindow", "Kontakto plotas, S"))
        self.sCombo.setItemText(0, _translate("MainWindow", "mm^2"))
        self.sCombo.setItemText(1, _translate("MainWindow", "cm^2"))
        self.label_2.setText(_translate("MainWindow", "Dielektrinė knstanta, ε"))
        self.label_3.setText(_translate("MainWindow", "Apkrovos varža, R"))
        self.rCombo.setItemText(0, _translate("MainWindow", "Ω"))
        self.rCombo.setItemText(1, _translate("MainWindow", "kΩ"))
        self.rCombo.setItemText(2, _translate("MainWindow", "MΩ"))
        self.label_4.setText(_translate("MainWindow", "Generatoriaus įtampa, U"))
        self.uCombo.setItemText(0, _translate("MainWindow", "mV"))
        self.uCombo.setItemText(1, _translate("MainWindow", "V"))
        self.label_5.setText(_translate("MainWindow", "Talpinis šuolis, U0"))
        self.u0Combo.setItemText(0, _translate("MainWindow", "mV"))
        self.u0Combo.setItemText(1, _translate("MainWindow", "V"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Impulso trukmė, t<span style=\" vertical-align:sub;\">imp</span></p></body></html>"))
        self.timpCombo.setItemText(0, _translate("MainWindow", "ns"))
        self.timpCombo.setItemText(1, _translate("MainWindow", "μs"))
        self.timpCombo.setItemText(2, _translate("MainWindow", "ms"))
        self.timpCombo.setItemText(3, _translate("MainWindow", "s"))
        self.label_7.setText(_translate("MainWindow", "Atsakymas"))
        self.exit_btn.setText(_translate("MainWindow", "Išeiti"))
        self.calculate_btn.setText(_translate("MainWindow", "Skaičiuoti"))
        self.answer_label.setText(_translate("MainWindow", "????"))
        self.menuFailas.setTitle(_translate("MainWindow", "Fai&las"))
        self.exit_action.setText(_translate("MainWindow", "&Uždaryti"))
