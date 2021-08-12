import os
import random
import subprocess, sys, time, ctypes
try:
    import pymem
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pymem'])
    import pymem

try:
    import mem_edit
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'mem_edit'])
    import mem_edit

try:
    import psutil
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'psutil'])
    import psutil

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
    from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 280)
        MainWindow.setMinimumSize(QtCore.QSize(200, 280))
        MainWindow.setMaximumSize(QtCore.QSize(200, 280))
        MainWindow.setBaseSize(QtCore.QSize(0, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, -10, 185, 284))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstscan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.firstscan.setObjectName("firstscan")
        self.verticalLayout.addWidget(self.firstscan)
        self.firstcheck = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.firstcheck.setObjectName("firstcheck")
        self.verticalLayout.addWidget(self.firstcheck)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.secondscan = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.secondscan.setObjectName("secondscan")
        self.verticalLayout_2.addWidget(self.secondscan)
        self.secondcheck = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.secondcheck.setObjectName("secondcheck")
        self.verticalLayout_2.addWidget(self.secondcheck)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMouseTracking(True)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.setValue(100)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">CatMoneyX</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Casino bet changer</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">by BarsTiger</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">simplified KotoGameScam</span></p></body></html>"))
        self.firstscan.setText(_translate("MainWindow", "100"))
        self.firstcheck.setText(_translate("MainWindow", "First check"))
        self.secondscan.setText(_translate("MainWindow", "50"))
        self.secondcheck.setText(_translate("MainWindow", "Second check"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">1000000</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Change bet"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">C</span></p><p><span style=\" font-size:11pt; font-weight:600;\">a</span></p><p><span style=\" font-size:11pt; font-weight:600;\">t</span></p><p><span style=\" font-size:11pt; font-weight:600;\">M</span></p><p><span style=\" font-size:11pt; font-weight:600;\">o</span></p><p><span style=\" font-size:11pt; font-weight:600;\">n</span></p><p><span style=\" font-size:11pt; font-weight:600;\">e</span></p><p><span style=\" font-size:11pt; font-weight:600;\">y</span></p><p><span style=\" font-size:11pt; font-weight:600;\">X</span></p></body></html>"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

address = []
straddress = []
sortedAddresses = []
wantToChangeAddresses = []
procName = "GTA5.exe"
wantedValue = 1000000

def firstcsan():
    global address, straddress
    value = int(ui.firstscan.text())
    print("I will check for " + str(value))
    pid = mem_edit.Process.get_pid_by_name(procName)
    with mem_edit.Process.open_process(pid) as p:
        address = p.search_all_memory(ctypes.c_int(int(value)))
        print('Found', len(address), 'addresses')
    for i in address:
        straddress.append(str(i))
    print(straddress)

def secondscan():
    global address, straddress
    sortedAddresses.clear()
    proc = pymem.Pymem(procName)
    valueAfterChange = int(ui.secondscan.text())
    print("I will leave only " + str(valueAfterChange))
    for addressFromAll in address:
        if proc.read_int(addressFromAll) == int(valueAfterChange):
            sortedAddresses.append(addressFromAll)
    print('Found after ThrowAwaySort:', len(sortedAddresses))
    address.clear()
    for i in sortedAddresses:
        address.append(i)
    straddress.clear()
    for i in address:
        straddress.append(str(i))
    print(straddress)

def scam():
    global address, straddress, wantedValue
    wantedValue = getfromslider()
    print("Started scamming to " + str(wantedValue))
    proc = pymem.Pymem(procName)
    for wantToChangeAddress in straddress:
        proc.write_int(int(wantToChangeAddress), int(wantedValue))
        print('Changed value in ' + str(wantToChangeAddress) + ' to ' + str(wantedValue))
    print('Values of addresses ' + str(straddress) + ' now are ' + str(wantedValue))

def getfromslider():
    global wantedValue
    wantedValue = 10000 * ui.horizontalSlider.value()
    ui.textEdit.setText(str(wantedValue))
    return wantedValue

ui.horizontalSlider.valueChanged.connect(getfromslider)
ui.firstcheck.clicked.connect(firstcsan)
ui.secondcheck.clicked.connect(secondscan)
ui.pushButton.clicked.connect(scam)

sys.exit(app.exec_())
