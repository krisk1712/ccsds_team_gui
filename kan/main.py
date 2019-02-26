# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_payload_win(object):
    def setupUi(self, payload_win):
        payload_win.setObjectName("payload_win")
        payload_win.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(payload_win)
        self.centralwidget.setObjectName("centralwidget")
        self.title_main = QtWidgets.QLabel(self.centralwidget)
        self.title_main.setGeometry(QtCore.QRect(260, 30, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_main.setFont(font)
        self.title_main.setObjectName("title_main")
        self.menu_labe = QtWidgets.QLabel(self.centralwidget)
        self.menu_labe.setGeometry(QtCore.QRect(270, 80, 231, 17))
        self.menu_labe.setObjectName("menu_labe")
        self.recv_menu = QtWidgets.QComboBox(self.centralwidget)
        self.recv_menu.setGeometry(QtCore.QRect(190, 110, 381, 25))
        self.recv_menu.setObjectName("recv_menu")
        self.ack_labe = QtWidgets.QLabel(self.centralwidget)
        self.ack_labe.setGeometry(QtCore.QRect(340, 160, 101, 17))
        self.ack_labe.setObjectName("ack_labe")
        self.ack_win = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ack_win.setGeometry(QtCore.QRect(80, 200, 661, 131))
        self.ack_win.setObjectName("ack_win")
        self.proc_win = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.proc_win.setGeometry(QtCore.QRect(80, 390, 661, 111))
        self.proc_win.setObjectName("proc_win")
        self.proc_labe = QtWidgets.QLabel(self.centralwidget)
        self.proc_labe.setGeometry(QtCore.QRect(320, 350, 171, 21))
        self.proc_labe.setObjectName("proc_labe")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 510, 661, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.recv_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recv_btn.setObjectName("recv_btn")
        self.horizontalLayout.addWidget(self.recv_btn)
        self.opnpld_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.opnpld_btn.setObjectName("opnpld_btn")
        self.horizontalLayout.addWidget(self.opnpld_btn)
        self.ext_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ext_btn.setObjectName("ext_btn")
        self.horizontalLayout.addWidget(self.ext_btn)
        payload_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(payload_win)
        QtCore.QMetaObject.connectSlotsByName(payload_win)

    def retranslateUi(self, payload_win):
        _translate = QtCore.QCoreApplication.translate
        payload_win.setWindowTitle(_translate("payload_win", "PAYLOAD DATA SIMUALTION"))
        self.title_main.setText(_translate("payload_win", "PAYLOAD DATA SIMULATION"))
        self.menu_labe.setText(_translate("payload_win", "SELECT TYPE OF PAYLOAD DATA "))
        self.ack_labe.setText(_translate("payload_win", "ACK WINDOW"))
        self.proc_labe.setText(_translate("payload_win", "PROCESSING WINDOW"))
        self.recv_btn.setText(_translate("payload_win", "Receive"))
        self.opnpld_btn.setText(_translate("payload_win", "Open Payload "))
        self.ext_btn.setText(_translate("payload_win", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    payload_win = QtWidgets.QMainWindow()
    ui = Ui_payload_win()
    ui.setupUi(payload_win)
    payload_win.show()
    sys.exit(app.exec_())

