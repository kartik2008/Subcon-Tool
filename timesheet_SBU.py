from PyQt5 import QtCore, QtGui, QtWidgets           #Importing the relevant libraries
import sqlite3                                       #Importing Library for Sqlite Database

class SBU_Timesheet(object):
    def setupUi(self, MainWindow):    
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 1080)
        #self.name_SBU = "P"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)    #This widget allows to add pages in a module
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        
        ### Page - 1: Details of Subcon under the given Sub Unit ####
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
        self.table.setGeometry(QtCore.QRect(50, 300, 1742, 500))     #Size of the Table
        self.table.setAutoFillBackground(True)
        self.table.setStyleSheet("QHeaderView::section{background-color: rgb(255, 191, 0); color: rgb(0, 0,0);} QTableWidget {gridline-color: rgb(0, 0, 0);}")                           #Table Header Properties can be changed from this line.          
        self.table.setAlternatingRowColors(True)
        self.table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.calculatedimensions()  # Calculates the no. of rows required for showing the relevant data in the table.
        if self.rows >= 15:         # The min. no. of rows in the table shall be 15
            self.table.setRowCount(self.rows)   
        else:
            self.table.setRowCount(15) 
        self.table.setColumnCount(10)  #No. of Columns
        self.table.setObjectName("table")
        for i in range(22):
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
        self.Headers = ["Subcon ID","Subcon Name","Unit","Sub Unit","Month","Customer Name","Customer Group Name","Project ID","Project Description","Request Status"]  #Header Names for the Table
        i = 0
        for names in self.Headers:
            self.table.horizontalHeaderItem(i).setText(names)    #The following loop adds the names to the Headers
            i = i + 1
            
        for i in range(22):
            self.table.setColumnWidth(i,self.columnwidth)        # Setting the same width to all the columns 
        self.loaddata_1()                                        # The function to load the data into the table
        self.stackedWidget.addWidget(self.page)                  # Adding page to the module
 
        ### Page - 2 : Show Details of Particular Subcon  and Take Action ###
        ## This Page consists of 2 Parts: 1) Subcon Information 2) Remarks of the Other Involved Authorities and Option to provide one's remarks
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(50, 60, 1761, 411))
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
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(1120, 90, 500, 330))
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
        self.vendor_hours = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.vendor_hours.setFont(font)
        self.vendor_hours.setObjectName("vendor_hours")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vendor_hours)
        self.vhours = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vhours.setFont(font)
        self.vhours.setObjectName("vhours")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vhours)
        self.vhours.setReadOnly(True)
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
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(50, 25, 1761, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        ## Part - 2: This section has 4 Horizontal Layouts, 4 Labels, 4 Text Edits of which 3 are Read Only, and 1 is Editable; 2 Action Buttons ##
        ## Variable Names: Labels:- remarks - for SBU remarks, remarks_PM - for Remarks of PM, remarks_EHC - for Remarks of EHC, reason_PM - for PM Reasons.
        ## Variable Names: Line Edit:- remark_value - for SBU remarks, Remark_value_PM - for Remarks of PM, Remark_value_EHC - for Remarks of EHC, reason_value_PM - for PM Reasons.
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(610, 720, 491, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remarks = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remarks.setFont(font)
        self.remarks.setObjectName("remarks")
        self.horizontalLayout.addWidget(self.remarks)
        self.remarks_value = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.remarks_value.setObjectName("remarks_value")
        self.horizontalLayout.addWidget(self.remarks_value)
        self.sendback = QtWidgets.QPushButton(self.page_2)
        self.sendback.setGeometry(QtCore.QRect(640, 850, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sendback.setFont(font)
        self.sendback.setObjectName("sendback")
        self.submit = QtWidgets.QPushButton(self.page_2)
        self.submit.setGeometry(QtCore.QRect(880, 850, 221, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 600, 491, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.remarks_pm = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remarks_pm.setFont(font)
        self.remarks_pm.setObjectName("remarks_pm")
        self.horizontalLayout_2.addWidget(self.remarks_pm)
        self.remarks_value_pm = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.remarks_value_pm.setReadOnly(True)
        self.remarks_value_pm.setObjectName("remarks_value_pm")
        self.horizontalLayout_2.addWidget(self.remarks_value_pm)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(610, 600, 491, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reason_pm = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reason_pm.setFont(font)
        self.reason_pm.setObjectName("reason_pm")
        self.horizontalLayout_3.addWidget(self.reason_pm)
        self.reason_value_pm = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.reason_value_pm.setReadOnly(True)
        self.reason_value_pm.setObjectName("reason_value_pm")
        self.horizontalLayout_3.addWidget(self.reason_value_pm)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(1200, 600, 491, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.remarks_ehc = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remarks_ehc.setFont(font)
        self.remarks_ehc.setObjectName("remarks_ehc")
        self.horizontalLayout_4.addWidget(self.remarks_ehc)
        self.remarks_value_ehc = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.remarks_value_ehc.setReadOnly(True)
        self.remarks_value_ehc.setObjectName("remarks_value_ehc")
        self.horizontalLayout_4.addWidget(self.remarks_value_ehc)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remarks_value_ehc.setFont(font)
        self.remarks_value.setFont(font)
        self.reason_value_pm.setFont(font)
        self.remarks_value_pm.setFont(font)
        self.stackedWidget.addWidget(self.page_2)                 ## Adding the second page to the module
        self.table.cellClicked.connect(self.TakeAction)           ## The function is applied to clicking of a cell in a row
        self.sendback.clicked.connect(self.senditback)            ## The function performs the tasks required for asking query.
        self.submit.clicked.connect(self.approve)                 ## The function performs the tasks required for approving the request
        MainWindow.setCentralWidget(self.centralwidget)

        ## Menubar ###
        self.menubar = QtWidgets.QMenuBar(self.centralwidget)
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(0,0,0); color: #e0e0e0; font-size: 20px;} QMenuBar::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 20px;} QMenu{background-color: rgb(0,0,0); color: rgb(255,255,255); font-size: 18px; font-weight: 150} QMenu::item:selected{background-color: #e0e0e0; color: #2e2e2e; font-size: 18px;}")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 32))
        self.homescreen = QtWidgets.QAction("Home", self.menubar)
        self.font_1 = QtGui.QFont()
        self.font_1.setBold(True)
        self.font_1.setWeight(30)
        self.menubar.addAction(self.homescreen)
        self.modules_menu = self.menubar.addMenu("Modules")
        self.modules_menu.setFont(self.font_1)
        self.accessdashboard = QtWidgets.QAction("Dashboard", self.menubar)
        self.menubar.addAction(self.accessdashboard)
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
        connection = sqlite3.connect('./EY_1')
        cur = connection.cursor()
        cur.execute('select count(*) from Timesheet_PM where Sub_Unit = ? and Decision = "Approve"',(self.name_SBU,))  ## Counts the no. of Subcons who are under the Sub Unit "P" and the Decision of PM is Approve, i.e. without PM approving, the Subcon will not be added here.
        result, = cur.fetchone()
        self.rows = int(result)

    def senditback(self):
        remarks = self.remarks_value.toPlainText()
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        cur.execute('update Timesheet_PM set Remarks_SBU = ?, Decision_SBU = "Query for PM", Request_Status = "Pending With PM" where Subcon_ID = ? and Month = ? and Year = ?', (remarks,self.Subcon_ID, self.Month, self.year,))  ## Updates the relevant info for the selected Subcon, Month and Year.
        connection.commit()
        connection.close()
        self.loaddata_1()                        ## Load the data into the Initial Table
        self.stackedWidget.setCurrentIndex(0)    ## Set the current index of module to 0, which loads the page -1 of the Module.

    def approve(self):
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
        remarks = self.remarks_value.toPlainText()  ## Stores the remarks put in by the SBU Head
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        variance = str(self.variance_value.text())[:-1]
        ## The given conditions check whether the Request can be approved at this Level or has to be transfered to a higher authority ###
        if float(variance) <= 4:
            cur.execute('update Timesheet_PM set Remarks_SBU = ?, Decision_SBU = "Approve", Request_Status = "Approved" where Subcon_ID = ? and Month = ? and Year = ?', (remarks,self.Subcon_ID, month, self.year,))  ## Updates the relevant info for the selected Subcon, Month and Year
        else:
            cur.execute('update Timesheet_PM set Remarks_SBU = ?, Decision_SBU = "Approve", Request_Status = "Pending With EHC" where Subcon_ID = ? and Month = ? and Year = ?', (remarks,self.Subcon_ID, month, self.year,))
        connection.commit()
        connection.close()
        self.loaddata_1()                       ## Load the data into the Initial Table
        self.stackedWidget.setCurrentIndex(0)   ## Set the current index of module to 0, which loads the page -1 of the Module. 

    def TakeAction(self,row1):
        self.Subcon_ID = self.table.item(row1,0).text()    # Stores the Subcon ID of the clicked Subcon
        self.Month = self.table.item(row1,4).text()        # Stores the Month of the clicked Subcon
        self.loaddata_2()                                  #Loads data into Page - 2
        self.stackedWidget.setCurrentIndex(1)              # Set the current index of module to 1, which loads the page -2 of the Module. 

    def loaddata_2(self):
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
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        result = cur.execute('select * from Timesheet_PM where Subcon_ID = ? and Month = ?',(self.Subcon_ID,month,))
        for row in result:
            self.sid.setText(str(row[0]))              #Add values to line edits
            self.sname.setText(str(row[1]))
            self.unit_s.setText(str(row[2]))
            self.sunit.setText(str(row[3]))
            self.month_name.setText(self.Month)
            self.cname.setText(str(row[5]))
            self.cgname.setText(str(row[6]))
            self.pid.setText(str(row[7]))
            self.pdesc.setText(str(row[8]))
            self.vhours.setText(str(row[11]))
            self.vrate.setText(str(row[12]))
            self.pamount.setText(str(row[13]))
            self.chours.setText(str(row[14]))
            self.crate.setText(str(row[15]))
            self.nrc_value.setText(str(row[16]))
            self.bamount.setText(str(row[17]))
            self.nbamount.setText(str(row[18]))
            self.variance_value.setText(str(row[19]) + '%')
            self.remarks_value_pm.setText(str(row[20]))
            self.reason_value_pm.setText(str(row[21]))
            self.remarks_value_ehc.setText(str(row[59]))
            self.year = int(row[24])
            ## The Condition checks whether the SBU head has any previous comments for the requested Subcon
            if str(row[56]) != "None":
                self.remarks_value.setText(str(row[56]))
            self.year = int(row[24])
            ## These conditions are used to give a color to the variance, to highlight the variance they are going to accept/reject.
            variance = 100*(row[11] - row[14])/row[11]
            self.variance_value.setText(str(variance) + '%') ## Calculating Variance 
            ## Highlighting variance based on the value 
            if variance <= 2.0: 
                self.variance_value.setStyleSheet('background-color: rgb(144,238,144);')
            elif variance > 2.0 and variance <= 4.0:
                self.variance_value.setStyleSheet('background-color: rgb(255,191,0);')
            else:
                self.variance_value.setStyleSheet('background-color: rgb(255,0,0);')
            
        
        result = cur.execute('select * from Timesheet_PM where Subcon_ID = ? and Month < ?',(self.Subcon_ID,month, ))
        
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
            self.ytd_variance_value.setText(str(100*(timesheet_hours - ytd_rus)/timesheet_hours) + '%')
            if float(100*(timesheet_hours - ytd_rus)/timesheet_hours) <= 2.0: 
                self.ytd_variance_value.setStyleSheet('background-color: rgb(144,238,144);')
            elif float(100*(timesheet_hours - ytd_rus)/timesheet_hours) > 2.0 and float(100*(timesheet_hours - ytd_rus)/timesheet_hours) <= 4.0:
                self.ytd_variance_value.setStyleSheet('background-color: rgb(255,191,0);')
            else:
                self.ytd_variance_value.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            self.ytd_variance_value.setText("0.0%")
            self.ytd_variance_value.setStyleSheet('background-color: rgb(144,238,144);')

        connection.close()


    def loaddata_1(self):
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        print(self.name_SBU)
        result = cur.execute('select * from Timesheet_PM where Unit = ? and Decision = "Approve"',(self.name_SBU,))
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
            self.table.setItem(tablerow,4, QtWidgets.QTableWidgetItem(month))
            self.table.setItem(tablerow,9, QtWidgets.QTableWidgetItem(str(row[57])))
            tablerow+=1
        connection.close()

    ## Sets Text to all the Labels ##
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
        self.vendor_rate.setText(_translate("MainWindow", "Vendor Rate (per hour):"))
        self.payment_Amount.setText(_translate("MainWindow", "Payment Amount (USD):"))
        self.rus_hours.setText(_translate("MainWindow", "RUS Hours:"))
        self.customer_rate.setText(_translate("MainWindow", "Customer Rate (per hour):"))
        self.nrc.setText(_translate("MainWindow", "Non Resource Cost (USD):"))
        self.billable_amount.setText(_translate("MainWindow", "Billable Amount (USD):"))
        self.nonbillable_amount.setText(_translate("MainWindow", "Non-Billable Amount (USD):"))
        self.variance.setText(_translate("MainWindow", "Variance (in %):"))
        self.vendor_hours.setText(_translate("MainWindow", "Timesheet Hours:"))
        self.label.setText(_translate("MainWindow", "Subcon Timesheet and Details Filling"))
        self.remarks.setText(_translate("MainWindow", "SBU Remarks:"))
        self.sendback.setText(_translate("MainWindow", "Query for PM"))
        self.submit.setText(_translate("MainWindow", "Approve"))
        self.remarks_pm.setText(_translate("MainWindow", "Variance Description:"))
        self.reason_pm.setText(_translate("MainWindow", "Variance Category:"))
        self.remarks_ehc.setText(_translate("MainWindow", "EHC Remarks:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SBU_Timesheet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

