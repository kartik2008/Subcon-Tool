## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 ## Library to import sqlite3, replace this with mysql connector of python

class PM_Renewal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(0,0,0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")

        ### Page 1: Dashboard ## 
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        ## Biggest Frame ## 
        self.frame = QtWidgets.QFrame(self.page1)
        self.frame.setGeometry(QtCore.QRect(20, 40, 1820, 1001))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        ## Request Summary Dashboard ## 
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(170, 420, 1491, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        ## Approved Requests Summary Table ##
        self.tableWidget7 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget7.setGeometry(QtCore.QRect(240, 100, 202, 92))
        self.tableWidget7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget7.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget7.setRowCount(3)
        self.tableWidget7.setColumnCount(2)
        self.tableWidget7.setObjectName("tableWidget7")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget7.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget7.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget7.setItem(2, 0, item)
        self.tableWidget7.horizontalHeader().setVisible(False)
        self.tableWidget7.horizontalHeader().setHighlightSections(False)
        self.tableWidget7.verticalHeader().setVisible(False)
        self.Approved = QtWidgets.QLabel(self.frame_2)
        self.Approved.setGeometry(QtCore.QRect(240, 60, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Approved.setFont(font)
        self.Approved.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Approved.setFrameShape(QtWidgets.QFrame.Box)
        self.Approved.setAlignment(QtCore.Qt.AlignCenter)
        self.Approved.setObjectName("Approved")

        ## Rejected Requests Summary Table ##
        self.tableWidget8 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget8.setGeometry(QtCore.QRect(660, 100, 202, 92))
        self.tableWidget8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget8.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget8.setRowCount(3)
        self.tableWidget8.setColumnCount(2)
        self.tableWidget8.setObjectName("tableWidget8")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget8.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget8.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget8.setItem(2, 0, item)
        self.tableWidget8.horizontalHeader().setVisible(False)
        self.tableWidget8.horizontalHeader().setHighlightSections(False)
        self.tableWidget8.verticalHeader().setVisible(False)
        self.Rejected = QtWidgets.QLabel(self.frame_2)
        self.Rejected.setGeometry(QtCore.QRect(660, 60, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Rejected.setFont(font)
        self.Rejected.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Rejected.setFrameShape(QtWidgets.QFrame.Box)
        self.Rejected.setAlignment(QtCore.Qt.AlignCenter)
        self.Rejected.setObjectName("Rejected")
        
        ## Pending Requests Summary Table ##
        self.tableWidget9 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget9.setGeometry(QtCore.QRect(1060, 100, 202, 92))
        self.tableWidget9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget9.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget9.setRowCount(3)
        self.tableWidget9.setColumnCount(2)
        self.tableWidget9.setObjectName("tableWidget9")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget9.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget9.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget9.setItem(2, 0, item)
        self.tableWidget9.horizontalHeader().setVisible(False)
        self.tableWidget9.horizontalHeader().setHighlightSections(False)
        self.tableWidget9.verticalHeader().setVisible(False)
        self.Progress = QtWidgets.QLabel(self.frame_2)
        self.Progress.setGeometry(QtCore.QRect(1060, 60, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Progress.setFont(font)
        self.Progress.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Progress.setFrameShape(QtWidgets.QFrame.Box)
        self.Progress.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress.setObjectName("Progress")
        self.summary = QtWidgets.QLabel(self.frame_2)
        self.summary.setGeometry(QtCore.QRect(0, 0, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.summary.setFont(font)
        self.summary.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.summary.setFrameShape(QtWidgets.QFrame.Box)
        self.summary.setAlignment(QtCore.Qt.AlignCenter)
        self.summary.setObjectName("summary")
        
        ## Dashboard - 1: Based on Contract Type and WO Expiry Date ##
        ## There are 6 Tables in this Dashboard ## 
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(15, 30, 1820, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        ## Contract Type = FP & WO Expiry Date < 30 days
        self.tableWidget1 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget1.setGeometry(QtCore.QRect(30, 100, 240, 182))
        self.tableWidget1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget1.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget1.setRowCount(6)
        self.tableWidget1.setColumnCount(2)
        self.tableWidget1.setObjectName("tableWidget1")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(4, 0, item)
        self.tableWidget1.horizontalHeader().setVisible(False)
        self.tableWidget1.horizontalHeader().setHighlightSections(False)
        self.tableWidget1.verticalHeader().setVisible(False)
        self.FP1 = QtWidgets.QLabel(self.frame_3)
        self.FP1.setGeometry(QtCore.QRect(30, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FP1.setFont(font)
        self.FP1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.FP1.setFrameShape(QtWidgets.QFrame.Box)
        self.FP1.setAlignment(QtCore.Qt.AlignCenter)
        self.FP1.setObjectName("FP1")
        self.view1 = QtWidgets.QPushButton(self.frame_3)
        self.view1.setGeometry(QtCore.QRect(30, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view1.setFont(font)
        self.view1.setObjectName("view1")
        
        ## Contract Type = T&M & WO Expiry Date < 30 days
        self.tableWidget2 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget2.setGeometry(QtCore.QRect(330, 100, 240, 182))
        self.tableWidget2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget2.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget2.setRowCount(6)
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.setObjectName("tableWidget2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget2.setItem(4, 0, item)
        self.tableWidget2.horizontalHeader().setVisible(False)
        self.tableWidget2.horizontalHeader().setHighlightSections(False)
        self.tableWidget2.verticalHeader().setVisible(False)
        self.view2 = QtWidgets.QPushButton(self.frame_3)
        self.view2.setGeometry(QtCore.QRect(330, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view2.setFont(font)
        self.view2.setObjectName("view2")
        self.TM1 = QtWidgets.QLabel(self.frame_3)
        self.TM1.setGeometry(QtCore.QRect(330, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TM1.setFont(font)
        self.TM1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.TM1.setFrameShape(QtWidgets.QFrame.Box)
        self.TM1.setAlignment(QtCore.Qt.AlignCenter)
        self.TM1.setObjectName("TM1")
        
        ## Contract Type = FP and T&M & WO Expiry Date < 30 days
        self.tableWidget3 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget3.setGeometry(QtCore.QRect(640, 100, 240, 182))
        self.tableWidget3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget3.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget3.setRowCount(6)
        self.tableWidget3.setColumnCount(2)
        self.tableWidget3.setObjectName("tableWidget3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget3.setItem(4, 0, item)
        self.tableWidget3.horizontalHeader().setVisible(False)
        self.tableWidget3.horizontalHeader().setHighlightSections(False)
        self.tableWidget3.verticalHeader().setVisible(False)
        self.view3 = QtWidgets.QPushButton(self.frame_3)
        self.view3.setGeometry(QtCore.QRect(640, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view3.setFont(font)
        self.view3.setObjectName("view3")
        self.Total1 = QtWidgets.QLabel(self.frame_3)
        self.Total1.setGeometry(QtCore.QRect(640, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Total1.setFont(font)
        self.Total1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Total1.setFrameShape(QtWidgets.QFrame.Box)
        self.Total1.setAlignment(QtCore.Qt.AlignCenter)
        self.Total1.setObjectName("Total1")

        ## Contract Type = FP & 60 days > WO Expiry Date > 30 days
        self.tableWidget4 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget4.setGeometry(QtCore.QRect(960, 100, 240, 182))
        self.tableWidget4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget4.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget4.setRowCount(6)
        self.tableWidget4.setColumnCount(2)
        self.tableWidget4.setObjectName("tableWidget4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget4.setItem(4, 0, item)
        self.tableWidget4.horizontalHeader().setVisible(False)
        self.tableWidget4.horizontalHeader().setHighlightSections(False)
        self.tableWidget4.verticalHeader().setVisible(False)
        self.view4 = QtWidgets.QPushButton(self.frame_3)
        self.view4.setGeometry(QtCore.QRect(960, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view4.setFont(font)
        self.view4.setObjectName("view4")
        self.FP2 = QtWidgets.QLabel(self.frame_3)
        self.FP2.setGeometry(QtCore.QRect(960, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FP2.setFont(font)
        self.FP2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.FP2.setFrameShape(QtWidgets.QFrame.Box)
        self.FP2.setAlignment(QtCore.Qt.AlignCenter)
        self.FP2.setObjectName("FP2")
        
        ## Contract Type = T&M &  30 days < WO Expiry Date < 60 days
        self.tableWidget5 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget5.setGeometry(QtCore.QRect(1250, 100, 240, 182))
        self.tableWidget5.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget5.setRowCount(6)
        self.tableWidget5.setColumnCount(2)
        self.tableWidget5.setObjectName("tableWidget5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget5.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget5.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget5.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget5.setItem(4, 0, item)
        self.tableWidget5.horizontalHeader().setVisible(False)
        self.tableWidget5.horizontalHeader().setHighlightSections(False)
        self.tableWidget5.verticalHeader().setVisible(False)
        self.TM2 = QtWidgets.QLabel(self.frame_3)
        self.TM2.setGeometry(QtCore.QRect(1250, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TM2.setFont(font)
        self.TM2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.TM2.setFrameShape(QtWidgets.QFrame.Box)
        self.TM2.setAlignment(QtCore.Qt.AlignCenter)
        self.TM2.setObjectName("TM2")
        self.view5 = QtWidgets.QPushButton(self.frame_3)
        self.view5.setGeometry(QtCore.QRect(1250, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view5.setFont(font)
        self.view5.setObjectName("view5")

        ## Contract Type = FP and T&M and 30 days < WO Expiry Date < 60 days
        self.tableWidget6 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget6.setGeometry(QtCore.QRect(1540, 100, 240, 182))
        self.tableWidget6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget6.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget6.setRowCount(6)
        self.tableWidget6.setColumnCount(2)
        self.tableWidget6.setObjectName("tableWidget6")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget6.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget6.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget6.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget6.setItem(4, 0, item)
        self.tableWidget6.horizontalHeader().setVisible(False)
        self.tableWidget6.horizontalHeader().setHighlightSections(False)
        self.tableWidget6.verticalHeader().setVisible(False)
        ## Adding Requests Sent Back Row to all the tables
        self.tableWidget1.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        self.tableWidget2.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        self.tableWidget3.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        self.tableWidget4.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        self.tableWidget5.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        self.tableWidget6.setItem(5, 0, QtWidgets.QTableWidgetItem("Requests Sent Back"))
        
        ## Setting Column width
        self.tableWidget1.setColumnWidth(0, 178)
        self.tableWidget1.setColumnWidth(1, 50)
        self.tableWidget2.setColumnWidth(0, 178)
        self.tableWidget2.setColumnWidth(1, 50)
        self.tableWidget3.setColumnWidth(0, 178)
        self.tableWidget3.setColumnWidth(1, 50)
        self.tableWidget4.setColumnWidth(0, 178)
        self.tableWidget4.setColumnWidth(1, 50)
        self.tableWidget5.setColumnWidth(0, 178)
        self.tableWidget5.setColumnWidth(1, 50)
        self.tableWidget6.setColumnWidth(0, 178)
        self.tableWidget6.setColumnWidth(1, 50)
        self.Total2 = QtWidgets.QLabel(self.frame_3)
        self.Total2.setGeometry(QtCore.QRect(1540, 60, 240, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Total2.setFont(font)
        self.Total2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Total2.setFrameShape(QtWidgets.QFrame.Box)
        self.Total2.setAlignment(QtCore.Qt.AlignCenter)
        self.Total2.setObjectName("Total2")
        self.view6 = QtWidgets.QPushButton(self.frame_3)
        self.view6.setGeometry(QtCore.QRect(1540, 282, 240, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.view6.setFont(font)
        self.view6.setObjectName("view6")
        self.summary_2 = QtWidgets.QLabel(self.frame_3)
        self.summary_2.setGeometry(QtCore.QRect(0, 0, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.summary_2.setFont(font)
        self.summary_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.summary_2.setFrameShape(QtWidgets.QFrame.Box)
        self.summary_2.setAlignment(QtCore.Qt.AlignCenter)
        self.summary_2.setObjectName("summary_2")

        ## Customer Analysis Dashboard ## 
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(170, 710, 1491, 261))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Customer Analysis")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 50, 1350, 155))
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setAlternatingRowColors(True)
        for i in range(5):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(i,item)

        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setColumnWidth(0, 300)
        self.tableWidget_2.setColumnWidth(1, 300)
        self.tableWidget_2.setColumnWidth(2, 250)
        self.tableWidget_2.setColumnWidth(3, 250)
        self.tableWidget_2.setColumnWidth(4, 248)
        self.tableWidget_2.setStyleSheet("QHeaderView::section { color: rgb(0, 0,0);}") ## Change the Header style. Requires knowlegdge of CSS
        self.tableWidget_2.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.headings = ["Customer Name","Contract Type","Subcon #", "Margin","Tenure"]
        j = 0
        for content in self.headings:
            self.tableWidget_2.horizontalHeaderItem(j).setText(content)
            j+=1
        self.loaddata_2()
        self.tableWidget1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.addWidget(self.page1)

        ## Page - Subcon Details #######
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Heading = QtWidgets.QLabel(self.page)
        self.Heading.setGeometry(QtCore.QRect(500,100, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setAlignment(QtCore.Qt.AlignCenter)
        self.Heading.setObjectName("Heading")
        self.Heading.setText("Subcontractor Details")

        ## Cancel Button ##
        self.goback = QtWidgets.QPushButton(self.page)
        self.goback.setGeometry(QtCore.QRect(820,870, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        self.goback.setText("Go Back")
        self.goback.clicked.connect(self.GoBack)
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(50, 300, 1750, 500))
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("QHeaderView::section{background-color: rgb(255, 191, 0); color: rgb(0, 0,0);} QTableWidget {gridline-color: rgb(0, 0, 0);}")
        self.table.setAlternatingRowColors(True)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(32)
        self.table.setObjectName("table")
        for i in range(32):
            item = QtWidgets.QTableWidgetItem()
            self.table.setHorizontalHeaderItem(i, item) 
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 0, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.columnwidth = 150
        self.Headers = ["Unit","Sub Unit","Subcon ID","Subcon Name","Date of Joining","Expected End Date","Customer Name","Customer Group Name","Project ID","Project Desc","Contract Type","Project Contribution Margin","Vendor Name","W2 Vendor","Subcon Role","Subcon Band","Subcon Experience","Country","City","Skill Family","Skill Type","Skill (Primary)","Skill (Secondary)","Location","Vendor Rate (per hour USD)","Customer Rate","Margin","Margin RAG","Tenure RAG","Project ID RAG","Subcon RAG","Cummulative RAG"]
        i = 0
        for names in self.Headers:
            self.table.horizontalHeaderItem(i).setText(names)
            i = i + 1
            
        for i in range(32):
            self.table.setColumnWidth(i,self.columnwidth)
               
        #self.loaddata()
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## Page 3: Action Screen ## 
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        ## Main Frame ##  
        self.frame_5 = QtWidgets.QFrame(self.page_2)
        self.frame_5.setGeometry(QtCore.QRect(50, 40, 1770, 970))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        
        ## Grid containing the Header Subcon Profile ## 
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 200, 50))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName("gridLayout")
        self.Subconprofile = QtWidgets.QLabel()
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.Subconprofile.setFont(self.font)
        self.Subconprofile.setText("Subcon Profile")
        self.Subconprofile.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Subconprofile.setFrameShape(QtWidgets.QFrame.Box)
        self.Subconprofile.setFixedHeight(35)
        self.Subconprofile.setAlignment(QtCore.Qt.AlignCenter)
        self.Subconprofile.setObjectName("Subconprofile")
        self.gridLayout_7.addWidget(self.Subconprofile,0,0,1,2)
        
        ## Grid containing all the Labels and Line Edits for showing Subcon Profile ##
        ## To remove any info:- 
        ## 1) Remove all the occurences of that info
        ## 2) Change the locations of others to fill its space.
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 1171, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.line_edits_1 = {}
        line_edits_1 = {
            "Subcon Name": (1,1),"Date of Joining": (2,1),"Customer Name": (1,3), "WO End Date": (2,3),"Tenure": (2,5),	
            "Vendor Name": (1,5), "Subcon Role": (3,1),"Subcon Band": (3,3),"Subcon Experience": (3,5),"Country": (4,1),	
            "City": (4,3),"Skill Family": (4,5),"Skill Type": (5,1),"Skill (Primary)": (5,3),"Skill (Secondary)": (5,5),
        }

        self.lables_1 = {}
        lables_1 = {
            "Subcon Name": (1,0),"Date of Joining": (2,0),"Customer Name": (1,2), "Tenure": (2,4),"WO End Date": (2,2),	
            "Vendor Name": (1,4), "Subcon Role": (3,0),"Subcon Band": (3,2),"Subcon Experience": (3,4),"Country": (4,0),	
            "City": (4,2),"Skill Family": (4,4),"Skill Type": (5,0),"Skill (Primary)": (5,2),"Skill (Secondary)": (5,4),
        }

        for lables_Text, pos in lables_1.items():
            self.lables_1[lables_Text] = QtWidgets.QLabel()
            self.lables_1[lables_Text].setText(lables_Text)
            self.lables_1[lables_Text].setFont(self.font)
            #self.lables[lables_Text].setStyleSheet("background-color: rgb(255, 191, 0);")
            self.lables_1[lables_Text].setWordWrap(True)
            self.gridLayout.addWidget(self.lables_1[lables_Text], pos[0], pos[1])
                
        for line_Text, pos in line_edits_1.items():
            self.line_edits_1[line_Text] = QtWidgets.QLineEdit()
            self.line_edits_1[line_Text].setReadOnly(True)
            self.gridLayout.addWidget(self.line_edits_1[line_Text], pos[0], pos[1])

        ## Grid to show Subcon Commercial Info ##
        ## Logic is similar to as explained above ##
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 370, 1171, 120))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Subconcommercial = QtWidgets.QLabel()
        self.Subconcommercial.setFont(self.font)
        self.Subconcommercial.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Subconcommercial.setFrameShape(QtWidgets.QFrame.Box)
        self.Subconcommercial.setFixedHeight(35)
        self.Subconcommercial.setObjectName("Subconcommercial")
        self.Subconcommercial.setAlignment(QtCore.Qt.AlignCenter)
        self.Subconcommercial.setText("Subcon Commercial")
        self.gridLayout_2.addWidget(self.Subconcommercial,0,0)

        self.line_edits_2 = {}
        line_edits_2 = {
            "Vendor Rate (per hour USD)": (1,1),	"Customer Rate Margin": (1,3),"Margin": (1,5),
        }
        self.lables_2 = {}
        lables_2 = {
            "Vendor Rate (per hour USD)": (1,0),	"Customer Rate Margin": (1,2),"Margin": (1,4),
        }

        for lables_Text, pos in lables_2.items():
            self.lables_2[lables_Text] = QtWidgets.QLabel()
            self.lables_2[lables_Text].setText(lables_Text)
            self.lables_2[lables_Text].setFont(self.font)
            #self.lables[lables_Text].setStyleSheet("background-color: rgb(255, 191, 0);")
            self.lables_2[lables_Text].setWordWrap(True)
            self.gridLayout_2.addWidget(self.lables_2[lables_Text], pos[0], pos[1])
                
        for line_Text, pos in line_edits_2.items():
            self.line_edits_2[line_Text] = QtWidgets.QLineEdit()
            self.line_edits_2[line_Text].setReadOnly(True)
            self.gridLayout_2.addWidget(self.line_edits_2[line_Text], pos[0], pos[1])
        self.gridLayout_2.setHorizontalSpacing(20)

        ### Grid to show Subcon Health Info ## 
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 510, 1171, 120))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Subconhealth = QtWidgets.QLabel()
        self.Subconhealth.setFont(self.font)
        self.Subconhealth.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Subconhealth.setFrameShape(QtWidgets.QFrame.Box)
        self.Subconhealth.setFixedHeight(35)
        self.Subconhealth.setFixedWidth(200)
        self.Subconhealth.setObjectName("Subconhealth")
        self.Subconhealth.setAlignment(QtCore.Qt.AlignCenter)
        self.Subconhealth.setText("Subcon Health")
        self.gridLayout_3.addWidget(self.Subconhealth,0,0,1,2)
        self.line_edits_3 = {}
        line_edits_3 = {
            "Margin RAG": (1,1),"Tenure RAG": (1,3),"Project ID RAG": (1,5),"Subcon RAG": (1,7),
        }
        self.lables_3 = {}
        lables_3 = {
            "Margin RAG": (1,0),"Tenure RAG": (1,2),"Project ID RAG": (1,4),"Subcon RAG": (1,6),
        }

        for lables_Text, pos in lables_3.items():
            self.lables_3[lables_Text] = QtWidgets.QLabel()
            self.lables_3[lables_Text].setText(lables_Text)
            self.lables_3[lables_Text].setFont(self.font)
            #self.lables[lables_Text].setStyleSheet("background-color: rgb(255, 191, 0);")
            self.lables_3[lables_Text].setWordWrap(True)
            self.gridLayout_3.addWidget(self.lables_3[lables_Text], pos[0], pos[1])
                
        for line_Text, pos in line_edits_3.items():
            self.line_edits_3[line_Text] = QtWidgets.QLineEdit()
            self.line_edits_3[line_Text].setReadOnly(True)
            self.gridLayout_3.addWidget(self.line_edits_3[line_Text], pos[0], pos[1])
        self.gridLayout_3.setHorizontalSpacing(15)

        ## Grid to give 4 options to the PM, Extend, Early Separation, CTP, and Release as per WO End Date
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 630, 900, 70))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.extend = QtWidgets.QPushButton()
        self.extend.setText("Extend")
        self.extend.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.extend.setFont(self.font)
        self.gridLayout_4.addWidget(self.extend,0,0)
        self.release = QtWidgets.QPushButton()
        self.release.setText("Early Separation")
        self.release.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.release.setFont(self.font)
        self.gridLayout_4.addWidget(self.release,0,1)
        self.ctp = QtWidgets.QPushButton()
        self.ctp.setText("CTP")
        self.ctp.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.ctp.setFont(self.font)
        self.gridLayout_4.addWidget(self.ctp,0,2)
        self.extend.setFixedHeight(40)
        self.release.setFixedHeight(40)
        self.ctp.setFixedHeight(40)
        self.extend.clicked.connect(self.doextension)
        self.release.clicked.connect(self.dorelease)
        self.ctp.clicked.connect(self.doctp)
        self.extension = 0  ## To capture the number of times the Extend button is clicked
        self.released = 0 ## To capture the number of times the Early Separation button is clicked
        self.ctped = 0 ## To capture the number of times the CTP button is clicked
        self.ReleaseWO = QtWidgets.QPushButton()   ## Release as per WO End Date button 
        self.ReleaseWO.setText("Release on WO End Date")
        self.ReleaseWO.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.ReleaseWO.setFont(self.font)
        self.ReleaseWO.clicked.connect(self.releaseonwo)
        self.ReleaseWO.setFixedHeight(40)
        self.gridLayout_4.addWidget(self.ReleaseWO,0,3)

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 700, 1171, 150))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")

         ## Grid to give 2 options to the PM, Project Details and Other Details
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(1191, 20, 570, 50))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.projectdetails = QtWidgets.QPushButton()
        self.projectdetails.setFont(self.font)
        self.projectdetails.setText("Project Details")
        self.projectdetails.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.projectdetails.setFixedHeight(35)
        self.projectdetails.setObjectName("Project Details")
        self.gridLayout_8.addWidget(self.projectdetails, 0, 0)
        self.otherdetails = QtWidgets.QPushButton()
        self.otherdetails.setFont(self.font)
        self.otherdetails.setText("Other Details")
        self.otherdetails.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.otherdetails.setFixedHeight(35)
        self.otherdetails.setObjectName("Other Details")
        self.gridLayout_8.addWidget(self.otherdetails, 0, 1)
        self.projectdetails.clicked.connect(self.showproject)
        self.counter = 0  ## No. of times Project Details button has been clicked
        self.otherdetails.clicked.connect(self.showother)
        self.counter_1 = 0  ## No. of times Other Details button has been clicked

        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")

        ## Grid to show remarks history button ##
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(1300, 370, 371, 51))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.history = QtWidgets.QPushButton(self.gridLayoutWidget_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.history.setFont(font)
        self.history.setObjectName("history")
        self.history.setText("Show Remarks History")
        self.history.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.history.setFixedHeight(40)
        self.history.setFixedWidth(300)
        self.history.clicked.connect(self.showhistory)
        self.gridLayout_9.addWidget(self.history, 0, 0, 1, 1)

        ## Previous Comments section ## 
        self.tabWidget = QtWidgets.QTabWidget(self.frame_5)
        self.tabWidget.setGeometry(QtCore.QRect(1200, 450, 541, 450))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")

        ## Adding 4 Tabs to the Previous Comments section ##
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_3")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        ## Assigning Titles to tabs ##
        self.tabWidget.addTab(self.tab, "Project Manager")
        self.tabWidget.addTab(self.tab_2, "Program Manager")
        self.tabWidget.addTab(self.tab_3, "SBU Head")
        self.tabWidget.addTab(self.tab_4, "EHC Approver")
        
        ## Show the last two transactions for the same Subcon ## 
        ## Transaction1 == Latest Transaction, Transaction2 == Second Last Transaction 
        ## variables with _1 are associated with PGM, _2 are with SBU Head, _3 are with EHC Approver
        ## We have 4 data points for each Transaction, Date, Decision, Remarks, Recommended Tenure
        self.transaction1 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.transaction1.setFont(font)
        self.transaction1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transaction1.setObjectName("transaction1")
        self.transaction1_date_PM = QtWidgets.QLabel(self.tab)
        self.transaction1_date_PM.setGeometry(QtCore.QRect(152, 35, 211, 31))
        self.transaction1_date_PM.setObjectName("transaction1_date_PM ")
        
        
        self.transaction1_1 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1_1.setGeometry(QtCore.QRect(20, 100, 151, 30))
        self.transaction1_1.setWordWrap(True)
        self.transaction1_1.setObjectName("transaction1_1")
        self.transaction1_2 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1_2.setGeometry(QtCore.QRect(20, 150, 151, 30))
        self.transaction1_2.setWordWrap(True)
        self.transaction1_2.setObjectName("transaction1_2")
        self.transaction1_3 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1_3.setGeometry(QtCore.QRect(20, 190, 151, 30))
        self.transaction1_3.setWordWrap(True)
        self.transaction1_3.setObjectName("transaction1_3")
        
        
        self.transaction1_decision_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction1_decision_PM.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_PM.setReadOnly(True)
        self.transaction1_decision_PM.setObjectName("transaction1_decision_PM")
        self.transaction1_remarks_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction1_remarks_PM.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_PM.setReadOnly(True)
        self.transaction1_remarks_PM.setObjectName("transaction1_remarks_PM")
        self.transaction1_recomendtenure_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction1_recomendtenure_PM.setGeometry(QtCore.QRect(180, 160, 321, 30))
        self.transaction1_recomendtenure_PM.setReadOnly(True)
        self.transaction1_recomendtenure_PM.setObjectName("transaction1_recomendtenure_PM")
        
        self.transaction1_decision_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction1_decision_PGM.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_PGM.setReadOnly(True)
        self.transaction1_decision_PGM.setObjectName("transaction1_decision_PGM")
        self.transaction1_remarks_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction1_remarks_PGM.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_PGM.setReadOnly(True)
        self.transaction1_remarks_PGM.setObjectName("transaction1_remarks_PGM")
        self.transaction1_recomendtenure_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction1_recomendtenure_PGM.setGeometry(QtCore.QRect(180, 160, 321, 30))
        self.transaction1_recomendtenure_PGM.setReadOnly(True)
        self.transaction1_recomendtenure_PGM.setObjectName("transaction1_recomendtenure_PGM")
        
        self.transaction1_decision_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction1_decision_SBU.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_SBU.setReadOnly(True)
        self.transaction1_decision_SBU.setObjectName("transaction1_decision_SBU")
        self.transaction1_remarks_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction1_remarks_SBU.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_SBU.setReadOnly(True)
        self.transaction1_remarks_SBU.setObjectName("transaction1_remarks_SBU")
        self.transaction1_recomendtenure_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction1_recomendtenure_SBU.setGeometry(QtCore.QRect(180, 160, 321, 30))
        self.transaction1_recomendtenure_SBU.setReadOnly(True)
        self.transaction1_recomendtenure_SBU.setObjectName("transaction1_recomendtenure_SBU")
        
        self.transaction1_decision_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction1_decision_EHC.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_EHC.setReadOnly(True)
        self.transaction1_decision_EHC.setObjectName("transaction1_decision_EHC")
        self.transaction1_remarks_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction1_remarks_EHC.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_EHC.setReadOnly(True)
        self.transaction1_remarks_EHC.setObjectName("transaction1_remarks_EHC")
        self.transaction1_recomendtenure_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction1_recomendtenure_EHC.setGeometry(QtCore.QRect(180, 160, 321, 30))
        self.transaction1_recomendtenure_EHC.setReadOnly(True)
        self.transaction1_recomendtenure_EHC.setObjectName("transaction1_recomendtenure_EHC")
        
        self.transaction2 = QtWidgets.QLabel(self.tabWidget)
        self.transaction2.setGeometry(QtCore.QRect(20, 245, 181, 31))
        self.transaction2.setFont(font)
        self.transaction2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transaction2.setWordWrap(True)
        self.transaction2.setObjectName("transaction2")

        self.transaction2_1 = QtWidgets.QLabel(self.tabWidget)
        self.transaction2_1.setGeometry(QtCore.QRect(20, 290, 151, 30))
        self.transaction2_1.setWordWrap(True)
        self.transaction2_1.setObjectName("transaction2_1")
        self.transaction2_2 = QtWidgets.QLabel(self.tabWidget)
        self.transaction2_2.setGeometry(QtCore.QRect(20, 340, 151, 30))
        self.transaction2_2.setWordWrap(True)
        self.transaction2_2.setObjectName("transaction2_2")
        self.transaction2_3 = QtWidgets.QLabel(self.tabWidget)
        self.transaction2_3.setGeometry(QtCore.QRect(20, 380, 151, 30))
        self.transaction2_3.setWordWrap(True)
        self.transaction2_3.setObjectName("transaction2_3")

        self.transaction2_decision_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction2_decision_PM.setGeometry(QtCore.QRect(180, 270, 321, 30))
        self.transaction2_decision_PM.setReadOnly(True)
        self.transaction2_decision_PM.setObjectName("transaction2_decision_PM")
        self.transaction2_remarks_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction2_remarks_PM.setGeometry(QtCore.QRect(180, 310, 321, 30))
        self.transaction2_remarks_PM.setReadOnly(True)
        self.transaction2_remarks_PM.setObjectName("transaction2_remarks_PM")
        self.transaction2_recomendtenure_PM = QtWidgets.QTextEdit(self.tab)
        self.transaction2_recomendtenure_PM.setGeometry(QtCore.QRect(180, 350, 321, 30))
        self.transaction2_recomendtenure_PM.setReadOnly(True)
        self.transaction2_recomendtenure_PM.setObjectName("transaction2_recomendtenure_PM")

        self.transaction2_decision_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction2_decision_PGM.setGeometry(QtCore.QRect(180, 270, 321, 30))
        self.transaction2_decision_PGM.setReadOnly(True)
        self.transaction2_decision_PGM.setObjectName("transaction1_decision_PGM")
        self.transaction2_remarks_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction2_remarks_PGM.setGeometry(QtCore.QRect(180, 310, 321, 30))
        self.transaction2_remarks_PGM.setReadOnly(True)
        self.transaction2_remarks_PGM.setObjectName("transaction1_remarks_PGM")
        self.transaction2_recomendtenure_PGM = QtWidgets.QTextEdit(self.tab_2)
        self.transaction2_recomendtenure_PGM.setGeometry(QtCore.QRect(180, 350, 321, 30))
        self.transaction2_recomendtenure_PGM.setReadOnly(True)
        self.transaction2_recomendtenure_PGM.setObjectName("transaction1_recomendtenure_PGM")
        
        self.transaction2_decision_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction2_decision_SBU.setGeometry(QtCore.QRect(180, 270, 321, 30))
        self.transaction2_decision_SBU.setReadOnly(True)
        self.transaction2_decision_SBU.setObjectName("transaction1_decision_SBU")
        self.transaction2_remarks_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction2_remarks_SBU.setGeometry(QtCore.QRect(180, 310, 321, 30))
        self.transaction2_remarks_SBU.setReadOnly(True)
        self.transaction2_remarks_SBU.setObjectName("transaction1_remarks_SBU")
        self.transaction2_recomendtenure_SBU = QtWidgets.QTextEdit(self.tab_3)
        self.transaction2_recomendtenure_SBU.setGeometry(QtCore.QRect(180, 350, 321, 30))
        self.transaction2_recomendtenure_SBU.setReadOnly(True)
        self.transaction2_recomendtenure_SBU.setObjectName("transaction1_recomendtenure_SBU")
        self.transaction2_decision_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction2_decision_EHC.setGeometry(QtCore.QRect(180, 270, 321, 30))
        self.transaction2_decision_EHC.setReadOnly(True)
        self.transaction2_decision_EHC.setObjectName("transaction1_decision_EHC")
        
        self.transaction2_remarks_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction2_remarks_EHC.setGeometry(QtCore.QRect(180, 310, 321, 30))
        self.transaction2_remarks_EHC.setReadOnly(True)
        self.transaction2_remarks_EHC.setObjectName("transaction1_remarks_EHC")
        self.transaction2_recomendtenure_EHC = QtWidgets.QTextEdit(self.tab_4)
        self.transaction2_recomendtenure_EHC.setGeometry(QtCore.QRect(180, 350, 321, 30))
        self.transaction2_recomendtenure_EHC.setReadOnly(True)
        self.transaction2_recomendtenure_EHC.setObjectName("transaction1_recomendtenure_EHC")

        self.transaction1_date_PGM = QtWidgets.QLabel(self.tab_2)
        self.transaction1_date_PGM.setGeometry(QtCore.QRect(152, 30, 211, 31))
        self.transaction1_date_PGM.setObjectName("transaction1_date_PGM")
        self.transaction1_date_SBU = QtWidgets.QLabel(self.tab_3)
        self.transaction1_date_SBU.setGeometry(QtCore.QRect(152, 30, 211, 31))
        self.transaction1_date_SBU.setObjectName("transaction1_date_SBU")
        self.transaction1_date_EHC = QtWidgets.QLabel(self.tab_4)
        self.transaction1_date_EHC.setGeometry(QtCore.QRect(152, 30, 211, 31))
        self.transaction1_date_EHC.setObjectName("transaction1_date_EHC")

        self.transaction2_date_PM = QtWidgets.QLabel(self.tab)
        self.transaction2_date_PM.setGeometry(QtCore.QRect(210, 215, 211, 31))
        self.transaction2_date_PM.setObjectName("transaction2_date_PM")
        self.transaction2_date_PGM = QtWidgets.QLabel(self.tab_2)
        self.transaction2_date_PGM.setGeometry(QtCore.QRect(210, 215, 211, 31))
        self.transaction2_date_PGM.setObjectName("transaction2_date_PGM")
        self.transaction2_date_SBU = QtWidgets.QLabel(self.tab_3)
        self.transaction2_date_SBU.setGeometry(QtCore.QRect(210, 215, 211, 31))
        self.transaction2_date_SBU.setObjectName("transaction2_date_SBU")
        self.transaction2_date_EHC = QtWidgets.QLabel(self.tab_3)
        self.transaction2_date_EHC.setGeometry(QtCore.QRect(210, 215, 211, 31))
        self.transaction2_date_EHC.setObjectName("transaction2_date_EHC")        
        
        self.transaction1_1.setFont(font)
        self.transaction1_2.setFont(font)
        self.transaction1_3.setFont(font)
        self.transaction2_1.setFont(font)
        self.transaction2_2.setFont(font)
        self.transaction2_3.setFont(font)
        self.transaction1.setText("Last Transaction:")
        self.transaction1_1.setText("Decision")
        self.transaction1_2.setText("Remarks")
        self.transaction1_3.setText("Recommended Tenure")
        self.transaction2.setText("Second Last Transaction:")
        self.transaction2_1.setText("Decision")
        self.transaction2_2.setText("Remarks")
        self.transaction2_3.setText("Recommended Tenure")
        self.tabWidget.setCurrentIndex(0)

        self.submit = QtWidgets.QPushButton(self.frame_5)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.submit.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.submit.setFixedHeight(40)
        self.submit.setFixedWidth(200)
        self.submit.setGeometry(QtCore.QRect(20, 895, 150, 40))
        self.goback_2 = QtWidgets.QPushButton(self.frame_5)
        self.goback_2.setObjectName("goback_2")
        self.goback_2.setText("Go Back")
        self.goback_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.goback_2.setFixedHeight(40)
        self.goback_2.setFixedWidth(200)
        self.goback_2.setGeometry(QtCore.QRect(250, 895, 150, 40))
        self.goback_2.clicked.connect(self.GoBack_2)
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        ## Menubar ##
        self.menubar = QtWidgets.QMenuBar(self.centralwidget)
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(0,0,0); color: #e0e0e0; font-size: 20px;} QMenuBar::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 20px;} QMenu{background-color: rgb(0,0,0); color: rgb(255,255,255); font-size: 18px; font-weight: 150} QMenu::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 18px;}")  ## Properties of Menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 32))
        self.homescreen = QtWidgets.QAction("Home", self.menubar)  ## Home Button on Menubar
        self.font_1 = QtGui.QFont()
        self.font_1.setBold(True)
        self.font_1.setWeight(30)
        self.menubar.addAction(self.homescreen)
        self.modules_menu = self.menubar.addMenu("Modules")  ## Modules menu
        self.modules_menu.setFont(self.font_1)
        self.accessdashboard = QtWidgets.QAction("Dashboard", self.menubar)  ## Dashboard Menu
        self.menubar.addAction(self.accessdashboard)
        ## Sub-menus under Modules Menu ## 
        self.hiring = QtWidgets.QAction("Subcon Hiring Request", self.menubar) 
        self.renewal = QtWidgets.QAction("Subcon Renewal", self.menubar)
        self.allocation = QtWidgets.QAction("Subcon Allocation Update", self.menubar)
        self.performance  = QtWidgets.QAction("Subcon Performance Evaluation", self.menubar)
        self.portfolio = QtWidgets.QAction("Subcon Portfolio", self.menubar)
        self.timesheet = QtWidgets.QAction("Timesheet and Expenses", self.menubar)
        self.vendor = QtWidgets.QAction("Vendor Management", self.menubar)
        self.modules_menu.addAction(self.hiring)
        self.modules_menu.addAction(self.renewal)
        self.modules_menu.addAction(self.allocation)
        self.modules_menu.addAction(self.performance)
        self.modules_menu.addAction(self.portfolio)
        self.modules_menu.addAction(self.timesheet)
        self.modules_menu.addAction(self.vendor)

        self.stackedWidget.setCurrentIndex(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget1.cellClicked.connect(self.ShowFPLess)
        self.tableWidget2.cellClicked.connect(self.ShowTMLess)
        self.tableWidget3.cellClicked.connect(self.ShowTotalLess)
        self.tableWidget4.cellClicked.connect(self.ShowFPMore)
        self.tableWidget5.cellClicked.connect(self.ShowTMMore)
        self.tableWidget6.cellClicked.connect(self.ShowTotalMore)
        self.view1.clicked.connect(self.FPLess)
        self.view2.clicked.connect(self.TMLess)
        self.view3.clicked.connect(self.TotalLess)
        self.view4.clicked.connect(self.FPMore)
        self.view5.clicked.connect(self.TMMore)
        self.view6.clicked.connect(self.TotalMore)
        self.table.cellClicked.connect(self.TakeAction)
        self.submit.clicked.connect(self.Insert1)
        self.Sent_Back = 0

    def showhistory(self):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('select count(*) from Decisions where Subcon_ID = ? order by Transaction_Date Desc LIMIT 2', (self.ID,))
        transactions, = cur.fetchone()  ## Calculate the number of previous transactions
        
        if transactions == 0:  ## If zero, then put all values as none
            self.transaction2_decision_PM.setText("None")
            self.transaction2_remarks_PM.setText("None")
            self.transaction2_recomendtenure_PM.setText("None")
            self.transaction2_decision_PGM.setText("None")
            self.transaction2_remarks_PGM.setText("None")
            self.transaction2_recomendtenure_PGM.setText("None")
            self.transaction2_decision_SBU.setText("None")
            self.transaction2_remarks_SBU.setText("None")
            self.transaction2_recomendtenure_SBU.setText("None")
            self.transaction2_decision_EHC.setText("None")
            self.transaction2_remarks_EHC.setText("None")
            self.transaction2_recomendtenure_EHC.setText("None")
            self.transaction1_decision_PM.setText("None")
            self.transaction1_remarks_PM.setText("None")
            self.transaction1_recomendtenure_PM.setText("None")
            self.transaction1_decision_PGM.setText("None")
            self.transaction1_remarks_PGM.setText("None")
            self.transaction1_recomendtenure_PGM.setText("None")
            self.transaction1_decision_SBU.setText("None")
            self.transaction1_remarks_SBU.setText("None")
            self.transaction1_recomendtenure_SBU.setText("None")
            self.transaction1_decision_EHC.setText("None")
            self.transaction1_remarks_EHC.setText("None")
            self.transaction1_recomendtenure_EHC.setText("None")
        
        elif transactions == 1:  ## If 1 transaction is present, then initialise the second transaction values as None
            self.transaction2_decision_PM.setText("None")
            self.transaction2_remarks_PM.setText("None")
            self.transaction2_recomendtenure_PM.setText("None")
            self.transaction2_decision_PGM.setText("None")
            self.transaction2_remarks_PGM.setText("None")
            self.transaction2_recomendtenure_PGM.setText("None")
            self.transaction2_decision_SBU.setText("None")
            self.transaction2_remarks_SBU.setText("None")
            self.transaction2_recomendtenure_SBU.setText("None")
            self.transaction2_decision_EHC.setText("None")
            self.transaction2_remarks_EHC.setText("None")
            self.transaction2_recomendtenure_EHC.setText("None")

        results = cur.execute('select * from Decisions where Subcon_ID = ? order by Transaction_Date Desc LIMIT 2', (self.ID,))  ## Query the last two transactions with details 
        i = 0
        ## The query has a max of 2 transactions, and the results are in descending order of Transaction Date.
        for row in results:
            if i == 0: ## If it is the latest Transaction, check for PM Decision and add values to Tab-1 accordingly
                if str(row[3]) == "Extend":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[4]))
                    self.transaction1_recomendtenure_PM.setText(str(row[5]))
                elif str(row[3]) == "Release":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText("None")
                    self.transaction1_recomendtenure_PM.setText("None")
                elif str(row[3]) == "Early":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[7]))
                    self.transaction1_recomendtenure_PM.setText(str(row[8]))
                else:
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[10]))
                    self.transaction1_recomendtenure_PM.setText(str(row[11]))
                ## Add values to other tabs for the latest transaction
                self.transaction1_decision_PGM.setText(str(row[13]))
                self.transaction1_remarks_PGM.setText(str(row[14]))
                self.transaction1_recomendtenure_PGM.setText(str(row[15]))
                self.transaction1_decision_SBU.setText(str(row[16]))
                self.transaction1_remarks_SBU.setText(str(row[17]))
                self.transaction1_recomendtenure_SBU.setText(str(row[18]))
                self.transaction1_decision_EHC.setText(str(row[19]))
                self.transaction1_remarks_EHC.setText(str(row[20]))
                self.transaction1_recomendtenure_EHC.setText(str(row[21]))
                self.transaction1_date_PM.setText(str(row[1]))
                self.transaction1_date_PGM.setText(str(row[24]))
                self.transaction1_date_SBU.setText(str(row[25]))
                self.transaction1_date_EHC.setText(str(row[26]))
            else:  ## If it is the second last transaction, check for PM Decision and add values to Tab-1 accordingly
                if str(row[3]) == "Extend":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[4]))
                    self.transaction1_recomendtenure_PM.setText(str(row[5]))
                elif str(row[3]) == "Release":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText("None")
                    self.transaction1_recomendtenure_PM.setText("None")
                elif str(row[3]) == "Early":
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[7]))
                    self.transaction1_recomendtenure_PM.setText(str(row[8]))
                else:
                    self.transaction1_decision_PM.setText(str(row[3]))
                    self.transaction1_remarks_PM.setText(str(row[10]))
                    self.transaction1_recomendtenure_PM.setText(str(row[11]))
                ## Add values to other tabs for the second latest transaction
                self.transaction2_decision_PGM.setText(str(row[13]))
                self.transaction2_remarks_PGM.setText(str(row[14]))
                self.transaction2_recomendtenure_PGM.setText(str(row[15]))
                self.transaction2_decision_SBU.setText(str(row[16]))
                self.transaction2_remarks_SBU.setText(str(row[17]))
                self.transaction2_recomendtenure_SBU.setText(str(row[18]))
                self.transaction2_decision_EHC.setText(str(row[19]))
                self.transaction2_remarks_EHC.setText(str(row[20]))
                self.transaction2_recomendtenure_EHC.setText(str(row[21]))
                self.transaction2_date_PM.setText(str(row[1]))   
                self.transaction2_date_PGM.setText(str(row[24]))
                self.transaction2_date_SBU.setText(str(row[25]))
                self.transaction2_date_EHC.setText(str(row[26])) 
            i = i+1
        connection.close()
        
    def releaseonwo(self):   ## If the User clicks on Release as per WO End Date, then assign Request to Subcon Admin and go to first page.
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('insert into Decisions (Subcon_ID, Decision_PM,Request_Status, Request_Pending_With, Transaction_Date) Values (?,"Release","Pending","Subcon Admin",datetime("now"))', (self.ID,))
        connection.commit()
        connection.close()
        self.loaddata_2()
        self.stackedWidget.setCurrentIndex(0)
    
    def GoBack_2(self):  ## Go to Page 2 without taking any action.
        self.transaction2_decision_PM.setText("None")
        self.transaction2_remarks_PM.setText("None")
        self.transaction2_recomendtenure_PM.setText("None")
        self.transaction2_decision_PGM.setText("None")
        self.transaction2_remarks_PGM.setText("None")
        self.transaction2_recomendtenure_PGM.setText("None")
        self.transaction2_decision_SBU.setText("None")
        self.transaction2_remarks_SBU.setText("None")
        self.transaction2_recomendtenure_SBU.setText("None")
        self.transaction2_decision_EHC.setText("None")
        self.transaction2_remarks_EHC.setText("None")
        self.transaction2_recomendtenure_EHC.setText("None")
        self.transaction1_decision_PM.setText("None")
        self.transaction1_remarks_PM.setText("None")
        self.transaction1_recomendtenure_PM.setText("None")
        self.transaction1_decision_PGM.setText("None")
        self.transaction1_remarks_PGM.setText("None")
        self.transaction1_recomendtenure_PGM.setText("None")
        self.transaction1_decision_SBU.setText("None")
        self.transaction1_remarks_SBU.setText("None")
        self.transaction1_recomendtenure_SBU.setText("None")
        self.transaction1_decision_EHC.setText("None")
        self.transaction1_remarks_EHC.setText("None")
        self.transaction1_recomendtenure_EHC.setText("None")
        self.stackedWidget.setCurrentIndex(1)

    def GoBack(self): # Go to Page 1 
        self.stackedWidget.setCurrentIndex(0)
    
    def FPLess(self):  ## Show all Transactions which have Contract Type = FP and Expiry Date Less than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where Contract_Type = "FP" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30 and Project_Manager = ?',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where Contract_Type = "FP" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Project_Manager = ? ',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def TMLess(self): ## Show all Transactions which have Contract Type = T&M and Expiry Date Less than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where Contract_Type = "T&M" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30 and Project_Manager = ? ',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where Contract_Type = "T&M" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Project_Manager = ?',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def TotalLess(self):  ## Show all Transactions which have Expiry Date Less than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30 and Project_Manager = ? ',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Project_Manager = ?',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    def FPMore(self): ## Show all Transactions which have Contract Type = FP and Expiry Date Greater than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where Contract_Type = "FP" and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where Contract_Type = "FP" and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def TMMore(self): ## Show all Transactions which have Contract Type = T&M and Expiry Date more than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where Contract_Type = "T&M" and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where Contract_Type = "T&M" and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def TotalMore(self): ## Show all Transactions which have Expiry Date more than 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT count(*) FROM Subcon_Info where ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        x, = cur.fetchone()
        self.rowcount = int(x)
        self.table.setRowCount(self.rowcount)
        results = cur.execute('SELECT * FROM Subcon_Info where ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Project_Manager = ?',(self.name_PM,))
        tablerow=0
        for row in results:
            for i in range(32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    def ShowFPLess(self, row1): ## Show Transactions which have Contract Type = FP and Expiry Date Less than 30 days and further conditions based on which row is clicked.
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        
        if row1 == 0:  # Show Requests for which Extension is initiated
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Extend",))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",))
        elif row1 == 2: # Show Requests for which Release is initiated
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Release",))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",))
        elif row1 == 3: # Show Requests for which Early Separation is initiated
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Early",))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",))
        elif row1 == 4: # Show Requests for which CTP is initiated
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("CTP",))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",))
        elif row1 == 1: # Show Requests for which Extension is not initiated i.e. no action taken yet
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?')
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?')
        else:  # Show Requests for which are sent back for query by the PGM
            cur.execute('select count(*) from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?')
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?')
            self.Sent_Back = 1  ## Sent_Back variable informs the system that the viewer is viewing Sent Back requests and take actions accordingly.
        tablerow=0
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    ## The logics for all the tables shall remain the same. The Queries will change acccording to the Contract Type and WO Expiry Date
    
    def ShowTMLess(self, row1):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Project_Manager = ?'
        tablerow=0
        if row1 == 0:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Extend",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",self.name_PM,))
        elif row1 == 2:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Release",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",self.name_PM,))
        elif row1 == 3:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Early",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",self.name_PM,))
        elif row1 == 4:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("CTP",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",self.name_PM,))
        elif row1 == 1:
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        else:
            cur.execute('select count(*) from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            self.Sent_Back = 1
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTotalLess(self, row1):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        tablerow=0
        if row1 == 0:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where  Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Extend",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",self.name_PM,))
        elif row1 == 2:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Release",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",self.name_PM,))
        elif row1 == 3:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("Early",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",self.name_PM,))
        elif row1 == 4:
            cur.execute('SELECT count(*) FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?',("CTP",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",self.name_PM,))
        elif row1 == 1:
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) >30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        else:
            cur.execute('select count(*) from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            self.Sent_Back = 1
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowFPMore(self, row1):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        sqlstr1 = 'SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        
        tablerow=0
        if row1 == 0:
            cur.execute(sqlstr1,("Extend",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",self.name_PM,))
        elif row1 == 2:
            cur.execute(sqlstr1,("Release",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",self.name_PM,))
        elif row1 == 3:
            cur.execute(sqlstr1,("Early",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",self.name_PM,))
        elif row1 == 4:
            cur.execute(sqlstr1,("CTP",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",self.name_PM,))
        elif row1 == 1:
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        else:
            cur.execute('select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            self.Sent_Back = 1
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTMMore(self, row1):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        sqlstr1 = 'SELECT count(*) FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        tablerow=0
        if row1 == 0:
            cur.execute(sqlstr1,("Extend",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",self.name_PM,))
        elif row1 == 2:
            cur.execute(sqlstr1,("Release",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",self.name_PM,))
        elif row1 == 3:
            cur.execute(sqlstr1,("Early",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",self.name_PM,))
        elif row1 == 4:
            cur.execute(sqlstr1,("CTP",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",self.name_PM,))
        elif row1 == 1:
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        else:
            cur.execute('select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info,Decisions  where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            self.Sent_Back = 1
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTotalMore(self, row1):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        sqlstr1 = 'SELECT count(*) FROM Subcon_Info, Decisions where Decisions.Decision_PM = ? And ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        tablerow=0
        if row1 == 0:
            cur.execute(sqlstr1,("Extend",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Extend",self.name_PM,))
        elif row1 == 2:
            cur.execute(sqlstr1,("Release",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Release",self.name_PM,))
        elif row1 == 3:
            cur.execute(sqlstr1,("Early",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("Early",self.name_PM,))
        elif row1 == 4:
            cur.execute(sqlstr1,("CTP",self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute(sqlstr,("CTP",self.name_PM,))
        elif row1 == 1:
            cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        else:
            cur.execute('select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            x, = cur.fetchone()
            self.rowcount = int(x)
            self.table.setRowCount(self.rowcount)
            results = cur.execute('select * from Subcon_Info,Decisions where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Project_Manager = ?',(self.name_PM,))
            self.Sent_Back = 1
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,self.rowcount):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    def doextension(self): ## When user clicks on Extend Button, the tool prompts the fields to put in remarks, date and reason.
        if self.released % 2 != 0:  ## Checks whether if Early separation or ctp button has been clicked or not. Odd no. signifies presence of that particular option. If any one of them are present, then delete and make space for options for extending. 
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.released+=1
        
        if self.ctped % 2 != 0:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.ctped+=1
        # If the user clicks the extend button and the contents under it are not present then show those contents, else delete them.
        if self.extension % 2 == 0:  
            self.extend_justification = QtWidgets.QLabel()
            self.extend_tenure = QtWidgets.QLabel()
            self.extend_reason = QtWidgets.QLabel()
            self.extend_justification.setFixedWidth(100)
            self.extend_reason.setFixedWidth(100)
            self.extend_reason.setWordWrap(True)
            self.extend_tenure.setFixedWidth(100)
            self.extend_justification.setFont(self.font)
            self.extend_tenure.setFont(self.font)
            self.extend_reason.setFont(self.font)
            self.extend_justification_value = QtWidgets.QTextEdit()
            self.extend_justification_value.setFixedHeight(40)
            self.combobox_1 = QtWidgets.QComboBox()
            self.Date = QtWidgets.QDateEdit()
            self.Date.setFixedHeight(40)
            self.extend_justification_value.setFixedWidth(250)
            self.combobox_1.setFixedWidth(300)
            self.combobox_1.setFixedHeight(40)
            self.Date.setFixedWidth(150)
            self.extend_justification.setWordWrap(True)
            self.extend_tenure.setWordWrap(True)
            self.extend_reason.setWordWrap(True)
            self.extend_justification.setText("Extension Justification")
            self.extend_tenure.setText("Extension Required Till")
            self.extend_reason.setText("Reason for Extension")
            self.gridLayout_5.addWidget(self.extend_justification,0,0)
            self.gridLayout_5.addWidget(self.extend_tenure,0,2)
            self.gridLayout_5.addWidget(self.extend_reason,0,4)
            self.gridLayout_5.addWidget(self.extend_justification_value,0,1)
            self.gridLayout_5.addWidget(self.combobox_1,0,5)
            self.gridLayout_5.addWidget(self.Date,0,3)
            self.extension+=1
            connection = sqlite3.connect('EY_1')
            cur = connection.cursor()
            results = cur.execute('select Renewal from Choices')
            reasons = []   ## Query to extract the reasons to select from 
            for row in results:
                if str(row[0]) != 'None':
                    reasons.append(str(row[0]))
            self.combobox_1.addItems(reasons)
            self.combobox_1.activated[str].connect(self.giveBackground)
            self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
            self.highestdate = QtCore.QDate(2075,1,1)  ## This is highest date 
            self.Date.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range
        
        else:
            ## Code to delete all the contents of this grid
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.extension+=1
    
    def giveBackground(self):  ## gives background color to chosen reason
        self.reason = self.combobox_1.currentText()
        if self.reason == "Cheaper via subcon route" or self.reason == "Low end work" or self.reason == "Niche skills" or self.reason == "Contractual obligation" or self.reason == "Short Term":
            self.subcon_rag = "Green"
            self.combobox_1.setStyleSheet("QComboBox{background:rgb(144,238,144)}")
        elif self.reason == "Customer recommended & critical subcons" or self.reason == "Mobility restriction":
            self.subcon_rag = "Amber"
            self.combobox_1.setStyleSheet("QComboBox{background:rgb(255,191,0)}")
        else:
            self.subcon_rag = "Red"
            self.combobox_1.setStyleSheet("QComboBox{background:rgb(255,0,0)}")    

    ## dorelease and doctp functions have the same logic ## 
    def dorelease(self):
        if self.extension % 2 != 0:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.extension+=1
        
        if self.ctped % 2 != 0:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.ctped+=1
        
        if self.released % 2 == 0:
            self.label7 = QtWidgets.QLabel()
            self.label8 = QtWidgets.QLabel()
            self.label9 = QtWidgets.QLabel()
            self.label7.setFixedWidth(100)
            self.label9.setFixedWidth(100)
            self.label9.setWordWrap(True)
            self.label8.setFixedWidth(100)
            self.label7.setFont(self.font)
            self.label8.setFont(self.font)
            self.label9.setFont(self.font)
            self.text_edit2 = QtWidgets.QTextEdit()
            self.text_edit2.setFixedHeight(40)
            self.combobox_2 = QtWidgets.QComboBox()
            self.combobox_2.addItems(["A","B", "C", "D"])
            self.Date1 = QtWidgets.QDateEdit()
            self.Date1.setFixedHeight(40)
            self.text_edit2.setFixedWidth(250)
            self.combobox_2.setFixedWidth(150)
            self.combobox_2.setFixedHeight(40)
            self.Date1.setFixedWidth(250)
            self.label7.setWordWrap(True)
            self.label8.setWordWrap(True)
            self.label9.setWordWrap(True)
            self.label7.setText("Release Justification")
            self.label8.setText("Release Date")
            self.label9.setText("Reason for Release")
            self.gridLayout_5.addWidget(self.label7,0,0)
            self.gridLayout_5.addWidget(self.label8,0,2)
            self.gridLayout_5.addWidget(self.label9,0,4)
            self.gridLayout_5.addWidget(self.text_edit2,0,1)
            self.gridLayout_5.addWidget(self.combobox_2,0,5)
            self.gridLayout_5.addWidget(self.Date1,0,3)
            self.released+=1
            self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
            self.highestdate = QtCore.QDate.fromString(self.line_edits_1['WO End Date'].text(), 'yyyy-MM-dd') ## This is highest date which is WO End Date
            self.Date1.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range
        
        else:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.released+=1

    def doctp(self):
        if  self.extension % 2 != 0:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.extension+=1
        
        if self.released % 2 != 0:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.released+=1
        
        if self.ctped % 2 == 0:
            self.label10 = QtWidgets.QLabel()
            self.label11 = QtWidgets.QLabel()
            self.label12 = QtWidgets.QLabel()
            self.label10.setFixedWidth(100)
            self.label12.setFixedWidth(100)
            self.label12.setWordWrap(True)
            self.label11.setFixedWidth(100)
            self.label10.setFont(self.font)
            self.label11.setFont(self.font)
            self.label12.setFont(self.font)
            self.text_edit3 = QtWidgets.QTextEdit()
            self.text_edit3.setFixedHeight(40)
            self.combobox_3 = QtWidgets.QComboBox()
            self.combobox_3.addItems(["A","B", "C", "D"])
            self.Date2 = QtWidgets.QDateEdit()
            self.Date2.setFixedHeight(40)
            self.text_edit3.setFixedWidth(250)
            self.combobox_3.setFixedWidth(150)
            self.combobox_3.setFixedHeight(40)
            self.Date2.setFixedWidth(250)
            self.label10.setWordWrap(True)
            self.label11.setWordWrap(True)
            self.label12.setWordWrap(True)
            self.label10.setText("CTP Justification")
            self.label11.setText("Tentative Hiring Date")
            self.label12.setText("Reason for CTP")
            self.gridLayout_5.addWidget(self.label10,0,0)
            self.gridLayout_5.addWidget(self.label11,0,2)
            self.gridLayout_5.addWidget(self.label12,0,4)
            self.gridLayout_5.addWidget(self.text_edit3,0,1)
            self.gridLayout_5.addWidget(self.combobox_3,0,5)
            self.gridLayout_5.addWidget(self.Date2,0,3)
            self.ctped+=1
            self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
            self.highestdate = QtCore.QDate.fromString(self.line_edits_1['WO End Date'].text(), 'yyyy-MM-dd') ## This is highest date which lower than WO End Date
            self.Date2.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range
        
        else:
            while self.gridLayout_5.count():
                child = self.gridLayout_5.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.ctped+=1
    
    def Insert1(self): ## When the PM clicks on submit button for a particular request, then this function is executed
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        ## This function checks which action the PM wants to take among Extend, early separation, ctp
        if self.Sent_Back: # Checks whether the PM is viewing a sent back request or some other request. If sent back, then update his comments, else insert a new row in the table.
            if self.extension % 2 != 0:
                self.mytext = self.extend_justification_value.toPlainText()
                self.mytext1 = self.Date2.date().toString("yyyy-MM-dd")
                self.mytext2 = self.combobox_1.currentText()
                cur.execute('update Decisions set Decision_PM = "Extend", PM_Extension_Justification = ?, PM_Extension_Tenure = ?,PM_Reason_Extension = ?,  Request_Pending_With  = "PGM", Transaction_Date = datetime("now") where Subcon_ID = ? order by Transaction_ID desc LIMIT 1', (self.mytext,self.mytext1,self.mytext2,self.ID,))
                cur.execute('update Subcon_Info set Subcon_RAG = ? where Subcon_ID = ?',(self.subcon_rag,self.ID,))
                self.extend_justification_value.setText("")
                self.combobox_1.clear()
        
            elif self.released % 2 != 0:
                self.mytext4 = self.text_edit2.toPlainText()
                self.date1 = self.Date1.date().toString("yyyy-MM-dd")
                self.mytext5 = self.combobox_2.currentText()
                cur.execute('update Decisions set Decision_PM = "Early", PM_Extension_Justification = ?, PM_Extension_Tenure = ?,PM_Reason_Extension = ?,  Request_Pending_With  = "PGM", Transaction_Date = datetime("now") where Subcon_ID = ? order by Transaction_ID desc LIMIT 1', (self.mytext,self.mytext1,self.mytext2,self.ID,))
                self.text_edit2.setText("")
        
            elif self.ctped % 2 != 0:
                self.mytext6 = self.text_edit3.toPlainText()
                self.date2 = self.Date2.date().toString("yyyy-MM-dd")
                self.mytext7 = self.combobox_3.currentText()
                cur.execute('update Decisions set Decision_PM = "CTP", PM_Extension_Justification = ?, PM_Extension_Tenure = ?,PM_Reason_Extension = ?,  Request_Pending_With  = "PGM", Transaction_Date = datetime("now") where Subcon_ID = ? order by Transaction_ID desc LIMIT 1', (self.mytext,self.mytext1,self.mytext2,self.ID,))
                self.text_edit3.setText("")
            self.Sent_Back = 0
        else:
            if self.extension % 2 != 0:
                self.mytext = self.extend_justification_value.toPlainText()
                self.mytext1 = self.Date.date().toString("yyyy-MM-dd")
                self.mytext2 = self.combobox_1.currentText()
                cur.execute('insert into Decisions (Subcon_ID, Decision_PM, PM_Extension_Justification, PM_Extension_Tenure,PM_Reason_Extension, Request_Status, Request_Pending_With, Transaction_Date) Values (?,"Extend",?,?,?,"Pending","PGM",datetime("now"))', (self.ID,self.mytext,self.mytext1,self.mytext2,))
                cur.execute('update Subcon_Info set Subcon_RAG = ? where Subcon_ID = ?',(self.subcon_rag,self.ID,))
                self.extend_justification_value.setText("")
                self.combobox_1.clear()
        
            elif self.released % 2 != 0:
                self.mytext4 = self.text_edit2.toPlainText()
                self.date1 = self.Date1.date().toString("yyyy-MM-dd")
                self.mytext5 = self.combobox_2.currentText()
                cur.execute('insert into Decisions (Subcon_ID, Decision_PM, PM_Release_Justification, PM_Release_Date,PM_Release_Reason, Request_Status, Request_Pending_With, Transaction_Date) Values (?,"Early",?,?,?,"Pending","Subcon Admin", datetime("now"))', (self.ID,self.mytext4, self.date1,self.mytext5,))
                self.text_edit2.setText("")
        
            elif self.ctped % 2 != 0:
                self.mytext6 = self.text_edit3.toPlainText()
                self.date2 = self.Date2.date().toString("yyyy-MM-dd")
                self.mytext7 = self.combobox_3.currentText()
                cur.execute('insert into Decisions (Subcon_ID, Decision_PM, PM_CTP_Justification, PM_CTP_Date,PM_CTP_Reason, Request_Status, Request_Pending_With, Transaction_Date) Values (?,"CTP",?,?,?,"Pending","Subcon Admin",datetime("now"))', (self.ID,self.mytext6, self.date2,self.mytext7,))
                self.text_edit3.setText("")
        connection.commit()
        connection.close()
        self.transaction2_decision_PM.setText("")
        self.transaction2_remarks_PM.setText("")
        self.transaction2_recomendtenure_PM.setText("")
        self.transaction2_decision_PGM.setText("")
        self.transaction2_remarks_PGM.setText("")
        self.transaction2_recomendtenure_PGM.setText("")
        self.transaction2_decision_SBU.setText("")
        self.transaction2_remarks_SBU.setText("")
        self.transaction2_recomendtenure_SBU.setText("")
        self.transaction2_decision_EHC.setText("")
        self.transaction2_remarks_EHC.setText("")
        self.transaction2_recomendtenure_EHC.setText("")
        self.transaction1_decision_PM.setText("")
        self.transaction1_remarks_PM.setText("")
        self.transaction1_recomendtenure_PM.setText("")
        self.transaction1_decision_PGM.setText("")
        self.transaction1_remarks_PGM.setText("")
        self.transaction1_recomendtenure_PGM.setText("")
        self.transaction1_decision_SBU.setText("")
        self.transaction1_remarks_SBU.setText("")
        self.transaction1_recomendtenure_SBU.setText("")
        self.transaction1_decision_EHC.setText("")
        self.transaction1_remarks_EHC.setText("")
        self.transaction1_recomendtenure_EHC.setText("")
        self.loaddata_2()
        self.stackedWidget.setCurrentIndex(0)
    
    def showproject(self):  ## To show project details on click of button
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1191, 70, 570, 200))
        self.line_edit = {}## The names of the line edits and their positions in the grid are mentioned in the dictionary
        line_edit = {
                "Unit": (0,1),"Sub Unit": (0,3),"Project_Description": (1,1),	
                "Project ID": (1,3), "Project Contribution Margin": (2,1)
            }

        self.lable = {} ## The Label names and their positions in the grid are mentioned in the dictionary
        lable = {
                "Unit": (0,0),"Sub Unit": (0,2),"Project_Description": (1,0),	
                "Project ID": (1,2),"Project Contribution Margin": (2,0)
        }
        if self.counter_1 % 2 != 0:## Counter_1 counts the number of times the other details button has been clicked. If button has been clicked odd no.of times, it means that we need to delete the labels from the gridlayout to make space for project details.
            while self.gridLayout_6.count():
                child = self.gridLayout_6.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.counter_1+=1
        if self.counter % 2 == 0: ## Counter counts the number of times the project details button has been clicked. If button has been clicked odd no.of times, it means that we need to delete the labels from the gridlayout and if even then add the labels and line edits to show info.
            for lables_Text, pos in lable.items():
                self.lable[lables_Text] = QtWidgets.QLabel()
                self.lable[lables_Text].setText(lables_Text)
                self.lable[lables_Text].setFont(self.font)
                self.lable[lables_Text].setWordWrap(True)
                self.gridLayout_6.addWidget(self.lable[lables_Text], pos[0], pos[1])
                
            for line_Text, pos in line_edit.items():
                self.line_edit[line_Text] = QtWidgets.QLineEdit()
                self.line_edit[line_Text].setReadOnly(True)
                self.gridLayout_6.addWidget(self.line_edit[line_Text], pos[0], pos[1])
            self.getdata_1()
            self.counter+=1
        else:
            while self.gridLayout_6.count():
                child = self.gridLayout_6.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.counter+=1

    def showother(self): ## Similar logics are used as in showprojectdetails part.
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1191, 70, 570, 200))
        self.line_edit_10 = {}
        line_edit_10 = {
                "Customer Group Name": (0,1),	
                "W2 Vendor": (0,3), "Location": (1,1),"Contract Type": (1,3), "Hiring Reason": (2,1),
            }

        self.lable_10 = {}
        lable_10 = {
                "Customer Group Name": (0,0),	
                "W2 Vendor": (0,2), "Location": (1,0),"Contract Type": (1,2), "Hiring Reason": (2,0),
        }

        if self.counter % 2 != 0:
            while self.gridLayout_6.count():
                child = self.gridLayout_6.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.counter+=1
        if self.counter_1 % 2 == 0:
            for lables_Text, pos in lable_10.items():
                self.lable_10[lables_Text] = QtWidgets.QLabel()
                self.lable_10[lables_Text].setText(lables_Text)
                self.lable_10[lables_Text].setFont(self.font)
                self.lable_10[lables_Text].setWordWrap(True)
                self.gridLayout_6.addWidget(self.lable_10[lables_Text], pos[0], pos[1])
                
            for line_Text, pos in line_edit_10.items():
                self.line_edit_10[line_Text] = QtWidgets.QLineEdit()
                self.line_edit_10[line_Text].setReadOnly(True)
                self.gridLayout_6.addWidget(self.line_edit_10[line_Text], pos[0], pos[1])
            self.getdata_2()
            self.counter_1+=1
        else:
            while self.gridLayout_6.count():
                child = self.gridLayout_6.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            self.counter_1+=1
    
    
    def getdata_1(self):  ## Function to fill in values for project details
        connection = sqlite3.connect("EY")
        cur = connection.cursor()
        result = cur.execute('SELECT * from Subcon_Info where Subcon_ID = ?', (self.ID,))
        for row in result:
            self.line_edit["Unit"].setText(str(row[0]))
            self.line_edit["Sub Unit"].setText(str(row[1]))
            self.line_edit["Project_Description"].setText(str(row[9]))
            self.line_edit["Project ID"].setText(str(row[8]))
            self.line_edit["Project Contribution Margin"].setText(str(row[11]) + '%')
            if str(row[29]) == "Red":
                self.line_edit["Project Contribution Margin"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[29]) == "Amber":
                self.line_edit["Project Contribution Margin"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edit["Project Contribution Margin"].setStyleSheet("background-color: rgb(144,238,144);")
        connection.commit()
        connection.close()

    def getdata_2(self):  ## Function to fill in values for other details
        connection = sqlite3.connect("EY")
        cur = connection.cursor()
        result = cur.execute('SELECT * from Subcon_Info where Subcon_ID = ?', (self.ID,))
        for row in result:
            self.line_edit_10["Customer Group Name"].setText(str(row[7]))
            self.line_edit_10["W2 Vendor"].setText(str(row[13]))
            self.line_edit_10["Location"].setText(str(row[23]))
            self.line_edit_10["Contract Type"].setText(str(row[10]))
            self.line_edit_10["Hiring Reason"].setText(str(row[28]))
            if str(row[30]) == "Red":
                self.line_edit_10["Hiring Reason"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[30]) == "Amber":
                self.line_edit_10["Hiring Reason"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edit_10["Hiring Reason"].setStyleSheet("background-color: rgb(144,238,144);")
        connection.commit()
        connection.close()
         

    def TakeAction(self, row):   # On clicking a cell of the Table on Page 2
        self.ID = self.table.item(row,2).text() ## Stores the Subcon ID of the selected person
        self.ID = str(self.ID)   
        self.loaddata_1()   ## Load data into Page 3
        self.stackedWidget.setCurrentIndex(2) ## Move to page 3
    
    
    def loaddata_1(self):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT (Julianday("now") - Julianday("Date_of_Joining")) FROM Subcon_Info where Subcon_ID = ?', (self.ID,))
        tenure, = cur.fetchone() ## Calculating tenure. It is the difference in the number of days between today and Joining Day
        tenure = round(tenure/30,1)
        self.line_edits_1["Tenure"].setText(str(tenure))   # Finally we report Tenure in months, so dividing it by 30
        if tenure > 12.0:
            self.line_edits_1["Tenure"].setStyleSheet("background-color: #f70d1a;")
            self.tenure_rag = "Red"
        elif tenure > 6.0 and tenure <= 12.0:
            self.tenure_rag = "Amber"
            self.line_edits_1["Tenure"].setStyleSheet("background-color: rgb(255,191,0);")
        else:
            self.tenure_rag = "Green"
            self.line_edits_1["Tenure"].setStyleSheet("background-color: rgb(144,238,144);")
        results = cur.execute('SELECT * FROM Subcon_Info where Subcon_ID = ?', (self.ID,))

        for row in results:
            self.line_edits_1["Subcon Name"].setText(str(row[3])) ## Add info to the relevant line edits
            self.line_edits_1["Date of Joining"].setText(str(row[4]))
            self.line_edits_1["Customer Name"].setText(str(row[6]))
            self.line_edits_1["WO End Date"].setText(str(row[5]))
            self.line_edits_1["Vendor Name"].setText(str(row[12]))
            self.line_edits_1["Subcon Role"].setText(str(row[14]))
            self.line_edits_1["Subcon Band"].setText(str(row[15]))
            self.line_edits_1["Subcon Experience"].setText(str(row[16]))
            self.line_edits_1["Country"].setText(str(row[17]))
            self.line_edits_1["City"].setText(str(row[18]))
            self.line_edits_1["Skill Family"].setText(str(row[19]))
            self.line_edits_1["Skill Type"].setText(str(row[20]))
            self.line_edits_1["Skill (Primary)"].setText(str(row[21]))
            self.line_edits_1["Skill (Secondary)"].setText(str(row[22]))
            self.line_edits_2["Vendor Rate (per hour USD)"].setText(str(row[24]))
            self.line_edits_2["Customer Rate Margin"].setText(str(row[25]))
            self.line_edits_2["Margin"].setText(str(row[26]))
            self.line_edits_3["Margin RAG"].setText(str(row[27]))
            self.line_edits_3["Tenure RAG"].setText(self.tenure_rag)
            self.line_edits_3["Project ID RAG"].setText(str(row[29]))
            self.line_edits_3["Subcon RAG"].setText(str(row[30]))
            # Highlight the Margin and Tenure based on their RAG
            if str(row[27]) == "Red":
                self.line_edits_2["Margin"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[27]) == "Amber":
                self.line_edits_2["Margin"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edits_2["Margin"].setStyleSheet("background-color: rgb(144,238,144);")
        connection.commit()
        connection.close()
    
    def loaddata_2(self):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        ## Query to count the no. of Transactions based on Decision on PM and Contract Type with 30 days < WO Expriry date < 60 days
        sqlstr = 'select count(*) from Decisions, Subcon_Info where Decisions.Decision_PM = ? AND Subcon_Info.Contract_Type = ? And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'

        ## Query to count the no. of Transactions based on Decision on PM and Contract Type with WO Expriry date < 30 days
        sqlstr1 = 'select count(*) from Decisions, Subcon_Info where Decisions.Decision_PM = ? AND Subcon_Info.Contract_Type = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        
        cur.execute(sqlstr1, ("Extend", "FP", self.name_PM,))
        R1, = cur.fetchone()
        self.tableWidget1.setItem(0,1,QtWidgets.QTableWidgetItem(str(R1)))
        cur.execute(sqlstr1, ("Extend", "T&M", self.name_PM,))
        R2, = cur.fetchone()
        self.tableWidget2.setItem(0,1,QtWidgets.QTableWidgetItem(str(R2)))
        self.tableWidget3.setItem(0,1,QtWidgets.QTableWidgetItem(str(R1 + R2)))
        
        cur.execute(sqlstr, ("Extend", "FP",self.name_PM,))
        R3, = cur.fetchone()
        self.tableWidget4.setItem(0,1,QtWidgets.QTableWidgetItem(str(R3)))
        cur.execute(sqlstr, ("Extend", "T&M",self.name_PM,))
        R4, = cur.fetchone()
        self.tableWidget5.setItem(0,1,QtWidgets.QTableWidgetItem(str(R4)))
        self.tableWidget6.setItem(0,1,QtWidgets.QTableWidgetItem(str(R3 + R4)))

        cur.execute(sqlstr1, ("Release", "FP",self.name_PM,))
        R5, = cur.fetchone()
        self.tableWidget1.setItem(2,1,QtWidgets.QTableWidgetItem(str(R5)))
        cur.execute(sqlstr1, ("Release", "T&M",self.name_PM,))
        R6, = cur.fetchone()
        self.tableWidget2.setItem(2,1,QtWidgets.QTableWidgetItem(str(R6)))
        self.tableWidget3.setItem(2,1,QtWidgets.QTableWidgetItem(str(R5 + R6)))

        cur.execute(sqlstr, ("Release", "FP",self.name_PM,))
        R7, = cur.fetchone()
        self.tableWidget4.setItem(2,1,QtWidgets.QTableWidgetItem(str(R7)))
        cur.execute(sqlstr, ("Release", "T&M",self.name_PM,))
        R8, = cur.fetchone()
        self.tableWidget5.setItem(2,1,QtWidgets.QTableWidgetItem(str(R8)))
        self.tableWidget6.setItem(2,1,QtWidgets.QTableWidgetItem(str(R7 + R8)))

        cur.execute(sqlstr1, ("Early", "FP",self.name_PM,))
        R9, = cur.fetchone()
        self.tableWidget1.setItem(3,1,QtWidgets.QTableWidgetItem(str(R9)))
        cur.execute(sqlstr1, ("Early", "T&M",self.name_PM,))
        R10, = cur.fetchone()
        self.tableWidget2.setItem(3,1,QtWidgets.QTableWidgetItem(str(R10)))
        self.tableWidget3.setItem(3,1,QtWidgets.QTableWidgetItem(str(R9 + R10)))
        
        cur.execute(sqlstr, ("Early", "FP",self.name_PM,))
        R11, = cur.fetchone()
        self.tableWidget4.setItem(3,1,QtWidgets.QTableWidgetItem(str(R11)))
        cur.execute(sqlstr, ("Early", "T&M",self.name_PM,))
        R12, = cur.fetchone()
        self.tableWidget5.setItem(3,1,QtWidgets.QTableWidgetItem(str(R12)))
        self.tableWidget6.setItem(3,1,QtWidgets.QTableWidgetItem(str(R11 + R12)))

        cur.execute(sqlstr1, ("CTP", "FP",self.name_PM,))
        R13, = cur.fetchone()
        self.tableWidget1.setItem(4,1,QtWidgets.QTableWidgetItem(str(R13)))
        cur.execute(sqlstr1, ("CTP", "T&M",self.name_PM,))
        R14, = cur.fetchone()
        self.tableWidget2.setItem(4,1,QtWidgets.QTableWidgetItem(str(R14)))
        self.tableWidget3.setItem(4,1,QtWidgets.QTableWidgetItem(str(R13 + R14)))

        cur.execute(sqlstr, ("CTP", "FP",self.name_PM,))
        R15, = cur.fetchone()
        self.tableWidget4.setItem(4,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(sqlstr, ("CTP", "T&M",self.name_PM,))
        R16, = cur.fetchone()
        self.tableWidget5.setItem(4,1,QtWidgets.QTableWidgetItem(str(R16)))
        self.tableWidget6.setItem(4,1,QtWidgets.QTableWidgetItem(str(R15 + R16)))
        
        ## Gives the No. of requests not initiated.
        ## Logic: The Subcons for whom there has been no transaction from the past 30 days and expiry date is less than 30 days is counted ##
        cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "FP" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        R19, = cur.fetchone()
        self.tableWidget1.setItem(1,1,QtWidgets.QTableWidgetItem(str(R19)))
        cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 30)) and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        R21, = cur.fetchone()
        self.tableWidget2.setItem(1,1,QtWidgets.QTableWidgetItem(str(R21)))
        self.tableWidget3.setItem(1,1,QtWidgets.QTableWidgetItem(str(R19 + R21)))

        
        ## Logic: The Subcons for whom there has been no transaction from the past 60 days and expiry date between 30 and 60 days is counted ##
        cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "FP"  and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        R17, = cur.fetchone()
        self.tableWidget4.setItem(1,1,QtWidgets.QTableWidgetItem(str(R17)))
        cur.execute('select count(*) from Subcon_Info where (not exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID) or exists (select * from Decisions where Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Decisions.Transaction_Date) - Julianday("now")) > 60)) and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = "T&M" and Subcon_Info.Project_Manager = ?',(self.name_PM,))
        R23, = cur.fetchone()
        self.tableWidget5.setItem(1,1,QtWidgets.QTableWidgetItem(str(R23)))
        self.tableWidget6.setItem(1,1,QtWidgets.QTableWidgetItem(str(R17 + R23)))

        ## Calculates the no. of sent back requests ##
        ## Logic: The Request is Pending with PM ## 
        sent_back = 'select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Contract_Type = ? and Subcon_Info.Project_Manager = ?'
        sent_back_more = 'select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = "Pending" AND Decisions.Request_Pending_With = "PM" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and ((Julianday(Expected_End_Date) - Julianday("now")) between 30 and 60) and Subcon_Info.Contract_Type = ? and Subcon_Info.Project_Manager = ?'

        cur.execute(sent_back, ("FP",self.name_PM,))
        R15, = cur.fetchone()
        self.tableWidget1.setItem(5,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(sent_back, ("T&M",self.name_PM,))
        R16, = cur.fetchone()
        self.tableWidget2.setItem(5,1,QtWidgets.QTableWidgetItem(str(R16)))
        self.tableWidget3.setItem(5,1,QtWidgets.QTableWidgetItem(str(R15 + R16)))

        cur.execute(sent_back_more, ("FP",self.name_PM,))
        R15, = cur.fetchone()
        self.tableWidget4.setItem(5,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(sent_back_more, ("T&M",self.name_PM,))
        R16, = cur.fetchone()
        self.tableWidget5.setItem(5,1,QtWidgets.QTableWidgetItem(str(R16)))
        self.tableWidget6.setItem(5,1,QtWidgets.QTableWidgetItem(str(R15 + R16)))

        ## The following Query gives the summary of the status of the requests initiated by the PM.
        query1 = 'select count(*) from Decisions, Subcon_Info where Decisions.Request_Status = ? and Subcon_Info.Contract_Type = ? and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Project_Manager = ?'
        cur.execute(query1, ("Approved", "FP",self.name_PM,))
        ApprovedFP, = cur.fetchone()
        self.tableWidget7.setItem(0,1,QtWidgets.QTableWidgetItem(str(ApprovedFP)))
        cur.execute(query1, ("Rejected", "FP",self.name_PM,))
        RejectedFP, = cur.fetchone()
        self.tableWidget8.setItem(0,1,QtWidgets.QTableWidgetItem(str(RejectedFP)))
        cur.execute(query1, ("Pending", "FP",self.name_PM,))
        PendingFP, = cur.fetchone()
        self.tableWidget9.setItem(0,1,QtWidgets.QTableWidgetItem(str(PendingFP)))
        cur.execute(query1, ("Approved", "T&M",self.name_PM,))
        ApprovedTM, = cur.fetchone()
        self.tableWidget7.setItem(1,1,QtWidgets.QTableWidgetItem(str(ApprovedTM)))
        cur.execute(query1, ("Rejected", "T&M",self.name_PM,))
        RejectedTM, = cur.fetchone()
        self.tableWidget8.setItem(1,1,QtWidgets.QTableWidgetItem(str(RejectedTM)))
        cur.execute(query1, ("Pending", "T&M",self.name_PM,))
        PendingTM, = cur.fetchone()
        self.tableWidget9.setItem(1,1,QtWidgets.QTableWidgetItem(str(PendingTM)))
        self.tableWidget9.setItem(2,1,QtWidgets.QTableWidgetItem(str(PendingFP + PendingTM)))
        self.tableWidget8.setItem(2,1,QtWidgets.QTableWidgetItem(str(RejectedFP + RejectedTM)))
        self.tableWidget7.setItem(2,1,QtWidgets.QTableWidgetItem(str(ApprovedFP + ApprovedTM)))

        ## Adding values to Dasboard-2 ##
        ## The Data is grouped by Customer Name and Contract Type
        results = cur.execute('Select Customer_Name, Contract_Type, Count(*), SUM(Vendor_Rate), SUM(Customer_Rate), Round(AVG(Julianday("now") - Julianday(Date_of_Joining)),0) from Subcon_Info group by Customer_Name, Contract_Type having Project_Manager = ?',(self.name_PM,))
        tablerow = 0
        for row in results:
            self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(round(100 - 100*(row[3]/row[4]),2)) + '%'))
            self.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(round(row[5]/30))))
            tablerow = tablerow + 1
        connection.commit()
        connection.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget7.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget7.isSortingEnabled()
        self.tableWidget7.setSortingEnabled(False)
        item = self.tableWidget7.item(0, 0)
        item.setText(_translate("MainWindow", "FP"))
        item = self.tableWidget7.item(1, 0)
        item.setText(_translate("MainWindow", "T&M"))
        item = self.tableWidget7.item(2, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget7.setSortingEnabled(__sortingEnabled)
        self.Approved.setText(_translate("MainWindow", "Approved"))
        self.tableWidget8.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget8.isSortingEnabled()
        self.tableWidget8.setSortingEnabled(False)
        item = self.tableWidget8.item(0, 0)
        item.setText(_translate("MainWindow", "FP"))
        item = self.tableWidget8.item(1, 0)
        item.setText(_translate("MainWindow", "T&M"))
        item = self.tableWidget8.item(2, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget8.setSortingEnabled(__sortingEnabled)
        self.Rejected.setText(_translate("MainWindow", "Rejected"))
        self.tableWidget9.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget9.isSortingEnabled()
        self.tableWidget9.setSortingEnabled(False)
        item = self.tableWidget9.item(0, 0)
        item.setText(_translate("MainWindow", "FP"))
        item = self.tableWidget9.item(1, 0)
        item.setText(_translate("MainWindow", "T&M"))
        item = self.tableWidget9.item(2, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget9.setSortingEnabled(__sortingEnabled)
        self.Progress.setText(_translate("MainWindow", "In Progress"))
        self.summary.setText(_translate("MainWindow", "Request Summary"))
        self.tableWidget1.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget1.isSortingEnabled()
        self.tableWidget1.setSortingEnabled(False)
        item = self.tableWidget1.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget1.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget1.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget1.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget1.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget1.setSortingEnabled(__sortingEnabled)
        self.FP1.setText(_translate("MainWindow", "Expiry Date < 30: FP "))
        self.view1.setText(_translate("MainWindow", "View all Results"))
        __sortingEnabled = self.tableWidget2.isSortingEnabled()
        self.tableWidget2.setSortingEnabled(False)
        item = self.tableWidget2.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget2.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget2.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget2.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget2.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget2.setSortingEnabled(__sortingEnabled)
        self.view2.setText(_translate("MainWindow", "View all Results"))
        self.TM1.setText(_translate("MainWindow", "Expiry Date < 30: T&M"))
        __sortingEnabled = self.tableWidget3.isSortingEnabled()
        self.tableWidget3.setSortingEnabled(False)
        item = self.tableWidget3.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget3.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget3.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget3.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget3.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget3.setSortingEnabled(__sortingEnabled)
        self.view3.setText(_translate("MainWindow", "View all Results"))
        self.Total1.setText(_translate("MainWindow", "Expiry Date < 30: Total "))
        __sortingEnabled = self.tableWidget4.isSortingEnabled()
        self.tableWidget4.setSortingEnabled(False)
        item = self.tableWidget4.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget4.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget4.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget4.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget4.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget4.setSortingEnabled(__sortingEnabled)
        self.view4.setText(_translate("MainWindow", "View all Results"))
        self.FP2.setText(_translate("MainWindow", "Expiry Date > 30: FP "))
        __sortingEnabled = self.tableWidget5.isSortingEnabled()
        self.tableWidget5.setSortingEnabled(False)
        item = self.tableWidget5.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget5.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget5.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget5.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget5.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget5.setSortingEnabled(__sortingEnabled)
        self.TM2.setText(_translate("MainWindow", "Expiry Date > 30: T&M "))
        self.view5.setText(_translate("MainWindow", "View all Results"))
        __sortingEnabled = self.tableWidget6.isSortingEnabled()
        self.tableWidget6.setSortingEnabled(False)
        item = self.tableWidget6.item(0, 0)
        item.setText(_translate("MainWindow", "Extensions Initiated"))
        item = self.tableWidget6.item(1, 0)
        item.setText(_translate("MainWindow", "Extensions Not Initiated"))
        item = self.tableWidget6.item(2, 0)
        item.setText(_translate("MainWindow", "Extensions Dropped"))
        item = self.tableWidget6.item(3, 0)
        item.setText(_translate("MainWindow", "Early Separation"))
        item = self.tableWidget6.item(4, 0)
        item.setText(_translate("MainWindow", "CTP Initiated"))
        self.tableWidget6.setSortingEnabled(__sortingEnabled)
        self.Total2.setText(_translate("MainWindow", "Expiry Date > 30: Total "))
        self.view6.setText(_translate("MainWindow", "View all Results"))
        self.summary_2.setText(_translate("MainWindow", "Dashboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PM_Renewal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

