# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quicklinkwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(782, 546)
        Form.setStyleSheet("QWidget{\n"
"        border-style:outset;\n"
"        border-width:3px;\n"
"\n"
"        color:rgb(85, 255, 127);\n"
"        border-radius: 8px;\n"
"        font: \"Arial\";\n"
"        font-size: 18px;\n"
"        border: 2px solid #00b894;\n"
"        background-color: #000000;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 591, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.url = QtWidgets.QTextEdit(self.layoutWidget)
        self.url.setMaximumSize(QtCore.QSize(600, 40))
        self.url.setStyleSheet("QTextEdit{\n"
"        border-radius: 6px;\n"
"        font: 9pt \"Arial\";\n"
"        font-size: 20px;\n"
"        border: 2px solid rgb(85, 0, 255);\n"
"        background-color: #000000;\n"
"        color: #00FF00;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        border-radius: 8px;\n"
"        font-size: 18px;\n"
"        background-color: #2d3436;\n"
"}")
        self.url.setObjectName("url")
        self.horizontalLayout_2.addWidget(self.url)
        self.urlButton = QtWidgets.QPushButton(self.layoutWidget)
        self.urlButton.setMinimumSize(QtCore.QSize(101, 0))
        self.urlButton.setStyleSheet("QPushButton{\n"
"        border-radius: 6px;\n"
"        font: 9pt \"Arial\";\n"
"        font-size: 20px;\n"
"        border: 2px solid rgb(85, 0, 255);\n"
"        background-color: #000000;\n"
"        color: #00FF00;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        border-radius: 8px;\n"
"        font-size: 18px;\n"
"        background-color: #2d3436;\n"
"}")
        self.urlButton.setObjectName("urlButton")
        self.horizontalLayout_2.addWidget(self.urlButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.command = QtWidgets.QTextEdit(self.layoutWidget)
        self.command.setMaximumSize(QtCore.QSize(600, 40))
        self.command.setStyleSheet("QTextEdit{\n"
"        border-radius: 6px;\n"
"        font: 9pt \"Arial\";\n"
"        font-size: 20px;\n"
"        border: 2px solid rgb(85, 0, 255);\n"
"        background-color: #000000;\n"
"        color: #00FF00;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        border-radius: 8px;\n"
"        font-size: 18px;\n"
"        background-color: #2d3436;\n"
"}")
        self.command.setObjectName("command")
        self.horizontalLayout_4.addWidget(self.command)
        self.cmdButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cmdButton.setMinimumSize(QtCore.QSize(101, 0))
        self.cmdButton.setStyleSheet("QPushButton{\n"
"        border-radius: 6px;\n"
"        font: 9pt \"Arial\";\n"
"        font-size: 20px;\n"
"        border: 2px solid rgb(85, 0, 255);\n"
"        background-color: #000000;\n"
"        color: #00FF00;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"        border-radius: 8px;\n"
"        font-size: 18px;\n"
"        background-color: #2d3436;\n"
"}")
        self.cmdButton.setObjectName("cmdButton")
        self.horizontalLayout_4.addWidget(self.cmdButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 160, 671, 361))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.control = QtWidgets.QTextEdit(self.layoutWidget1)
        self.control.setMinimumSize(QtCore.QSize(0, 0))
        self.control.setBaseSize(QtCore.QSize(200, 200))
        self.control.setObjectName("control")
        self.verticalLayout.addWidget(self.control)
        self.whoamiText = QtWidgets.QTextEdit(self.layoutWidget1)
        self.whoamiText.setMaximumSize(QtCore.QSize(16777215, 40))
        self.whoamiText.setObjectName("whoamiText")
        self.verticalLayout.addWidget(self.whoamiText)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.returnText = QtWidgets.QTextEdit(self.layoutWidget1)
        self.returnText.setMinimumSize(QtCore.QSize(511, 341))
        self.returnText.setMaximumSize(QtCore.QSize(511, 600))
        self.returnText.setObjectName("returnText")
        self.horizontalLayout.addWidget(self.returnText)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.urlButton.setText(_translate("Form", "link"))
        self.cmdButton.setText(_translate("Form", "command"))
