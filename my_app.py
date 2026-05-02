
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QListWidget, QLineEdit) 
from instr import *
from second_win import *
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class TestWin(QWidget):
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text(), self.line_test2.text(), self.line_test3.text())
        self.tw = FinalWin(self.exp)

class MainWin(QWidget):
    def __init(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y )
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.leyout_line = QVBoxLayout()
        self.leyout_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TextWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
app=QApplication([])
mw= MainWin()
app.exec_()
