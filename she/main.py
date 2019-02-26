# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataProcessing(object):
    def setupUi(self, DataProcessing):
        DataProcessing.setObjectName("DataProcessing")
        DataProcessing.resize(800, 737)
        self.centralwidget = QtWidgets.QWidget(DataProcessing)
        self.centralwidget.setObjectName("centralwidget")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(280, 40, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.recv_combo = QtWidgets.QLabel(self.centralwidget)
        self.recv_combo.setGeometry(QtCore.QRect(220, 90, 391, 20))
        self.recv_combo.setObjectName("recv_combo")
        self.recv_opt = QtWidgets.QComboBox(self.centralwidget)
        self.recv_opt.setGeometry(QtCore.QRect(180, 130, 451, 25))
        self.recv_opt.setObjectName("recv_opt")
        self.ack_labe = QtWidgets.QLabel(self.centralwidget)
        self.ack_labe.setGeometry(QtCore.QRect(80, 210, 101, 17))
        self.ack_labe.setObjectName("ack_labe")
        self.dpt_labe = QtWidgets.QLabel(self.centralwidget)
        self.dpt_labe.setGeometry(QtCore.QRect(80, 390, 171, 17))
        self.dpt_labe.setObjectName("dpt_labe")
        self.ack_win = QtWidgets.QTextBrowser(self.centralwidget)
        self.ack_win.setGeometry(QtCore.QRect(80, 240, 671, 121))
        self.ack_win.setObjectName("ack_win")
        self.dpt_win = QtWidgets.QTextBrowser(self.centralwidget)
        self.dpt_win.setGeometry(QtCore.QRect(80, 420, 671, 192))
        self.dpt_win.setObjectName("dpt_win")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 620, 671, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.btn_hrlayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.btn_hrlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_hrlayout.setObjectName("btn_hrlayout")
        self.recv_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recv_btn.setObjectName("recv_btn")
        self.btn_hrlayout.addWidget(self.recv_btn)
        self.opnfile_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.opnfile_btn.setObjectName("opnfile_btn")
        self.btn_hrlayout.addWidget(self.opnfile_btn)
        self.ext_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ext_btn.setObjectName("ext_btn")
        self.btn_hrlayout.addWidget(self.ext_btn)
        DataProcessing.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataProcessing)
        QtCore.QMetaObject.connectSlotsByName(DataProcessing)

    def retranslateUi(self, DataProcessing):
        _translate = QtCore.QCoreApplication.translate
        DataProcessing.setWindowTitle(_translate("DataProcessing", "MainWindow"))
        self.main_title.setText(_translate("DataProcessing", "DATA PROCESSING WINDOW"))
        self.recv_combo.setText(_translate("DataProcessing", "SELECT WHAT COMMAND YOU WOULD LIKE TO RECEIVE"))
        self.ack_labe.setText(_translate("DataProcessing", "ACK WINDOW"))
        self.dpt_labe.setText(_translate("DataProcessing", "DATA PROCESSING TASK"))
        self.recv_btn.setText(_translate("DataProcessing", "Receive"))
        self.opnfile_btn.setText(_translate("DataProcessing", "Open FILE"))
        self.ext_btn.setText(_translate("DataProcessing", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataProcessing = QtWidgets.QMainWindow()
    ui = Ui_DataProcessing()
    ui.setupUi(DataProcessing)
    DataProcessing.show()
    sys.exit(app.exec_())

