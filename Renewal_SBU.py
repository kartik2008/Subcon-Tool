## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 ## Library to import sqlite3, replace this with mysql connector of python

class SBU_Renewal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(0,0,0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        ## Page -1: Dashboard Page ## 
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.centralwidget.setObjectName("centralwidget")

        ## Biggest Frame ##
        self.frame = QtWidgets.QFrame(self.page1)
        self.frame.setGeometry(QtCore.QRect(20, 40, 1821, 1001))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        ## Dashboard - 1: Action Summary based on Contract Type and WO Expiry Date ##
        ## There are 6 Tables in this Dashboard ## 
        self.frame_1 = QtWidgets.QFrame(self.frame)
        self.frame_1.setGeometry(QtCore.QRect(20, 170, 1781, 281))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")

        ## Contract Type = FP & WO Expiry Date < 30 days
        self.tableWidget1 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget1.setGeometry(QtCore.QRect(60, 110, 202, 152))
        self.tableWidget1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget1.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget1.setRowCount(5)
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
        self.FP1 = QtWidgets.QLabel(self.frame_1)
        self.FP1.setGeometry(QtCore.QRect(60, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FP1.setFont(font)
        self.FP1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.FP1.setFrameShape(QtWidgets.QFrame.Box)
        self.FP1.setAlignment(QtCore.Qt.AlignCenter)
        self.FP1.setObjectName("FP1")

        ## Contract Type = T&M & WO Expiry Date < 30 days
        self.tableWidget2 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget2.setGeometry(QtCore.QRect(360, 110, 202, 152))
        self.tableWidget2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget2.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget2.setRowCount(5)
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
        self.TM1 = QtWidgets.QLabel(self.frame_1)
        self.TM1.setGeometry(QtCore.QRect(360, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TM1.setFont(font)
        self.TM1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.TM1.setFrameShape(QtWidgets.QFrame.Box)
        self.TM1.setAlignment(QtCore.Qt.AlignCenter)
        self.TM1.setObjectName("TM1")
        
        ## Contract Type = FP and T&M and WO Expiry Date < 30 days
        self.tableWidget3 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget3.setGeometry(QtCore.QRect(660, 110, 202, 152))
        self.tableWidget3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget3.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget3.setRowCount(5)
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
        self.Total1 = QtWidgets.QLabel(self.frame_1)
        self.Total1.setGeometry(QtCore.QRect(660, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Total1.setFont(font)
        self.Total1.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Total1.setFrameShape(QtWidgets.QFrame.Box)
        self.Total1.setAlignment(QtCore.Qt.AlignCenter)
        self.Total1.setObjectName("Total1")
        self.summary = QtWidgets.QLabel(self.frame_1)
        self.summary.setGeometry(QtCore.QRect(0, 0, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.summary.setFont(font)
        self.summary.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.summary.setFrameShape(QtWidgets.QFrame.Box)
        self.summary.setAlignment(QtCore.Qt.AlignCenter)
        self.summary.setObjectName("summary")
        self.FP2 = QtWidgets.QLabel(self.frame_1)
        self.FP2.setGeometry(QtCore.QRect(980, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FP2.setFont(font)
        self.FP2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.FP2.setFrameShape(QtWidgets.QFrame.Box)
        self.FP2.setAlignment(QtCore.Qt.AlignCenter)
        self.FP2.setObjectName("FP2")
        self.TM2 = QtWidgets.QLabel(self.frame_1)
        self.TM2.setGeometry(QtCore.QRect(1270, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TM2.setFont(font)
        self.TM2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.TM2.setFrameShape(QtWidgets.QFrame.Box)
        self.TM2.setAlignment(QtCore.Qt.AlignCenter)
        self.TM2.setObjectName("TM2")
        self.Total2 = QtWidgets.QLabel(self.frame_1)
        self.Total2.setGeometry(QtCore.QRect(1550, 70, 202, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Total2.setFont(font)
        self.Total2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.Total2.setFrameShape(QtWidgets.QFrame.Box)
        self.Total2.setAlignment(QtCore.Qt.AlignCenter)
        self.Total2.setObjectName("Total2")

        ## Contract Type = FP &  30 days < WO Expiry Date < 60 days
        self.tableWidget4 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget4.setGeometry(QtCore.QRect(980, 110, 202, 152))
        self.tableWidget4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget4.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget4.setRowCount(5)
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

        ## Contract Type = T&M &  30 days < WO Expiry Date < 60 days
        self.tableWidget5 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget5.setGeometry(QtCore.QRect(1270, 110, 202, 152))
        self.tableWidget5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget5.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget5.setRowCount(5)
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

        ## Contract Type = FP and T&M and  30 days < WO Expiry Date < 60 days
        self.tableWidget6 = QtWidgets.QTableWidget(self.frame_1)
        self.tableWidget6.setGeometry(QtCore.QRect(1550, 110, 202, 152))
        self.tableWidget6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget6.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.tableWidget6.setRowCount(5)
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
        
        ## Customer Analysis Dashboard ## 
        
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(130, 540, 1491, 261))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 101, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Dashboard-2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
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
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setColumnWidth(0, 300)
        self.tableWidget_2.setColumnWidth(1, 300)
        self.tableWidget_2.setColumnWidth(2, 250)
        self.tableWidget_2.setColumnWidth(3, 250)
        self.tableWidget_2.setColumnWidth(4, 248)
        self.tableWidget_2.setStyleSheet("QHeaderView::section { color: rgb(0, 0,0);}")
        self.tableWidget_2.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.headings = ["Customer Name","Contract Type","Subcon #", "Margin","Tenure"]
        j = 0
        for content in self.headings:
            self.tableWidget_2.horizontalHeaderItem(j).setText(content)
            j+=1
        self.loaddata_2()
        self.stackedWidget.addWidget(self.page1)
        
        ### Page - 2: Details ######
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
        ## Table ##
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(50, 300, 1750, 500))
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("QHeaderView::section{background-color: rgb(255, 191, 0); color: rgb(0, 0,0);} QTableWidget {gridline-color: rgb(0, 0, 0);}")
        self.table.setAlternatingRowColors(True)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.table.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setRowCount(15)
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
        self.stackedWidget.addWidget(self.page)

        ### Page - 3: Take Action #####

        ### Page - 3: Action Screen #####
        ## Refer to PM_Renewal File to read the comments related to UI of Page - 3. All the features are almost the same.
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2") 
        
        ## Main Frame ##
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 40, 1770, 970))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        ## Grid containing the Header Subcon Profile ## 
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.frame_3)
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
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_3)
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
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
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
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
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
        

        ## Provides space to fill Remarks, Decision, and Actionable Date
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 670, 1171, 120))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label4 = QtWidgets.QLabel()
        self.label5 = QtWidgets.QLabel()
        self.label6 = QtWidgets.QLabel()
        self.label4.setFixedWidth(80)
        self.label6.setFixedWidth(120)
        self.label6.setWordWrap(True)
        self.label5.setFixedWidth(80)
        self.label4.setFont(self.font)
        self.label5.setFont(self.font)
        self.label6.setFont(self.font)
        self.text_edit1 = QtWidgets.QTextEdit()
        self.text_edit1.setFixedHeight(40)
        self.combobox_1 = QtWidgets.QComboBox()
        self.combobox_1.addItems(["Approve","Query", "Reject", "Conditional Approval"])
        self.Date = QtWidgets.QDateEdit()
        self.Date.setFixedHeight(40)
        self.text_edit1.setFixedWidth(250)
        self.combobox_1.setFixedWidth(150)
        self.combobox_1.setFixedHeight(40)
        self.Date.setFixedWidth(250)
        self.label4.setWordWrap(True)
        self.label5.setWordWrap(True)
        self.label6.setWordWrap(True)
        self.label4.setText("Remarks")
        self.label5.setText("Decision")
        self.label6.setText("Extension Required Till")
        self.gridLayout_5.addWidget(self.label4,0,0)
        self.gridLayout_5.addWidget(self.label5,0,2)
        self.gridLayout_5.addWidget(self.label6,0,4)
        self.gridLayout_5.addWidget(self.text_edit1,0,1)
        self.gridLayout_5.addWidget(self.combobox_1,0,3)
        self.gridLayout_5.addWidget(self.Date,0,5)
        self.lowestdate = QtCore.QDate.currentDate()  ## Person has to extend till a date greater than today's date
        self.highestdate = QtCore.QDate(2075,1,1)  ## This is highest date 
        self.Date.setDateRange(self.lowestdate,self.highestdate)  ## Setting the date range


        ## Grid to give 2 options to the PM, Project Details and Other Details
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.frame_3)
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
        self.counter = 0 ## No. of times Project Details button has been clicked
        self.otherdetails.clicked.connect(self.showother)
        self.counter_1 = 0  ## No. of times Other Details button has been clicked

        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName("gridLayout_6")

        ## Grid to show remarks history button ##
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.frame_3)
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
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
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
        self.transaction1_date_PM.setObjectName("transaction1_date_PM")
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
        self.transaction2 = QtWidgets.QLabel(self.tabWidget)
        self.transaction2.setGeometry(QtCore.QRect(20, 245, 181, 31))
        self.transaction2.setFont(font)
        self.transaction2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.transaction2.setWordWrap(True)
        self.transaction2.setObjectName("transaction2")
        
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
        

        self.submit = QtWidgets.QPushButton(self.frame_3)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.submit.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.submit.setFixedHeight(40)
        self.submit.setFixedWidth(200)
        self.submit.setGeometry(QtCore.QRect(20, 895, 150, 40))
        self.goback_2 = QtWidgets.QPushButton(self.frame_3)
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
        
        self.stackedWidget.setCurrentIndex(0)
        self.tableWidget1.cellClicked.connect(self.ShowFPLess)
        self.tableWidget2.cellClicked.connect(self.ShowTMLess)
        self.tableWidget3.cellClicked.connect(self.ShowTotalLess)
        self.tableWidget4.cellClicked.connect(self.ShowFPMore)
        self.tableWidget5.cellClicked.connect(self.ShowTMMore)
        self.tableWidget6.cellClicked.connect(self.ShowTotalMore)
        self.table.cellClicked.connect(self.TakeAction)
        self.submit.clicked.connect(self.Insert1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def GoBack_2(self):   ## Go to Page 2
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
                "W2 Vendor": (0,3), "Location": (1,1),"Contract Type": (1,3),  "Extension Reason":(2,1),
            }

        self.lable_10 = {}
        lable_10 = {
                "Customer Group Name": (0,0),	
                "W2 Vendor": (0,2), "Location": (1,0),"Contract Type": (1,2), "Extension Reason":(2,0),
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
            #self.line_edit_10["Hiring Reason"].setText(str(row[28]))
            if str(row[30]) == "Red":
                self.line_edit_10["Extension Reason"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[30]) == "Amber":
                self.line_edit_10["Extension Reason"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edit_10["Extension Reason"].setStyleSheet("background-color: rgb(144,238,144);")
        result = cur.execute('SELECT * from Decisions where Subcon_ID = ? order by Transaction_Date Desc LIMIT 1', (self.ID,))
        for row in result:
            self.line_edit_10["Extension Reason"].setText(str(row[6]))
        connection.commit()
        connection.close()
    
    def Insert1(self):   ## On clicking the Submit button, the function inserts/update the info in the Decisions Table.
        self.text_1 = self.text_edit1.toPlainText() # Captures remarks
        self.text_2 = self.combobox_1.currentText() # Captures Decision
        self.text_3 = self.Date.date().toString("yyyy-MM-dd")  ## Captures Date of Action
        connection = sqlite3.connect("EY")
        cur = connection.cursor()
        
        if self.Cummulative == "Amber":  # If Cumulative RAG = Amber, Approval or conditional approval implies Closing and Approving of Request
            if self.text_2 == "Approve":
                cur.execute('update Decisions set  Decision_SBU = "Approve", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Status = "Approved", Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,self.ID,))
            elif self.text_2 == "Conditional Approval":
                cur.execute('update Decisions set  Decision_SBU = "Conditional Approval", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Status = "Approved", Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,self.ID,))
            elif self.text_2 == "Query":
                cur.execute('update Decisions set Decision_SBU = "Query", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Pending_With = ?, Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,"PGM",self.ID,))
            else:
                cur.execute('update Decisions set Decision_SBU = "Reject", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Status = "Rejected", Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,self.ID,))
        else:   # If Cumulative RAG = Red, Approval or conditional approval implies Request is pending with EHC approver.
            if self.text_2 == "Approve":
                cur.execute('update Decisions set Decision_SBU = "Approve", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Pending_With = ?, Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,"EHC",self.ID,))
            elif self.text_2 == "Conditional Approval":
                cur.execute('update Decisions set Decision_SBU = "Conditional Approval", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Pending_With = ?, Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,"EHC",self.ID,))
            elif self.text_2 == "Query":
                cur.execute('update Decisions set Decision_SBU = "Query", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Pending_With = ?, Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,"PGM",self.ID,))
            else:
                cur.execute('update Decisions set Decision_SBU = "Reject", SBU_Remarks = ?, SBU_Extension_Tenure = ?, Request_Status = "Rejected", Transaction_Date_SBU = datetime("now") where Subcon_ID = ? and Request_Status = "Pending"', (self.text_1,self.text_3,self.ID,))
        
        connection.commit()
        connection.close()
        self.text_edit1.setText("")
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

    def TakeAction(self, row):   # On clicking a cell of the Table on Page 2
        self.ID = self.table.item(row,2).text()  ## Stores the Subcon ID of the selected person
        self.ID = str(self.ID)   
        self.loaddata_1()   ## Load data into Page 3
        self.stackedWidget.setCurrentIndex(2) ## Move to page 3
    
    def loaddata_1(self):   ## Loading data into Page 3
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        cur.execute('SELECT (Julianday("now") - Julianday("Date_of_Joining")) FROM Subcon_Info where Subcon_ID = ?', (self.ID,))
        tenure, = cur.fetchone()
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

        results = cur.execute('SELECT * FROM Subcon_Info where Subcon_ID = ?', (self.ID,)) ## Query data for the selected subcon
        
        for row in results:   
            self.line_edits_1["Subcon Name"].setText(str(row[3]))  ## Add info to the relevant line edits
            self.line_edits_1["Date of Joining"].setText(str(row[4]))
            self.line_edits_1["Customer Name"].setText(str(row[6]))
            #self.line_edits_1["Contract Type"].setText(str(row[10]))
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
            #self.line_edits_1["Location"].setText(str(row[23]))
            self.line_edits_2["Vendor Rate (per hour USD)"].setText(str(row[24]))
            self.line_edits_2["Customer Rate Margin"].setText(str(row[25]))
            self.line_edits_2["Margin"].setText(str(row[26]))
            self.line_edits_3["Margin RAG"].setText(str(row[27]))
            self.line_edits_3["Tenure RAG"].setText(self.tenure_rag)
            self.line_edits_3["Project ID RAG"].setText(str(row[29]))
            self.line_edits_3["Subcon RAG"].setText(str(row[30]))
            self.Cummulative = str(row[31])
            # Highlight the Margin and Tenure based on their RAG
            if str(row[27]) == "Red":
                self.line_edits_2["Margin"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[27]) == "Amber":
                self.line_edits_2["Margin"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edits_2["Margin"].setStyleSheet("background-color: rgb(144,238,144);")
            if str(row[28]) == "Red":
                self.line_edits_1["Tenure"].setStyleSheet("background-color: #f70d1a;")
            elif str(row[28]) == "Amber":
                self.line_edits_1["Tenure"].setStyleSheet("background-color: rgb(255,191,0);")
            else:
                self.line_edits_1["Tenure"].setStyleSheet("background-color: rgb(144,238,144);")
        connection.commit()
        connection.close()
    
    def GoBack(self): ## Move to Page 1
        self.stackedWidget.setCurrentIndex(0)
    
    def ShowFPLess(self, row1):  ## Show the info of all the Subcons under the Category, Contract Type = FP and WO Expiry Date < 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_SBU = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID AND Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?'
        
        if row1 == 0:   # All the approved and conditionally approved requests
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID AND Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1:  # All the rejected requests
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2:  # All the requests sent back for query
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3:  # All the unattended requests under SBU Head
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = "FP" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:   # all the requests under SBU Head
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and Subcon_Info.Contract_Type = "FP" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        tablerow=0
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    ## The logics for all the tables shall remain the same. The Queries will change acccording to the Contract Type and WO Expiry Date
    
    def ShowTMLess(self, row1): ## Show the info of all the Subcons under the Category, Contract Type = T&M and WO Expiry Date < 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_SBU = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?'
        tablerow=0
        if row1 == 0:
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1:
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2:
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3:
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = "T&M" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and Subcon_Info.Contract_Type = "T&M" and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTotalLess(self, row1):  ## Show the info of all the Subcons under the Category, WO Expiry Date < 30 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Decisions.Decision_SBU = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?'
        tablerow=0
        if row1 == 0:
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1:
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2:
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3:
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowFPMore(self, row1): ## Show the info of all the Subcons under the Category, Contract Type = FP and 30 days < WO Expiry Date < 60 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND Decisions.Decision_SBU = ? And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?'
        tablerow=0
        if row1 == 0:  ## All the Approved and Conditionally Approved Requests
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "FP" AND (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1: ## All the Rejected Requests
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2: ## All the Requests sent back for Query
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3: ## All the Requests which are not attended by SBU Head
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = "FP" and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:  ## All the Requests under SBU Head
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and Subcon_Info.Contract_Type = "FP" and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTMMore(self, row1): ## Show the info of all the Subcons under the Category, Contract Type = T&M and 30 days < WO Expiry Date < 60 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND Decisions.Decision_SBU = ? And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ? '
        tablerow=0
        if row1 == 0:
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where Subcon_Info.Contract_Type = "T&M" AND (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green"  and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1:
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2:
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3:
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = "T&M" and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and Subcon_Info.Contract_Type = "T&M" and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)
    
    def ShowTotalMore(self, row1):   ## Show the info of all the Subcons under the Category, 30 days < WO Expiry Date < 60 days
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM Subcon_Info, Decisions where Decisions.Decision_SBU = ? And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green"  and Subcon_Info.Unit = ?'
        tablerow=0
        if row1 == 0:
            results = cur.execute('SELECT * FROM Subcon_Info, Decisions where (Decisions.Decision_SBU = "Approve" or Decisions.Decision_SBU = "Conditional Approval") And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green"  and Subcon_Info.Unit = ?',(self.name_SBU,))
        elif row1 == 1:
            results = cur.execute(sqlstr,("Reject",self.name_SBU,))
        elif row1 == 2:
            results = cur.execute(sqlstr,("Query",self.name_SBU,))
        elif row1 == 3:
            results = cur.execute('select * from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        else:
            results = cur.execute('select * from Subcon_Info, Decisions where (Decisions.Decision_PGM = "Approve" or Decisions.Decision_PGM = "Conditional Approval") and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?',(self.name_SBU,))
        for row in results:
            for i in range(0,32):
                self.table.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(row[i])))
            tablerow+=1
        for i in range(tablerow,15):
            for j in range(32):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            i+=1 
        connection.commit()
        connection.close()
        self.stackedWidget.setCurrentIndex(1)

    def loaddata_2(self):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        ## Adding values to Dashboards on Page 1 ##

        ## For Dashboard 1 - Adding values based on the Contract Type and WO Expiry date, and requests in the purview of SBU Head ##
        sqlstr = 'select count(*) from Decisions, Subcon_Info where Decisions.Decision_SBU = ? AND Subcon_Info.Contract_Type = ? And ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60) AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Cummulative_RAG != "Green" and Subcon_Info.Unit = ?'
        sqlstr1 = 'select count(*) from Decisions, Subcon_Info where Decisions.Decision_SBU = ? AND Subcon_Info.Contract_Type = ? And (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  AND Decisions.Subcon_ID = Subcon_Info.Subcon_ID  and Subcon_Info.Cummulative_RAG != "Green"and Subcon_Info.Unit = ?'
        
        cur.execute(sqlstr1, ("Approve", "FP", self.name_SBU,))
        R1, = cur.fetchone()  ## Approved Requests of FP and Expiry date < 30
        cur.execute(sqlstr1, ("Conditional Approval", "FP", self.name_SBU,))
        R_1, = cur.fetchone()  ## Conditionally Approved Requests of FP and Expiry date < 30
        self.tableWidget1.setItem(0,1,QtWidgets.QTableWidgetItem(str(R1+R_1)))
        cur.execute(sqlstr1, ("Approve", "T&M",self.name_SBU,)) ## Approved Requests of T&M and Expiry date < 30
        R_2, = cur.fetchone()  
        cur.execute(sqlstr1, ("Conditional Approval", "T&M",self.name_SBU,)) ## Conditionally Approved Requests of T&M and Expiry date < 30
        R2, = cur.fetchone()
        self.tableWidget2.setItem(0,1,QtWidgets.QTableWidgetItem(str(R2 + R_2)))
        self.tableWidget3.setItem(0,1,QtWidgets.QTableWidgetItem(str(R1 + R2 + R_1 + R_2)))


        cur.execute(sqlstr, ("Approve", "FP",self.name_SBU,)) ## Approved Requests of FP and 30 < Expiry date < 60
        R3, = cur.fetchone()
        cur.execute(sqlstr, ("Conditional Approval", "FP",self.name_SBU,)) ## Conditionally Approved Requests of FP and 30 < Expiry date < 60
        R_3, = cur.fetchone()
        self.tableWidget4.setItem(0,1,QtWidgets.QTableWidgetItem(str(R3 + R_3)))
        cur.execute(sqlstr, ("Approve", "T&M",self.name_SBU,))   ## Approved Requests of T&M and 30 < Expiry date < 60
        R4, = cur.fetchone()
        cur.execute(sqlstr, ("Conditional Approval", "T&M",self.name_SBU,)) ## Conditionally Approved Requests of T&M and 30 < Expiry date < 60
        R_4, = cur.fetchone()
        self.tableWidget5.setItem(0,1,QtWidgets.QTableWidgetItem(str(R4 + R_4)))
        self.tableWidget6.setItem(0,1,QtWidgets.QTableWidgetItem(str(R4 + R3 + R_4 + R_3)))

        cur.execute(sqlstr1, ("Reject", "FP",self.name_SBU,)) ## Rejected Requests of FP and Expiry date < 30
        R5, = cur.fetchone()
        self.tableWidget1.setItem(1,1,QtWidgets.QTableWidgetItem(str(R5)))
        cur.execute(sqlstr1, ("Reject", "T&M",self.name_SBU,)) ## Rejected Requests of T&M and Expiry date < 30
        R6, = cur.fetchone()
        self.tableWidget2.setItem(1,1,QtWidgets.QTableWidgetItem(str(R6)))
        self.tableWidget3.setItem(1,1,QtWidgets.QTableWidgetItem(str(R5 + R6)))

        cur.execute(sqlstr, ("Reject", "FP",self.name_SBU,)) ## Rejected Requests of FP and 30 < Expiry date < 60
        R7, = cur.fetchone()
        self.tableWidget4.setItem(1,1,QtWidgets.QTableWidgetItem(str(R7)))
        cur.execute(sqlstr1, ("Reject", "T&M",self.name_SBU,)) ## Rejected Requests of T&M and 30 < Expiry date < 60
        R8, = cur.fetchone()
        self.tableWidget5.setItem(1,1,QtWidgets.QTableWidgetItem(str(R8)))
        self.tableWidget6.setItem(1,1,QtWidgets.QTableWidgetItem(str(R7 + R8)))

        cur.execute(sqlstr1, ("Query", "FP",self.name_SBU,))   ## Sent Back for Query of FP and Expiry date < 30
        R9, = cur.fetchone()
        self.tableWidget1.setItem(2,1,QtWidgets.QTableWidgetItem(str(R9)))
        cur.execute(sqlstr1, ("Query", "T&M",self.name_SBU,))  ## Sent Back for Query of T&M and Expiry date < 30
        R10, = cur.fetchone()
        self.tableWidget2.setItem(2,1,QtWidgets.QTableWidgetItem(str(R10)))
        self.tableWidget3.setItem(2,1,QtWidgets.QTableWidgetItem(str(R9 + R10)))
        
        cur.execute(sqlstr, ("Query", "FP",self.name_SBU,)) ## Sent Back for Query of FP and 30 < Expiry date < 60
        R11, = cur.fetchone()
        self.tableWidget4.setItem(2,1,QtWidgets.QTableWidgetItem(str(R11)))
        cur.execute(sqlstr, ("Query", "T&M",self.name_SBU,)) ## Sent Back for Query of T&M and 30 < Expiry date < 60
        R12, = cur.fetchone()
        self.tableWidget5.setItem(2,1,QtWidgets.QTableWidgetItem(str(R12)))
        self.tableWidget6.setItem(2,1,QtWidgets.QTableWidgetItem(str(R11 + R12)))

        ## Logic: Cumulative RAG is Red or Amber, Decision by PGM is Approve, Request Status is Pending, and There is no value in Decision_SBU
        que1 = 'select count(*) from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = ? and (Julianday(Subcon_Info.Expected_End_Date) - Julianday("now"))  between 0 and 30  and Subcon_Info.Cummulative_RAG != "Green" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID and Subcon_Info.Unit = ?'
        que2 = 'select count(*) from Subcon_Info, Decisions where Decisions.Request_Pending_With = "SBU Head" and Decisions.Request_Status = "Pending" and Decisions.Decision_SBU IS NULL and Subcon_Info.Contract_Type = ? and ((Julianday(Subcon_Info.Expected_End_Date) - Julianday("now")) between 30 and 60 and Subcon_Info.Cummulative_RAG != "Green" and Decisions.Subcon_ID = Subcon_Info.Subcon_ID) and Subcon_Info.Unit = ?'
        
        cur.execute(que1,("FP",self.name_SBU,))  ## No action initiated of FP and Expiry date < 30
        R13, = cur.fetchone()
        self.tableWidget1.setItem(3,1,QtWidgets.QTableWidgetItem(str(R13)))
        cur.execute(que1, ("T&M",self.name_SBU,)) ## No action initiated of T&M and Expiry date < 30
        R14, = cur.fetchone()
        self.tableWidget2.setItem(3,1,QtWidgets.QTableWidgetItem(str(R14)))
        self.tableWidget3.setItem(3,1,QtWidgets.QTableWidgetItem(str(R13 + R14)))

        cur.execute(que2, ("FP",self.name_SBU,)) ## No action initiated of FP and 30 < Expiry date < 60
        R15, = cur.fetchone()
        self.tableWidget4.setItem(3,1,QtWidgets.QTableWidgetItem(str(R15)))
        cur.execute(que2, ("T&M",self.name_SBU,)) ## No action initiated of T&M and 30 < Expiry date < 60
        R16, = cur.fetchone()
        self.tableWidget5.setItem(3,1,QtWidgets.QTableWidgetItem(str(R16)))
        self.tableWidget6.setItem(3,1,QtWidgets.QTableWidgetItem(str(R15 + R16)))
        
        self.tableWidget1.setItem(4,1,QtWidgets.QTableWidgetItem(str(R1 + R5 + R9 + R13 + R_1)))
        self.tableWidget2.setItem(4,1,QtWidgets.QTableWidgetItem(str(R2 + R6 + R10 + R14 + R_2)))
        self.tableWidget3.setItem(4,1,QtWidgets.QTableWidgetItem(str(R1 + R5 + R9 + R13 + R2 + R6 + R10 + R14 + R_1 + R_2)))
        self.tableWidget4.setItem(4,1,QtWidgets.QTableWidgetItem(str(R3 + R7 + R11 + R15 + R_3)))
        self.tableWidget5.setItem(4,1,QtWidgets.QTableWidgetItem(str(R4 + R8 + R12 + R16 + R_4)))
        self.tableWidget6.setItem(4,1,QtWidgets.QTableWidgetItem(str(R3 + R7 + R11 + R15 + R4 + R8 + R12 + R16 + R_3 + R_4)))


        ## Adding values to Dasboard-2 ##
        ## The Data is grouped by Customer Name and Contract Type
        results = cur.execute('Select Customer_Name, Contract_Type, Count(*), SUM(Vendor_Rate), SUM(Customer_Rate), Round(AVG(Julianday("now") - Julianday(Date_of_Joining)),0) from Subcon_Info group by Customer_Name, Contract_Type having Subcon_Info.Unit = ?',(self.name_SBU,))
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
        self.tableWidget1.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget1.isSortingEnabled()
        self.tableWidget1.setSortingEnabled(False)
        item = self.tableWidget1.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget1.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget1.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget1.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget1.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget1.setSortingEnabled(__sortingEnabled)
        self.FP1.setText(_translate("MainWindow", "Expiry Date < 30: FP"))
        self.tableWidget2.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget2.isSortingEnabled()
        self.tableWidget2.setSortingEnabled(False)
        item = self.tableWidget2.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget2.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget2.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget2.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget2.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget2.setSortingEnabled(__sortingEnabled)
        self.TM1.setText(_translate("MainWindow", "Expiry Date < 30: T&M"))
        self.tableWidget3.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget3.isSortingEnabled()
        self.tableWidget3.setSortingEnabled(False)
        item = self.tableWidget3.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget3.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget3.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget3.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget3.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget3.setSortingEnabled(__sortingEnabled)
        self.Total1.setText(_translate("MainWindow", "Expiry Date < 30: Total"))
        self.summary.setText(_translate("MainWindow", "Action Report"))
        self.FP2.setText(_translate("MainWindow", "Expiry Date > 30: FP"))
        self.TM2.setText(_translate("MainWindow", "Expiry Date > 30: T&M"))
        self.Total2.setText(_translate("MainWindow", "Expiry Date > 30: Total"))
        self.tableWidget4.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget4.isSortingEnabled()
        self.tableWidget4.setSortingEnabled(False)
        item = self.tableWidget4.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget4.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget4.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget4.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget4.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget4.setSortingEnabled(__sortingEnabled)
        self.tableWidget5.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget5.isSortingEnabled()
        self.tableWidget5.setSortingEnabled(False)
        item = self.tableWidget5.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget5.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget5.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget5.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget5.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget5.setSortingEnabled(__sortingEnabled)
        self.tableWidget6.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget6.isSortingEnabled()
        self.tableWidget6.setSortingEnabled(False)
        item = self.tableWidget6.item(0, 0)
        item.setText(_translate("MainWindow", "Approved"))
        item = self.tableWidget6.item(1, 0)
        item.setText(_translate("MainWindow", "Rejected"))
        item = self.tableWidget6.item(2, 0)
        item.setText(_translate("MainWindow", "Sent Back"))
        item = self.tableWidget6.item(3, 0)
        item.setText(_translate("MainWindow", "No ActionYet"))
        item = self.tableWidget6.item(4, 0)
        item.setText(_translate("MainWindow", "Total"))
        self.tableWidget6.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SBU_Renewal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

