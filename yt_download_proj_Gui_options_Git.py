from __future__ import unicode_literals
import youtube_dl
import os

from PyQt5 import QtWidgets, QtCore, QtGui
#QFileDialog
from PyQt5_learn_Pyuic5_Edit import Ui_MainWindow
import sys
import model

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
        
        #self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        #f_Name= str(self.openFileNameDialog)
        f_Name= self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
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

    def openFileNameDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        #fileName, _ = str(QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        #fileName, _ = str(QtWidgets.QFileDialog.selectFile(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        if fileName:
            print(fileName)
        return fileName
    
    #t_fileName= self.openFileNameDialog()
        # DownloadFolderName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) ")
        # if DownloadFolderName:
        #     print(DownloadFolderName)
    
    def openFileNameDialog2(self):
        # DownloadFolderName, _ = input(QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) "))
        #DownloadFolderName, _ = QtWidgets.QFileDialog.setDirectory(None, "Select the folder", "")
        DownloadFolderName = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory'))
        # if DownloadFolderName:
        #     print(DownloadFolderName)
        return DownloadFolderName

    # def saveVideo(self):
    #     saveVid, _ = QtWidgets.QFileDialog.saveFileContent(None, "Save file", "","All files (*.*) " )

    def saveFileDialog(self):
        try:
            self.pushButtonSaveAs.clicked.disconnect()
        except (AttributeError, TypeError):
            pass
        options = QtWidgets.QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog # Qt's builtin File Dialogue
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Open", "", "All Files (*.*)", options=options)
        if fileName:
            try:
                with open(fileName, 'w') as file:
                    file.write(self.plainTextEdit.toPlainText())
                self.statusBar().showMessage("'" + fileName + "' saved successfully")
                self.labelLoading.setPixmap(self.distro)
            except PermissionError:
                pass
                self.statusBar().showMessage("Unable to save '" + fileName + "'")
        self.pushButtonSaveAs.clicked.connect(lambda: self.saveFileDialog())

    # Save Button's Actons↓ 

    def DownloadVideos(self):
        #file_Input = str(self.openFileNameDialog())
        #with open(file_Input) as f:
        #fN= self.openFileNameDialog2.getOpenFileName

        with open(f_Name) as f:

        #with open(fileName) as f:
            my_list = list(f)
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