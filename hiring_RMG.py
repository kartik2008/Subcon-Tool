## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 ## Library to import sqlite3, replace this with mysql connector of python

class RMG_hiring(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        
        ## Request Summary Dashboard ## 

        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")

        ## Main Frame ##
        self.frame = QtWidgets.QFrame(self.page1)
        self.frame.setGeometry(QtCore.QRect(20, 40, 1800, 980))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        ## Frame containing the Request Summary Tables ## 
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(300, 230, 1190, 301))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.summary = QtWidgets.QLabel(self.frame_2)
        self.summary.setGeometry(QtCore.QRect(0, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.summary.setFont(font)
        self.summary.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.summary.setFrameShape(QtWidgets.QFrame.Box)
        self.summary.setAlignment(QtCore.Qt.AlignCenter)
        self.summary.setObjectName("summary")

        ## Table 1: Contract Type = FP. There are 4 rows: Pending Requests, Approved Requests, Rejected Requests, and Requests Sent Back 
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(260, 70, 279, 162))
        self.tableWidget.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        for i in range(4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
        self.tableWidget.setColumnWidth(0,219)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
         
        ## Table 2: Contract Type = T&M. There are 4 rows: Pending Requests, Approved Requests, Rejected Requests, and Requests Sent Back 
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(660, 70, 279, 162))
        self.tableWidget_2.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget_2.setRowCount(4)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        for i in range(4):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
        self.tableWidget_2.setColumnWidth(0,219)
        self.tableWidget_2.setColumnWidth(1,50)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(40)
        
        ## Button to view all requests of contract Type = FP
        self.view1 = QtWidgets.QPushButton(self.frame_2)
        self.view1.setGeometry(QtCore.QRect(260, 230, 279, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.view1.setFont(font)
        self.view1.setObjectName("view1")
        ## Button to view all requests of contract Type = T&M
        self.view2 = QtWidgets.QPushButton(self.frame_2)
        self.view2.setGeometry(QtCore.QRect(660, 230, 279, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.view2.setFont(font)
        self.view2.setObjectName("view2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(260, 40, 279, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(660, 40, 279, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        ## Button to Initiate New Hiring Request ##
        self.newrequest = QtWidgets.QPushButton(self.frame)
        self.newrequest.setGeometry(QtCore.QRect(759, 720, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newrequest.setFont(font)
        self.newrequest.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.newrequest.setObjectName("newrequest")

        self.loaddata_2()
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.addWidget(self.page1)

        ## Page - 2: Request Details ###

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
        self.Heading.setText("Requests")
        ## Cancel button ##
        self.goback = QtWidgets.QPushButton(self.page)
        self.goback.setGeometry(QtCore.QRect(820,870, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        self.goback.setText("Go Back")
        self.goback.clicked.connect(self.GoBack)

        ## Table ##
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(50, 300, 1742, 500))
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("QHeaderView::section{background-color: rgb(255, 191, 0); color: rgb(0, 0,0);} QTableWidget {gridline-color: rgb(0, 0, 0);}")
        self.table.setAlternatingRowColors(True)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setRowCount(15)
        self.table.setColumnCount(10) ## no. of columns 
        self.table.setObjectName("table")
        for i in range(11):
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
        self.columnwidth = 174
        self.Headers = ["Transaction ID","Unit","Sub Unit","Customer Name","Customer Group Name","Project ID","Project Desc","Project Contribution Margin","Contract Type", "Request Status"] ## Headers for columns 
        i = 0
        for names in self.Headers:
            self.table.horizontalHeaderItem(i).setText(names)
            i = i + 1
            
        for i in range(11):
            self.table.setColumnWidth(i,self.columnwidth)
               
        self.stackedWidget.addWidget(self.page)

        ## Page - 3: Form Filling ##
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2") 
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 40, 1770, 970))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget_1 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_1.setGeometry(QtCore.QRect(20, 20, 200, 50))
        self.gridLayoutWidget_1.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_1)
        self.gridLayout_1.setObjectName("gridLayout")
        self.profileinfo = QtWidgets.QLabel()
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.profileinfo.setFont(self.font)
        self.profileinfo.setText("Profile Details")
        self.profileinfo.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.profileinfo.setFrameShape(QtWidgets.QFrame.Box)
        self.profileinfo.setFixedHeight(35)
        self.profileinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.profileinfo.setObjectName("profileinfo")
        self.gridLayout_1.addWidget(self.profileinfo,0,0,1,2)
        
        ## Grid to fill the details regarding Subcon Basic Profile ##
        ## To remove any info:- 
        ## 1) Remove all the occurences of that info
        ## 2) Change the locations of others to fill its space.
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 70, 1700, 400))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.line_edits_1 = {}
        line_edits_1 = {
            "Unit": (1,1), "Sub Unit": (1,3),"Customer Name": (1,5),"Customer Group Name": (1,7), "Project ID": (2,1), "Project Description": (2,3),"Project Contribution Margin (%)": (2,5), "Contract Type": (2,7), "Subcon Role": (3,5),"Subcon Band": (3,7),"Subcon Experience": (4,1),"Country": (4,5),	
            "City": (4,3),"Skill Family": (5,1),"Skill Type": (5,3),"Skill (Primary)": (5,5),"Skill (Secondary)": (5,7),
        }

        self.lables_1 = {}
        lables_1 = {
            "Unit": (1,0), "Sub Unit": (1,2),"Date of Joining": (3,0),"Customer Name": (1,4),"Customer Group Name": (1,6), "WO End Date": (3,2), "Project ID": (2,0), "Project Description": (2,2),"Project Contribution Margin (%)": (2,4), "Contract Type": (2,6), "Subcon Role": (3,4),"Subcon Band": (3,6),"Subcon Experience": (4,0),"Country": (4,4),	"Hiring Reason": (4,6),
            "City": (4,2),"Skill Family": (5,0),"Skill Type": (5,2),"Skill (Primary)": (5,4),"Skill (Secondary)": (5,6),
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
            self.gridLayout.addWidget(self.line_edits_1[line_Text], pos[0], pos[1])

        self.doj = QtWidgets.QDateEdit()
        self.gridLayout.addWidget(self.doj,3,1)
        self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
        self.highestdate = QtCore.QDate(2075,1,1)  ## This is highest date 
        self.doj.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range
        self.woend = QtWidgets.QDateEdit()
        self.gridLayout.addWidget(self.woend,3,3)
        self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
        self.highestdate = QtCore.QDate(2075,1,1)  ## This is highest date 
        self.woend.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range
        
        self.hiring_reason = QtWidgets.QComboBox()
        self.loadreasons()
        self.gridLayout.addWidget(self.hiring_reason,4,7)

        ## Grid to fill the Subcon Commercials ##
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 500, 1300, 150))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.commercialinfo = QtWidgets.QLabel()
        self.commercialinfo.setFont(self.font)
        self.commercialinfo.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.commercialinfo.setFrameShape(QtWidgets.QFrame.Box)
        self.commercialinfo.setFixedHeight(35)
        self.commercialinfo.setFixedWidth(200)
        self.commercialinfo.setObjectName("commercialinfo")
        self.commercialinfo.setAlignment(QtCore.Qt.AlignCenter)
        self.commercialinfo.setText("Commercial Details")
        self.gridLayout_2.addWidget(self.commercialinfo,0,0,1,2)

        self.line_edits_2 = {}
        line_edits_2 = {
            "Vendor Rate (per hour USD)": (2,1),	"Customer Rate Margin": (2,3),"Margin": (2,5),
        }
        self.lables_2 = {}
        lables_2 = {
            "Vendor Rate (per hour USD)": (2,0),	"Customer Rate Margin": (2,2),"Margin": (2,4),
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
            self.gridLayout_2.addWidget(self.line_edits_2[line_Text], pos[0], pos[1])
        self.gridLayout_2.setHorizontalSpacing(20)

        
        ## Button to submit the filled form ##
        self.generaterequest = QtWidgets.QPushButton(self.frame_3)
        self.generaterequest.setObjectName("generaterequest")
        self.generaterequest.setText("Generate Request")
        self.generaterequest.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.generaterequest.setFixedHeight(40)
        self.generaterequest.setFixedWidth(200)
        self.generaterequest.setGeometry(QtCore.QRect(20, 895, 150, 40))

        ## To go back to previous page ##
        self.goback_2 = QtWidgets.QPushButton(self.frame_3)
        self.goback_2.setObjectName("goback_2")
        self.goback_2.setText("Go Back")
        self.goback_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.goback_2.setFixedHeight(40)
        self.goback_2.setFixedWidth(200)
        self.goback_2.setGeometry(QtCore.QRect(250, 895, 150, 40))
        self.goback_2.clicked.connect(self.GoBack_2)
        
        self.stackedWidget.addWidget(self.page_2)

        ### Page - 4: Form Reviewing - Pre-filled Data is presented. The only difference between Page -3 and Page-4 is that Line Edits are read only in Page-4.###
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3") 
        self.frame_4 = QtWidgets.QFrame(self.page_3)
        self.frame_4.setGeometry(QtCore.QRect(50, 40, 1770, 970))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 200, 50))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName("gridLayout")
        self.profileinfo_1 = QtWidgets.QLabel()
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setWeight(75)
        self.profileinfo_1.setFont(self.font)
        self.profileinfo_1.setText("Profile Details")
        self.profileinfo_1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.profileinfo_1.setFrameShape(QtWidgets.QFrame.Box)
        self.profileinfo_1.setFixedHeight(35)
        self.profileinfo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.profileinfo_1.setObjectName("profileinfo_1")
        self.gridLayout_4.addWidget(self.profileinfo_1,0,0,1,2)
        
        
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_4)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 70, 1650, 300))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName("gridLayout")

        self.line_edit_1 = {}
        line_edit_1 = {
            "Unit": (1,1), "Sub Unit": (1,3),"Date of Joining": (3,1),"Customer Name": (1,5),"Customer Group Name": (1,7), "WO End Date": (3,3), "Project ID": (2,1), "Project Description": (2,3),"Project Contribution Margin (%)": (2,5), "Contract Type": (2,7), "Subcon Role": (3,5),"Subcon Band": (3,7),"Subcon Experience": (4,1),"Country": (4,5),	"Hiring Reason": (4,7),
            "City": (4,3),"Skill Family": (5,1),"Skill Type": (5,3),"Skill (Primary)": (5,5),"Skill (Secondary)": (5,7),
        }

        self.lable_1 = {}
        lable_1 = {
            "Unit": (1,0), "Sub Unit": (1,2),"Date of Joining": (3,0),"Customer Name": (1,4),"Customer Group Name": (1,6), "WO End Date": (3,2), "Project ID": (2,0), "Project Description": (2,2),"Project Contribution Margin (%)": (2,4), "Contract Type": (2,6), "Subcon Role": (3,4),"Subcon Band": (3,6),"Subcon Experience": (4,0),"Country": (4,4),	"Hiring Reason": (4,6),
            "City": (4,2),"Skill Family": (5,0),"Skill Type": (5,2),"Skill (Primary)": (5,4),"Skill (Secondary)": (5,6),
        }

        for lables_Text, pos in lable_1.items():
            self.lable_1[lables_Text] = QtWidgets.QLabel()
            self.lable_1[lables_Text].setText(lables_Text)
            self.lable_1[lables_Text].setFont(self.font)
            #self.lables[lables_Text].setStyleSheet("background-color: rgb(255, 191, 0);")
            self.lable_1[lables_Text].setWordWrap(True)
            self.gridLayout_5.addWidget(self.lable_1[lables_Text], pos[0], pos[1])
                
        for line_Text, pos in line_edit_1.items():
            self.line_edit_1[line_Text] = QtWidgets.QLineEdit()
            #self.line_edit_1[line_Text].setReadOnly(True)
            self.gridLayout_5.addWidget(self.line_edit_1[line_Text], pos[0], pos[1])

        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_4)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(20, 370, 1171, 120))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.commercialinfo_1 = QtWidgets.QLabel()
        self.commercialinfo_1.setFont(self.font)
        self.commercialinfo_1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.commercialinfo_1.setFrameShape(QtWidgets.QFrame.Box)
        self.commercialinfo_1.setFixedHeight(35)
        self.commercialinfo_1.setFixedWidth(200)
        self.commercialinfo_1.setObjectName("commercialinfo_1")
        self.commercialinfo_1.setAlignment(QtCore.Qt.AlignCenter)
        self.commercialinfo_1.setText("Commercial Details")
        self.gridLayout_6.addWidget(self.commercialinfo_1,0,0,1,2)

        self.line_edit_2= {}
        line_edit_2 = {
            "Vendor Rate (per hour USD)": (1,1),	"Customer Rate Margin": (1,3),"Margin": (1,5),
        }
        self.lable_2 = {}
        lable_2 = {
            "Vendor Rate (per hour USD)": (1,0),	"Customer Rate Margin": (1,2),"Margin": (1,4),
        }

        for lables_Text, pos in lable_2.items():
            self.lable_2[lables_Text] = QtWidgets.QLabel()
            self.lable_2[lables_Text].setText(lables_Text)
            self.lable_2[lables_Text].setFont(self.font)
            #self.lables[lables_Text].setStyleSheet("background-color: rgb(255, 191, 0);")
            self.lable_2[lables_Text].setWordWrap(True)
            self.gridLayout_6.addWidget(self.lable_2[lables_Text], pos[0], pos[1])
                
        for line_Text, pos in line_edit_2.items():
            self.line_edit_2[line_Text] = QtWidgets.QLineEdit()
            #self.line_edit_2[line_Text].setReadOnly(True)
            self.gridLayout_6.addWidget(self.line_edit_2[line_Text], pos[0], pos[1])
        self.gridLayout_6.setHorizontalSpacing(20)

        ## Grid Which provides Remarks entering, Option to cancel or Answer Query and any Reason RMG wants to give ##
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.frame_4)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(20, 670, 900, 120))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName("gridLayout_5")
        self.label4 = QtWidgets.QLabel()
        self.label5 = QtWidgets.QLabel()
        self.label4.setFixedWidth(80)
        self.label5.setFixedWidth(80)
        self.label4.setFont(self.font)
        self.label5.setFont(self.font)
        self.text_edit1 = QtWidgets.QTextEdit()
        self.text_edit1.setFixedHeight(40)
        self.combobox_1 = QtWidgets.QComboBox()
        self.combobox_1.addItems(["Cancel Request","Respond to Query"])
        self.text_edit1.setFixedWidth(250)
        self.combobox_1.setFixedWidth(250)
        self.combobox_1.setFixedHeight(40)
        self.label4.setWordWrap(True)
        self.label5.setWordWrap(True)
        self.label4.setText("Remarks")
        self.label5.setText("Decision")
        self.gridLayout_8.addWidget(self.label4,0,0)
        self.gridLayout_8.addWidget(self.label5,0,2)
        self.gridLayout_8.addWidget(self.text_edit1,0,1)
        self.gridLayout_8.addWidget(self.combobox_1,0,3)

        ## Submit Button ##
        self.submit = QtWidgets.QPushButton(self.frame_4)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.submit.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.submit.setFixedHeight(40)
        self.submit.setFixedWidth(200)
        self.submit.setGeometry(QtCore.QRect(20, 895, 150, 40))

        ## GO back button ##
        self.goback_3 = QtWidgets.QPushButton(self.frame_4)
        self.goback_3.setObjectName("goback_3")
        self.goback_3.setText("Go Back")
        self.goback_3.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.goback_3.setFixedHeight(40)
        self.goback_3.setFixedWidth(200)
        self.goback_3.setGeometry(QtCore.QRect(250, 895, 150, 40))
        self.goback_3.clicked.connect(self.GoBack_3)
        
        ## Grid to show Remarks History Button #
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.frame_4)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(1300, 450, 371, 51))
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

        ## Feature to Show Transaction History ###
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setGeometry(QtCore.QRect(1200, 550, 541, 250))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")

        ## 3 Tabs for Project Manager, SBU Head, EHC Appover
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab, "Project Manager")
        self.tabWidget.addTab(self.tab_2, "SBU Head")
        self.tabWidget.addTab(self.tab_3, "EHC Approver")
        self.transaction1 = QtWidgets.QLabel(self.tabWidget)  ## Last Transaction Label
        self.transaction1.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.transaction1.setFont(font)
        self.transaction1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transaction1.setObjectName("transaction1")
        self.transaction1_date_RMG = QtWidgets.QLabel(self.tab)    ## Last Transaction Date Label
        self.transaction1_date_RMG.setGeometry(QtCore.QRect(152, 35, 211, 31))
        self.transaction1_date_RMG.setObjectName("transaction1_date_RMG")
        
        self.transaction1_1 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1_1.setGeometry(QtCore.QRect(20, 100, 151, 30))
        self.transaction1_1.setWordWrap(True)
        self.transaction1_1.setObjectName("transaction1_1")
        self.transaction1_2 = QtWidgets.QLabel(self.tabWidget)
        self.transaction1_2.setGeometry(QtCore.QRect(20, 150, 151, 30))
        self.transaction1_2.setWordWrap(True)
        self.transaction1_2.setObjectName("transaction1_2")
        
        self.transaction1_decision_RMG = QtWidgets.QTextEdit(self.tab)   
        self.transaction1_decision_RMG.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_RMG.setReadOnly(True)
        self.transaction1_decision_RMG.setObjectName("transaction1_decision_RMG")
        self.transaction1_remarks_RMG = QtWidgets.QTextEdit(self.tab)
        self.transaction1_remarks_RMG.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_RMG.setReadOnly(True)
        self.transaction1_remarks_RMG.setObjectName("transaction1_remarks_RMG")
        
        self.transaction1_decision_SBU = QtWidgets.QTextEdit(self.tab_2)
        self.transaction1_decision_SBU.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_SBU.setReadOnly(True)
        self.transaction1_decision_SBU.setObjectName("transaction1_decision_SBU")
        self.transaction1_remarks_SBU = QtWidgets.QTextEdit(self.tab_2)
        self.transaction1_remarks_SBU.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_SBU.setReadOnly(True)
        self.transaction1_remarks_SBU.setObjectName("transaction1_remarks_SBU")
        
        self.transaction1_decision_EHC = QtWidgets.QTextEdit(self.tab_3)
        self.transaction1_decision_EHC.setGeometry(QtCore.QRect(180, 76, 321, 30))
        self.transaction1_decision_EHC.setReadOnly(True)
        self.transaction1_decision_EHC.setObjectName("transaction1_decision_EHC")
        self.transaction1_remarks_EHC = QtWidgets.QTextEdit(self.tab_3)
        self.transaction1_remarks_EHC.setGeometry(QtCore.QRect(180, 120, 321, 30))
        self.transaction1_remarks_EHC.setReadOnly(True)
        self.transaction1_remarks_EHC.setObjectName("transaction1_remarks_EHC")

        self.transaction1_date_SBU = QtWidgets.QLabel(self.tab_2)
        self.transaction1_date_SBU.setGeometry(QtCore.QRect(152, 30, 211, 31))
        self.transaction1_date_SBU.setObjectName("transaction1_date_SBU")
        self.transaction1_date_EHC = QtWidgets.QLabel(self.tab_3)
        self.transaction1_date_EHC.setGeometry(QtCore.QRect(152, 30, 211, 31))
        self.transaction1_date_EHC.setObjectName("transaction1_date_EHC")

        
        self.transaction1_1.setFont(font)
        self.transaction1_2.setFont(font)
        self.transaction1.setText("Last Transaction:")
        self.transaction1_1.setText("Decision")
        self.transaction1_2.setText("Remarks")
        self.tabWidget.setCurrentIndex(0)


        self.stackedWidget.addWidget(self.page_3)
        self.hiring_reason.setStyleSheet("QComboBox{background:rgb(144,238,144)}")
        self.subcon_rag = 'Green'
        self.hiring_reason.activated[str].connect(self.giveBackground)
        self.line_edits_1['Project Contribution Margin (%)'].textChanged.connect(self.giveBackgroundProject)
        self.line_edits_2['Customer Rate Margin'].textChanged.connect(self.calculatemargin)
        self.line_edits_2['Vendor Rate (per hour USD)'].textChanged.connect(self.calculatemargin)
        self.line_edit_1['Project Contribution Margin (%)'].textChanged.connect(self.giveBackgroundProject_1)
        self.line_edit_2['Customer Rate Margin'].textChanged.connect(self.calculatemargin_1)
        self.line_edit_2['Vendor Rate (per hour USD)'].textChanged.connect(self.calculatemargin_1)

        MainWindow.setCentralWidget(self.centralwidget)
        ## Menubar ##
        self.menubar = QtWidgets.QMenuBar(self.centralwidget)
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(0,0,0); color: #e0e0e0; font-size: 20px;} QMenuBar::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 20px;} QMenu{background-color: rgb(0,0,0); color: rgb(255,255,255); font-size: 18px; font-weight: 150} QMenu::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 18px;}") ## Properties of Menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 32))
        self.homescreen = QtWidgets.QAction("Home", self.menubar) ## Home Button on Menubar
        self.font_1 = QtGui.QFont()
        self.font_1.setBold(True)
        self.font_1.setWeight(30)
        self.menubar.addAction(self.homescreen)
        self.modules_menu = self.menubar.addMenu("Modules")  ## Modules menu
        self.modules_menu.setFont(self.font_1)
        self.accessdashboard = QtWidgets.QAction("Dashboard", self.menubar) ## Dashboard Menu
        self.menubar.addAction(self.accessdashboard)

        ## Sub-menus under Modules Menu
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

        self.view1.clicked.connect(self.FPall)
        self.view2.clicked.connect(self.TMall)
        self.newrequest.clicked.connect(self.request)
        self.generaterequest.clicked.connect(self.Insertintotable)
        self.table.cellClicked.connect(self.TakeAction)
        self.submit.clicked.connect(self.Insert1)
        self.tableWidget.cellClicked.connect(self.showFP)
        self.tableWidget_2.cellClicked.connect(self.showTM)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def calculatemargin_1(self):
        if self.line_edit_2["Vendor Rate (per hour USD)"].text() != '' and self.line_edit_2['Customer Rate Margin'].text() != '':
            vendor_Rate = float(self.line_edit_2["Vendor Rate (per hour USD)"].text())
            customer_Rate = float(self.line_edit_2["Customer Rate Margin"].text())
            self.margin = round(100*(1 - (vendor_Rate/customer_Rate)),2)
            self.line_edit_2['Margin'].setText(str(self.margin) + '%')
            if self.margin < 25.0:
                self.line_edit_2['Margin'].setStyleSheet('background-color: rgb(255,0,0);')
                self.margin_rag = 'Red'
            elif self.margin >= 30.0:
                self.line_edit_2['Margin'].setStyleSheet('background-color: rgb(144,238,144);')
                self.margin_rag = 'Green'
            else:
                self.line_edit_2['Margin'].setStyleSheet('background-color: rgb(255,191,0);')
                self.margin_rag = 'Amber'
    
    def calculatemargin(self):
        if self.line_edits_2["Vendor Rate (per hour USD)"].text() != '' and self.line_edits_2['Customer Rate Margin'].text() != '':
            vendor_Rate = float(self.line_edits_2["Vendor Rate (per hour USD)"].text())
            customer_Rate = float(self.line_edits_2["Customer Rate Margin"].text())
            self.margin = round(100*(1 - (vendor_Rate/customer_Rate)),2)
            self.line_edits_2['Margin'].setText(str(self.margin) + '%')
            if self.margin < 25.0:
                self.line_edits_2['Margin'].setStyleSheet('background-color: rgb(255,0,0);')
                self.margin_rag = 'Red'
            elif self.margin >= 30.0:
                self.line_edits_2['Margin'].setStyleSheet('background-color: rgb(144,238,144);')
                self.margin_rag = 'Green'
            else:
                self.line_edits_2['Margin'].setStyleSheet('background-color: rgb(255,191,0);')
                self.margin_rag = 'Amber'
    
    def giveBackgroundProject_1(self,text):
        if text != '%':
            project = float(text[:-1])
            if project >= 30.0: 
                self.line_edit_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(144,238,144);')
                self.project_rag = 'Green'
            elif project >= 25.0 and project < 30.0:
                self.line_edit_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(255,191,0);')
                self.project_rag = 'Amber'
            else:
                self.line_edit_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(255,0,0);')
                self.project_rag = 'Red'
    
    def giveBackgroundProject(self,text):
        if text != '':
            project = float(text)
            if project >= 30.0: 
                self.line_edits_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(144,238,144);')
                self.project_rag = 'Green'
            elif project >= 25.0 and project < 30.0:
                self.line_edits_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(255,191,0);')
                self.project_rag = 'Amber'
            else:
                self.line_edits_1['Project Contribution Margin (%)'].setStyleSheet('background-color: rgb(255,0,0);')
                self.project_rag = 'Red'

    def giveBackground(self):
        self.reason = self.hiring_reason.currentText()
        if self.reason == "Cheaper via subcon route" or self.reason == "Low end work" or self.reason == "Niche skills" or self.reason == "Contractual obligation" or self.reason == "Short Term":
            self.hiring_reason.setStyleSheet("QComboBox{background:rgb(144,238,144)}")
            self.subcon_rag = 'Green'
        elif self.reason == "Customer recommended & critical subcons" or self.reason == "Mobility restriction":
            self.hiring_reason.setStyleSheet("QComboBox{background:rgb(255,191,0)}")
            self.subcon_rag = 'Amber'
        else:
            self.hiring_reason.setStyleSheet("QComboBox{background:rgb(255,0,0)}")    
            self.subcon_rag = 'Red'

    def loadreasons(self): ## Loads reasons for Drop down menu
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        results = cur.execute('select Hiring from Choices')
        reasons = []
        for row in results:
            if str(row[0]) != 'None':
                reasons.append(str(row[0]))
        self.hiring_reason.addItems(reasons)
    
    
    def showFP(self,row1):## For Dashboard containing info about the Contract Type - FP, clicking on a cell in row, different queries shall be executed
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select * from Hiring where Contract_Type = "FP" and Request_Status = ? and RMG_ID = ?'
        if row1 == 0:   ## All request with Request Status = Pending
            results = cur.execute(query1,("Pending",self.name_RMG,))
        elif row1 == 1: ## All request with Request Status = Approved
            results = cur.execute(query1,("Approved",self.name_RMG,))
        elif row1 == 2:   ## All request with Request Status = Rejected
            results = cur.execute(query1,("Rejected",self.name_RMG,))
        else:    ## Requests which are sent back for query by SBU Head
            results = cur.execute('select * from Hiring where Request_Status = "Pending" and Request_Pending_With = "RMG" and Contract_Type = "FP" and RMG_ID = ?',(self.name_RMG,))
        tablerow=0
        for row in results:   # Add values to the table
            self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[37])))
            for i in range(1,9):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i+1])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(11):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)   ## Move to Page 2
    
    def showTM(self,row1):  ## For Dashboard containing info about the Contract Type - T&M, clicking on a cell in row, different queries shall be executed
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select * from Hiring where Contract_Type = "T&M" and Request_Status = ? and RMG_ID = ?'
        if row1 == 0:
            results = cur.execute(query1,("Pending",self.name_RMG,))
        elif row1 == 1:
            results = cur.execute(query1,("Approved",self.name_RMG,))
        elif row1 == 2:
            results = cur.execute(query1,("Rejected",self.name_RMG,))
        else:
            results = cur.execute('select * from Hiring where Request_Status = "Pending" and Request_Pending_With = "RMG" and Contract_Type = "T&M" and RMG_ID = ?', (self.name_RMG,))
        tablerow=0
        for row in results:
            self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[37])))
            for i in range(1,9):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i+1])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(11):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def showhistory(self):  ## Function to Show Transaction History, gets activated on clicking the Show Remarks Button ##
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('select count(*) from Hiring where Transaction_ID = ?',(self.ID,))## To check if there was any previous transactions for this subcon
        number, = cur.fetchone()
        if number == 0: ## If no transaction is there, then set all values to none
            self.transaction1_decision_RMG.setText("None")
            self.transaction1_remarks_RMG.setText("None")
            self.transaction1_date_RMG.setText("None")
            self.transaction1_decision_SBU.setText("None")
            self.transaction1_remarks_SBU.setText("None")
            self.transaction1_date_SBU.setText("None")
            self.transaction1_decision_EHC.setText("None")
            self.transaction1_remarks_EHC.setText("None")
            self.transaction1_date_EHC.setText("None")
        else:       ## Otherwise insert the values.
            results = cur.execute('select Decision_RMG, Remarks_RMG, Transaction_Date, Decision_SBU, Remarks_SBU, Transaction_Date_SBU, Decision_EHC, Remarks_EHC, Transaction_Date_EHC from Hiring where Transaction_ID = ?',(self.ID,))
            for row in results:
                self.transaction1_decision_RMG.setText(str(row[0]))
                self.transaction1_remarks_RMG.setText(str(row[1]))
                self.transaction1_date_RMG.setText(str(row[2]))
                self.transaction1_decision_SBU.setText(str(row[3]))
                self.transaction1_remarks_SBU.setText(str(row[4]))
                self.transaction1_date_SBU.setText(str(row[5]))
                self.transaction1_decision_EHC.setText(str(row[6]))
                self.transaction1_remarks_EHC.setText(str(row[7]))
                self.transaction1_date_EHC.setText(str(row[8]))
        connection.commit()
        connection.close()
    
    def Insert1(self):  ## On clicking the Submit button this function comes into play
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        text24 = self.combobox_1.currentText()   ## RMG can cancel the initiated request if the SBU head hasn't taken any decision
        text25 = self.text_edit1.toPlainText()
        text1 = self.line_edit_1["Unit"].text()
        text2 = self.line_edit_1["Sub Unit"].text()
        text3 = self.line_edit_1["Customer Name"].text()
        text4 = self.line_edit_1["Customer Group Name"].text()
        text5 = self.line_edit_1["Project ID"].text()
        text6 = self.line_edit_1["Project Description"].text()
        text7 = str(self.line_edit_1["Project Contribution Margin (%)"].text())
        text8 = self.line_edit_1["Contract Type"].text()
        text9 = self.line_edit_1["Date of Joining"].text()
        text10 = self.line_edit_1["WO End Date"].text()
        text11 = self.line_edit_1["Subcon Role"].text()
        text12 = self.line_edit_1["Subcon Band"].text()
        text13 = self.line_edit_1["Subcon Experience"].text()
        text14 = self.line_edit_1["City"].text()
        text15 = self.line_edit_1["Country"].text()
        text16 = self.line_edit_1["Hiring Reason"].text()
        text17 = self.line_edit_1["Skill Family"].text()
        text18 = self.line_edit_1["Skill Type"].text()
        text19 = self.line_edit_1["Skill (Primary)"].text()
        text20 = self.line_edit_1["Skill (Secondary)"].text()
        text21 = self.line_edit_2["Vendor Rate (per hour USD)"].text()
        text22 = self.line_edit_2["Customer Rate Margin"].text()
        text23 = str(self.line_edit_2["Margin"].text())
        if text23 != '%':
            margin = float(text23[:-1])
            if margin >= 30.0: 
                self.margin_rag = 'Green'
            elif margin >= 25.0 and margin < 30.0:
                self.margin_rag = 'Amber'
            else:
                self.margin_rag = 'Red'
        if text7 != '%':
            project = float(text7[:-1])
            if project >= 30.0: 
                self.project_rag = 'Green'
            elif project >= 25.0 and project < 30.0:
                self.project_rag = 'Amber'
            else:
                self.project_rag = 'Red'
        
        if self.margin_rag == 'Red' or self.project_rag == 'Red' or self.subcon_rag == 'Red':
            self.Cummulative = "Red"
        else:
            if self.margin_rag == 'Amber' or self.project_rag == 'Amber' or self.subcon_rag == 'Amber':
                self.Cummulative = "Amber"
            else:
                self.Cummulative = "Green"

        if text24 == "Cancel Request":
            cur.execute('update Hiring set Decision_RMG = "Canceled", Request_Status = "Canceled", Request_Status = "", Decision_SBU = "", Transaction_Date = datetime("now"), Remarks_RMG = ? where Transaction_ID = ?', (text25,self.ID,))
        else:
            cur.execute('update Hiring set Unit = ?, Sub_Unit = ?,Customer_Name = ?, Customer_Group_Name = ?, Project_ID = ?, Project_Desc = ?,Project_Contribution_Margin = ?, Contract_Type = ?, DOJ = ?,WO_End_Date = ?,Subcon_Role = ?,Subcon_Band = ?,Subcon_Exp = ?,City  = ?, Country = ?, Hiring_Reason = ?,Skill_Family = ?, Skill_Type = ?, Skill_Primary = ?, Skill_Secondary = ?,Vendor_Rate = ?, Customer_Rate = ?,Margin = ?,Margin_RAG = ?,Project_RAG = ?, Cummulative_RAG,Decision_RMG = "Requested", Request_Status = "Pending", Request_Pending_With = "SBU Head", Transaction_Date = datetime("now"), Remarks_RMG = ? where Transaction_ID = ?', (text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,self.margin_rag,self.project_rag,self.Cummulative,text25,self.ID,))
        connection.commit()
        connection.close()
        self.text_edit1.setText("")
        self.transaction1_decision_RMG.setText("")
        self.transaction1_remarks_RMG.setText("")
        self.transaction1_date_RMG.setText("")
        self.transaction1_decision_SBU.setText("")
        self.transaction1_remarks_SBU.setText("")
        self.transaction1_date_SBU.setText("")
        self.transaction1_decision_EHC.setText("")
        self.transaction1_remarks_EHC.setText("")
        self.transaction1_date_EHC.setText("")
        self.loaddata_2()   ## Load Data on page 1
        self.stackedWidget.setCurrentIndex(0)  ## Move to Page 1

    def GoBack_3(self):  ## Move to Page 2
        self.transaction1_decision_RMG.setText("")
        self.transaction1_remarks_RMG.setText("")
        self.transaction1_date_RMG.setText("")
        self.transaction1_decision_SBU.setText("")
        self.transaction1_remarks_SBU.setText("")
        self.transaction1_date_SBU.setText("")
        self.transaction1_decision_EHC.setText("")
        self.transaction1_remarks_EHC.setText("")
        self.transaction1_date_EHC.setText("")
        self.stackedWidget.setCurrentIndex(1)

    def TakeAction(self, row):  ## On clicking on any cell of a row 
        self.ID = self.table.item(row,0).text()   ## Store the First value of the row, which is the Transaction ID of the request
        self.ID = str(self.ID)   
        self.loaddata_1()
        self.stackedWidget.setCurrentIndex(3)
    
    def loaddata_1(self):    ## Load Data into the Information page
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Transaction_ID = ?', (self.ID,))  ## Query based on the selected Transaction ID
        
        for row in results:
            self.line_edit_1["Unit"].setText(str(row[2]))
            self.line_edit_1["Sub Unit"].setText(str(row[3]))
            self.line_edit_1["Customer Name"].setText(str(row[4]))
            self.line_edit_1["Customer Group Name"].setText(str(row[5]))
            self.line_edit_1["Project ID"].setText(str(row[6]))
            self.line_edit_1["Project Description"].setText(str(row[7]))
            self.line_edit_1["Project Contribution Margin (%)"].setText(str(row[8]))
            self.line_edit_1["Contract Type"].setText(str(row[9]))
            self.line_edit_1["Date of Joining"].setText(str(row[10]))
            self.line_edit_1["WO End Date"].setText(str(row[11]))
            self.line_edit_1["Subcon Role"].setText(str(row[12]))
            self.line_edit_1["Subcon Band"].setText(str(row[13]))
            self.line_edit_1["Subcon Experience"].setText(str(row[14]))
            self.line_edit_1["City"].setText(str(row[15]))
            self.line_edit_1["Country"].setText(str(row[16]))
            self.line_edit_1["Hiring Reason"].setText(str(row[17]))
            self.line_edit_1["Skill Family"].setText(str(row[18]))
            self.line_edit_1["Skill Type"].setText(str(row[19]))
            self.line_edit_1["Skill (Primary)"].setText(str(row[20]))
            self.line_edit_1["Skill (Secondary)"].setText(str(row[21]))
            self.line_edit_2["Vendor Rate (per hour USD)"].setText(str(row[22]))
            self.line_edit_2["Customer Rate Margin"].setText(str(row[23]))
            self.line_edit_2["Margin"].setText(str(row[24]))
            self.subcon_rag = str(row[27])
            if str(row[25]) == "Red":
                self.line_edit_2["Margin"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[25]) == "Green":
                self.line_edit_2["Margin"].setStyleSheet("background-color: rgb(144,238,144);")
            else:
                self.line_edit_2["Margin"].setStyleSheet("background-color: rgb(255,191,0);")
            if str(row[26]) == "Red":
                self.line_edit_1["Project Contribution Margin (%)"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[26]) == "Green":
                self.line_edit_1["Project Contribution Margin (%)"].setStyleSheet("background-color: rgb(144,238,144);")
            else:
                self.line_edit_1["Project Contribution Margin (%)"].setStyleSheet("background-color: rgb(255,191,0);")
            if str(row[27]) == "Red":
                self.line_edit_1["Hiring Reason"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[27]) == "Green":
                self.line_edit_1["Hiring Reason"].setStyleSheet("background-color: rgb(144,238,144);")
            else:
                self.line_edit_1["Hiring Reason"].setStyleSheet("background-color: rgb(255,191,0);")
        connection.commit()
        connection.close()

    def Insertintotable(self):  ## Store values added in the Line Edits into different values and insert a new row containing the same into the Hiring Table.
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        text1 = self.line_edits_1["Unit"].text()
        text2 = self.line_edits_1["Sub Unit"].text()
        text3 = self.line_edits_1["Customer Name"].text()
        text4 = self.line_edits_1["Customer Group Name"].text()
        text5 = self.line_edits_1["Project ID"].text()
        text6 = self.line_edits_1["Project Description"].text()
        text7 = str(self.line_edits_1["Project Contribution Margin (%)"].text()) + '%'
        text8 = self.line_edits_1["Contract Type"].text()
        text9 = self.doj.date().toString("yyyy-MM-dd")
        text10 = self.woend.date().toString("yyyy-MM-dd")
        text11 = self.line_edits_1["Subcon Role"].text()
        text12 = self.line_edits_1["Subcon Band"].text()
        text13 = self.line_edits_1["Subcon Experience"].text()
        text14 = self.line_edits_1["City"].text()
        text15 = self.line_edits_1["Country"].text()
        text16 = self.hiring_reason.currentText()
        text17 = self.line_edits_1["Skill Family"].text()
        text18 = self.line_edits_1["Skill Type"].text()
        text19 = self.line_edits_1["Skill (Primary)"].text()
        text20 = self.line_edits_1["Skill (Secondary)"].text()
        text21 = self.line_edits_2["Vendor Rate (per hour USD)"].text()
        text22 = self.line_edits_2["Customer Rate Margin"].text()
        text23 = str(self.line_edits_2["Margin"].text())
        ## Calculate Cumulative RAG on the basis of values of Margin RAG, Project ID RAG and Subcon RAG
        if self.margin_rag == 'Red' or self.project_rag == 'Red' or self.subcon_rag == 'Red':
            self.Cummulative = "Red"
        else:
            if self.margin_rag == 'Amber' or self.project_rag == 'Amber' or self.subcon_rag == 'Amber':
                self.Cummulative = "Amber"
            else:
                self.Cummulative = "Green"
        cur.execute('insert into Hiring (Transaction_Date, Unit, Sub_Unit,Customer_Name, Customer_Group_Name, Project_ID, Project_Desc,Project_Contribution_Margin, Contract_Type, DOJ,WO_End_Date,Subcon_Role,Subcon_Band,Subcon_Exp,City, Country, Hiring_Reason,Skill_Family, Skill_Type, Skill_Primary, Skill_Secondary,Vendor_Rate, Customer_Rate,Margin,Margin_RAG,Project_RAG,Subcon_RAG,Cummulative_RAG, Decision_RMG, Request_Status, Request_Pending_With, RMG_ID) values (datetime("now"), ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"Requested","Pending","SBU Head",?)',(text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,self.margin_rag,self.project_rag,self.subcon_rag,self.Cummulative,self.name_RMG,))
        connection.commit()
        connection.close()
        self.line_edits_1["Unit"].setText("")
        self.line_edits_1["Sub Unit"].setText("")
        self.line_edits_1["Customer Name"].setText("")
        self.line_edits_1["Customer Group Name"].setText("")
        self.line_edits_1["Project ID"].setText("")
        self.line_edits_1["Project Description"].setText("")
        self.line_edits_1["Project Contribution Margin (%)"].setText("")
        self.line_edits_1["Contract Type"].setText("")
        self.doj.date().toString("yyyy-MM-dd")
        self.woend.date().toString("yyyy-MM-dd")
        self.line_edits_1["Subcon Role"].setText("")
        self.line_edits_1["Subcon Band"].setText("")
        self.line_edits_1["Subcon Experience"].setText("")
        self.line_edits_1["City"].setText("")
        self.line_edits_1["Country"].setText("")
        self.line_edits_1["Skill Family"].setText("")
        self.line_edits_1["Skill Type"].setText("")
        self.line_edits_1["Skill (Primary)"].setText("")
        self.line_edits_1["Skill (Secondary)"].setText("")
        self.line_edits_2["Vendor Rate (per hour USD)"].setText("")
        self.line_edits_2["Customer Rate Margin"].setText("")
        self.line_edits_2["Margin"].setText("")
        self.line_edits_2['Margin'].setStyleSheet("background-color: rgb(255,255,255);")
        self.line_edits_1['Project Contribution Margin (%)'].setStyleSheet("background-color: rgb(255,255,255);")
        self.stackedWidget.setCurrentIndex(0)  ## Move to page 1
      
    def GoBack_2(self):   ## Move to page 1
        self.stackedWidget.setCurrentIndex(0)
    
    def request(self):    ## Initiate a new Hiring Request
        self.stackedWidget.setCurrentIndex(2)

    def FPall(self): ## To show all the requests under the Contract Type FP and are under the purview of RMG
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Contract_Type = "FP" and RMG_ID = ?',(self.name_RMG,))
        tablerow=0
        for row in results:
            self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[37])))
            for i in range(1,9):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i+1])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(11):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def TMall(self): ## To show all the requests under the Contract Type T&M and are under the purview of RMG
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Contract_Type = "T&M" and RMG_ID = ?',(self.name_RMG,))
        tablerow=0
        for row in results:
            self.table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[37])))
            for i in range(1,9):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i+1])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(11):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    def GoBack(self):   ## Move to Page 1
        self.loaddata_2()
        self.stackedWidget.setCurrentIndex(0)
    
    def loaddata_2(self):  ## Load data into Dashboards on Page 1
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select count(*) from Hiring where Request_Status = ? and Contract_Type = ? and RMG_ID = ?'
        cur.execute(query1, ("Approved", "FP",self.name_RMG,))
        ApprovedFP, = cur.fetchone()
        self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(str(ApprovedFP)))
        cur.execute(query1, ("Rejected", "FP",self.name_RMG,))
        RejectedFP, = cur.fetchone()
        self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(str(RejectedFP)))
        cur.execute(query1, ("Pending", "FP",self.name_RMG,))
        PendingFP, = cur.fetchone()
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(str(PendingFP)))
        cur.execute(query1, ("Approved", "T&M",self.name_RMG,))
        ApprovedTM, = cur.fetchone()
        self.tableWidget_2.setItem(1,1,QtWidgets.QTableWidgetItem(str(ApprovedTM)))
        cur.execute(query1, ("Rejected", "T&M",self.name_RMG,))
        RejectedTM, = cur.fetchone()
        self.tableWidget_2.setItem(2,1,QtWidgets.QTableWidgetItem(str(RejectedTM)))
        cur.execute(query1, ("Pending", "T&M",self.name_RMG,))
        PendingTM, = cur.fetchone()
        self.tableWidget_2.setItem(0,1,QtWidgets.QTableWidgetItem(str(PendingTM)))

        query2 = 'select count(*) from Hiring where Request_Status = "Pending" and Request_Pending_With = "RMG" and Contract_Type = ? and RMG_ID = ?'
        cur.execute(query2, ("FP",self.name_RMG,))
        R15, = cur.fetchone()
        self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(query2, ("T&M",self.name_RMG,))
        R16, = cur.fetchone()
        self.tableWidget_2.setItem(3,1,QtWidgets.QTableWidgetItem(str(R16)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.summary.setText(_translate("MainWindow", "Summary"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Pending Requests"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Approved Requests"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Rejected Requests"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Requests Sent Back"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "Pending Requests"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "Approved Requests"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainWindow", "Rejected Requests"))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("MainWindow", "Requests Sent Back"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.view1.setText(_translate("MainWindow", "View All Results"))
        self.view2.setText(_translate("MainWindow", "View All Results"))
        self.label.setText(_translate("MainWindow", "Contract Type: FP"))
        self.label_2.setText(_translate("MainWindow", "Contract Type: T&M"))
        self.newrequest.setText(_translate("MainWindow", "Initiate New Hiring Request"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RMG_hiring()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

