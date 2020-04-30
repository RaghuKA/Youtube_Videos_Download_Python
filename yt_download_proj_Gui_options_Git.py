from __future__ import unicode_literals
import youtube_dl
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5_learn_Pyuic5 import Ui_MainWindow
import sys

#self.selectDownloadInputFileBtn.clicked.connect(self.openFileNameDialog)
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox_VideoQuality.addItem("First item") #add item
        self.ui.comboBox_VideoQuality.addItemmi("Second item")
        
        #self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        #self.ui.pushButton_Browse_for_DownloadFolder.clicked.connect(self.openFileNameDialog2)
        self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos)

        #f_Name= self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        if fileName:
            print(fileName)
        return fileName

        # DownloadFolderName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) ")
        # if DownloadFolderName:
        #     print(DownloadFolderName)
    
    def openFileNameDialog2(self):
        DownloadFolderName, _ = input(QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) "))
        if DownloadFolderName:
            print(DownloadFolderName)

    def DownloadVideos(self):
        file_Input = self.openFileNameDialog()
        with open(file_Input) as f:
            my_list = list(f)
        print(my_list)
        ydl_opts = {}
        os.mkdir('Downloaded_videos2')
        os.chdir('Downloaded_videos2')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(my_list)        


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())