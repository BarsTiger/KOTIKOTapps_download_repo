import ctypes, sys, os, subprocess

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
    from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(361, 190))
        MainWindow.setMaximumSize(QtCore.QSize(361, 190))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ON = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ON.sizePolicy().hasHeightForWidth())
        self.ON.setSizePolicy(sizePolicy)
        self.ON.setStyleSheet("QPushButton{\n"
"font-size: 50px;\n"
"font-family: Arial\n"
"}")
        self.ON.setText("ON")
        self.ON.setObjectName("ON")
        self.horizontalLayout.addWidget(self.ON)
        self.OFF = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.OFF.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OFF.sizePolicy().hasHeightForWidth())
        self.OFF.setSizePolicy(sizePolicy)
        self.OFF.setMinimumSize(QtCore.QSize(50, 50))
        self.OFF.setStyleSheet("QPushButton{\n"
"font-size: 50px;\n"
"font-family: Arial\n"
"}")
        self.OFF.setObjectName("OFF")
        self.horizontalLayout.addWidget(self.OFF)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KOTO_LAN_Control"))
        self.ON.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ON</span></p></body></html>"))
        self.OFF.setText(_translate("MainWindow", "OFF"))


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    exit()

def off():
    os.system('netsh interface set interface name="Ethernet" admin=DISABLED')
    print("Turned OFF")

def on():
    os.system('netsh interface set interface name="Ethernet" admin=ENABLED')
    print("Turned ON")
    print("May take a while, about 30 seconds")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

os.system('cls' if os.name == 'nt' else 'clear')
os.system('title KOTO_LAN_Control')

ui.ON.clicked.connect(on)
ui.OFF.clicked.connect(off)

sys.exit(app.exec_())
