#Timesheet trackerjacker

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QMainWindow)
from PyQt5.QtCore import *
from PyQt5.QtGui import *

labels = ['WBS', 'Hours Tracked', 'Manual Input', 'Overall Hours']
codes = ['94.03.56', '94.03.72', '94.03.66', 'General', 'Total']
hourinput = [2, 4, 6, 0]
hours = [str(hourinput[0]), str(hourinput[1]), str(hourinput[2]), str(hourinput[3]), str(sum(hourinput[:]))]

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Buttons
        #self.QStartButton.clicked.connect(self.start_timer)
        #self.QStopButton.clicked.connect(self.stop_timer)

        self.hour_track = HourTrack(self)
        self.setCentralWidget(self.hour_track)

        self.hour_total = HourTotal(self)
        self.addDockWidget(self, BottomDockWidgetArea, self.hour_total)
        

class HourTotal(QWidget):

    def __init__(self, parent):
        super(HourTotal, self).__init__(parent)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('banana')    
        

class HourTrack(QWidget):
    
    def __init__(self, parent):
        super(HourTrack, self).__init__(parent)
        
        
        self.initUI()
        
        
    def initUI(self):

        something = 'banana'
        grid = QGridLayout()
        grid.setSpacing(1)

        i = 0
        
        for label in labels:
            labelrow = QLabel(label)
            labelrow.setAlignment(Qt.AlignCenter)
            grid.addWidget(labelrow, 0, i)
            i += 1
            
        
        i = 1
        
        for code in codes:
            coderow = QLabel(code)
            coderow.setAlignment(Qt.AlignCenter)
            grid.addWidget(coderow, i, 0)
            i += 1

        i = 1

        hourrow = dict()
        
        for hour in hours:
            hourrow[i] = QLabel(hour)
            hourrow[i].setAlignment(Qt.AlignCenter)
            grid.addWidget(hourrow[i], i, 1)
            i += 1

        i = 1

        self.inputrow = dict()

        self.onlyFloat = QDoubleValidator()
        
        for i1em in range(len(codes)):
            self.inputrow[i] = QLineEdit()
            self.inputrow[i].setAlignment(Qt.AlignCenter)
            self.inputrow[i].setValidator(self.onlyFloat)
            grid.addWidget(self.inputrow[i], i, 2)
            i += 1


        i = 1

        self.totalrow = dict()
        
        for hour in hours:
            self.totalrow[i] = QLabel()
            self.totalrow[i].setAlignment(Qt.AlignCenter)
            grid.addWidget(self.totalrow[i], i, 3)
            i += 1
           
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        

        #for count in range(1, len(hours)+1):
        self.inputrow[1].textChanged[str].connect(self.TextInput1)
        self.inputrow[2].textChanged[str].connect(self.TextInput2)
        self.inputrow[3].textChanged[str].connect(self.TextInput3)
        self.inputrow[4].textChanged[str].connect(self.TextInput4)
        self.inputrow[5].textChanged[str].connect(self.TextInput5)


        
            #self.changenum = count
    
    def TextInput1(self, text):
        if text == "":
            self.totalrow[1].setText(str(float(hours[0])))
        else:
            self.totalrow[1].setText(str(float(text)+float(hours[0])))

    def TextInput2(self, text):
        self.totalrow[2].setText(str(float(text)+float(hours[1])))

    def TextInput3(self, text):
        self.totalrow[3].setText(str(float(text)+float(hours[2])))

    def TextInput4(self, text):
        self.totalrow[4].setText(str(float(text)+float(hours[3])))

    def TextInput5(self, text):
        self.totalrow[5].setText(str(float(text)+float(hours[4])))
        

        '''
        WBS = QLabel('WBS')
        author = QLabel('Author')
        review = QLabel('Review')

        WBSEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(WBS, 1, 0)
        grid.addWidget(WBSEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
        '''
'''
def timerEvent():
    global time
    time = time.addSecs(1)
    print(time.toString("hh:mm:ss"))


app = QCoreApplication(sys.argv)

timer = QTimer()
time = QTime(0, 0, 0)

timer.timeout.connect(timerEvent)
timer.start(100)
'''
   
        
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
