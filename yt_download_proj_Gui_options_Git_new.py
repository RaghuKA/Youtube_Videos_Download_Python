from __future__ import unicode_literals
import youtube_dl
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5_learn_Pyuic5_Edit import Ui_MainWindow
import sys
import model
from PyQt5.QtCore import QUrl,QObject,pyqtSlot

#self.selectDownloadInputFileBtn.clicked.connect(self.openFileNameDialog)
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        #super(mywindow, self).__init__()
        super().__init__()
        self.model = model.Model()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.ui.comboBox_VideoQuality.addItem("First item") #add item
        self.ui.comboBox_VideoQuality.addItem("Second item")

        # openFile = QtWidgets.QAction("&open File", self)
        # openFile.setStatusTip('Open File')
        # openFile.triggered.connect(self.file_open)

        self.fileName = None

        #self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        #fName= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.file_open))
        file_Input= self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        
        
        #file_Input = str(self.openFileNameDialog())
        
        #f_Name= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))
        self.ui.pushButton_Browse_for_DownloadFolder.clicked.connect(self.openFileNameDialog2)
        self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos)

        

        #f_Name= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))

    def refreshAll( self ):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.lineEdit.setText( self.model.getFileName() )
        self.textEdit.setText( self.model.getFileContents() )

    def file_open(self):
        #name= QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        name= QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        #file_Input=open("name", 'r')

    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ):
            self.fileName = fileName
            self.fileContents = open( fileName, 'r' ).read()
        else:
            self.fileContents = ""
            self.fileName = ""
    
    def getFileName( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.fileName

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ",options=options)
        #fileName, _ = str(QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        #fileName, _ = str(QtWidgets.QFileDialog.selectFile(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        if fileName:
            self.model.setFileName( fileName )
            self.refreshAll()

        # if fileName:
        #     print(fileName)
        #     #self.inputFileLineEdit.setText(filename)
        # return fileName
    
     
    def openFileNameDialog2(self):
        # DownloadFolderName, _ = input(QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) "))
        #DownloadFolderName, _ = QtWidgets.QFileDialog.setDirectory(None, "Select the folder", "")
        DownloadFolderName = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory'))
        # if DownloadFolderName:
        #     print(DownloadFolderName)
        return DownloadFolderName

    # def saveVideo(self):
    #     saveVid, _ = QtWidgets.QFileDialog.saveFileContent(None, "Save file", "","All files (*.*) " )

    # def saveFileDialog(self):
    #     try:
    #         self.pushButtonSaveAs.clicked.disconnect()
    #     except (AttributeError, TypeError):
    #         pass
    #     options = QtWidgets.QFileDialog.Options()
    #     # options |= QFileDialog.DontUseNativeDialog # Qt's builtin File Dialogue
    #     fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Open", "", "All Files (*.*)", options=options)
    #     if fileName:
    #         try:
    #             with open(fileName, 'w') as file:
    #                 file.write(self.plainTextEdit.toPlainText())
    #             self.statusBar().showMessage("'" + fileName + "' saved successfully")
    #             self.labelLoading.setPixmap(self.distro)
    #         except PermissionError:
    #             pass
    #             self.statusBar().showMessage("Unable to save '" + fileName + "'")
    #     self.pushButtonSaveAs.clicked.connect(lambda: self.saveFileDialog())

    # Save Button's Actons↓ 

    def DownloadVideos(self):
        fileName =  self.lineEdit.text()
        #file_Input = str(ui.openFileNameDialog().getFileName)
        #file_Input = open(str(self.openFileNameDialog.fileName), 'r')
        #with open(self.) as f:
        #fN= self.openFileNameDialog2.getOpenFileName

        
        with open(fileName) as f:

        #with open(fileName) as f:
            my_list = list(fileName)
        print(my_list)
        ydl_opts = {}
        #os.mkdir('Downloaded_videos2')
        #os.chdir('Downloaded_videos2')
        #QtWidgets.QFileDialog.saveFileContent(None, "Save file", "","All files (*.*) " )
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(my_list)        


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())