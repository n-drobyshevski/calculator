from PyQt5 import QtCore, QtGui, QtWidgets

from ui import Ui_MainWindow

ui = Ui_MainWindow()

def write(name):
    if ui.main_label.text() == "TextLabel":
        ui.main_label.setText(name.text())
    else:
        ui.main_label.setText(ui.main_label.text() + name.text())

def calculate():
    res = eval(ui.main_label.text())
    ui.main_label.setText(str(res))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.btn_1.clicked.connect(lambda:write(ui.btn_1))
    ui.btn_2.clicked.connect(lambda:write(ui.btn_2))
    ui.btn_3.clicked.connect(lambda:write(ui.btn_3))
    ui.btn_4.clicked.connect(lambda:write(ui.btn_4))
    ui.btn_5.clicked.connect(lambda:write(ui.btn_5))
    ui.btn_6.clicked.connect(lambda:write(ui.btn_6))
    ui.btn_7.clicked.connect(lambda:write(ui.btn_7))
    ui.btn_8.clicked.connect(lambda:write(ui.btn_8))
    ui.btn_9.clicked.connect(lambda:write(ui.btn_9))
    ui.btn_zero.clicked.connect(lambda:write(ui.btn_zero))
    ui.btn_plus.clicked.connect(lambda:write(ui.btn_plus))
    ui.btn_minus.clicked.connect(lambda:write(ui.btn_minus))
    ui.btn_multiply.clicked.connect(lambda:write(ui.btn_multiply))
    ui.btn_divise.clicked.connect(lambda:write(ui.btn_divise))
    ui.btn_equal.clicked.connect(calculate)
    #ui.btn_equal.clicked.connect(lambda:ui.main_label.setText(ui.btn_1.text()))


    sys.exit(app.exec_())