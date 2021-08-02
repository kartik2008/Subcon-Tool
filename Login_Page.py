from PyQt5 import QtCore, QtGui, QtWidgets

class login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ## The Login Page has been divided into 2 sections. The left section is the main login part. The right section is the decorative part.
        
        # Right Section 
        self.bgimage = QtWidgets.QLabel(self.centralwidget)
        self.bgimage.setGeometry(QtCore.QRect(600, 0, 1320, 1080))
        self.bgimage.setText("")
        self.bgimage.setPixmap(QtGui.QPixmap("images_1320x1080.jpeg"))   ## To change the back. img Upload the photo in the Subcon Solution Folder, and replace the name of the photo here.
        self.bgimage.setObjectName("bgimage")
        self.ey_logo = QtWidgets.QLabel(self.centralwidget)
        self.ey_logo.setGeometry(QtCore.QRect(1770, 960, 101, 101))
        self.ey_logo.setText("")
        self.ey_logo.setPixmap(QtGui.QPixmap("EY_100x100.png")) ## EY logo. If you want to change it, replace the new file here.
        self.ey_logo.setObjectName("ey_logo")  
        
        ## Left Section:- Has the Following features
        # 1) Clients' logo
        # 2) Content - Welcome, Let's Get you started
        # 3) Username and Password Options
        # 4) Login Button and Forgot
        # 5) Last Login feature
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 230, 381, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.company_logo = QtWidgets.QLabel(self.widget)
        self.company_logo.setText("")
        self.company_logo.setPixmap(QtGui.QPixmap("company_logo.jpeg"))    ## Change company's logo here.
        self.company_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.company_logo.setObjectName("company_logo")
        self.verticalLayout_2.addWidget(self.company_logo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.content_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.content_1.setFont(font)
        self.content_1.setAlignment(QtCore.Qt.AlignCenter)
        self.content_1.setObjectName("content_1")
        self.verticalLayout_2.addWidget(self.content_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.content_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.content_2.setFont(font)
        self.content_2.setAlignment(QtCore.Qt.AlignCenter)
        self.content_2.setObjectName("content_2")
        self.verticalLayout_2.addWidget(self.content_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.username = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username)
        self.email = QtWidgets.QLineEdit(self.widget)    ## Line Edit to enter email id
        self.email.setObjectName("email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.email)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.password = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.password)
        self.pwd = QtWidgets.QLineEdit(self.widget) ## Line Edit to enter Password 
        self.pwd.setObjectName("pwd")
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        reg_ex = QtCore.QRegExp('[a-zA-Z0-9._%+-@$]{8,10}')  ## Constraints on password, 8-10 characters, include lowercase, uppercase, 0-9 digits, and some symbols
        input_validator = QtGui.QRegExpValidator(reg_ex, self.pwd)
        self.pwd.setValidator(input_validator)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pwd)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 680, 241, 101))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.login = QtWidgets.QPushButton(self.widget1)
        self.login.setObjectName("login")
        self.verticalLayout_3.addWidget(self.login)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.forgot = QtWidgets.QPushButton(self.widget1)
        self.forgot.setObjectName("forgot")
        self.verticalLayout_3.addWidget(self.forgot)
        self.lastlogin = QtWidgets.QLabel(self.centralwidget)
        self.lastlogin.setGeometry(QtCore.QRect(50, 1016, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lastlogin.setFont(font)
        self.lastlogin.setObjectName("lastlogin")
        self.lastlogin_value = QtWidgets.QLabel(self.centralwidget)
        self.lastlogin_value.setGeometry(QtCore.QRect(140, 1020, 161, 17))
        self.lastlogin_value.setObjectName("lastlogin_value")
        self.content_1.raise_()
        self.content_2.raise_()
        self.login.raise_()
        self.forgot.raise_()
        self.content_1.raise_()
        self.content_2.raise_()
        self.company_logo.raise_()
        self.login.raise_()
        self.forgot.raise_()
        self.bgimage.raise_()
        self.ey_logo.raise_()
        self.lastlogin.raise_()
        self.lastlogin_value.raise_()
        self.flag = 0
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):   ## This function adds names to the Labels used in the Code. 
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lastlogin.setText(_translate("MainWindow", "Last Login:"))
        self.content_1.setText(_translate("MainWindow", "Welcome Back!"))
        self.content_2.setText(_translate("MainWindow", "Let\'s Get You Started"))
        self.username.setText(_translate("MainWindow", "Username"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.forgot.setText(_translate("MainWindow", "Forgot Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

