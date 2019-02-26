# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TELECOMMAND(object):
    def setupUi(self, TELECOMMAND):
        TELECOMMAND.setObjectName("TELECOMMAND")
        TELECOMMAND.resize(937, 658)
        self.centralwidget = QtWidgets.QWidget(TELECOMMAND)
        self.centralwidget.setObjectName("centralwidget")
        self.tc_comb = QtWidgets.QComboBox(self.centralwidget)
        self.tc_comb.setGeometry(QtCore.QRect(250, 130, 431, 25))
        self.tc_comb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tc_comb.setObjectName("tc_comb")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tc_comb.addItem("")
        self.tccombo_title = QtWidgets.QLabel(self.centralwidget)
        self.tccombo_title.setGeometry(QtCore.QRect(380, 90, 191, 17))
        self.tccombo_title.setObjectName("tccombo_title")
        self.proc_labe = QtWidgets.QLabel(self.centralwidget)
        self.proc_labe.setGeometry(QtCore.QRect(380, 200, 211, 16))
        self.proc_labe.setObjectName("proc_labe")
        self.ack_labe = QtWidgets.QLabel(self.centralwidget)
        self.ack_labe.setGeometry(QtCore.QRect(440, 360, 101, 17))
        self.ack_labe.setObjectName("ack_labe")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(360, 20, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.proc_win = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.proc_win.setGeometry(QtCore.QRect(70, 240, 811, 101))
        self.proc_win.setObjectName("proc_win")
        self.ack_win = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ack_win.setGeometry(QtCore.QRect(70, 380, 811, 131))
        self.ack_win.setObjectName("ack_win")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 530, 811, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verify_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.verify_btn.setObjectName("verify_btn")
        self.horizontalLayout.addWidget(self.verify_btn)
        self.send_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout.addWidget(self.send_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.isro_logo = QtWidgets.QLabel(self.centralwidget)
        self.isro_logo.setGeometry(QtCore.QRect(30, 30, 91, 81))
        self.isro_logo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.isro_logo.setText("")
        self.isro_logo.setPixmap(QtGui.QPixmap("../../../../../../home/kannan/Downloads/isro_logo.ico"))
        self.isro_logo.setObjectName("isro_logo")
        TELECOMMAND.setCentralWidget(self.centralwidget)

        self.retranslateUi(TELECOMMAND)
        self.tc_comb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TELECOMMAND)

    def retranslateUi(self, TELECOMMAND):
        _translate = QtCore.QCoreApplication.translate
        TELECOMMAND.setWindowTitle(_translate("TELECOMMAND", "TELECOMMAND SIMULATOR"))
        self.tc_comb.setCurrentText(_translate("TELECOMMAND", "AXIS_STABLIZE"))
        self.tc_comb.setItemText(0, _translate("TELECOMMAND", "AXIS_STABLIZE"))
        self.tc_comb.setItemText(1, _translate("TELECOMMAND", "EARTH_AQUS"))
        self.tc_comb.setItemText(2, _translate("TELECOMMAND", "SUN_AQUS"))
        self.tc_comb.setItemText(3, _translate("TELECOMMAND", "TRANSMITTER _ON"))
        self.tc_comb.setItemText(4, _translate("TELECOMMAND", "TRANSMITTER _OFF"))
        self.tc_comb.setItemText(5, _translate("TELECOMMAND", "SPS_ON"))
        self.tc_comb.setItemText(6, _translate("TELECOMMAND", "SPS_OFF"))
        self.tc_comb.setItemText(7, _translate("TELECOMMAND", "DEPLOY_SOLARPANEL"))
        self.tc_comb.setItemText(8, _translate("TELECOMMAND", "PAYLOAD DATA"))
        self.tccombo_title.setText(_translate("TELECOMMAND", "SELECT A TELECOMMAND"))
        self.proc_labe.setText(_translate("TELECOMMAND", "TELECOMMAND PROCESSING"))
        self.ack_labe.setText(_translate("TELECOMMAND", "ACK WINDOW"))
        self.main_title.setText(_translate("TELECOMMAND", "TELECOMMAND SIMLUTAOR"))
        self.verify_btn.setText(_translate("TELECOMMAND", "Verify"))
        self.send_btn.setText(_translate("TELECOMMAND", "Send"))
        self.cancel_btn.setText(_translate("TELECOMMAND", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TELECOMMAND = QtWidgets.QMainWindow()
    ui = Ui_TELECOMMAND()
    ui.setupUi(TELECOMMAND)
    TELECOMMAND.show()
    sys.exit(app.exec_())

