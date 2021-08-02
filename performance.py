from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_5(object):
    def setupUi_5(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.home.setText("Home")
        self.home.setGeometry(QtCore.QRect(0, 0, 100, 40))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("Work in progress")
        self.label.setGeometry(QtCore.QRect(400, 400, 400, 40))
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_5()
    ui.setupUi_5(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())