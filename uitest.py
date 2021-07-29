import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

import os
os.getcwd()
path = os.path.dirname('D:\\New Storage\\Coding\\Python Projects\\Timesheet Tracker\\')

labels = ['WBS', 'Hours Tracked', 'Manual Input', 'Overall Hours']
codes = ['94.03.56', '94.03.72', '94.03.66', 'General', 'Total']
hourinput = [2, 4, 6, 0]
hours = [str(hourinput[0]), str(hourinput[1]), str(hourinput[2]), str(hourinput[3]), str(sum(hourinput[:]))]


class OpenMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenMain, self).__init__()
        uic.loadUi(os.path.join(path,'tracker.ui'), self)
        self.initUI()

    def initUI(self):
        self.ac1.setText(codes[1])
        self.ac2.setText(codes[2])

        self.hour1.setText(hours[0])

        self.manual1.textChanged[str].connect(self.TextInput1)
        self.onlyFloat = QtGui.QDoubleValidator()
        self.manual1.setValidator(self.onlyFloat)

        self.show()

    def TextInput1(self, text):
        if text == '':
            self.total1.setText(str(float(hours[0])))
        else:
            self.total1.setText(str(float(text)+float(hours[0])))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = OpenMain()
    sys.exit(app.exec_())

