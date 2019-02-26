from PyQt5 import QtWidgets,QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtTest 
 
from main import Ui_payload_win 
 
import sys
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
 
        self.ui = Ui_payload_win()
    
        self.ui.setupUi(self)
        
        isrologo = QPixmap('./img/isro.png')

        self.ui.isro_logo.setPixmap(isrologo)

        self.ui.verify_btn.clicked.connect(self.vbtnClicked)
        
        self.ui.send_btn.clicked.connect(self.sbtnClicked)

        self.ui.cancel_btn.clicked.connect(exit)

    def vbtnClicked(self):
        tc = ["SIS","Solar panel","Axis Stablize","SPS","Payload data","Sun aqus","Earth Aqus"]

        for i in tc:
            if self.ui.telecm_menu.currentText() == i:  
                self.ui.ack_view.setPlainText("The command "+ self.ui.telecm_menu.currentText()+" is verified and being processed... " )
                

    def sbtnClicked(self):
        
        tc = ["SIS","Solar panel","Axis Stablize","SPS","Payload data","Sun Aqus","Earth Aqus"]
        self.ui.ack_view.setPlainText("The command "+ self.ui.telecm_menu.currentText() +" is being Processed....\n" )
        QtTest.QTest.qWait(5000) # uisng time.sleep in terminal on wards pls use it bro
        self.ui.ack_view.appendPlainText("The command "+ self.ui.telecm_menu.currentText() +" is being send to the satellite \n")
        on_launch = QPixmap('./img/satstowed.png')
        on_solarpaneldep = QPixmap('./img/satdeployes.png')
        on_AixStab = QPixmap('./img/asat-img.jpeg')
        on_SPS = QPixmap('./img/satps.jpeg')
        on_payloadat = QPixmap('./img/satonpayload.jpeg')
        on_earthAqu = QPixmap('./img/eartjh-aqus.jpg')
        on_sunAqu = QPixmap('./img/satonsun.jpeg')
        for i in tc:
            if self.ui.telecm_menu.currentText() == "SIS":
                self.ui.img_wid.setPixmap(on_launch)
            elif self.ui.telecm_menu.currentText() == "Solar panel":
                self.ui.img_wid.setPixmap(on_solarpaneldep)  
            elif self.ui.telecm_menu.currentText() == "Axis Stablize":
                self.ui.img_wid.setPixmap(on_AixStab) 
            elif self.ui.telecm_menu.currentText() == "SPS":
                self.ui.img_wid.setPixmap(on_SPS) 
            elif self.ui.telecm_menu.currentText() == "Payload data":
                self.ui.img_wid.setPixmap(on_payloadat) 
            elif self.ui.telecm_menu.currentText() == "Sun aqus":
                self.ui.img_wid.setPixmap(on_sunAqu) 
            elif self.ui.telecm_menu.currentText() == "Earth Aqus":
                self.ui.img_wid.setPixmap(on_earthAqu) 
            else:
                self.ui.ack_view.setPlainText("Sorry no other option to be selected")

app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())