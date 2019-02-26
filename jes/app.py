from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtTest 
 
from main import Ui_TELECOMMAND
 
import sys
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
 
        self.ui = Ui_TELECOMMAND()
    
        self.ui.setupUi(self)

        self.ui.verify_btn.clicked.connect(self.vbtnClicked)
        
        self.ui.send_btn.clicked.connect(self.sbtnClicked)

        self.ui.cancel_btn.clicked.connect(exit)

    def vbtnClicked(self):
        tc = ["AXIS_STABLIZE","EARTH_AQUS","SUN_AQUS","TRANSMITTER _ON","TRANSMITTER _OFF","SPS_ON","SPS_OFF","DEPLOY_SOLARPANEL","PAYLOAD DATA"]

        if self.ui.tc_comb.currentText() == "AXIS_STABLIZE":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...")
        elif self.ui.tc_comb.currentText() == "EARTH_AQUS":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...")  
        elif self.ui.tc_comb.currentText() == "SUN_AQUS":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...") 
        elif self.ui.tc_comb.currentText() == "TRANSMITTER _ON":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...") 
        elif self.ui.tc_comb.currentText() == "TRANSMITTER _OFF":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...") 
        elif self.ui.tc_comb.currentText() == "SPS_ON":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...") 
        elif self.ui.tc_comb.currentText() == "SPS_OFF":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...") 
        elif self.ui.tc_comb.currentText() == "DEPLOY_SOLARPANEL":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...")
        elif self.ui.tc_comb.currentText() == "PAYLOAD DATA":
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is on VERFICATION STAGE...")
            QtTest.QTest.qWait(5000)
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  verified...")
        else:
            self.ui.ack_win.setPlainText("Sorry no other option to be selected")
                

    def sbtnClicked(self):
        
        tc = ["AXIS_STABLIZE","EARTH_AQUS","SUN_AQUS","TRANSMITTER _ON","TRANSMITTER _OFF","SPS_ON","SPS_OFF","DEPLOY_SOLARPANEL","PAYLOAD DATA"]
        


        if self.ui.tc_comb.currentText() == "AXIS_STABLIZE":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 01AECD23 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,01AECD23,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...")
        elif self.ui.tc_comb.currentText() == "EARTH_AQUS":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 8789AC43 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,8789AC43,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...")  
        elif self.ui.tc_comb.currentText() == "SUN_AQUS":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 69984ACD <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,69984ACD,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...") 
        elif self.ui.tc_comb.currentText() == "TRANSMITTER _ON":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> ACD1437DF <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,ACD1437DF,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...") 
        elif self.ui.tc_comb.currentText() == "TRANSMITTER _OFF":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 76AC1340 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,76AC1340,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...") 
        elif self.ui.tc_comb.currentText() == "SPS_ON":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 987ADC34 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,987ADC34,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...") 
        elif self.ui.tc_comb.currentText() == "SPS_OFF":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 76ADFCB1 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,76ADFCB1,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...") 
        elif self.ui.tc_comb.currentText() == "DEPLOY_SOLARPANEL":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 76AC1340 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,76AC1340,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...")
        elif self.ui.tc_comb.currentText() == "PAYLOAD DATA":
            self.ui.ack_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is being Processed.....")
            self.ui.proc_win.appendPlainText("The Command "+ self.ui.tc_comb.currentText() + " is  Processing...")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The Equivalent packet data of  "+ self.ui.tc_comb.currentText() + " is --> 68AECD120 <--")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("The PACKET for "+ self.ui.tc_comb.currentText() + " is shown below..")
            self.ui.proc_win.appendPlainText("---> [4EA36B01,83EC,[AA55BB66,1A0E,68AECD120,0101],1212]")
            QtTest.QTest.qWait(2000)
            self.ui.proc_win.appendPlainText("Sending the Command as packet to the satellite...")
            QtTest.QTest.qWait(1000)
            self.ui.ack_win.appendPlainText("THE command is sent to satellite...")
        else:
            self.ui.ack_win.setPlainText("Sorry no other option to be selected")

app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())