## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 ## Library to import sqlite3, replace this with mysql connector of python
from datetime import datetime
import calendar

class PM_Timesheet(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 1084)
        #self.name_PM = "Kartik"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)         #This widget allows to add pages in a module
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")

        ### Page - 1: Details of Subcon under the given Project Manager ####
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
        self.Heading.setText("Timesheet Summary")
        self.table = QtWidgets.QTableWidget(self.page)
        self.table.setGeometry(QtCore.QRect(50, 300, 1742, 500))         #Size of the Table
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("QHeaderView::section{background-color: rgb(255, 191, 0); color: rgb(0, 0,0);} QTableWidget {gridline-color: rgb(0, 0, 0);}")                                           #Table Header Properties can be changed from this line.          
        self.table.setAlternatingRowColors(True)      # Alternating Row Colors have been added here.          
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.calculatedimensions()                      # Calculates the no. of rows required for showing the relevant data in the table.
        if self.rows >= 15:                             # The min. no. of rows in the table shall be 15
            self.table.setRowCount(self.rows)   
        else:
            self.table.setRowCount(15)
        self.table.setColumnCount(10)  ## Column Count 
        self.table.setObjectName("table")
        for i in range(25):
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
        self.Headers = ["Subcon ID","Subcon Name","Unit","Sub Unit","Month","Customer Name","Customer Group Name","Project ID","Project Description","Request Status"]   #Header Names for the Table
        i = 0
        for names in self.Headers:
            self.table.horizontalHeaderItem(i).setText(names)            #The following loop adds the names to the Headers
            i = i + 1
            
        for i in range(10):
            self.table.setColumnWidth(i,self.columnwidth)        # Setting the same width to all the columns 
        self.loaddata_1()                                        # The function to load the data into the table
        self.stackedWidget.addWidget(self.page)                  # Adding page to the module

        ### Page - 2 : Show Details of Particular Subcon  and Take Action ###
        ## This Page consists of 3 Parts: 1) Subcon Information 2) Timesheet Review and Suggest Changes to the Subcon by PM 3) Remarks of the Other Involved Authorities and Option to provide one's remarks
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(30, 60, 1761, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        ## Subcon Base Info ##
        self.subcon_info = QtWidgets.QLabel(self.frame)
        self.subcon_info.setGeometry(QtCore.QRect(60,50, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subcon_info.setFont(font)
        self.subcon_info.setObjectName("subcon_info")
        self.subcon_info.setText("Subcon Info")
        self.subcon_info.setFrameShape(QtWidgets.QFrame.Box)
        self.subcon_info.setAlignment(QtCore.Qt.AlignCenter)
        self.subcon_info.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 90, 500, 320))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.subcon_id = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subcon_id.setFont(font)
        self.subcon_id.setObjectName("subcon_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subcon_id)
        self.subcon_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subcon_name.setFont(font)
        self.subcon_name.setObjectName("subcon_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subcon_name)
        self.sid = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sid.setFont(font)
        self.sid.setReadOnly(True)
        self.sid.setObjectName("sid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sid)
        self.sname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sname.setFont(font)
        self.sname.setReadOnly(True)
        self.sname.setObjectName("sname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sname)
        self.pid = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pid.setFont(font)
        self.pid.setReadOnly(True)
        self.pid.setObjectName("pid")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pid)
        self.project_id = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.project_id.setFont(font)
        self.project_id.setObjectName("project_id")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.project_id)
        self.unit = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.unit.setFont(font)
        self.unit.setObjectName("unit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.unit)
        self.unit_s = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.unit_s.setFont(font)
        self.unit_s.setReadOnly(True)
        self.unit_s.setObjectName("unit_s")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.unit_s)
        self.subunit = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subunit.setFont(font)
        self.subunit.setObjectName("subunit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.subunit)
        self.sunit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sunit.setFont(font)
        self.sunit.setReadOnly(True)
        self.sunit.setObjectName("sunit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sunit)
        self.customer_group = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.customer_group.setFont(font)
        self.customer_group.setObjectName("customer_group")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.customer_group)
        self.project_Desc = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.project_Desc.setFont(font)
        self.project_Desc.setObjectName("project_Desc")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.project_Desc)
        self.pdesc = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pdesc.setFont(font)
        self.pdesc.setReadOnly(True)
        self.pdesc.setObjectName("pdesc")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pdesc)
        self.customer_name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.customer_name.setFont(font)
        self.customer_name.setObjectName("customer_name")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.customer_name)
        self.cname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cname.setFont(font)
        self.cname.setReadOnly(True)
        self.cname.setObjectName("cname")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cname)
        self.cgname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cgname.setFont(font)
        self.cgname.setReadOnly(True)
        self.cgname.setObjectName("cgname")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cgname)
        self.month = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.month.setFont(font)
        self.month.setObjectName("month")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.month)
        self.month_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.month_name.setFont(font)
        self.month_name.setReadOnly(True)
        self.month_name.setObjectName("month_name")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.month_name)

        ## YTD Information ##
        self.ytd_info = QtWidgets.QLabel(self.frame)
        self.ytd_info.setGeometry(QtCore.QRect(620,50, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_info.setFont(font)
        self.ytd_info.setObjectName("ytd_info")
        self.ytd_info.setText("YTD Summary")
        self.ytd_info.setFrameShape(QtWidgets.QFrame.Box)
        self.ytd_info.setAlignment(QtCore.Qt.AlignCenter)
        self.ytd_info.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.formLayoutWidget_1 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_1.setGeometry(QtCore.QRect(610, 100, 480, 330))
        self.formLayoutWidget_1.setObjectName("formLayoutWidget_1")
        self.formLayout_1 = QtWidgets.QFormLayout(self.formLayoutWidget_1)
        self.formLayout_1.setObjectName("formLayout_1")
        self.ytd_vendor_hours = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_vendor_hours.setFont(font)
        self.ytd_vendor_hours.setWordWrap(True)
        self.ytd_vendor_hours.setObjectName("ytd_vendor_hours")
        self.ytd_vendor_hours.setText("Timesheet Hours: ")
        self.formLayout_1.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ytd_vendor_hours)
        self.ytd_vhours = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_vhours.setFont(font)
        self.ytd_vhours.setReadOnly(True)
        self.ytd_vhours.setObjectName("ytd_vhours")
        self.formLayout_1.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ytd_vhours)
        self.ytd_payment_Amount = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_payment_Amount.setFont(font)
        self.ytd_payment_Amount.setText("Payment Amount (USD): ")
        self.ytd_payment_Amount.setObjectName("ytd_payment_Amount")
        self.formLayout_1.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ytd_payment_Amount)
        self.ytd_pamount = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_pamount.setFont(font)
        self.ytd_pamount.setReadOnly(True)
        self.ytd_pamount.setObjectName("ytd_pamount")
        self.formLayout_1.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ytd_pamount)
        self.ytd_rus_hours = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_rus_hours.setFont(font)
        self.ytd_rus_hours.setText("RUS Hours: ")
        self.ytd_rus_hours.setObjectName("ytd_rus_hours")
        self.formLayout_1.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ytd_rus_hours)
        self.ytd_chours = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_chours.setFont(font)
        self.ytd_chours.setObjectName("ytd_chours")
        self.formLayout_1.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ytd_chours)
        self.ytd_chours.setReadOnly(True)
        self.ytd_nonbillable_amount = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_nonbillable_amount.setFont(font)
        self.ytd_nonbillable_amount.setText("Un-Billed Cost (USD): ")
        self.ytd_nonbillable_amount.setObjectName("ytd_nonbillable_amount")
        self.formLayout_1.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.ytd_nonbillable_amount)
        self.ytd_billable_amount = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_billable_amount.setFont(font)
        self.ytd_billable_amount.setText("Billable Cost (USD): ")
        self.ytd_billable_amount.setObjectName("ytd_billable_amount")
        self.formLayout_1.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ytd_billable_amount)
        self.ytd_bamount = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_bamount.setFont(font)
        self.ytd_bamount.setReadOnly(True)
        self.ytd_bamount.setObjectName("ytd_bamount")
        self.formLayout_1.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ytd_bamount)
        self.ytd_nbamount = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_nbamount.setFont(font)
        self.ytd_nbamount.setReadOnly(True)
        self.ytd_nbamount.setObjectName("ytd_nbamount")
        self.formLayout_1.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ytd_nbamount)
        self.ytd_variance = QtWidgets.QLabel(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ytd_variance.setFont(font)
        self.ytd_variance.setText("Variance (%): ")
        self.ytd_variance.setObjectName("variance")
        self.formLayout_1.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ytd_variance)
        self.ytd_variance_value = QtWidgets.QLineEdit(self.formLayoutWidget_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ytd_variance_value.setFont(font)
        self.ytd_variance_value.setReadOnly(True)
        self.ytd_variance_value.setObjectName("variance_value")
        self.formLayout_1.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ytd_variance_value)

        ## Current Months' Summary ## 
        self.current_info = QtWidgets.QLabel(self.frame)
        self.current_info.setGeometry(QtCore.QRect(1130,50, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.current_info.setFont(font)
        self.current_info.setObjectName("current_info")
        self.current_info.setText("Current Months' Summary")
        self.current_info.setFrameShape(QtWidgets.QFrame.Box)
        self.current_info.setAlignment(QtCore.Qt.AlignCenter)
        self.current_info.setStyleSheet("background-color: rgb(255, 191, 0);")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(1120, 100, 500, 330))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.vendor_rate = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.vendor_rate.setFont(font)
        self.vendor_rate.setWordWrap(True)
        self.vendor_rate.setObjectName("vendor_rate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vendor_rate)
        self.vrate = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vrate.setFont(font)
        self.vrate.setReadOnly(True)
        self.vrate.setObjectName("vrate")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vrate)
        self.crate = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.crate.setFont(font)
        self.crate.setObjectName("crate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.crate)
        self.customer_rate = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.customer_rate.setFont(font)
        self.customer_rate.setWordWrap(True)
        self.customer_rate.setObjectName("customer_rate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.customer_rate)
        self.payment_Amount = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.payment_Amount.setFont(font)
        self.payment_Amount.setObjectName("payment_Amount")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.payment_Amount)
        self.pamount = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pamount.setFont(font)
        self.pamount.setReadOnly(True)
        self.pamount.setObjectName("pamount")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pamount)
        self.rus_hours = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rus_hours.setFont(font)
        self.rus_hours.setObjectName("rus_hours")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rus_hours)
        self.chours = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chours.setFont(font)
        self.chours.setObjectName("chours")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.chours)
        self.crate.setReadOnly(True)
        self.chours.setReadOnly(True)
        self.nonbillable_amount = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nonbillable_amount.setFont(font)
        self.nonbillable_amount.setObjectName("nonbillable_amount")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.nonbillable_amount)
        self.nrc = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nrc.setFont(font)
        self.nrc.setObjectName("nrc")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nrc)
        self.nrc_value = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nrc_value.setFont(font)
        self.nrc_value.setObjectName("nrc_value")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nrc_value)
        self.billable_amount = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.billable_amount.setFont(font)
        self.billable_amount.setObjectName("billable_amount")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.billable_amount)
        self.bamount = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bamount.setFont(font)
        self.bamount.setReadOnly(True)
        self.bamount.setObjectName("bamount")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.bamount)
        self.nbamount = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nbamount.setFont(font)
        self.nbamount.setReadOnly(True)
        self.nbamount.setObjectName("nbamount")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nbamount)
        self.variance = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.variance.setFont(font)
        self.variance.setObjectName("variance")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.variance)
        self.variance_value = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.variance_value.setFont(font)
        self.variance_value.setReadOnly(True)
        self.variance_value.setObjectName("variance_value")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.variance_value)
        
        ## Heading of the Page ##
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(30, 25, 1761, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        ## Part - 2: This contains a Table Widget, which allows the PM to edit the Timesheet submitted by Subcon ##
        self.tablewidget = QtWidgets.QTableWidget(self.page_2)
        self.tablewidget.setGeometry(QtCore.QRect(40, 500, 1731, 291))
        self.tablewidget.setRowCount(6)  # 6 Rows
        self.tablewidget.setColumnCount(8)  # 8 Columns
        self.tablewidget.setObjectName("tablewidget")

        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            self.tablewidget.setVerticalHeaderItem(i, item)  # Adding 6 Vertical Headers
        for i in range(8):
            item = QtWidgets.QTableWidgetItem()
            self.tablewidget.setHorizontalHeaderItem(i, item)   # Adding 8 Horizontal Headers
        
        self.tablewidget.horizontalHeader().setDefaultSectionSize(210)  # Setting Horizontal Header Size
        self.tablewidget.verticalHeader().setDefaultSectionSize(45)     # Setting Vertical Header Size
        self.vendor_hours = QtWidgets.QLabel(self.page_2)               # Label for Vendor Hours
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vendor_hours.setFont(font)
        self.vendor_hours.setObjectName("vendor_hours")
        self.vendor_hours.setGeometry(QtCore.QRect(30,830,120,35))
        self.vhours = QtWidgets.QLineEdit(self.page_2)                   # Line Edit to display Vendor Hours
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vhours.setFont(font)
        self.vhours.setReadOnly(True)
        self.vhours.setObjectName("vhours")
        self.vhours.setGeometry(QtCore.QRect(160,830,100,35))

        self.Remark_subcon = QtWidgets.QLabel(self.page_2)              # Label for Subcon Remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remark_subcon.setFont(font)
        self.Remark_subcon.setObjectName("Remarks_subcon")
        self.Remark_subcon.setText("Subcon Remarks:")
        self.Remark_subcon.setGeometry(QtCore.QRect(290,830,130,35))
        self.Remark_value_subcon = QtWidgets.QTextEdit(self.page_2)   # Line Edit to display Subcon Remarks
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Remark_value_subcon.setFont(font)
        self.Remark_value_subcon.setObjectName("Remark_value_subcon")
        self.Remark_value_subcon.setReadOnly(True)
        self.Remark_value_subcon.setGeometry(QtCore.QRect(430,830,170,35))

        self.Remarks = QtWidgets.QLabel(self.page_2)                # Label for PM Remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remarks.setFont(font)
        self.Remarks.setObjectName("Remarks")
        self.Remarks.setText("Variance Description:")
        self.Remarks.setGeometry(QtCore.QRect(1040,830,150,35))
        self.Remarks_value = QtWidgets.QTextEdit(self.page_2)       # Line Edit to display PM Remarks
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Remarks_value.setFont(font)
        self.Remarks_value.setObjectName("Remarks_value")
        self.Remarks_value.setGeometry(QtCore.QRect(1200,830,180,35))

        self.Reason = QtWidgets.QLabel(self.page_2)                # Label for PM Remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reason.setFont(font)
        self.Reason.setObjectName("Reasons")
        self.Reason.setText("LOV Reason:")
        self.Reason.setGeometry(QtCore.QRect(630,830,120,35))
        self.Reason_value = QtWidgets.QComboBox(self.page_2)       # Line Edit to display PM Remarks
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Reason_value.setFont(font)
        self.Reason_value.setObjectName("Remarks_value")
        self.Reason_value.setGeometry(QtCore.QRect(760,830,250,35))

        self.Remark_sbu = QtWidgets.QLabel(self.page_2)             # Label for SBU remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remark_sbu.setFont(font)
        self.Remark_sbu.setObjectName("Remarks_sbu")
        self.Remark_sbu.setText("SBU Remarks:")
        self.Remark_sbu.setGeometry(QtCore.QRect(1410,830,90,35))
        self.Remark_value_sbu = QtWidgets.QTextEdit(self.page_2)    # Line Edit to display SBU Remarks
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Remark_value_sbu.setFont(font)
        self.Remark_value_sbu.setObjectName("Remark_value_sbu")
        self.Remark_value_sbu.setReadOnly(True)
        self.Remark_value_sbu.setGeometry(QtCore.QRect(1510,830,250,35))

        # self.sendback = QtWidgets.QPushButton(self.page_2)            # Button to send Query to Subcon 
        # self.sendback.setGeometry(QtCore.QRect(570,900,200,40))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.sendback.setFont(font)
        # self.sendback.setObjectName("sendback")
        # self.sendback.setText("Query for Subcon")
        self.submit = QtWidgets.QPushButton(self.page_2)                 # Button to submit the progress
        self.submit.setGeometry(QtCore.QRect(830,900,200,40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.goback = QtWidgets.QPushButton(self.page_2)                # Button to cancel transaction and return to 1st page
        self.goback.setGeometry(QtCore.QRect(1100,900,200,40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.goback.setFont(font)
        self.goback.setObjectName("goback")
        self.goback.setText("Go Back")
        self.goback.clicked.connect(self.GoBack)
        self.nrc_value.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_2)                   # Add this to the module
        self.table.cellClicked.connect(self.TakeAction)             # The function is applied to clicking of a cell in a row
        self.tablewidget.itemChanged.connect(self.calculatevendorhours)    # When a person edits a cell and presses the enter key, the vendor hours inc by that number
        self.submit.clicked.connect(self.submitprogress)  # saving progress
        #self.sendback.clicked.connect(self.senditback)  # sending it back

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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculatedimensions(self):
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        cur.execute('select count(*) from Timesheet_PM where Project_Manager = ?',(self.name_PM,)) # Counts the data entries from Subcons under PM who has logged in.
        result, = cur.fetchone()
        self.rows = int(result)  ## Stores the no.of rows

    def calculatevendorhours(self):
        values = []                 ## Stores the no.of hours added by the person for the span of 30 days
        
        ## Month stores the name of the month, but we require the month number in future computations. Hence the below conditional statements.
        if self.Month == "January":
            month = 1
        elif self.Month == "February":
            month = 2
        elif self.Month == "March":
            month = 3
        elif self.Month == "April":
            month = 4
        elif self.Month == "June":
            month = 6
        elif self.Month == "July":
            month = 7
        elif self.Month == "August":
            month = 8
        elif self.Month == "September":
            month = 9
        elif self.Month == "May":
            month = 5
        elif self.Month == "October":
            month = 10
        elif self.Month == "November":
            month = 11
        else:
            month = 12
        
        daynumber = calendar.weekday(self.year,month,1)  ## Calculates the day on the 1st of the selected month and year.
        tablecol = daynumber                             ## Tablecol stores the col of the table from where the 1st value can be added.
        k = 0           ### K stores the no. of values added in the table. This is used to restrict the person from entering more than 31 values for a month.
        
        ## Logic: Store the values in the first row into "values", if there is no value in a cell, then assume 0 in that cell.  
        for i in range(31):    
            if tablecol <= 6:    
                if self.tablewidget.item(1,tablecol) is not None:
                    if self.tablewidget.item(1,tablecol).text() != '' and self.tablewidget.item(1,tablecol).text() != 'None':     
                        values.append(float(self.tablewidget.item(1,tablecol).text()))
                    else:
                        values.append(float(0))          
                    tablecol+=1
                    k+=1
        
        for j in range(2,6):
            for i in range(7):
                if k <=32:
                    if self.tablewidget.item(j,i) is not None:
                        if self.tablewidget.item(j,i).text() != '':
                            if self.tablewidget.item(j,i).text() != 'None':
                                values.append(float(self.tablewidget.item(j,i).text()))
                            else:
                                values.append(float(0))
                else:
                    break
                k+=1
        if len(values) == 30:
            values.append(float(0))

        vhours = sum(values)                                  # sum of all the values = vendor total hours
        self.vhours.setText(str(sum(values)))
        vrate = float(self.vrate.text())                     # vendor rate as displayed in the Vendor Rate info
        self.pamount.setText(str(vhours*vrate))        # Payment amount = vendor hours * vendor rate
        
        if self.chours.text() != '' and self.chours.text() != 'None':
            rus = float(self.chours.text())
            self.nbamount.setText(str((vhours - rus) * vrate))
            if vhours != 0.0:
                self.variance_value.setText(str(round(100*(vhours - rus)/vhours,2)) + '%')
                if 100*(vhours - rus)/vhours <= 2.0:
                        self.variance_value.setStyleSheet('background-color: rgb(144,238,144);')
                elif 100*(vhours - rus)/vhours > 2.0 and 100*(vhours - rus)/vhours <= 4.0:
                    self.variance_value.setStyleSheet('background-color: rgb(255,191,0);')
                else:
                    self.variance_value.setStyleSheet('background-color: rgb(255,0,0);')

    def GoBack(self):               ## Function to cancel the transaction
        self.loaddata_1()           ## loaddata into the initial table
        self.stackedWidget.setCurrentIndex(0)   ## Display the first page
        self.Reason_value.clear()    
   
    def senditback(self):
        values = []               
        if self.Month == "January":
            month = 1
        elif self.Month == "February":
            month = 2
        elif self.Month == "March":
            month = 3
        elif self.Month == "April":
            month = 4
        elif self.Month == "June":
            month = 6
        elif self.Month == "July":
            month = 7
        elif self.Month == "August":
            month = 8
        elif self.Month == "September":
            month = 9
        elif self.Month == "May":
            month = 5
        elif self.Month == "October":
            month = 10
        elif self.Month == "November":
            month = 11
        else:
            month = 12
        
        daynumber = calendar.weekday(self.year,month,1)
        tablecol = daynumber
        k = 0
        for i in range(31):
            if tablecol <= 6:
                if self.tablewidget.item(1,tablecol).text() != '':
                    values.append(float(self.tablewidget.item(1,tablecol).text()))
                else:
                    values.append(float(0))
                tablecol+=1
                k+=1
        for j in range(2,6):
            for i in range(7):
                if k <=32:
                    if self.tablewidget.item(j,i).text() != '':
                        values.append(float(self.tablewidget.item(j,i).text()))
                    else:
                        values.append(float(0))
                else:
                    break
                k+=1
        if len(values) == 30:
            values.append(float(0))

        ## Store the values of payamount, non-billable amount, variance and remarks of PM
        pamount = self.pamount.text()
        nbamount = self.nbamount.text()
        variance = float(str(self.variance_value.text())[:-1])
        remarks = self.Remarks_value.toPlainText()
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()

        ## Update the Timesheet of PM with the updated values of Payamount, non-billable amount, variance, day-to-day values of hours for the month, His Remarks, The Request Status shall be updated to Pending with Subcon and PM Decision = Query for Subcon

        cur.execute('update Timesheet_PM set Payment_amount = ?, NonBillable_amount = ?,Variance = ?,one = ?,two = ?,three = ?,four = ?,five = ?,six = ?,seven = ?,eight = ?,nine = ?,ten = ?,eleven = ?,twelve = ?,thirteen = ?,fourteen = ?,fifteen = ?,sixteen = ?,seventeen = ?,eighteen = ?,nineteen = ?,twenty = ?,twentyone = ?,twentytwo = ?,twentythree = ?,twentyfour = ?,twentyfive = ?,twentysix = ?,twentyseven = ?,twentyeight = ?,twentynine = ?,thirty = ?,thirtyone = ?,Total_Hours = ?, Decision = "Query for Subcon", Remarks = ?, Request_Status = "Pending with Subcon" where Subcon_ID = ? and Year = ? and Month = ?', (pamount,nbamount,variance,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),remarks,self.Subcon_ID,self.year,self.Month,))

        ## Update the Timesheet of Subcon with the updated day-to-day values of hours for the month
        cur.execute('update Timesheet_Subcon set one = ?,two = ?,three = ?,four = ?,five = ?,six = ?,seven = ?,eight = ?,nine = ?,ten = ?,eleven = ?,twelve = ?,thirteen = ?,fourteen = ?,fifteen = ?,sixteen = ?,seventeen = ?,eighteen = ?,nineteen = ?,twenty = ?,twentyone = ?,twentytwo = ?,twentythree = ?,twentyfour = ?,twentyfive = ?,twentysix = ?,twentyseven = ?,twentyeight = ?,twentynine = ?,thirty = ?,thirtyone = ?,Total_Hours = ? where Subcon_ID = ? and Year = ? and Month = ?', (values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.Subcon_ID,self.year,self.Month,))
        connection.commit()
        connection.close()
        self.loaddata_1()
        self.Reason_value.clear()        
        self.Remarks_value.setText("")
        self.stackedWidget.setCurrentIndex(0)

    
    def submitprogress(self):
        if self.Month == "January":
            month = 1
        elif self.Month == "February":
            month = 2
        elif self.Month == "March":
            month = 3
        elif self.Month == "April":
            month = 4
        elif self.Month == "June":
            month = 6
        elif self.Month == "July":
            month = 7
        elif self.Month == "August":
            month = 8
        elif self.Month == "September":
            month = 9
        elif self.Month == "May":
            month = 5
        elif self.Month == "October":
            month = 10
        elif self.Month == "November":
            month = 11
        else:
            month = 12
        
        ## Find the current values 
        pamount = self.pamount.text()
        if self.nbamount.text() != "None" and self.nbamount.text() != "":
            nbamount = self.nbamount.text()
        if self.variance_value.text() != "None" and self.variance_value.text() != "":
            variance = float(str(self.variance_value.text())[:-1])
        reason = self.Reason_value.currentText()
        remarks = self.Remarks_value.toPlainText()
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        
        ## If rus hours not submitted, then show error message 
        if self.chours.text() == "":
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setText("Please get the RUS hours approved before submitting the Timesheet")
            self.error_dialog.exec_()
        else:
            if variance <= 2.0: ## If variance is less than 10%, then approve the timesheet.
                connection = sqlite3.connect('EY_1')
                cur = connection.cursor()
                cur.execute('update Timesheet_PM set Payment_amount = ?, NonBillable_amount = ?,Variance = ?,Remarks = ?, Reason = ?, Decision = "Approve", Request_Status = "Approved" where Subcon_ID = ? and Month = ?', (pamount,nbamount,variance,remarks,reason,self.Subcon_ID,month,))
                connection.commit()
                connection.close()
                self.loaddata_1()
            elif variance > 2.0:  # If variance is greater than 10%, then send the request to SBU head
                connection = sqlite3.connect('EY_1')
                cur = connection.cursor()
                cur.execute('update Timesheet_PM set Payment_amount = ?, NonBillable_amount = ?,Variance = ?, Remarks = ?, Reason = ?, Decision = "Approve", Request_Status = "Pending With SBU Head" where Subcon_ID = ? and Month = ?', (pamount,nbamount,variance,remarks,reason,self.Subcon_ID,month,))
                connection.commit()
                connection.close()
                self.error_dialog = QtWidgets.QMessageBox()
                self.error_dialog.setText("The Variance for the given transaction is greater than 2 percent and has been sent for SBU Heads' approval")
                self.error_dialog.exec_()
                self.loaddata_1()
            self.Reason_value.clear()  
            self.Remarks_value.setText("")      
            self.stackedWidget.setCurrentIndex(0)


    def showdata(self):                 ## This function autofills the data into the tablewidget i.e. Timesheet
        for i in range(7):
            for j in range(6):
                self.tablewidget.setItem(j,i,QtWidgets.QTableWidgetItem(str("")))
        
        if self.Month == "January":
            month = 1
        elif self.Month == "February":
            month = 2
        elif self.Month == "March":
            month = 3
        elif self.Month == "April":
            month = 4
        elif self.Month == "June":
            month = 6
        elif self.Month == "July":
            month = 7
        elif self.Month == "August":
            month = 8
        elif self.Month == "September":
            month = 9
        elif self.Month == "May":
            month = 5
        elif self.Month == "October":
            month = 10
        elif self.Month == "November":
            month = 11
        else:
            month = 12
        daynumber = calendar.weekday(self.year,month,1)
        tablecol = daynumber
        if month % 2 !=0 or month == 8:
            k = 30
            for i in range(tablecol,0,-1):
                self.tablewidget.setItem(0,i-1,QtWidgets.QTableWidgetItem(str(k)))
                k = k-1
        else:
            k = 31
            for i in range(tablecol,0,-1):
                self.tablewidget.setItem(0,i-1,QtWidgets.QTableWidgetItem(str(k)))
                k = k-1
        for i in range(1,8):
            if tablecol <= 6:
                self.tablewidget.setItem(0,tablecol,QtWidgets.QTableWidgetItem(str(i)))
                tablecol+=1
        for i in range(7):
            self.tablewidget.item(0,i).setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        
        daynumber = calendar.weekday(self.year,month,1)
        tablecol = daynumber
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        result = cur.execute('select * from Timesheet_PM where Subcon_ID = ? and Month = ? and Year = ?',(self.Subcon_ID,month,self.year,))
        k = 0
        for row in result:
            for i in range(7):
                if tablecol <= 6:
                    self.tablewidget.setItem(1,tablecol,QtWidgets.QTableWidgetItem(str(row[k+25])))
                    tablecol+=1
                    k+=1
                else:
                    break
            for i in range(7):
                self.tablewidget.setItem(2,i,QtWidgets.QTableWidgetItem(str(row[k+25])))
                k+=1
            for i in range(7):
                self.tablewidget.setItem(3,i,QtWidgets.QTableWidgetItem(str(row[k+25])))
                k+=1
            for i in range(7):
                self.tablewidget.setItem(4,i,QtWidgets.QTableWidgetItem(str(row[k+25])))
                k+=1
            for i in range(7):
                if k < 31:
                    self.tablewidget.setItem(5,i,QtWidgets.QTableWidgetItem(str(row[k+25])))
                    k+=1
        ### This is used to populate the Total Hours per week column
        for i in range(1,6):
            sum_1 = 0
            for j in range(7):
                if self.tablewidget.item(i,j) is not None:
                    if self.tablewidget.item(i,j).text() != '' and self.tablewidget.item(i,j).text() != 'None':
                        sum_1 = sum_1 + float(self.tablewidget.item(i,j).text())
            self.tablewidget.setItem(i,7,QtWidgets.QTableWidgetItem(str(sum_1)))
            self.tablewidget.item(i,7).setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) ## Prevents editing of cells
        for i in range(5,7):
            for j in range(6):
                self.tablewidget.item(j,i).setBackground(QtGui.QColor(211,211,211))  ## Sets background of Saturday and Sunday Columns to Grey


    def TakeAction(self,row1):
        self.Subcon_ID = self.table.item(row1,0).text()  ## Stores Subcon ID of the clicked cell
        self.Month = self.table.item(row1,4).text()      ## Stores Month of the clicked cell
        self.loaddata_2()                               ## Loads data into the Information part of Page-2
        self.showdata()                                 ## Loads data into the timesheet part of Page-2
        self.stackedWidget.setCurrentIndex(1)
    
    def loaddata_2(self):
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        if self.Month == "January":
            month = 1
        elif self.Month == "February":
            month = 2
        elif self.Month == "March":
            month = 3
        elif self.Month == "April":
            month = 4
        elif self.Month == "June":
            month = 6
        elif self.Month == "July":
            month = 7
        elif self.Month == "August":
            month = 8
        elif self.Month == "September":
            month = 9
        elif self.Month == "May":
            month = 5
        elif self.Month == "October":
            month = 10
        elif self.Month == "November":
            month = 11
        else:
            month = 12
        result = cur.execute('select * from Timesheet_PM where Subcon_ID = ? and Month = ?',(self.Subcon_ID,month,))
        for row in result:
            self.sid.setText(str(row[0]))
            self.sname.setText(str(row[1]))
            self.unit_s.setText(str(row[2]))
            self.sunit.setText(str(row[3]))
            self.month_name.setText(self.Month)
            self.cname.setText(str(row[5]))
            self.cgname.setText(str(row[6]))
            self.pid.setText(str(row[7]))
            self.pdesc.setText(str(row[8]))
            self.Remark_value_subcon.setText(str(row[58]))
            self.Remark_value_sbu.setText(str(row[56]))
            if str(row[12]) != "None":
                self.vrate.setText(str(row[12]))
            if str(row[13]) != "None":
                self.pamount.setText(str(row[13]))
            if str(row[14]) != "None" and str(row[14]) != "":
                self.chours.setText(str(row[14]))
                variance = 100*(row[11] - row[14])/row[11]
                self.variance_value.setText(str(variance) + '%') ## Calculating Variance 
                ## Highlighting variance based on the value 
                if variance <= 2.0: 
                    self.variance_value.setStyleSheet('background-color: rgb(144,238,144);')
                elif variance > 2.0 and variance <= 4.0:
                    self.variance_value.setStyleSheet('background-color: rgb(255,191,0);')
                else:
                    self.variance_value.setStyleSheet('background-color: rgb(255,0,0);')
            if str(row[15]) != "None":
                self.crate.setText(str(row[15]))
            if str(row[16]) != "None":
                self.nrc_value.setText(str(row[16]))
            if str(row[17]) != "None":
                self.bamount.setText(str(row[17]))
            if str(row[18]) != "None":
                self.nbamount.setText(str(row[18]))
                
            self.year = int(row[24])

        result = cur.execute('select * from Timesheet_PM where Subcon_ID = ? and Month < ? and Year <= ?',(self.Subcon_ID,month, self.year,))
        
        timesheet_hours = 0
        payment_amount = 0
        ytd_rus = 0
        billable_bamount = 0
        nonbillable_nbamount = 0
        for row in result:
            timesheet_hours = timesheet_hours + float(row[11])
            payment_amount = payment_amount + float(row[13])
            ytd_rus = ytd_rus + float(row[14])
            billable_bamount = billable_bamount + float(row[17]) 
            nonbillable_nbamount = nonbillable_nbamount + float(row[18])
        self.ytd_nbamount.setText(str(nonbillable_nbamount))
        self.ytd_bamount.setText(str(billable_bamount))
        self.ytd_vhours.setText(str(timesheet_hours))
        self.ytd_pamount.setText(str(payment_amount))
        self.ytd_chours.setText(str(ytd_rus))
        if timesheet_hours > 0.0:
            self.ytd_variance_value.setText(str(round(100*(timesheet_hours - ytd_rus)/timesheet_hours,2)) + '%')
            if float(100*(timesheet_hours - ytd_rus)/timesheet_hours) <= 2.0: 
                self.ytd_variance_value.setStyleSheet('background-color: rgb(144,238,144);')
            elif float(100*(timesheet_hours - ytd_rus)/timesheet_hours) > 2.0 and float(100*(timesheet_hours - ytd_rus)/timesheet_hours) <= 4.0:
                self.ytd_variance_value.setStyleSheet('background-color: rgb(255,191,0);')
            else:
                self.ytd_variance_value.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            self.ytd_variance_value.setText("0.0%")
            self.ytd_variance_value.setStyleSheet('background-color: rgb(144,238,144);')
        
        results = cur.execute('select Timesheet_Variance from Choices')
        categories = [] 
        for row in results:
            if str(row[0]) != 'None':
                categories.append(str(row[0]))   ## Reasons are being fetched from Choices table.
        self.Reason_value.addItems(categories)
        
        connection.close()



    def loaddata_1(self):  ## Load Data into the table 1
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        result = cur.execute('select * from Timesheet_PM where Project_Manager = ?', (self.name_PM,))  ## Query all subcon data for this particular PM
        tablerow = 0
        for row in result:
            for i in range(9):
                self.table.setItem(tablerow,i, QtWidgets.QTableWidgetItem(str(row[i])))

            if int(row[4]) == 1:
                month = "January"
            elif int(row[4]) == 2:
                month = "February"
            elif int(row[4]) == 3:
                month = "March"
            elif int(row[4]) == 4:
                month = "April"
            elif int(row[4]) == 5:
                month = "May"
            elif int(row[4]) == 6:
                month = "June"
            elif int(row[4]) == 7:
                month = "July"
            elif int(row[4]) == 8:
                month = "August"
            elif int(row[4]) == 9:
                month = "September"
            elif int(row[4]) == 10:
                month = "October"
            elif int(row[4]) == 11:
                month = "November"
            else:
                month = "Decemeber"
            
            self.table.setItem(tablerow,4,QtWidgets.QTableWidgetItem(month))
            self.table.setItem(tablerow,9,QtWidgets.QTableWidgetItem(str(row[57])))
            #self.table.setItem(tablerow,10,QtWidgets.QTableWidgetItem(str(row[22])))
            tablerow+=1        
        connection.close()
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subcon_id.setText(_translate("MainWindow", "Subcon ID:"))
        self.subcon_name.setText(_translate("MainWindow", "Subcon Name:"))
        self.project_id.setText(_translate("MainWindow", "Project ID:"))
        self.unit.setText(_translate("MainWindow", "Unit:"))
        self.subunit.setText(_translate("MainWindow", "Sub Unit:"))
        self.customer_group.setText(_translate("MainWindow", "Customer Group Name:"))
        self.project_Desc.setText(_translate("MainWindow", "Project Description:"))
        self.customer_name.setText(_translate("MainWindow", "Customer Name:"))
        self.month.setText(_translate("MainWindow", "Month:"))
        self.vendor_hours.setText(_translate("MainWindow", "Timesheet Hours:"))
        self.vendor_rate.setText(_translate("MainWindow", "Vendor Rate (per hour USD):"))
        self.customer_rate.setText(_translate("MainWindow", "Customer Rate (per hour USD):"))
        self.payment_Amount.setText(_translate("MainWindow", "Payment Amount (USD):"))
        self.rus_hours.setText(_translate("MainWindow", "RUS Hours:"))
        self.nonbillable_amount.setText(_translate("MainWindow", "Un-Billed Cost (USD):"))
        self.nrc.setText(_translate("MainWindow", "Non Resource Cost (USD):"))
        self.billable_amount.setText(_translate("MainWindow", "Billable Amount (USD):"))
        self.variance.setText(_translate("MainWindow", "Variance (%):"))
        self.label.setText(_translate("MainWindow", "Subcon Timesheet and Details Filling"))
        item = self.tablewidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Week1"))
        item = self.tablewidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Week2"))
        item = self.tablewidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Week3"))
        item = self.tablewidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Week4"))
        item = self.tablewidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Week5"))
        item = self.tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Monday"))
        item = self.tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tuesday"))
        item = self.tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Wednesday"))
        item = self.tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thursday"))
        item = self.tablewidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Friday"))
        item = self.tablewidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Saturday"))
        item = self.tablewidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sunday"))
        item = self.tablewidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Total Hours for Week"))
        __sortingEnabled = self.tablewidget.isSortingEnabled()
        self.tablewidget.setSortingEnabled(False)
        self.tablewidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PM_Timesheet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

