from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtTest import *
# from gui import Ui_MainWindow
# from dialog import Ui_dialog
import random
from functools import partial
import sys,time,threading,os
from PyQt5 import QtCore, QtGui, QtWidgets

DEFAULT_SEPERATORS = ['=', ':', " = "]

greenbg = "background-color:green; color: #fff;"
redbg = "background-color:red; color: #fff;"
defaultbg = "background-color:rgb(240,240,240); color: rgb(0,0,40)"

thestylesheet = """
QPushButton{
  background-color: #ffffff;
  border-style: outset;
  color:rgb(0,0,40);
  font-size: 20px;
  border-radius: 10px;
  border-style:solid;
  border-width: 2px;
  border-color: #000000;
  padding: 4px;
}
QPushButton:hover {
  font-size: 25px;
  border-color: red;
  border-width: 2px;
}

QLabel{
  font-size: 40px;
  color: white;
  font-style: bold;
}
QMenu{
    background-color: gray;
    color: white;

}
QMenuBar {
    background-color: rgb(15,20,25);
    color:white;

    font-size: 20px;
}
QMenuBar::item:selected {
    background: white;
    color:rgb(15,20,25);
}
QMainWindow{
    background-color: rgb(0,0,40);
    color:black;
    border-style:none;
    border-radius: 10px;
}
QLCDNumber {
  color:white;

  border-radius:10px;
  border:2px solid white;
}

"""

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(313, 301)
        dialog.setStyleSheet("background-color: #fff;")
        #dialog.setWindowIcon(QIcon(os.getcwd()+'\\title.jpg'))
        dialog.setWindowTitle("bitrogen")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 241, 81))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 221, 81))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 241, 81))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        dialog.setFixedSize(dialog.size())

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "bitrogen"))
        self.label_2.setText(_translate("dialog", " <a href=\"https://github.com/bitrogen\"> <font face=verdana size=24 color=black> Github</font> </a>"))
        self.label_3.setText(_translate("dialog", " <a href=\"https://www.youtube.com/channel/UCDx-KTToe7EB1OcTbmN_-8g\"> <font face=verdana size=12 color=red> Youtube</font> </a>"))
        self.label_4.setText(_translate("dialog", " <a href=\"https://bitrogen.github.io\"> <font face=verdana size=24 color=aqua> bitrogen</font> </a>"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 596)
        #MainWindow.setWindowIcon("image.jfif")
        MainWindow.setStyleSheet(thestylesheet)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(60, 40, 641, 191))
        self.questionLabel.setStyleSheet("")
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName("questionLabel")
        self.answer1 = QtWidgets.QPushButton(self.centralwidget)
        self.answer1.setGeometry(QtCore.QRect(60, 260, 311, 71))
        self.answer1.setObjectName("answer1")
        self.answer2 = QtWidgets.QPushButton(self.centralwidget)
        self.answer2.setGeometry(QtCore.QRect(420, 260, 281, 71))
        self.answer2.setObjectName("answer2")
        self.answer3 = QtWidgets.QPushButton(self.centralwidget)
        self.answer3.setGeometry(QtCore.QRect(60, 350, 311, 71))
        self.answer3.setObjectName("answer3")
        self.answer4 = QtWidgets.QPushButton(self.centralwidget)
        self.answer4.setGeometry(QtCore.QRect(420, 350, 281, 71))
        self.answer4.setObjectName("answer4")
        self.timeBar = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeBar.setGeometry(QtCore.QRect(420, 440, 281, 81))
        self.timeBar.setObjectName("timeBar")
        self.scoreBar = QtWidgets.QLCDNumber(self.centralwidget)
        self.scoreBar.setGeometry(QtCore.QRect(60, 440, 311, 81))
        self.scoreBar.setObjectName("scoreBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionbitrogen = QtWidgets.QAction(MainWindow)
        self.actionbitrogen.setObjectName("actionbitrogen")
        self.menuFile.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionbitrogen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.answer1.setText(_translate("MainWindow", "PushButton"))
        self.answer2.setText(_translate("MainWindow", "PushButton"))
        self.answer3.setText(_translate("MainWindow", "PushButton"))
        self.answer4.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionbitrogen.setText(_translate("MainWindow", "bitrogen"))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.userInterface = Ui_MainWindow()
        self.userInterface.setupUi(self)
        self.setWindowTitle('Quiz Program')
        self.setWindowIcon(QIcon(os.getcwd()+'\\title.jpg'))
        self.count = 0
        self.flag = True
        self.buttons = [
            self.userInterface.answer1,
            self.userInterface.answer2,
            self.userInterface.answer3,
            self.userInterface.answer4
        ]
        self.buttons[0].clicked.connect(partial(self.Control, 0))
        self.buttons[1].clicked.connect(partial(self.Control, 1))
        self.buttons[2].clicked.connect(partial(self.Control, 2))
        self.buttons[3].clicked.connect(partial(self.Control, 3))
        self.setFixedSize(self.size())
        self.rights = 0
        self.wrongs = 0
        self.lengthofData = 0
        self.userInterface.actionOpen.triggered.connect(self.openFile)
        self.SetStatusButtons(False)
        self.userInterface.questionLabel.setText("Question")
        self.userInterface.answer1.setText("Answer 1")
        self.userInterface.answer2.setText("Answer 2")
        self.userInterface.answer3.setText("Answer 3")
        self.userInterface.answer4.setText("Answer 4")
        self.userInterface.actionbitrogen.triggered.connect(self.aboutBitrogen)

    def SetStatusButtons(self, status):
        [self.buttons[i].setEnabled(status) for i in range(4)]

    def openFile(self):
        self.BCpath,ftype = QFileDialog.getOpenFileName(self, 'Open file','c:\\',"txt files (*.txt)")
        if self.BCpath == "":
            self.userInterface.questionLabel.setText('The file was in invalid format.\nPlease use ":" or "=" to seperate \nthe word and its meaning.')
            return
        with open(self.BCpath, "r+", encoding='utf-8') as file:
            rawData = file.readlines()
            for seperator in DEFAULT_SEPERATORS:
                if rawData[0].count(seperator) == 1:
                    self.seperator = seperator
            self.lengthofData = len(rawData)
            rawData2 = [line.split(self.seperator) for line in rawData]
            self.data = [[line[0], line[1][:-1]] for line in rawData2]
        self.start()
        self.startTimer()

    def aboutBitrogen(self):
        dialog = QDialog()
        dialog.ui = Ui_dialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.label_2.setOpenExternalLinks(True)
        dialog.ui.label_3.setOpenExternalLinks(True)
        dialog.ui.label_4.setOpenExternalLinks(True)
        dialog.exec_()


    def Control(self, buttonIndex):
        self.SetStatusButtons(False)
        answerofUser = self.buttons[buttonIndex].text()
        if self.theAnswer[1] == answerofUser:
            self.TrueAnswer(answerofUser, buttonIndex)
            QTest.qWait(1000)
            self.start()


        else:
            self.WrongAnswer(answerofUser, buttonIndex)
            QTest.qWait(1000)
            self.start()

    def TrueAnswer(self, answerofUser, buttonIndex):
        self.buttons[buttonIndex].setStyleSheet(greenbg)
        self.rights += 1
        self.userInterface.scoreBar.display(self.rights)


    def WrongAnswer(self, answerofUser, buttonIndex):
        self.wrongs+=1
        self.buttons[buttonIndex].setStyleSheet(redbg)
        self.data.append(self.theAnswer)
        for button in self.buttons:
            if button.text() == self.theAnswer[1]:
                button.setStyleSheet(greenbg)


    def startTimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    def showTime(self):
        if self.flag:
            self.count += 1
            self.userInterface.timeBar.display(self.count)
        else:
            pass


    def getRandomQuestion(self):
        chosen0 = random.choice(self.data)
        self.data.remove(chosen0)
        random.shuffle(self.data)
        chosen1 = self.data[-1]
        chosen2 = self.data[-2]
        chosen3 = self.data[-3]
        self.theAnswer = chosen0

        answerset = [chosen0[1],chosen1[1],chosen2[1],chosen3[1]]
        random.shuffle(answerset)
        return answerset


    def start(self):
        print(len(self.data))
        if len(self.data) >= 4:
            self.SetStatusButtons(True)
            answerset = self.getRandomQuestion()
            self.userInterface.questionLabel.setText(self.theAnswer[0])
            self.userInterface.answer1.setText(answerset[0])
            self.userInterface.answer2.setText(answerset[1])
            self.userInterface.answer3.setText(answerset[2])
            self.userInterface.answer4.setText(answerset[3])

            self.buttons[0].setStyleSheet(defaultbg)
            self.buttons[1].setStyleSheet(defaultbg)
            self.buttons[2].setStyleSheet(defaultbg)
            self.buttons[3].setStyleSheet(defaultbg)
        else:
            self.finished()

    def finished(self):
        self.flag = False
        score = 10*self.lengthofData - self.count + self.rights*10 - self.wrongs*5
        self.userInterface.questionLabel.setText(f"Your score was {score}!")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
