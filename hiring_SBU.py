## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 ## Library to import sqlite3, replace this with mysql connector of python

class SBU_hiring(object):
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

        ## Table 1: Contract Type = FP. There are 4 rows:  Approved Requests, Rejected Requests, and Sent back for Query and No Action Yet 
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

        ## Table 1: Contract Type = T&M. There are 4 rows:  Approved Requests, Rejected Requests, and Sent back for Query and No Action Yet
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
        self.view1 = QtWidgets.QPushButton(self.frame_2)   # To see all results of Contract Type FP
        self.view1.setGeometry(QtCore.QRect(260, 230, 279, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.view1.setFont(font)
        self.view1.setObjectName("view1")
        self.view2 = QtWidgets.QPushButton(self.frame_2)  # To see all results of Contract Type T&M
        self.view2.setGeometry(QtCore.QRect(660, 230, 279, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.view2.setFont(font)
        self.view2.setObjectName("view2")
        self.label = QtWidgets.QLabel(self.frame_2)   ## Label to show Contract Type FP
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
        self.label_2 = QtWidgets.QLabel(self.frame_2)  ## Label to show Contract Type T&M
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
        self.loaddata_2()
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stackedWidget.addWidget(self.page1)

        ## Page - 2: Table View ###

        self.page = QtWidgets.QWidget()  
        self.page.setObjectName("page")
        self.Heading = QtWidgets.QLabel(self.page)  ## Label for Heading
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
        # Table #
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
        self.table.setColumnCount(10)  ## Column Count 
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
        self.columnwidth = 174  ## Width of the table columns
        self.Headers = ["Transaction ID","Unit","Sub Unit","Customer Name","Customer Group Name","Project ID","Project Desc","Project Contribution Margin","Contract Type","Request Status"]  ## Add Headers here 
        i = 0
        for names in self.Headers:
            self.table.horizontalHeaderItem(i).setText(names)
            i = i + 1
            
        for i in range(11):
            self.table.setColumnWidth(i,self.columnwidth)
      
        self.stackedWidget.addWidget(self.page)

        ### Page - 3: Form Reviewing###
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
        
        ## Grid to show the details regarding Subcon Basic Profile ##
        ## To remove any info:- 
        ## 1) Remove all the occurences of that info
        ## 2) Change the locations of others to fill its space.
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
            self.line_edit_1[line_Text].setReadOnly(True)
            self.gridLayout_5.addWidget(self.line_edit_1[line_Text], pos[0], pos[1])

        ## Grid to show the Subcon Commercials ##
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

        self.line_edit_2 = {}
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
            self.line_edit_2[line_Text].setReadOnly(True)
            self.gridLayout_6.addWidget(self.line_edit_2[line_Text], pos[0], pos[1])
        self.gridLayout_6.setHorizontalSpacing(20)

        ## Grid Which provides Remarks entering, Options to approve, reject, ask query and any Reason SBU wants to give ##
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
        self.combobox_1.addItems(["Approve Request","Conditional Approval","Send Back for Query", "Reject Request"])
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

        ## Submit button ##
        self.submit = QtWidgets.QPushButton(self.frame_4)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.submit.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.submit.setFixedHeight(40)
        self.submit.setFixedWidth(200)
        self.submit.setGeometry(QtCore.QRect(20, 895, 150, 40))

        ## Go back button ##
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
        self.table.cellClicked.connect(self.TakeAction)
        self.submit.clicked.connect(self.Insert1)
        self.tableWidget.cellClicked.connect(self.showFP)
        self.tableWidget_2.cellClicked.connect(self.showTM)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def showhistory(self):   ## Function to Show Transaction History, gets activated on clicking the Show Remarks Button ##
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('select count(*) from Hiring where Transaction_ID = ?',(self.ID,))
        number, = cur.fetchone()
        if number == 0:
            self.transaction1_decision_RMG.setText("None")
            self.transaction1_remarks_RMG.setText("None")
            self.transaction1_date_RMG.setText("None")
            self.transaction1_decision_SBU.setText("None")
            self.transaction1_remarks_SBU.setText("None")
            self.transaction1_date_SBU.setText("None")
            self.transaction1_decision_EHC.setText("None")
            self.transaction1_remarks_EHC.setText("None")
            self.transaction1_date_EHC.setText("None")
        else:
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
    
    def Insert1(self):    ## On clicking the Submit Button 
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        text1 = self.combobox_1.currentText() ## Check for Decision Type
        text2 = self.text_edit1.toPlainText() ## Store the remarks
        if self.Cummulative != "Red":    ## If the cumulative RAG is Green or Amber, then Approval by SBU head means final approval
            if text1 == "Approve Request" and self.Cummulative != "Red":
                cur.execute('update Hiring set Decision_SBU = "Approve Request", Request_Status = "Approved", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            elif text1 == "Conditional Approval" and self.Cummulative != "Red":
                cur.execute('update Hiring set Decision_SBU = "Conditional Approval", Request_Status = "Approved", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            elif text1 == "Send Back for Query":
                cur.execute('update Hiring set Decision_SBU = "Send Back for Query", Request_Status = "Pending", Request_Pending_With = "RMG", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            else:
                cur.execute('update Hiring set Decision_SBU = "Reject Request", Request_Status = "Rejected", Request_Pending_With = "", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))

        else:    ## If the cumulative RAG is red, then approval of EHC will be required
            if text1 == "Approve Request":
                cur.execute('update Hiring set Decision_SBU = "Approve Request", Request_Status = "Pending", Request_Pending_With = "EHC", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            elif text1 == "Conditional Approval":
                cur.execute('update Hiring set Decision_SBU = "Conditional Approval", Request_Status = "Pending", Request_Pending_With = "EHC", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            elif text1 == "Send Back for Query":
                cur.execute('update Hiring set Decision_SBU = "Send Back for Query", Request_Status = "Pending", Request_Pending_With = "RMG", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
            else:
                cur.execute('update Hiring set Decision_SBU = "Reject Request", Request_Status = "Rejected", Request_Pending_With = "", Transaction_Date_SBU = datetime("now"), Remarks_SBU = ? where Transaction_ID = ?', (text2,self.ID,))
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
        self.loaddata_2()
        self.stackedWidget.setCurrentIndex(0)

    def GoBack_3(self):
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

    def TakeAction(self, row):   ## On clicking on any cell of a row
        self.ID = self.table.item(row,0).text()   ## Store the First value of the row, which is the Transaction ID of the request
        self.ID = str(self.ID)   
        self.loaddata_1()   ## Load the data into Page 3
        self.stackedWidget.setCurrentIndex(2)  ## Move to page 3
    
    def loaddata_1(self): ## Loading data to page 3
        connection = sqlite3.connect('EY')## connect to database
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Transaction_ID = ?', (self.ID,))## Query all the information for the given Transaction ID
        
        for row in results:
            self.line_edit_1["Unit"].setText(str(row[2]))## Add the relevant info to the relevant column
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
            self.Cummulative = str(row[28])
            ## Give the Background color to the margin and Tenure Line Edit to highlight their importance
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
    
    def showFP(self,row1):   ## For Dashboard containing info about the Contract Type - FP, clicking on a cell in row, different queries shall be executed
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select * from Hiring where Contract_Type = "FP" and Decision_SBU = ? and Unit = ?'
        if row1 == 1:   ## Query to show approved and conditionally approved requests by SBU Head
            results = cur.execute('select * from Hiring where Contract_Type = "FP" and (Decision_SBU = "Approve Request" or Decision_SBU = "Conditional Approval") and Unit = ?',(self.name_SBU,))
        elif row1 == 2:  ## Query to show rejected requests
            results = cur.execute(query1,("Reject Request",self.name_SBU,))
        elif row1 == 3:     ## Query to show sent back requests
            results = cur.execute(query1,("Send Back for Query",self.name_SBU,))
        else:       ## Query to show unreviewed requests
            results = cur.execute('select * from Hiring where Decision_RMG = "Requested" and Decision_SBU IS NULL and Contract_Type = "FP" and Unit = ?',(self.name_SBU,))
        tablerow=0
        for row in results:## on execution of queries, add the relevant info into the table on Page 2
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
        self.stackedWidget.setCurrentIndex(1)## Move to page 2
    
    def showTM(self,row1):   ## For Dashboard containing info about the Contract Type - T&M, clicking on a cell in row, different queries shall be executed
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select * from Hiring where Contract_Type = "T&M" and Decision_SBU = ? and Unit = ?'
        if row1 == 1:
            results = cur.execute('select * from Hiring where Contract_Type = "T&M" and (Decision_SBU = "Approve Request" or Decision_SBU = "Conditional Approval") and Unit = ?',(self.name_SBU,))
        elif row1 == 2:
            results = cur.execute(query1,("Reject Request",self.name_SBU,))
        elif row1 == 3:
            results = cur.execute(query1,("Send Back for Query",self.name_SBU,))
        else:
            results = cur.execute('select * from Hiring where Decision_RMG = "Requested" and Decision_SBU IS NULL and Contract_Type = "T&M" and Unit = ?',(self.name_SBU,))
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

    def FPall(self):    ## To show all the requests under the Contract Type FP and are under the purview of SBU
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Contract_Type = "FP" and Decision_RMG = "Requested" and Unit = ?',(self.name_SBU,))
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
    
    def TMall(self):     ## To show all the requests under the Contract Type T&M and are under the purview of SBU Head
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        results = cur.execute('SELECT * FROM Hiring where Contract_Type = "T&M" and Decision_RMG = "Requested" and Unit = ?',(self.name_SBU,))
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

    def GoBack(self):          ## Move to Page 1
        self.stackedWidget.setCurrentIndex(0)
    
    def loaddata_2(self):       ## Load data into Dashboards on Page 1
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        query1 = 'select count(*) from Hiring where Decision_SBU = ? and Contract_Type = ? and Unit = ?'
        cur.execute(query1, ("Approve Request", "FP",self.name_SBU,))
        ApprovedFP, = cur.fetchone()
        cur.execute(query1, ("Conditional Approval", "FP",self.name_SBU,))
        conditionFP, = cur.fetchone()
        self.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(str(ApprovedFP + conditionFP)))
        cur.execute(query1, ("Reject Request", "FP",self.name_SBU,))
        RejectedFP, = cur.fetchone()
        self.tableWidget.setItem(2,1,QtWidgets.QTableWidgetItem(str(RejectedFP)))
        cur.execute(query1, ("Send Back for Query", "FP",self.name_SBU,))
        PendingFP, = cur.fetchone()
        self.tableWidget.setItem(3,1,QtWidgets.QTableWidgetItem(str(PendingFP)))
        cur.execute(query1, ("Approve Request", "T&M",self.name_SBU,))
        ApprovedTM, = cur.fetchone()
        cur.execute(query1, ("Conditional Approval", "T&M",self.name_SBU,))
        conditionTM, = cur.fetchone()
        self.tableWidget_2.setItem(1,1,QtWidgets.QTableWidgetItem(str(ApprovedTM + conditionTM)))
        cur.execute(query1, ("Reject Request", "T&M",self.name_SBU,))
        RejectedTM, = cur.fetchone()
        self.tableWidget_2.setItem(2,1,QtWidgets.QTableWidgetItem(str(RejectedTM)))
        cur.execute(query1, ("Send Back for Query", "T&M",self.name_SBU,))
        PendingTM, = cur.fetchone()
        self.tableWidget_2.setItem(3,1,QtWidgets.QTableWidgetItem(str(PendingTM)))

        query2 = 'select count(*) from Hiring where Decision_RMG = "Requested" and Decision_SBU IS NULL and Contract_Type = ? and Unit = ?'
        cur.execute(query2, ("FP",self.name_SBU,))
        R15, = cur.fetchone()
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(query2, ("T&M",self.name_SBU,))
        R16, = cur.fetchone()
        self.tableWidget_2.setItem(0,1,QtWidgets.QTableWidgetItem(str(R16)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.summary.setText(_translate("MainWindow", "Summary"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Requests Not Attended"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Approved Requests"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Rejected Requests"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Sent Back for Query"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "Requests Not Attended"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "Approved Requests"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainWindow", "Rejected Requests"))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("MainWindow", "Sent Back for Query"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.view1.setText(_translate("MainWindow", "View All Results"))
        self.view2.setText(_translate("MainWindow", "View All Results"))
        self.label.setText(_translate("MainWindow", "Contract Type: FP"))
        self.label_2.setText(_translate("MainWindow", "Contract Type: T&M"))
        #self.newrequest.setText(_translate("MainWindow", "Initiate New Hiring Request"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SBU_hiring()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

