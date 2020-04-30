# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Raghu-Software-Practice\Nitin_Python_Project\PyQt5_learn_Pyuic5.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Browse_for_InputFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Browse_for_InputFile.setGeometry(QtCore.QRect(350, 70, 131, 41))
        self.pushButton_Browse_for_InputFile.setObjectName("pushButton_Browse_for_InputFile")
        self.comboBox_VideoQuality = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_VideoQuality.setGeometry(QtCore.QRect(250, 170, 69, 22))
        self.comboBox_VideoQuality.setObjectName("comboBox_VideoQuality")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_SelectFile = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectFile.setGeometry(QtCore.QRect(90, 60, 121, 16))
        self.label_SelectFile.setObjectName("label_SelectFile")
        self.label_DownloadOptions = QtWidgets.QLabel(self.centralwidget)
        self.label_DownloadOptions.setGeometry(QtCore.QRect(100, 140, 121, 16))
        self.label_DownloadOptions.setObjectName("label_DownloadOptions")
        self.label_VideoQuality = QtWidgets.QLabel(self.centralwidget)
        self.label_VideoQuality.setGeometry(QtCore.QRect(110, 170, 121, 16))
        self.label_VideoQuality.setObjectName("label_VideoQuality")
        self.pushButton_Browse_for_DownloadFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Browse_for_DownloadFolder.setGeometry(QtCore.QRect(350, 240, 181, 41))
        self.pushButton_Browse_for_DownloadFolder.setObjectName("pushButton_Browse_for_DownloadFolder")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 250, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_SelectFile_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectFile_2.setGeometry(QtCore.QRect(90, 230, 141, 16))
        self.label_SelectFile_2.setObjectName("label_SelectFile_2")
        self.label_SelectFile_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectFile_3.setGeometry(QtCore.QRect(350, 210, 181, 21))
        self.label_SelectFile_3.setObjectName("label_SelectFile_3")
        self.pushButton_DownloadVideos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DownloadVideos.setGeometry(QtCore.QRect(240, 340, 121, 31))
        self.pushButton_DownloadVideos.setObjectName("pushButton_DownloadVideos")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Browse_for_InputFile.setText(_translate("MainWindow", "Browse Input File"))
        self.label_SelectFile.setText(_translate("MainWindow", "Select a file:"))
        self.label_DownloadOptions.setText(_translate("MainWindow", "Download options"))
        self.label_VideoQuality.setText(_translate("MainWindow", "Select Video Quality"))
        self.pushButton_Browse_for_DownloadFolder.setText(_translate("MainWindow", "Browse for Download location"))
        self.label_SelectFile_2.setText(_translate("MainWindow", "Select Download Folder:"))
        self.label_SelectFile_3.setText(_translate("MainWindow", "Select Download location:"))
        self.pushButton_DownloadVideos.setText(_translate("MainWindow", "Download Videos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
