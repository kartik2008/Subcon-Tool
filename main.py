## Import self-made Python Modules from the Subcon Solution Folder##
## From each module import the relevant class ## 
## connection = sqlite.connect(databasename) is the line of code which needs to be replaced with the different database.
## For example: If we choose to use mysql database server then,
#connection = mysql.connector.connect(host='localhost',database='Electronics',user='pynative',password='pynative@#29')

from PyQt5 import QtCore, QtGui, QtWidgets
from Login_Page import login
from options import Modules
from Renewal_PM import PM_Renewal
from Renewal_PGM import PGM_Renewal
from Renewal_SBU import SBU_Renewal
from Renewal_EHC import EHC_Renewal
from allocation import Ui_MainWindow_4
from performance import Ui_MainWindow_5
from timesheet_subcon import Subcon_Timesheet
from timesheet_PM import PM_Timesheet
from timesheet_SBU import SBU_Timesheet
from vendor import Ui_MainWindow_7
from portfolio import Ui_MainWindow_8
from dashboard import ApplicationWindow
from hiring_RMG import RMG_hiring
from hiring_SBU import SBU_hiring
from hiring_EHC import EHC_hiring
import sys
import sqlite3   ## Library to import sqlite3, replace this with mysql connector of python
import random
import smtplib, ssl
from email.message import EmailMessage

class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = login()                                   ## Create an object of the class login, which setups the Login Page
        self.ui.setupUi(self)    
        self.ui.login.clicked.connect(self.validate)        ## This function validates the login id and password
        self.ui.forgot.clicked.connect(self.sendemail)      ## Function to send emails to user who click on forgot password button

    def validate(self):
        self.user = self.ui.email.text()                    ## Stores username
        self.passwd = self.ui.pwd.text()                    ## Stores password
        connection = sqlite3.connect("EY")                  ## connect with Database "EY" 
        cur = connection.cursor()                           
        
        result = cur.execute('Select last_login from User_Info where username = ?', (self.user,))  ## Stores the last login
        
        for last in result:
            self.ui.lastlogin_value.setText(str(last[0])) 
        
        result = cur.execute('SELECT EXISTS (SELECT 1 FROM User_Info WHERE username = ? AND password = ?)', (self.user, self.passwd,)) # Check if the username and password is correct, this gives 1 if there exists a user, and 0 if not
        for row in result:
            if row[0]:              ## If user exists, then store his role and name   
                ans = cur.execute('SELECT * FROM User_Info where username = ?', (self.user,))
                for roles in ans:
                    self.role = str(roles[5])
                    self.name = str(roles[6])
                    self.name_ID = str(roles[7])
                
                cur.execute('update User_Info set last_login = datetime("now") where username = ?', (self.user,))
                self.gotohome()     ## Go to the Page which displays options.
            else:                   ## If the password is not valid
                if self.ui.flag:    ## If temporary password is valid then check temp pass and username and give access if correct
                    result_1 = cur.execute('SELECT EXISTS (SELECT 1 FROM User_Info WHERE username = ? AND temp_password = ?)', (self.user, str(self.temp),))
                    for row_1 in result_1:
                        if row_1[0]:
                            self.flag = 0
                            ans = cur.execute('SELECT * FROM User_Info where username = ?', (self.user,))
                            for roles in ans:
                                self.role = roles[5]
                                self.name = roles[6]
                                self.name_ID = str(roles[7])
                            
                            cur.execute('update User_Info set last_login = datetime("now") where username = ?', (self.user,))
                            cur.execute('update User_Info set temp_password = ""')
                            self.gotohome()
                        else:
                            self.error_dialog = QtWidgets.QErrorMessage()
                            self.error_dialog.showMessage('Wrong Password')  
                else:   ## Else display error message
                    self.error_dialog = QtWidgets.QMessageBox()
                    self.error_dialog.setText("Wrong Username or Password")
                    self.error_dialog.setWindowTitle("Attention!")
                    self.error_dialog.exec_()
                
        connection.commit()
        connection.close()
        
                
    def sendemail(self):
        self.user = self.ui.email.text()   ## stores the email address
        self.temp = random.randint(1000000,99999999)   ### generates a random temp password 
        connection = sqlite3.connect("EY")
        cur = connection.cursor()
        cur.execute('Update User_Info set temp_password = ?, Temp_time = datetime("now") where username = ?', (str(self.temp), self.user,)) ## shows temp password and current time. 
        connection.commit()
        connection.close()
        ## Email Sending code ##
        msg = EmailMessage()  
        msg.set_content("Your temporary password is: " + str(self.temp) + "\n" + "\n" + "This Password shall remain active only for 10 mins, post which it becomes invalid.")
        msg["Subject"] = "Temporary password"
        msg["From"] = ""    ## Adding the email id which is to be used for sending temporary password
        msg["To"] = self.user    

        context=ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:  ## For gmail, we use Port 587
            smtp.starttls(context=context)  
            smtp.login(msg["From"], "") ## Add the password associated with the senders' email id in "".   
            smtp.send_message(msg)
        
        self.ui.flag = 1    ## set the flag as 1 to allow the system to know that it should check for the username and temporary password

    def gotosubconextension(self):    ## Function to access the Subcon Renewal Module
        ## Only the Project Manager, Program Manager, SBU Head and EHC Approver can access this module. If it is one of them, then open their pages.
        if self.role == "PM" or self.role == "PGM" or self.role == "SBU Head" or self.role == "EHC": 
            if self.role == "PM":
                self.ui_1 = PM_Renewal()
                self.ui_1.name_PM = self.name_ID
                self.ui_1.setupUi(self)
            elif self.role == "PGM":
                self.ui_1 = PGM_Renewal()
                self.ui_1.name_PGM = self.name_ID
                self.ui_1.setupUi(self)
            elif self.role == "SBU Head":
                self.ui_1 = SBU_Renewal()
                self.ui_1.name_SBU = self.name_ID
                self.ui_1.setupUi(self)
            else:
                self.ui_1 = EHC_Renewal()
                self.ui_1.setupUi(self)
            self.ui_1.homescreen.triggered.connect(self.gotohome)   ## Giving functionality to home menu in menubar
            self.ui_1.accessdashboard.triggered.connect(self.gotodashboard)  ## Giving functionality to dashboard menu in menubar
            self.profile = self.ui_1.menubar.addMenu(self.name)    ## Adding name of person on the menubar and adding functionality to logout from the tool.
            self.logout = QtWidgets.QAction("Logout", self.ui_1.menubar)
            self.profile.addAction(self.logout)
            self.logout.triggered.connect(self.gotologinpage)  
        else:   ## If someone else tries to access the module, then showing an error.
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setText("You cannot access this module")
            self.error_dialog.exec_()   
    
    def gotosubconhiring(self): ## Function to access the Subcon Hiring Request Module
        ## Only the Corp RMG, SBU Head and EHC Approver can access this module. If it is one of them, then open their pages.
        if self.role == "RMG" or self.role == "SBU Head" or self.role == "EHC":
            if self.role == "RMG":
                self.ui_2 = RMG_hiring()
                self.ui_2.name_RMG = self.name_ID
                self.ui_2.setupUi(self)
            elif self.role == "SBU Head":
                self.ui_2 = SBU_hiring()
                self.ui_2.name_SBU = self.name_ID
                self.ui_2.setupUi(self)
            else:
                self.ui_2 = EHC_hiring()
                self.ui_2.setupUi(self)
            self.ui_2.homescreen.triggered.connect(self.gotohome)
            self.ui_2.accessdashboard.triggered.connect(self.gotodashboard)
            self.profile = self.ui_2.menubar.addMenu(self.name)
            self.logout = QtWidgets.QAction("Logout", self.ui_2.menubar)
            self.profile.addAction(self.logout)
            self.logout.triggered.connect(self.gotologinpage)
        else:   ## If someone else tries to access the module, then showing an error.
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setText("You cannot access this module")
            self.error_dialog.exec_() 

    def gotosubconallocation(self):     ## Function to access the Subcon Allocation Update Module
        if self.role == "PM":
            self.ui_4 = Ui_MainWindow_4()
            self.ui_4.setupUi_4(self)
            self.ui_4.home.clicked.connect(self.gotohome)
    
    def gotosubconperformance(self):  ## Function to access the Subcon Performance Evaluation Module
        if self.role == "PM":
            self.ui_5 = Ui_MainWindow_5()
            self.ui_5.setupUi_5(self)
            self.ui_5.home.clicked.connect(self.gotohome)
    
    def gototimesheet(self):    ## Function to access the Timesheet & Expenses Module
        ## Only the Subcon, SBU Head and Project Manager can access this module. If it is one of them, then open their pages.
        if self.role == "PM" or self.role == "SBU Head" or self.role == "Subcon":
            if self.role == "PM":
                self.ui_17 = PM_Timesheet()
                self.ui_17.name_PM = self.name_ID
                self.ui_17.setupUi(self)
            elif self.role == "SBU Head":
                self.ui_17 = SBU_Timesheet()
                self.ui_17.name_SBU = self.name_ID
                self.ui_17.setupUi(self)
            elif self.role == "Subcon":
                self.ui_17 = Subcon_Timesheet()
                self.ui_17.setupUi(self)
            self.ui_17.homescreen.triggered.connect(self.gotohome)
            self.ui_17.accessdashboard.triggered.connect(self.gotodashboard)
            self.profile = self.ui_17.menubar.addMenu(self.name)
            self.logout = QtWidgets.QAction("Logout", self.ui_17.menubar)
            self.profile.addAction(self.logout)
            self.logout.triggered.connect(self.gotologinpage)  
        else:   ## If someone else tries to access the module, then showing an error.
            self.error_dialog = QtWidgets.QMessageBox()
            self.error_dialog.setText("You cannot access this module")
            self.error_dialog.exec_() 

    def gotovendor(self):   ## Function to access the Vendor Management Module
        if self.role == "PM":
            self.ui_7 = Ui_MainWindow_7()
            self.ui_7.setupUi_7(self)
    
    def gotosubconportfolio(self):     ## Function to access the Subcon Portfolio Module
        if self.role == "PM":
            self.ui_8 = Ui_MainWindow_8()
            self.ui_8.setupUi_8(self)
            self.ui_8.home.clicked.connect(self.gotohome)
    def gotodashboard(self):        ## Function to access the Dashboard Module
        self.ui_9 = ApplicationWindow()
        self.ui_9.__init__()

    def gotohome(self):         ## Function to access the Home Page
        self.ui_10 = Modules()
        self.ui_10.setupUi(self)
        self.ui_10.Subconextensionicon.clicked.connect(self.gotosubconextension)
        self.ui_10.Subconhiringicon.clicked.connect(self.gotosubconhiring)
        #self.ui_10.Subconallocationicon.clicked.connect(self.gotosubconallocation)
        #self.ui_10.Subconperformanceicon.clicked.connect(self.gotosubconperformance)
        self.ui_10.Timesheeticon.clicked.connect(self.gototimesheet)
        #self.ui_10.Subconportfolioicon.clicked.connect(self.gotosubconportfolio)
        self.ui_10.Dashboardicon.clicked.connect(self.gotodashboard)
        #self.ui_10.Vendoricon.clicked.connect(self.gotovendor)
        self.profile = self.ui_10.menubar.addMenu(self.name)
        self.logout = QtWidgets.QAction("Logout", self.ui_10.menubar)
        self.profile.addAction(self.logout)
        self.logout.triggered.connect(self.gotologinpage)
    
    def gotologinpage(self):
        self.ui = login()
        self.ui.setupUi(self)
        self.ui.login.clicked.connect(self.validate)
        self.ui.forgot.clicked.connect(self.sendemail)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    kartik = mainwindow()
    kartik.show()
    sys.exit(app.exec_())
