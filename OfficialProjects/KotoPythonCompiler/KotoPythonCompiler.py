import sys, os, subprocess
import py_compile

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
    from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 380)
        MainWindow.setMinimumSize(QtCore.QSize(490, 380))
        MainWindow.setMaximumSize(QtCore.QSize(490, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.path = QtWidgets.QTextEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(0, 30, 491, 31))
        self.path.setObjectName("path")
        self.appName = QtWidgets.QTextBrowser(self.centralwidget)
        self.appName.setGeometry(QtCore.QRect(0, 0, 491, 31))
        self.appName.setObjectName("appName")
        self.openbutton = QtWidgets.QPushButton(self.centralwidget)
        self.openbutton.setGeometry(QtCore.QRect(0, 60, 141, 51))
        self.openbutton.setObjectName("openbutton")
        self.openbutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.openbutton_2.setGeometry(QtCore.QRect(140, 60, 351, 51))
        self.openbutton_2.setObjectName("openbutton_2")
        self.logs = QtWidgets.QTextEdit(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(0, 110, 491, 201))
        self.logs.setReadOnly(True)
        self.logs.setAcceptRichText(True)
        self.logs.setObjectName("logs")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 310, 491, 41))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
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
        self.path.setPlaceholderText(_translate("MainWindow", "Path/To/File.py"))
        self.appName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">KOTO PythonCompiler</span></p></body></html>"))
        self.openbutton.setText(_translate("MainWindow", "Open file"))
        self.openbutton_2.setText(_translate("MainWindow", "Compile file to .pyc (will appear near .py file)"))
        self.logs.setPlaceholderText(_translate("MainWindow", "Logs will appear here"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">©KOTIKOT, script by BarsTiger</span></p></body></html>"))

    def openFile(self, MainWindow):
        self.path.setText(str(QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open Python File', '*.py')[0]))


def pycompile():
    path_to_file = getFromPath()
    path_to_compiled = os.path.split(str(path_to_file))[0] + "/" + os.path.splitext(os.path.basename(path_to_file))[0] + ".pyc"
    try:
        if os.path.splitext(os.path.basename(path_to_file))[1] == ".py":
            ui.logs.append("Starting")
            py_compile.compile(path_to_file, cfile=path_to_compiled)
            ui.logs.append("Generated .pyc file to " + path_to_compiled)
        else:
            ui.logs.append("Error. Not .py file")
    except:
        ui.logs.append("Error. Check for file existence")

pathToFile = ""

def getFromPath():
    global pathToFile
    pathToFile = ui.path.toPlainText()
    return pathToFile

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.openbutton.clicked.connect(ui.openFile)
ui.openbutton_2.clicked.connect(getFromPath)
ui.openbutton_2.clicked.connect(pycompile)

sys.exit(app.exec_())
