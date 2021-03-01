from PyQt5 import QtCore, QtGui, QtWidgets
import math

import functions
from ui import Ui_MainWindow

ui = Ui_MainWindow()


def write(name):
    if ui.main_label.text() == "0":
        ui.main_label.setText(name.text())
    else:
        ui.main_label.setText(ui.main_label.text() + name.text())

'''
def analyse():
    one_number = functions.check_for_sqrt(ui.main_label.text())
    if not one_number:
        inter_text = functions.check_for_sqrt(ui.main_label.text())
        inter_text = functions.check_for_square(inter_text)
        inter_text = functions.check_for_square(inter_text)
        return inter_text
    else:
        return False

'''
def calculate():
    text = functions.analyse(ui.main_label.text())
    print(f'{text} -- exit from analyse')
    #print(f'{text is False} -- is false')
    if text:
        print('entred in if')
        try:
            #print(eval(text))
            res = eval(text)
            #print(f'{res} -- eval res ')
        except ZeroDivisionError:
            ui.main_label.setText('ZeroDivisionError')
        except BaseException as Exp:
            print(f'{Exp} is exсepted')
        else:
            print('try block passed')
            res = functions.check_output(res)
            ui.main_label.setText(str(res))

    else:
        ui.main_label.setText(ui.main_label.text())



def erase():
    ui.main_label.setText(ui.main_label.text()[:-1])


def clear():
    ui.main_label.setText("0")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.btn_1.clicked.connect(lambda: write(ui.btn_1))
    ui.btn_2.clicked.connect(lambda: write(ui.btn_2))
    ui.btn_3.clicked.connect(lambda: write(ui.btn_3))
    ui.btn_4.clicked.connect(lambda: write(ui.btn_4))
    ui.btn_5.clicked.connect(lambda: write(ui.btn_5))
    ui.btn_6.clicked.connect(lambda: write(ui.btn_6))
    ui.btn_7.clicked.connect(lambda: write(ui.btn_7))
    ui.btn_8.clicked.connect(lambda: write(ui.btn_8))
    ui.btn_9.clicked.connect(lambda: write(ui.btn_9))
    ui.btn_zero.clicked.connect(lambda: write(ui.btn_zero))
    ui.btn_plus.clicked.connect(lambda: write(ui.btn_plus))
    ui.btn_minus.clicked.connect(lambda: write(ui.btn_minus))
    ui.btn_sqrt.clicked.connect(lambda: write(ui.btn_sqrt))
    ui.btn_power.clicked.connect(lambda: write(ui.btn_power))
    ui.btn_dot.clicked.connect(lambda: write(ui.btn_dot))
    ui.btn_multiply.clicked.connect(lambda: write(ui.btn_multiply))
    ui.btn_divise.clicked.connect(lambda: write(ui.btn_divise))
    ui.btn_open_parenthesis.clicked.connect(lambda: write(ui.btn_open_parenthesis))
    ui.btn_close_parenthesis.clicked.connect(lambda: write(ui.btn_close_parenthesis))
    ui.btn_equal.clicked.connect(calculate)
    ui.btn_backspace.clicked.connect(erase)
    ui.btn_clear.clicked.connect(clear)

    sys.exit(app.exec_())
