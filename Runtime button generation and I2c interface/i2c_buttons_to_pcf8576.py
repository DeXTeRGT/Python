#Declare imports
import sys
from pcf8574 import PCF8574
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    newBtn={} #declare a dict to store the buttons array
    is_pressed=1
    I2C_BUS = PCF8574(1,0x20)

    def __init__(self):
        super().__init__()
        self.title = 'Button array at runtime'
        self.left = 100
        self.top = 100
        self.width = 470
        self.height = 100
        self.initUI()

    def initUI(self):
        #declare main window properties
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)

        #show the button that will generate the new buttons @ runtime 
        self.button = QPushButton('Generate 8 buttons', self)
        self.button.move(0,77)
        self.button.resize(470,23)
        self.button.clicked.connect(self.on_click)
        #and show them all
        self.show()
    #declare the function that would take care of button generation    
    def on_click(self):
        xpos=0
        btn_id=0
        self.button.setEnabled(False)
        #main generation loop - it will generate 5 buttons (for more buttons you would also need to change the window dimmensions so you can see them)
        for btn_id in range(0,8):
            #declare the new button object - one per loop and set the properties (also that would add them to the dict that was created as a class method)
            self.newBtn[btn_id] = QPushButton('BTTN ' + str(btn_id), self)
            self.newBtn[btn_id].resize(50,50)
            self.newBtn[btn_id].move(xpos, 0)
            if self.I2C_BUS.port[btn_id]==False:
                self.newBtn[btn_id].setText('ON')
                self.newBtn[btn_id].setStyleSheet("border: 5px solid red; border-radius:25px; background-color: green;")
            else:
                self.newBtn[btn_id].setText('OFF')
                self.newBtn[btn_id].setStyleSheet("border: 5px solid yellow; border-radius:25px; background-color: red;")
            #self.newBtn[btn_id].setStyleSheet("border: 5px solid; border-radius:25px; background-color: palette(base);")
            #show the whole thing - without this the buttons would not appear on the main form even if you declare them
            self.newBtn[btn_id].show()
            #increment some local vars to keep the track of the button idx and increpent the x position so that would be visible 
            #if you feel so inclined you can actually take the window dimensions and make a new row of buttons if the declared buttons
            #are not going to fit 
            btn_id = btn_id+1
            xpos=xpos+60
        for btn_instance, button in enumerate(self.newBtn.values()):
            #declare a lambda function that would take care of every instance of the button 
            #sending also the button index to know which button was clicked

            button.clicked.connect(lambda checked, btn_instance=btn_instance: self.open_link(btn_instance))
    #the function that would be called when a button is clicked
    #with the corresonding index
    def open_link(self, instance_number):
        #print(instance_number)
        if self.newBtn[instance_number].text()=='OFF':
            self.newBtn[instance_number].setStyleSheet("border: 5px solid red; border-radius:25px; background-color: green;")
            self.newBtn[instance_number].setText('ON')
            self.I2C_BUS.port[instance_number]=False
        else:
            self.newBtn[instance_number].setStyleSheet("border: 5px solid yellow; border-radius:25px; background-color: red;")
            self.newBtn[instance_number].setText('OFF')
            self.I2C_BUS.set_output(instance_number,True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
