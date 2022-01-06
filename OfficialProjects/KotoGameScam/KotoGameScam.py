import random
import subprocess, sys, time, ctypes
from threading import Thread

################### Imports that might be not installed #####################
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

################### Some variables #####################
address = []
straddress = []
sortedAddresses = []
wantToChangeAddresses = []

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.model = QtGui.QStandardItemModel()
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(721, 437)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 60, 251, 21))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.AllProcessListInGUI = QtWidgets.QTextBrowser(self.centralwidget)
        self.AllProcessListInGUI.setGeometry(QtCore.QRect(0, 80, 251, 331))
        self.AllProcessListInGUI.setObjectName("AllProcessListInGUI")

        self.processName = QtWidgets.QTextEdit(self.centralwidget)
        self.processName.setGeometry(QtCore.QRect(0, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.processName.setFont(font)
        self.processName.setObjectName("processName")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 0, 251, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.processOK = QtWidgets.QPushButton(self.centralwidget)
        self.processOK.setGeometry(QtCore.QRect(210, 30, 41, 31))
        self.processOK.setObjectName("processOK")

        self.ScannedValue = QtWidgets.QLineEdit(self.centralwidget)
        self.ScannedValue.setGeometry(QtCore.QRect(260, 0, 461, 41))
        self.ScannedValue.setObjectName("ScannedValue")

        self.FirstScan = QtWidgets.QPushButton(self.centralwidget)
        self.FirstScan.setGeometry(QtCore.QRect(260, 40, 161, 41))
        self.FirstScan.setObjectName("FirstScan")

        self.SortValues = QtWidgets.QPushButton(self.centralwidget)
        self.SortValues.setGeometry(QtCore.QRect(420, 40, 301, 41))
        self.SortValues.setObjectName("SortValues")

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(260, 80, 461, 21))
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.ScannedValue_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ScannedValue_2.setGeometry(QtCore.QRect(260, 310, 461, 41))
        self.ScannedValue_2.setObjectName("ScannedValue_2")

        self.AdressOK = QtWidgets.QPushButton(self.centralwidget)
        self.AdressOK.setGeometry(QtCore.QRect(670, 100, 51, 71))
        self.AdressOK.setObjectName("AdressOK")

        self.UnselAll = QtWidgets.QPushButton(self.centralwidget)
        self.UnselAll.setGeometry(QtCore.QRect(670, 240, 51, 71))
        self.UnselAll.setObjectName("UnselAll")

        self.SelectAll = QtWidgets.QPushButton(self.centralwidget)
        self.SelectAll.setGeometry(QtCore.QRect(670, 170, 51, 71))
        self.SelectAll.setObjectName("SelectAll")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 350, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.generateListOfAddresses()

    def generateListOfAddresses(self):
        self.model = QtGui.QStandardItemModel(self)
        for line in straddress:
            self.item = QtGui.QStandardItem(line)
            self.item.setCheckable(True)
            self.item.setCheckState(QtCore.Qt.Checked)
            self.model.appendRow(self.item)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setModel(self.model)
        self.listView.setGeometry(QtCore.QRect(260, 100, 411, 211))
        self.listView.show()


    def onAccepted(self):
        self.choices = [self.model.item(i).text() for i in range(self.model.rowCount()) if
                        self.model.item(i).checkState() == QtCore.Qt.Checked]
        self.accept()

    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)

    def addressSelCheck(self):
        wantToChangeAddresses.clear()
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                wantToChangeAddresses.append(address[i])
        print("Addresses that will be changed: " + str(wantToChangeAddresses))

    def generateRandomAdresses(self):
        address.append(str(random.randint(1, 50000)))
        self.generateListOfAddresses()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("KotoGameScam", "KotoGameScam"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All process</p></body></html>"))
        self.processName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.processName.setPlaceholderText(_translate("MainWindow", "GTA5.exe"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Process here (from all process)</span></p></body></html>"))
        self.processOK.setText(_translate("MainWindow", "OK"))
        self.ScannedValue.setPlaceholderText(_translate("MainWindow", "Value"))
        self.FirstScan.setText(_translate("MainWindow", "First Scan Value"))
        self.SortValues.setText(_translate("MainWindow", "ThrowAwaySort Values"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Adresses with this value</p></body></html>"))
        self.ScannedValue_2.setPlaceholderText(_translate("MainWindow", "New value"))
        self.AdressOK.setText(_translate("MainWindow", "OK"))
        self.UnselAll.setText(_translate("MainWindow", "Unselect \nall"))
        self.SelectAll.setText(_translate("MainWindow", "Select \nall"))
        self.pushButton.setText(_translate("MainWindow", "SCAM VALUES"))


################### Launching GUI #####################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

################### Getting values and GUI functions #####################
value = 0
valueAfterChange = 0
wantedValue = 0


################### Working functions #####################
print("Logs:")

def getalproc():
    allproc = []
    for proc in psutil.process_iter():
        allproc.append(str(proc.name()))
    allproc.sort()
    normproc = []
    for element in allproc:
        if element not in normproc:
            normproc.append(element)
    for i in normproc:
        ui.AllProcessListInGUI.append(i)

def getProcFromText():
    global procName
    procName = str(ui.processName.toPlainText())
    print("Ok, I will search in " + procName)

def get_pid(process_name):
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
    return pid

def firstcsan():
    try:
        global address
        value = int(ui.ScannedValue.text())
        print("I will check for " + str(value))
        pid = get_pid(procName)
        with mem_edit.Process.open_process(pid) as p:
            address = p.search_all_memory(ctypes.c_int(int(value)))
            print('Found', len(address), 'addresses')
        for i in address:
            straddress.append(str(i))
        ui.generateListOfAddresses()
    except:
        pass

def sort():
    try:
        sortedAddresses.clear()
        proc = pymem.Pymem(procName)
        valueAfterChange = int(ui.ScannedValue.text())
        print("I will leave only " + str(valueAfterChange))
        for addressFromAll in address:
            try:
                if proc.read_int(addressFromAll) == int(valueAfterChange):
                    sortedAddresses.append(addressFromAll)
            except:
                pass
        print('Found after ThrowAwaySort:', len(sortedAddresses))
        address.clear()
        for i in sortedAddresses:
            address.append(i)
        straddress.clear()
        for i in address:
            straddress.append(str(i))
        ui.generateListOfAddresses()
    except:
        pass

def scam():
    try:
        wantedValue = int(ui.ScannedValue_2.text())
        print("Started scamming to " + str(wantedValue))
        proc = pymem.Pymem(procName)
        for wantToChangeAddress in wantToChangeAddresses:
            proc.write_int(wantToChangeAddress, int(wantedValue))
            print('Changed value in ' + str(wantToChangeAddress) + ' to ' + str(wantedValue))
        print('Values of addresses ' + str(wantToChangeAddresses) + ' now are ' + str(wantedValue))
    except:
        pass

getalproc()

################### Checking buttons #####################
ui.SelectAll.clicked.connect(ui.select)
ui.UnselAll.clicked.connect(ui.unselect)
ui.AdressOK.clicked.connect(ui.addressSelCheck)
ui.processOK.clicked.connect(getProcFromText)
ui.FirstScan.clicked.connect(firstcsan)
ui.SortValues.clicked.connect(sort)
ui.pushButton.clicked.connect(scam)


################### Exiting #####################
sys.exit(app.exec_())