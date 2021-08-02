from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime
import calendar

class Subcon_Timesheet(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1850, 1084)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 100, 1781, 220))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(220, 60, 521, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.projectid = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.projectid.setFont(font)
        self.projectid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.projectid.setObjectName("projectid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.projectid)
        self.pid = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pid.setFont(font)
        self.pid.setObjectName("pid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pid)
        self.projectdesc = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.projectdesc.setFont(font)
        self.projectdesc.setObjectName("projectdesc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.projectdesc)
        self.pdesc = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pdesc.setFont(font)
        self.pdesc.setObjectName("pdesc")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pdesc)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(1030, 60, 521, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.projectmanager = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.projectmanager.setFont(font)
        self.projectmanager.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.projectmanager.setObjectName("projectmanager")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.projectmanager)
        self.pm = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pm.setFont(font)
        self.pm.setObjectName("pm")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pm)
        self.month = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.month.setFont(font)
        self.month.setObjectName("month")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.month)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.options = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.options.setObjectName("options")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.options)
        self.pid.setReadOnly(True)
        self.pdesc.setReadOnly(True)
        self.pm.setReadOnly(True)
        self.timesheet = QtWidgets.QLabel(self.centralwidget)
        self.timesheet.setGeometry(QtCore.QRect(30, 60, 1781, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.timesheet.setFont(font)
        self.timesheet.setFrameShape(QtWidgets.QFrame.Box)
        self.timesheet.setAlignment(QtCore.Qt.AlignCenter)
        self.timesheet.setObjectName("timesheet")
        
        current_month = datetime.now().month  ## Determines the current Month
        self.year = datetime.now().year  ## Determines the current year
        ## User shall get a 5 month window to fill the timesheet. 2 previous months, 1 current month, 2 next months
        if current_month == 1: ## Depending on the number associated with the month, we add options. January = 1 
            self.options.addItems(["November", "December","January","February","March"])
        elif current_month == 2:
            self.options.addItems(["December","January","February","March","April"])
        elif current_month == 3:
            self.options.addItems(["January","February","March","April","May"])
        elif current_month == 4:
            self.options.addItems(["February","March","April","May","June"])
        elif current_month == 5:
            self.options.addItems(["March","April","May","June","July"])
        elif current_month == 6:
            self.options.addItems(["April","May","June","July","August"])
        elif current_month == 7:
            self.options.addItems(["May","June","July","August","September"])
        elif current_month == 8:
            self.options.addItems(["June","July","August","September","October"])
        elif current_month == 9:
            self.options.addItems(["July","August","September","October","November"])
        elif current_month == 10:
            self.options.addItems(["August","September","October","November","December"])
        elif current_month == 11:
            self.options.addItems(["September","October","November","December","January"])
        else:
            self.options.addItems(["October","November","December","January","February"])
        
        self.loaddata()  
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(660, 360, 521, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        ## Once the person has selected the month of his/her choice, he can update or review his timesheet for that month.
        self.update = QtWidgets.QPushButton(self.horizontalLayoutWidget)   ## Update button
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update.setFont(font)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.review = QtWidgets.QPushButton(self.horizontalLayoutWidget)  ## Review Button
        font = QtGui.QFont()
        font.setPointSize(11)
        self.review.setFont(font)
        self.review.setObjectName("review")
        self.horizontalLayout.addWidget(self.review)
        self.update.clicked.connect(self.showupdate)
        self.review.clicked.connect(self.showreview)
        self.tablewidget = QtWidgets.QTableWidget(self.centralwidget)  ## Timesheet filling table
        self.tablewidget.setGeometry(QtCore.QRect(40, 440, 1731, 291))
        self.tablewidget.setRowCount(6)
        self.tablewidget.setColumnCount(8)
        self.tablewidget.setObjectName("tablewidget")
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tablewidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget.setItem(1, 0, item)
        self.tablewidget.horizontalHeader().setDefaultSectionSize(210)
        self.tablewidget.verticalHeader().setDefaultSectionSize(45)
        
        self.vendor_hours = QtWidgets.QLabel(self.centralwidget)  ## Shows the vendor hours added by the Subcon. Value increases as the Subcon fills the timesheet.
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vendor_hours.setFont(font)
        self.vendor_hours.setText("Vendor Hours")
        self.vendor_hours.setObjectName("vendor_hours")
        self.vendor_hours.setGeometry(QtCore.QRect(390,830,130,35))
        self.vhours = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vhours.setFont(font)
        self.vhours.setReadOnly(True)
        self.vhours.setObjectName("vhours")
        self.vhours.setGeometry(QtCore.QRect(530,830,200,35))

        self.Remark_pm = QtWidgets.QLabel(self.centralwidget)  ## PM remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remark_pm.setFont(font)
        self.Remark_pm.setObjectName("Remark_pm")
        self.Remark_pm.setText("PM Remarks:")
        self.Remark_pm.setGeometry(QtCore.QRect(760,830,120,35))
        self.Remark_value_pm = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Remark_value_pm.setFont(font)
        self.Remark_value_pm.setObjectName("Remark_value_pm")
        self.Remark_value_pm.setReadOnly(True)
        self.Remark_value_pm.setGeometry(QtCore.QRect(910,830,300,35))

        self.Remarks = QtWidgets.QLabel(self.centralwidget)  ## Subcon Remarks
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remarks.setFont(font)
        self.Remarks.setObjectName("Remarks")
        self.Remarks.setText("Subcon Remarks:")
        self.Remarks.setGeometry(QtCore.QRect(1240,830,120,35))
        self.Remarks_value = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Remarks_value.setFont(font)
        self.Remarks_value.setObjectName("Remarks_value")
        self.Remarks_value.setGeometry(QtCore.QRect(1370,830,300,35))

        self.submit = QtWidgets.QPushButton()  ## Submit Button
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(720,920,200,40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        self.save = QtWidgets.QPushButton()  ## Save Button
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(950,920,200,40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.save.setText("Save")
        self.updated = 0
        self.reviewed = 0
        self.data()
        self.submit.clicked.connect(self.submittoPM)
        self.save.clicked.connect(self.saveprogress)
        self.vhours.setText("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.tablewidget.itemChanged.connect(self.calculatevendorhours)
        self.options.activated[str].connect(self.data)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def data(self):  ## auto-fill the Previous Remarks of Subcon and PM for the given month
        selected_month = self.options.currentText()  ## stores the name of month selected
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        result = cur.execute('select Remarks_Subcon, Remarks from Timesheet_PM where Subcon_ID = 2025 and Month = ?',(selected_month,))
        for row in result:
            self.Remarks_value.setText(str(row[0]))
            self.Remark_value_pm.setText(str(row[1]))

    def calculatevendorhours(self):  ## Calculate the vendor hours. Explaination is written in Timesheet_SBU and Timesheet_PM
        self.selectedmonth = self.options.currentText()
        values = []
        if self.selectedmonth == "January":
            month = 1
        elif self.selectedmonth == "February":
            month = 2
        elif self.selectedmonth == "March":
            month = 3
        elif self.selectedmonth == "April":
            month = 4
        elif self.selectedmonth == "June":
            month = 6
        elif self.selectedmonth == "July":
            month = 7
        elif self.selectedmonth == "August":
            month = 8
        elif self.selectedmonth == "September":
            month = 9
        elif self.selectedmonth == "May":
            month = 5
        elif self.selectedmonth == "October":
            month = 10
        elif self.selectedmonth == "November":
            month = 11
        else:
            month = 12
        daynumber = calendar.weekday(self.year,month,1)
        tablecol = daynumber
        k = 0
        for i in range(31):
            if tablecol <= 6:
                if self.tablewidget.item(1,tablecol) is not None:
                    if self.tablewidget.item(1,tablecol).text() != '':
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
                            values.append(float(self.tablewidget.item(j,i).text()))
                        else:
                            values.append(float(0))
                else:
                    break
                k+=1
        if len(values) == 30:
            values.append(float(0))
        vhours = sum(values)
        self.vhours.setText(str(sum(values)))

    def submittoPM(self): ## Function gets executed when Submit button is clicked
        values = []  ## Stores the values added in Timesheet
        self.selectedmonth = self.options.currentText()
        if self.selectedmonth == "January":
            month = 1
        elif self.selectedmonth == "February":
            month = 2
        elif self.selectedmonth == "March":
            month = 3
        elif self.selectedmonth == "April":
            month = 4
        elif self.selectedmonth == "June":
            month = 6
        elif self.selectedmonth == "July":
            month = 7
        elif self.selectedmonth == "August":
            month = 8
        elif self.selectedmonth == "September":
            month = 9
        elif self.selectedmonth == "May":
            month = 5
        elif self.selectedmonth == "October":
            month = 10
        elif self.selectedmonth == "November":
            month = 11
        else:
            month = 12

        ## Finds which day was on 1st of the selected month
        daynumber = calendar.weekday(self.year,month,1)
        tablecol = daynumber
        k = 0
        ## Stores the values in the timesheet. Whenever there is no value added, add 0 in its place
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
        
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        ## Store the relevant info from Subcon_Info table and add into Timesheet_PM and Timesheet_Subcon
        result = cur.execute('select Subcon_Name,Unit, Sub_Unit,Customer_Name, Customer_Group_Name,Contract_Type, Vendor_Name, Vendor_Rate, Customer_Rate from Subcon_Info where Subcon_ID = 2025')
        for row in result:
            name = str(row[0])
            unit = str(row[1])
            subunit = str(row[2])
            customer = str(row[3])
            customergroup = str(row[4])
            contract = str(row[5])
            vendor = str(row[6])
        
        connection.close()
        
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        if self.updated:  ## If the person is filling the sheet, then insert a new row with relevant info
            cur.execute('insert into Timesheet_Subcon (Subcon_ID,Project_ID,Project_Description, Project_Manager,Month, Year,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,Total_Hours, Remarks_Subcon) VALUES (2025,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(self.pid.text(),self.pdesc.text(),self.pm.text(),self.selectedmonth,self.year,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.Remarks_value.toPlainText(),))
            cur.execute('insert into Timesheet_PM (Subcon_ID,Project_ID,Project_Description, Project_Manager,Month, Year,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,Total_Hours, Remarks_Subcon, Request_Status, Decision) VALUES (2025,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,NULL)',(self.pid.text(),self.pdesc.text(),self.pm.text(),self.selectedmonth,self.year,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.Remarks_value.toPlainText(),"Pending with PM",))
            self.updated = 0
        
        else:  ## else, update the info for the current month and year
            cur.execute('update Timesheet_Subcon set one = ?,two = ?,three = ?,four = ?,five = ?,six = ?,seven = ?,eight = ?,nine = ?,ten = ?,eleven = ?,twelve = ?,thirteen = ?,fourteen = ?,fifteen = ?,sixteen = ?,seventeen = ?,eighteen = ?,nineteen = ?,twenty = ?,twentyone = ?,twentytwo = ?,twentythree = ?,twentyfour = ?,twentyfive = ?,twentysix = ?,twentyseven = ?,twentyeight = ?,twentynine = ?,thirty = ?,thirtyone = ?,Total_Hours = ?, Remarks_Subcon = ? where Subcon_ID = 2025 and Month = ? and Year = ?',(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.selectedmonth,self.year,self.Remarks_value.toPlainText(),))
            cur.execute('update Timesheet_PM set one = ?,two = ?,three = ?,four = ?,five = ?,six = ?,seven = ?,eight = ?,nine = ?,ten = ?,eleven = ?,twelve = ?,thirteen = ?,fourteen = ?,fifteen = ?,sixteen = ?,seventeen = ?,eighteen = ?,nineteen = ?,twenty = ?,twentyone = ?,twentytwo = ?,twentythree = ?,twentyfour = ?,twentyfive = ?,twentysix = ?,twentyseven = ?,twentyeight = ?,twentynine = ?,thirty = ?,thirtyone = ?,Total_Hours = ?, Remarks_Subcon = ? where Subcon_ID = 2025 and Month = ? and Year = ?',(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.selectedmonth,self.year,self.Remarks_value.toPlainText(),))
            self.reviewed = 0
        
        cur.execute('update Timesheet_PM set Subcon_Name = ?, Unit = ?, Sub_Unit = ?, Customer_Name = ?, Customer_Group_Name = ?, Contract_Type = ?, Vendor_Name = ? where Subcon_ID = 2025 and Month = ? and Year = ?',(name,unit,subunit,customer,customergroup,contract,vendor,self.selectedmonth,self.year,))
        connection.commit()
        connection.close()
        ## Show the message Timesheet submitted.
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setText("Your Timesheet has been submitted to the Project Manager for Approval")
        self.error_dialog.exec_()

    def saveprogress(self): ## Similar to submittoPM, but values are not added in the Timesheet_PM table.
        values = []
        self.selectedmonth = self.options.currentText()
        if self.selectedmonth == "January":
            month = 1
        elif self.selectedmonth == "February":
            month = 2
        elif self.selectedmonth == "March":
            month = 3
        elif self.selectedmonth == "April":
            month = 4
        elif self.selectedmonth == "June":
            month = 6
        elif self.selectedmonth == "July":
            month = 7
        elif self.selectedmonth == "August":
            month = 8
        elif self.selectedmonth == "September":
            month = 9
        elif self.selectedmonth == "May":
            month = 5
        elif self.selectedmonth == "October":
            month = 10
        elif self.selectedmonth == "November":
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
        
        connection = sqlite3.connect('EY_1')
        cur = connection.cursor()
        if self.updated:
            cur.execute('insert into Timesheet_Subcon (Subcon_ID,Project_ID,Project_Description, Project_Manager,Month, Year,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,Total_Hours) VALUES (2025,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(self.pid.text(),self.pdesc.text(),self.pm.text(),self.selectedmonth,self.year,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),))
            self.updated = 0
        
        else:
            cur.execute('update Timesheet_Subcon set one = ?,two = ?,three = ?,four = ?,five = ?,six = ?,seven = ?,eight = ?,nine = ?,ten = ?,eleven = ?,twelve = ?,thirteen = ?,fourteen = ?,fifteen = ?,sixteen = ?,seventeen = ?,eighteen = ?,nineteen = ?,twenty = ?,twentyone = ?,twentytwo = ?,twentythree = ?,twentyfour = ?,twentyfive = ?,twentysix = ?,twentyseven = ?,twentyeight = ?,twentynine = ?,thirty = ?,thirtyone = ?,Total_Hours = ? where Subcon_ID = 2025 and Month = ? and Year = ?',(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11],values[12],values[13],values[14],values[15],values[16],values[17],values[18],values[19],values[20],values[21],values[22],values[23],values[24],values[25],values[26],values[27],values[28],values[29],values[30],sum(values),self.selectedmonth,self.year,))
            self.reviewed = 0
        connection.commit()
        connection.close()

        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setText("Your Timesheet has been saved. You can update the same by Clicking on Review my Timesheet Button")
        self.error_dialog.exec_()
    
    def showupdate(self):  ## When Fill my timesheet is chose, clear the contents of table and let user fill the timesheet from beginning
        self.updated = 1
        self.reviewed = 0
        for i in range(8):
            for j in range(6):
                self.tablewidget.setItem(j,i,QtWidgets.QTableWidgetItem(str("")))
        self.selectedmonth = self.options.currentText()
        if self.selectedmonth == "January":
            month = 1
        elif self.selectedmonth == "February":
            month = 2
        elif self.selectedmonth == "March":
            month = 3
        elif self.selectedmonth == "April":
            month = 4
        elif self.selectedmonth == "June":
            month = 6
        elif self.selectedmonth == "July":
            month = 7
        elif self.selectedmonth == "August":
            month = 8
        elif self.selectedmonth == "September":
            month = 9
        elif self.selectedmonth == "May":
            month = 5
        elif self.selectedmonth == "October":
            month = 10
        elif self.selectedmonth == "November":
            month = 11
        else:
            month = 12

        self.tablewidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
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
        ## Gives background color to Saturday and Sunday Columns.
        for i in range(5,7):
            for j in range(6):
                self.tablewidget.item(j,i).setBackground(QtGui.QColor(211,211,211))

        ## Disable editing of Dates##
        for i in range(7):
            self.tablewidget.item(0,i).setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

        ## Function to calculate and display total hours per week ##
        for i in range(1,6):
            sum_1 = 0
            for j in range(7):
                if self.tablewidget.item(i,j) is not None:
                    if self.tablewidget.item(i,j).text() != '':
                        sum_1 = sum_1 + float(self.tablewidget.item(i,j).text())
            self.tablewidget.setItem(i,7,QtWidgets.QTableWidgetItem(str(sum_1)))
            self.tablewidget.item(i,7).setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 
        
        
    def showreview(self):  
        self.reviewed = 1
        self.updated = 0
        self.selectedmonth = self.options.currentText()
        for i in range(8):
            for j in range(6):
                self.tablewidget.setItem(j,i,QtWidgets.QTableWidgetItem(str("")))
        
        if self.selectedmonth == "January":
            month = 1
        elif self.selectedmonth == "February":
            month = 2
        elif self.selectedmonth == "March":
            month = 3
        elif self.selectedmonth == "April":
            month = 4
        elif self.selectedmonth == "June":
            month = 6
        elif self.selectedmonth == "July":
            month = 7
        elif self.selectedmonth == "August":
            month = 8
        elif self.selectedmonth == "September":
            month = 9
        elif self.selectedmonth == "May":
            month = 5
        elif self.selectedmonth == "October":
            month = 10
        elif self.selectedmonth == "November":
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
        result = cur.execute('select * from Timesheet_Subcon where Subcon_ID = 2025 and Month = ? and Year = ?',(self.selectedmonth,self.year,))
        k = 0
        for row in result:
            for i in range(7):
                if tablecol <= 6:
                    self.tablewidget.setItem(1,tablecol,QtWidgets.QTableWidgetItem(str(row[k+6])))
                    tablecol+=1
                    k+=1
                else:
                    break
            for i in range(7):
                self.tablewidget.setItem(2,i,QtWidgets.QTableWidgetItem(str(row[k+6])))
                k+=1
            for i in range(7):
                self.tablewidget.setItem(3,i,QtWidgets.QTableWidgetItem(str(row[k+6])))
                k+=1
            for i in range(7):
                self.tablewidget.setItem(4,i,QtWidgets.QTableWidgetItem(str(row[k+6])))
                k+=1
            for i in range(7):
                if k < 31:
                    self.tablewidget.setItem(5,i,QtWidgets.QTableWidgetItem(str(row[k+6])))
                    k+=1

        for i in range(1,6):
            sum_1 = 0
            for j in range(7):
                if self.tablewidget.item(i,j) is not None:
                    if self.tablewidget.item(i,j).text() != '':
                        sum_1 = sum_1 + float(self.tablewidget.item(i,j).text())
            self.tablewidget.setItem(i,7,QtWidgets.QTableWidgetItem(str(sum_1)))
            self.tablewidget.item(i,7).setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) 

        for i in range(5,7):
            for j in range(6):
                self.tablewidget.item(j,i).setBackground(QtGui.QColor(211,211,211))   
        
    def loaddata(self):
        connection = sqlite3.connect('EY')
        cur = connection.cursor()
        result = cur.execute('select Project_ID, Project_Desc, Project_Manager from Subcon_Info where Subcon_ID = 2025')
        for row in result:
            self.pid.setText(str(row[0]))
            self.pdesc.setText(str(row[1]))
            self.pm.setText(str(row[2]))
        connection.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.projectid.setText(_translate("MainWindow", "Project ID:"))
        self.projectdesc.setText(_translate("MainWindow", "Project Description:"))
        self.projectmanager.setText(_translate("MainWindow", "Project Manager:"))
        self.month.setText(_translate("MainWindow", "Month:"))
        self.timesheet.setText(_translate("MainWindow", "TIMESHEET"))
        self.update.setText(_translate("MainWindow", "Fill My Timesheet"))
        self.review.setText(_translate("MainWindow", "Review My Timesheet"))
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
    ui = Subcon_Timesheet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

