from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KOTIKOTlauncher(object):
    def setupUi(self, KOTIKOTlauncher):
        # self.gridLayout.addWidget(self.pushButton, столбец, ряд, 1, 1)

        KOTIKOTlauncher.setObjectName("KOTIKOTlauncher")
        KOTIKOTlauncher.resize(434, 434)
        KOTIKOTlauncher.setMinimumSize(QtCore.QSize(50, 50))
        KOTIKOTlauncher.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.centralwidget = QtWidgets.QWidget(KOTIKOTlauncher)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 435))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_1.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        KOTIKOTlauncher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KOTIKOTlauncher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        KOTIKOTlauncher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KOTIKOTlauncher)
        self.statusbar.setObjectName("statusbar")
        KOTIKOTlauncher.setStatusBar(self.statusbar)

        self.retranslateUi(KOTIKOTlauncher)
        QtCore.QMetaObject.connectSlotsByName(KOTIKOTlauncher)

    def retranslateUi(self, KOTIKOTlauncher):
        _translate = QtCore.QCoreApplication.translate
        KOTIKOTlauncher.setWindowTitle(_translate("KOTIKOTlauncher", "MainWindow"))
        self.pushButton_1.setText(_translate("KOTIKOTlauncher", "AutoShipper"))
        self.pushButton_2.setText(_translate("KOTIKOTlauncher", "Bars`s auto\nbridger"))
        self.pushButton_3.setText(_translate("KOTIKOTlauncher", "CatBench"))
        self.pushButton_4.setText(_translate("KOTIKOTlauncher", "CoolAutoPressers"))
        self.pushButton_5.setText(_translate("KOTIKOTlauncher", "FilesConnector"))
        self.pushButton_6.setText(_translate("KOTIKOTlauncher", "Meowarch"))
        self.pushButton_7.setText(_translate("KOTIKOTlauncher", "PyQt converter"))
        self.pushButton_8.setText(_translate("KOTIKOTlauncher", "fileGenerator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KOTIKOTlauncher = QtWidgets.QMainWindow()
    ui = Ui_KOTIKOTlauncher()
    ui.setupUi(KOTIKOTlauncher)
    KOTIKOTlauncher.show()
    sys.exit(app.exec_())
