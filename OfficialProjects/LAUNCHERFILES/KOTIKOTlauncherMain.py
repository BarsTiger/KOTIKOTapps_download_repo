from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_KOTIKOTlauncher(object):
    @staticmethod
    def genSize() -> tuple:
        with open("OfficialProjects/LAUNCHERFILES/apps.json") as appsfile:
            apps = len(list(json.load(appsfile)))
        h = 1
        w = 1
        while h * w < apps:
            h += 1
            if h * w < apps:
                w += 1
        return h * 105 + 5, w * 105 + 25, w

    def setupUi(self, KOTIKOTlauncher):
        self.genSize()
        KOTIKOTlauncher.setObjectName("KOTIKOTlauncher")
        self.size = self.genSize()
        KOTIKOTlauncher.resize(self.size[0], self.size[1])
        KOTIKOTlauncher.setMinimumSize(QtCore.QSize(self.size[0], self.size[1]))
        KOTIKOTlauncher.setMaximumSize(QtCore.QSize(self.size[0], self.size[1]))

        self.centralwidget = QtWidgets.QWidget(KOTIKOTlauncher)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 425, 425))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        with open("OfficialProjects/LAUNCHERFILES/apps.json") as appsfile:
            apps = list(json.load(appsfile))

        self.buttons = list()
        for i in range(len(apps)):
            self.buttons.append(QtWidgets.QPushButton(self.gridLayoutWidget))
            self.buttons[i].setMinimumSize(QtCore.QSize(100, 100))
            self.buttons[i].setMaximumSize(QtCore.QSize(100, 100))
            self.buttons[i].setObjectName(apps[i])
            self.buttons[i].setText(apps[i])
            self.gridLayout.addWidget(self.buttons[i], i // self.size[2], i % self.size[2], 1, 1)

        KOTIKOTlauncher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KOTIKOTlauncher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 21))
        self.menubar.setObjectName("menubar")
        KOTIKOTlauncher.setMenuBar(self.menubar)

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.actionOpen_settings = QtWidgets.QAction(KOTIKOTlauncher)
        self.actionOpen_settings.setObjectName("actionOpen_settings")
        self.menuSettings.addAction(self.actionOpen_settings)

        self.retranslateUi(KOTIKOTlauncher)
        QtCore.QMetaObject.connectSlotsByName(KOTIKOTlauncher)

    def retranslateUi(self, KOTIKOTlauncher):
        _translate = QtCore.QCoreApplication.translate
        KOTIKOTlauncher.setWindowTitle(_translate("KOTIKOTlauncher", "KOTIKOTlauncher"))
        self.menuSettings.setTitle(_translate("KOTIKOTlauncher", "Settings"))
        self.actionOpen_settings.setText(_translate("KOTIKOTlauncher", "Open settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KOTIKOTlauncher = QtWidgets.QMainWindow()
    ui = Ui_KOTIKOTlauncher()
    ui.setupUi(KOTIKOTlauncher)
    KOTIKOTlauncher.show()
    sys.exit(app.exec_())
