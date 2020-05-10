from __future__ import unicode_literals
import youtube_dl
import os

from PyQt5 import QtWidgets, QtCore, QtGui, uic
#from PyQt5_learn_Pyuic5_Edit import Ui_MainWindow
import sys
import model
from PyQt5.QtCore import QUrl,QObject,pyqtSlot #, QStringList
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout #, QWidget
#from gi.overrides.Pango import Layout
import functools 
import operator

#from PyQt5 import QtWidgets, QtCore, QtWidgets, uic, QtGui
#self.selectDownloadInputFileBtn.clicked.connect(self.openFileNameDialog)
# class mywindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         #super(mywindow, self).__init__()
#         super().__init__()
#         #self.model = model.Model()
        
#class SampleQt (QtWidgets.QMainWindow, Ui_MainWindow):

glob_ui_file = "PyQt5_learn_Pyuic5.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(glob_ui_file)

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, download_location_string=""):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        # self.setupUi (self)
        
        # self.Ui_MainWindow.comboBox_VideoQuality.addItem("First item") #add item
        # self.Ui_MainWindow.comboBox_VideoQuality.addItem("Second item")
        

        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        self.ui.comboBox_VideoQuality.addItem("First item") #add item
        self.ui.comboBox_VideoQuality.addItem("Second item")

        # openFile = QtWidgets.QAction("&open File", self)
        # openFile.setStatusTip('Open File')
        # openFile.triggered.connect(self.file_open)

        #self.mywindow.openFileDialog.fileName = str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog()))

        #self.button.clicked.connect(self.getFileName)
        #fN=str()
        #fN= self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        # get_filepath_url = QUrl.fromLocalFile(fN)
        # print(get_filepath_url)    

        #fN =None
        #fN= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))
        
        self.download_location_string = download_location_string
        self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
        

        #fName= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.file_open))
        #file_Input2= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))
        
        
        #file_Input = str(self.openFileNameDialog())
        
        #f_Name= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))
        #self.ui.pushButton_Browse_for_DownloadFolder.clicked.connect(self.openFileNameDialog2)
        #self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos(fN))
        self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos)

    # def init_ui(self):
    #     self.fileName = None
    #     layout = QVBoxLayout()
    #     layout.addWidget(self.openFileNameDialog)
    #     self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog)
    #     self.ui.pushButton_DownloadVideos.clicked.connect(self.DownloadVideos)



    #self.fileName = None

    #filePath= openFileNameDialog.fileName[0]

        #f_Name= str(self.ui.pushButton_Browse_for_InputFile.clicked.connect(self.openFileNameDialog))

    # def refreshAll( self ):
    #     '''
    #     Updates the widgets whenever an interaction happens.
    #     Typically some interaction takes place, the UI responds,
    #     and informs the model of the change.  Then this method
    #     is called, pulling from the model information that is
    #     updated in the GUI.
    #     '''
    #     self.lineEdit.setText( self.model.getFileName() )
    #     self.textEdit.setText( self.model.getFileContents() )
    # def convertTuple(self,tup): 
    #     str = functools.reduce(operator.add, (tup)) 
    #     return str
    
    def convertTuple(self,tup): 
        str =  ''.join(tup) 
        return str

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
        #return self.fileName
        print (self.download_location_string)

    def openFileNameDialog(self):
        #def retfilepath():
        #     options = QtWidgets.QFileDialog.Options()
        #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #     fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ",options=options)
        #options = QtWidgets.QFileDialog.Options()
        #options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #fileName = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ",options=options)
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) ")
        print(fileName)
        #fileName, _ = str(QtWidgets.QFileDialog.getOpenFileName(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        #fileName, _ = str(QtWidgets.QFileDialog.selectFile(None, "Browse Input File", "", "Input Files (*.txt *.csv) "))
        get_filepath_url = QUrl.fromLocalFile(fileName)
        print(type(get_filepath_url))
        #human_readable_filepath_url = fileName.toDisplayString () [8:]
        #human_readable_filepath_url = get_filepath_url.toDisplayString () [8:]
        human_readable_filepath_url = fileName
        print(human_readable_filepath_url)
        #self.FilePathField.setText (human_readable_filepath_url)
        #self.centralWidget.FilePathField.setText(human_readable_filepath_url)
        #self.copy_label.setText (human_readable_filepath_url)
        # here you are assigning value to the class member download_loaction_string
        self.download_location_string = human_readable_filepath_url
        
        
        
        #     get_filepath_url = QUrl.gfromLocalFile(fileName)
        #     #print(get_filepath_url)
        # print(fileName)
        # dlg = QFileDialog()
        # # dlg.setFileMode(QFileDialog.AnyFile)
        # # dlg.setFilter("Text files (*.txt)")
        # filenames = QStringList()
        # if dlg.exec_():
        #     filenames = dlg.selectedFiles()

        #filePath=fileName[0]  
        #return retfilepath  
        #return self.fileName  

        # if fileName:
        #     self.model.setFileName( fileName )
        #     self.refreshAll()
        #file_Input= fileName
        #return file_Input
        # if fileName:
        #     print(fileName)
        #     #self.inputFileLineEdit.setText(filename)
        #return fileName
    
     
    def openFileNameDialog2(self):
        # DownloadFolderName, _ = input(QtWidgets.QFileDialog.getOpenFileName(None, "Browse for Download Location", "", "Input Files (*.*) "))
        #DownloadFolderName, _ = QtWidgets.QFileDialog.setDirectory(None, "Select the folder", "")
        DownloadFolderName = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory'))
        # if DownloadFolderName:
        #     print(DownloadFolderName)

        downloc= QFileDialog()
        DownloadFolderName.get
        
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
    #path= self.ui.openFileNameDialog.fileName[0]
    def DownloadVideos(self):
        #fileName =  self.lineEdit.text()
        #file_Input = str(ui.openFileNameDialog().getFileName)
        #file_Input = open(str(self.openFileNameDialog.fileName), 'r')
        #with open(self.) as f:
        #fN= self.openFileNameDialog2.getOpenFileName

        #fN=self.openFileNameDialog.file_Input
        #path=self.openFileNameDialog.fileName[0]
        #fil=self.ui.pushButton_DownloadVideos.clicked.connect(self.openFileNameDialog.fileName[0])

        #with open(self.openFileNameDialog.fileName[0]) as f:

        #with open(fp) as f:
        #with open(filenames[0]) as f:
            
        with open(download_location_string) as f:
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