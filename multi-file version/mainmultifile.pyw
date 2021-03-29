from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtTest import *
from gui import Ui_MainWindow
from dialog import Ui_dialog
import random
from functools import partial
import sys,time,threading,os


DEFAULT_SEPERATORS = ['=', ':', " = "]

greenbg = "background-color:green; color: #fff;"
redbg = "background-color:red; color: #fff;"
defaultbg = "background-color:rgb(240,240,240); color: rgb(0,0,40)"

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
        if len(self.data) >= 3:
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
