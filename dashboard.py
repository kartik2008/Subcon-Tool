import sys
import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

from matplotlib.backends.qt_compat import QtCore, QtWidgets, QtGui
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import sqlite3

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self._main.resize(1850,1000)
        self.setCentralWidget(self._main)
        
        self.gridlayout_1 = QtWidgets.QWidget(self._main)
        self.gridlayout_1.setGeometry(QtCore.QRect(0,0,1700,50))
        self.gridlayout = QtWidgets.QGridLayout(self.gridlayout_1)
        self.sbu_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sbu_label.setFont(font)
        self.sbu_label.setText("SBU: ")
        self.sbu_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.sbu_label,0,0)
        self.gridlayout.addWidget(self.sbu_options,0,1)

        self.ibg_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ibg_label.setFont(font)
        self.ibg_label.setText("IBG: ")
        self.ibg_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.ibg_label,0,2)
        self.gridlayout.addWidget(self.ibg_options,0,3)

        self.ibu_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ibu_label.setFont(font)
        self.ibu_label.setText("IBU: ")
        self.ibu_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.ibu_label,0,4)
        self.gridlayout.addWidget(self.ibu_options,0,5)

        self.location_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.location_label.setFont(font)
        self.location_label.setText("Location: ")
        self.location_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.location_label,0,6)
        self.gridlayout.addWidget(self.location_options,0,7)

        self.month_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.month_label.setFont(font)
        self.month_label.setText("Month: ")
        self.month_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.month_label,0,8)
        self.gridlayout.addWidget(self.month_options,0,9)

        self.year_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.year_label.setFont(font)
        self.year_label.setText("Year: ")
        self.year_options = QtWidgets.QComboBox()
        self.gridlayout.addWidget(self.year_label,0,10)
        self.gridlayout.addWidget(self.year_options,0,11)

        self.sbu_label.setFixedWidth(60)
        self.ibg_label.setFixedWidth(60)
        self.ibu_label.setFixedWidth(60)
        self.month_label.setFixedWidth(60)
        self.year_label.setFixedWidth(60)
        self.location_label.setFixedWidth(80)

        

        self.layout_1 = QtWidgets.QWidget(self._main)
        self.layout_1.setGeometry(QtCore.QRect(0,50,600,950))
        self.layout = QtWidgets.QVBoxLayout(self.layout_1)
        # self.button = QtWidgets.QPushButton()
        # self.button.setText("Kartik")
        # self.layout.addWidget(self.button)
        self.subcon_movement = FigureCanvas(Figure(figsize=(5, 3)))
        self.toolbar_1 = NavigationToolbar(self.subcon_movement, self)
        self.layout.addWidget(self.toolbar_1)
        self.layout.addWidget(self.subcon_movement)

        self.cost_movement = FigureCanvas(Figure(figsize=(5, 3)))
        self.toolbar_2 = NavigationToolbar(self.cost_movement, self)
        self.layout.addWidget(self.toolbar_2)
        self.layout.addWidget(self.cost_movement)
        
        
        self.layout_2 = QtWidgets.QWidget(self._main)
        self.layout_2.setGeometry(QtCore.QRect(610,50,600,950))
        self.layout_2 = QtWidgets.QVBoxLayout(self.layout_2)
        # self.button = QtWidgets.QPushButton()
        # self.button.setText("Kartik")
        # self.layout.addWidget(self.button)
        self.TM_movement = FigureCanvas(Figure(figsize=(5, 3)))
        self.toolbar_3 = NavigationToolbar(self.TM_movement, self)
        self.layout_2.addWidget(self.toolbar_3)
        self.layout_2.addWidget(self.TM_movement)
        
        self.W2_movement = FigureCanvas(Figure(figsize=(5, 3)))
        self.toolbar_5 = NavigationToolbar(self.W2_movement, self)
        self.layout_2.addWidget(self.toolbar_5)
        self.layout_2.addWidget(self.W2_movement)

        
        
        self.layout_3 = QtWidgets.QWidget(self._main)
        self.layout_3.setGeometry(QtCore.QRect(1220,50,600,485))
        self.layout_3 = QtWidgets.QVBoxLayout(self.layout_3)
        # self.button = QtWidgets.QPushButton()
        # self.button.setText("Kartik")
        # self.layout.addWidget(self.button)
        self.hiring_movement = FigureCanvas(Figure(figsize=(5, 3)))
        self.toolbar_4 = NavigationToolbar(self.hiring_movement, self)
        self.layout_3.addWidget(self.toolbar_4)
        self.layout_3.addWidget(self.hiring_movement)


        df = pd.read_excel("/home/kartikg/Desktop/Subcon Solution/subcon report.xlsx", sheet_name = "Subcon Base")

        df_1 = pd.read_excel("/home/kartikg/Desktop/Subcon Solution/subcon report.xlsx", sheet_name = "Data")

        self.dataframe = df
        self.provideoptions()

        df['DATE OF JOINING'] = pd.to_datetime(df['DATE OF JOINING']).dt.date
        df['DEACTIVATION DATE'] = pd.to_datetime(df['DEACTIVATION DATE']).dt.date
        df1 = df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "T&M")]
        march_TM = len(df1.index)
        df2 = df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "Cap T&M")]
        march_capTM = len(df2.index)
        df3 = df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "FP")]
        march_FP = len(df3.index)

        df4 = df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "T&M")]
        april_TM = len(df4.index)
        df5 = df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "Cap T&M")]
        april_capTM = len(df5.index)
        df6 = df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "FP")]
        april_FP = len(df6.index)

        df7 = df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "T&M")]
        may_TM = len(df7.index)
        df8 = df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "Cap T&M")]
        may_capTM = len(df8.index)
        df9 = df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "FP")]
        may_FP = len(df9.index)

        df10 = df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "T&M")]
        june_TM = len(df4.index)
        df11 = df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "Cap T&M")]
        june_capTM = len(df5.index)
        df12 = df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull())) & (df['CONTRACT_TYPE'] == "FP")]
        june_FP = len(df6.index)

        data = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'FP' : [march_FP, april_FP,may_FP,june_FP],'T&M' : [march_TM, april_TM,may_TM,june_TM],'Cap T&M' : [march_capTM, april_capTM,may_capTM,june_capTM]})
        Total_Subcons = [(march_FP+march_TM+march_capTM),(april_FP+april_TM+april_capTM),(may_FP+may_TM+may_capTM),(june_FP+june_TM+june_capTM)]

        df_1['percent HC'] = (Total_Subcons/df_1['Head Count'])*100

        self._static_ax = self.subcon_movement.figure.subplots()
        fig = data.plot(x = 'Months',kind = 'bar', stacked=True,title='Movement of number of subcons',ylabel = 'No.of Active Subcontractors',color=["#D3D3D3","#FFBF00","#FFB6C1"], ax = self._static_ax)
        fig.set_ylim(0,6000)
        y_offset = 5

        for bar in fig.patches:
            fig.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height(),2),
            # Center the labels and style them a bit.
            ha='center',
            color='black',
            weight='bold',
            size=8
        )

        fig2 = df_1['percent HC'].plot(color = 'black', marker = 'o', secondary_y=True,ax = self._static_ax)
        fig2.set_ylim(0,7)
        fig2.set_ylabel('Subcon (%) of Total HC')
        l = [0,1,2,3]
        for x,y in zip(l,df_1['percent HC']):

            label = format(str(round(y,2)) + '%')

            fig2.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-15), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])
        plt.subplots_adjust(left=0.1, bottom=0.1, right=1.5, top=1.5)
        
        march_associate = (df1['Monthly Cost'].sum() + df2['Monthly Cost'].sum() + df3['Monthly Cost'].sum())/1000000
        april_associate = (df4['Monthly Cost'].sum() + df5['Monthly Cost'].sum() + df6['Monthly Cost'].sum())/1000000
        may_associate = (df7['Monthly Cost'].sum() + df8['Monthly Cost'].sum() + df9['Monthly Cost'].sum())/1000000
        june_associate = (df10['Monthly Cost'].sum() + df11['Monthly Cost'].sum() + df12['Monthly Cost'].sum())/1000000
        
        sproc_spend = pd.read_excel("/home/kartikg/Desktop/Subcon Solution/subcon report.xlsx", sheet_name = "SPROC spend")
        revenue = pd.read_excel("/home/kartikg/Desktop/Subcon Solution/subcon report.xlsx", sheet_name = "Revenue")
        sproc_spend['REPORTED_MONTH'] = pd.to_datetime(sproc_spend['REPORTED_MONTH']).dt.date
        sproc_1 = sproc_spend[sproc_spend['REPORTED_MONTH'] == datetime.date(2021,3,1)]
        sproc_2 = sproc_spend[sproc_spend['REPORTED_MONTH'] == datetime.date(2021,4,1)]
        sproc_3 = sproc_spend[sproc_spend['REPORTED_MONTH'] == datetime.date(2021,5,1)]
        sproc_4 = sproc_spend[sproc_spend['REPORTED_MONTH'] == datetime.date(2021,6,1)]
        march_sproc = sproc_1['Spend'].sum()
        april_sproc = sproc_2['Spend'].sum()
        may_sproc = sproc_3['Spend'].sum()
        june_sproc = sproc_4['Spend'].sum()
        revenue['REPORTED_MONTH'] = pd.to_datetime(revenue['REPORTED_MONTH']).dt.date
        data_1 = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'Associates' : [march_associate, april_associate,may_associate,june_associate],'SPROC' : [march_sproc, april_sproc,may_sproc,june_sproc]})
        Total_cost = data_1['Associates'] + data_1['SPROC']
        revenue_1 = revenue[revenue['REPORTED_MONTH'] == datetime.date(2021,3,1)]
        revenue_2 = revenue[revenue['REPORTED_MONTH'] == datetime.date(2021,4,1)]
        revenue_3 = revenue[revenue['REPORTED_MONTH'] == datetime.date(2021,5,1)]
        revenue_4 = revenue[revenue['REPORTED_MONTH'] == datetime.date(2021,6,1)]
        march_revenue = revenue_1['Revenue Total'].sum()
        april_revenue = revenue_2['Revenue Total'].sum()
        may_revenue = revenue_3['Revenue Total'].sum()
        june_revenue = revenue_4['Revenue Total'].sum()
        Revenue = [march_revenue,april_revenue,may_revenue,june_revenue]
        Perc_revenue = (Total_cost/Revenue)*100
        
        self._dynamic_ax = self.cost_movement.figure.subplots()
        fig = data_1.plot(x = 'Months',kind = 'bar', stacked=True,title='Movement of cost',ylabel = 'Cost Incurred (USD Million)',color=["#D3D3D3","#FFBF00"], ax = self._dynamic_ax)
        fig.set_ylim(0,100)
        y_offset =-5

        for bar in fig.patches:
            fig.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height(),2),
            # Center the labels and style them a bit.
            ha='center',
            color='black',
            weight='bold',
            size=8
        )

        fig2 = Perc_revenue.plot(color = 'black', marker = 'o', secondary_y=True,ax = self._dynamic_ax)
        fig2.set_ylabel('Cost as % of revenue')
        fig2.set_ylim(0,18)
        l = [0,1,2,3]
        for x,y in zip(l,Perc_revenue):
            label = format(str(round(y,2)) + '%')
            fig2.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-15), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])

        df_2 = df1[df1['On/Off'] == 'Onsite']
        TM_onsite_march = df_2['Monthly Revenue'].sum()/1000000
        df_2 = df1[(df1['On/Off'] == 'Offshore')]
        TM_offshore_march = df_2['Monthly Revenue'].sum()/1000000

        df_2 = df4[(df4['On/Off'] == 'Onsite')]
        TM_onsite_april = df_2['Monthly Revenue'].sum()/1000000
        df_2 = df4[(df4['On/Off'] == 'Offshore')]
        TM_offshore_april = df_2['Monthly Revenue'].sum()/1000000

        df_2 = df7[(df7['On/Off'] == 'Onsite')]
        TM_onsite_may = df_2['Monthly Revenue'].sum()/1000000
        df_2 = df7[(df7['On/Off'] == 'Offshore')]
        TM_offshore_may = df_2['Monthly Revenue'].sum()/1000000

        df_2 = df10[(df10['On/Off'] == 'Onsite')]
        TM_onsite_june = df_2['Monthly Revenue'].sum()/1000000
        df_2 = df10[(df10['On/Off'] == 'Offshore')]
        TM_offshore_june = df_2['Monthly Revenue'].sum()/1000000

        data_2 = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'Onsite' : [TM_onsite_march,TM_onsite_april,TM_onsite_may,TM_onsite_june],'Offshore' : [TM_offshore_march,TM_offshore_april,TM_offshore_may,TM_offshore_june]})
        march_vendorrate = df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull()))]['VENDOR_RT_HR_USD'].sum()
        april_vendorrate = df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull()))]['VENDOR_RT_HR_USD'].sum()
        may_vendorrate = df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull()))]['VENDOR_RT_HR_USD'].sum()
        june_vendorrate = df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull()))]['VENDOR_RT_HR_USD'].sum()

        march_clientrate = df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull()))]['CLIENT_RT_HR_USD'].sum()
        april_clientrate = df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull()))]['CLIENT_RT_HR_USD'].sum()
        may_clientrate = df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull()))]['CLIENT_RT_HR_USD'].sum()
        june_clientrate = df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull()))]['CLIENT_RT_HR_USD'].sum()

        march_margin = (1 - (march_vendorrate/march_clientrate))*100
        april_margin = (1 - (april_vendorrate/april_clientrate))*100
        may_margin = (1 - (may_vendorrate/may_clientrate))*100
        june_margin = (1 - (june_vendorrate/june_clientrate))*100

        self.Axes = self.TM_movement.figure.subplots()
        fig = data_2.plot(x = 'Months',kind = 'bar', stacked=True,title='Movement of T&M margin',ylabel = 'Cost Incurred Revenue(USD Million)',color=["#D3D3D3","#FFBF00"], ax = self.Axes)
        fig.set_ylim(0,25)
        y_offset =0 

        for bar in fig.patches:
            fig.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height(),2),
            # Center the labels and style them a bit.
            ha='center',
            color='black',
            weight='bold',
            size=8
        )
            
        data_6 = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'Margins' : [march_margin,april_margin,may_margin,june_margin]}) 
        fig2 = data_6['Margins'].plot(color = 'black', marker = 'o', secondary_y=True, ax = self.Axes)
        fig2.set_ylabel('Margin %')
        fig2.set_ylim(0,46)
        l = [0,1,2,3]
        for x,y in zip(l,data_6['Margins']):

            label = format(str(round(y,2)) + '%')

            fig2.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-15), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center


        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])

        hiring_march_FP = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,3,1)) & (df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['CONTRACT_TYPE'] == 'FP')].index)
        hiring_april_FP = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,4,1)) & (df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['CONTRACT_TYPE'] == 'FP')].index)
        hiring_may_FP = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,5,1)) & (df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['CONTRACT_TYPE'] == 'FP')].index)
        hiring_june_FP = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,6,1)) & (df['DATE OF JOINING'] < datetime.date(2021,7,1)) & (df['CONTRACT_TYPE'] == 'FP')].index)

        hiring_march_TM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,3,1)) & (df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['CONTRACT_TYPE'] == 'T&M')].index)
        hiring_april_TM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,4,1)) & (df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['CONTRACT_TYPE'] == 'T&M')].index)
        hiring_may_TM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,5,1)) & (df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['CONTRACT_TYPE'] == 'T&M')].index)
        hiring_june_TM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,6,1)) & (df['DATE OF JOINING'] < datetime.date(2021,7,1)) & (df['CONTRACT_TYPE'] == 'T&M')].index)

        hiring_march_capTM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,3,1)) & (df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['CONTRACT_TYPE'] == 'Cap T&M')].index)
        hiring_april_capTM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,4,1)) & (df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['CONTRACT_TYPE'] == 'Cap T&M')].index)
        hiring_may_capTM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,5,1)) & (df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['CONTRACT_TYPE'] == 'Cap T&M')].index)
        hiring_june_capTM = len(df[(df['DATE OF JOINING'] >= datetime.date(2021,6,1)) & (df['DATE OF JOINING'] < datetime.date(2021,7,1)) & (df['CONTRACT_TYPE'] == 'Cap T&M')].index)

        data_3 = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'FP' : [hiring_march_FP,hiring_april_FP,hiring_may_FP,hiring_june_FP],'T&M' : [hiring_march_TM,hiring_april_TM,hiring_may_TM, hiring_june_TM],'Cap T&M':[hiring_march_capTM,hiring_april_capTM,hiring_may_capTM, hiring_june_capTM]})
        march_hiring = df[(df['DATE OF JOINING'] >= datetime.date(2021,3,1)) & (df['DATE OF JOINING'] < datetime.date(2021,4,1))]
        Difference_march = ((march_hiring['VENDOR_RT_HR_USD'].sum() - march_hiring['Bechmark Rate'].sum())/march_hiring['VENDOR_RT_HR_USD'].sum())*100

        april_hiring = df[(df['DATE OF JOINING'] >= datetime.date(2021,4,1)) & (df['DATE OF JOINING'] < datetime.date(2021,5,1))]
        Difference_april = ((april_hiring['VENDOR_RT_HR_USD'].sum() - april_hiring['Bechmark Rate'].sum())/april_hiring['VENDOR_RT_HR_USD'].sum())*100

        may_hiring = df[(df['DATE OF JOINING'] >= datetime.date(2021,5,1)) & (df['DATE OF JOINING'] < datetime.date(2021,6,1))]
        Difference_may = ((may_hiring['VENDOR_RT_HR_USD'].sum() - may_hiring['Bechmark Rate'].sum())/may_hiring['VENDOR_RT_HR_USD'].sum())*100

        june_hiring = df[(df['DATE OF JOINING'] >= datetime.date(2021,6,1)) & (df['DATE OF JOINING'] < datetime.date(2021,7,1))]
        Difference_june = ((june_hiring['VENDOR_RT_HR_USD'].sum() - june_hiring['Bechmark Rate'].sum())/june_hiring['VENDOR_RT_HR_USD'].sum())*100

        self.Axes_1 = self.hiring_movement.figure.subplots()
        fig = data_3.plot.bar(x = 'Months', stacked=True,title='Hiring movement',ylabel = 'No. of New Hires',color=["#D3D3D3","#FFBF00","#FFB6C1"], ax = self.Axes_1)
        fig.set_ylim(0,1200)
        y_offset = 4

        for bar in fig.patches:
            fig.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height()),
            # Center the labels and style them a bit.
            ha='center',
            color='black',
            weight='bold',
            size=10
        )

        data_7 = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'Difference' : [Difference_march,Difference_april,Difference_may,Difference_june]}) 
        fig2 = data_7['Difference'].plot(color = 'black', marker = 'o', secondary_y=True, ax = self.Axes_1)
        fig2.set_ylabel('% variance with rate card')
        fig2.set_ylim(0,20)
        l = [0,1,2,3]
        for x,y in zip(l,data_7['Difference']):

            label = format(str(round(y,2)) + '%')

            fig2.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-15), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])

        W2_march = len(df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) &  (df['W2 Status '] == "Yes") & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull()))].index)
        NonW2_march = len(df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) &  (df['W2 Status '] == "No") & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull()))].index)

        W2_april = len(df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['W2 Status '] == "Yes") & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull()))].index)
        NonW2_april = len(df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['W2 Status '] == "No") & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull()))].index)

        W2_may = len(df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['W2 Status '] == "Yes") & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull()))].index)
        NonW2_may = len(df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['W2 Status '] == "No") & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull()))].index)

        W2_june = len(df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['W2 Status '] == "Yes") & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull()))].index)
        NonW2_june = len(df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['W2 Status '] == "No") & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull()))].index)

        TotalHC_march = len(df[(df['DATE OF JOINING'] < datetime.date(2021,3,1)) &  (df['CURRENT COUNTRY'] == "United States") & ((df['DEACTIVATION DATE'] > datetime.date(2021,3,31)) | (df['DEACTIVATION DATE'].isnull()))].index)
        TotalHC_april = len(df[(df['DATE OF JOINING'] < datetime.date(2021,4,1)) & (df['CURRENT COUNTRY'] == "United States") & ((df['DEACTIVATION DATE'] > datetime.date(2021,4,30)) | (df['DEACTIVATION DATE'].isnull()))].index)
        TotalHC_june = len(df[(df['DATE OF JOINING'] < datetime.date(2021,6,1)) & (df['CURRENT COUNTRY'] == "United States") & ((df['DEACTIVATION DATE'] > datetime.date(2021,6,30)) | (df['DEACTIVATION DATE'].isnull()))].index)
        TotalHC_may = len(df[(df['DATE OF JOINING'] < datetime.date(2021,5,1)) & (df['CURRENT COUNTRY'] == "United States") & ((df['DEACTIVATION DATE'] > datetime.date(2021,5,31)) | (df['DEACTIVATION DATE'].isnull()))].index)

        TotalHC = [TotalHC_march,TotalHC_april,TotalHC_may,TotalHC_june]

        self.Axes_2 = self.W2_movement.figure.subplots()
        W2_stacked = pd.DataFrame({'Months':['March - 21', 'April - 21', 'May - 21', 'June - 21'],'W2' : [W2_march,W2_april,W2_may,W2_june],'Non W2' : [NonW2_march, NonW2_april, NonW2_may,NonW2_june]})
        fig = W2_stacked.plot(x = 'Months',kind = 'bar', stacked=True,title='W2/Non-W2 composition movement',ylabel = 'W2 vs Non W2 HC',color=["#D3D3D3","#FFBF00"], ax = self.Axes_2)
        fig.set_ylim(0,2400)
        y_offset =0 

        for bar in fig.patches:
            fig.text(
            # Put the text in the middle of each bar. get_x returns the start
            # so we add half the width to get to the middle.
            bar.get_x() + bar.get_width() / 2,
            # Vertically, add the height of the bar to the start of the bar,
            # along with the offset.
            bar.get_height() + bar.get_y() + y_offset,
            # This is actual value we'll show.
            round(bar.get_height(),2),
            # Center the labels and style them a bit.
            ha='center',
            color='black',
            weight='bold',
            size=8
        )
            
        Percent_HC = (W2_stacked['W2']/TotalHC)*100
        W2_line = Percent_HC.plot(color = 'black', marker = 'o', secondary_y=True, ax = self.Axes_2)
        W2_line.set_ylabel('W2 % of Total HC of Subcon')
        l = [0,1,2,3]
        for x,y in zip(l,Percent_HC):

            label = format(str(round(y,2)) + '%')

            W2_line.annotate(label, # this is the text
                        (x,y), # these are the coordinates to position the label
                        textcoords="offset points", # how to position the text
                        xytext=(0,-15), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

        W2_line.set_ylim(0,60)
        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])
 
    def provideoptions(self):
        SBU = self.dataframe['SBU_GROUP'].unique() 
        IBU = self.dataframe['PROJ_IBU_ID'].unique()
        IBG = self.dataframe['PROJ_IBG_ID'].unique()
        Month = ['January','February','March','April','May','June','July','August','September','October','November','December']
        Location = ['Onsite','Offshore']
        Year = []
        year = datetime.datetime.now().year
        for i in range(year,2000,-1):
            Year.append(str(i))
        self.sbu_options.addItems(SBU)
        self.ibu_options.addItems(IBU)
        self.ibg_options.addItems(IBG)
        self.location_options.addItems(Location)
        self.month_options.addItems(Month)
        self.year_options.addItems(Year)
    

if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
       qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    #app.activateWindow()
    #app.raise_()
    sys.exit(qapp.exec_())
