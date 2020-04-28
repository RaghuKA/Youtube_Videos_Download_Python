# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Raghu-Software-Practice\Nitin_Python_Project\my_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from __future__ import unicode_literals
import youtube_dl
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectDownloadInputFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectDownloadInputFileBtn.setGeometry(QtCore.QRect(100, 170, 121, 71))
        self.selectDownloadInputFileBtn.setObjectName("selectDownloadInputFileBtn")

        
        self.SelectDownloadLocationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SelectDownloadLocationBtn.setGeometry(QtCore.QRect(100, 260, 151, 71))
        self.SelectDownloadLocationBtn.setObjectName("SelectDownloadLocationBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectDownloadInputFileBtn.clicked.connect(self.openFileNameDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectDownloadInputFileBtn.setText(_translate("MainWindow", "Browse file"))
        self.SelectDownloadLocationBtn.setText(_translate("MainWindow", "Specify Download location"))

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse file", "", "Input Files (*.txt *.csv) ")
        if fileName:
            print(fileName)

    #def Download_yt(self):
        with open(fileName) as f:
            my_list = list(f)
        print(my_list)

        ydl_opts = {}
        os.mkdir('Downloaded_videos2')
        os.chdir('F:/Raghu-Software-Practice/Nitin_Python_Project/Downloaded_videos2')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(my_list)
    
    # def file_open(self):
    #     name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
