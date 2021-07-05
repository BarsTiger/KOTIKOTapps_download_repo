import subprocess, sys
import time

#CanBeInstalled imports
try:
    import psutil
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'psutil'])
    import psutil

try:
    import PyQt5
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])

try:
    import mem_edit
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'mem_edit'])
    import mem_edit

from PyQt5 import QtCore, QtGui, QtWidgets

buttontxt = "Public\nSingle \nSession"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 219)
        MainWindow.setMinimumSize(QtCore.QSize(200, 219))
        MainWindow.setMaximumSize(QtCore.QSize(200, 219))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.setText(buttontxt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KotoGTAsingler"))

def sus():
    global buttontxt
    pid = mem_edit.Process.get_pid_by_name("GTA5.exe")
    p = psutil.Process(pid)
    p.suspend()
    ui.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
    time.sleep(10)
    p.resume()
    ui.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton.clicked.connect(sus)

sys.exit(app.exec_())

