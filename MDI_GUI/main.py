from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
from PyQt5 import uic, QtWidgets
import sys
 
 
 
class MDIWindow(QMainWindow):
 
    count = 0
    def __init__(self, parent=None):
        super(MDIWindow, self).__init__(parent)
        uic.loadUi('ui/main_mdi.ui', self)
        self.setWindowTitle("XXX YYY ZZZ")
        self.menu_File.triggered[QAction].connect(self.WindowTrig)

    def WindowTrig(self, p):
  
        if p.text() == "New":
            for win in range(1, 20):
                MDIWindow.count = MDIWindow.count + 1
                sub = MDIWindowSL()
                #sub.setWidget(QTextEdit())
                sub.setWindowTitle("Sub Window" + str(MDIWindow.count))
                self.mdi.addSubWindow(sub)
                sub.show()
 
        if p.text() == "cascade":
            self.mdi.cascadeSubWindows()
 
        if p.text() == "Tiled":
            self.mdi.tileSubWindows()

class MDIWindowSL(QtWidgets.QDialog):
    #user_class=0
    #logged_user=''
    def __init__(self, parent=None):
        super(MDIWindowSL, self).__init__(parent)
        uic.loadUi('C:/dev_prj/InfraMon/ui/login.ui', self)
        #self.MplWidget=mplwidget
        self.l_login.clicked.connect (self.PrintInfo)
    
    def PrintInfo(self):
        print(self.windowTitle())

 
app = QApplication(sys.argv)
mdi  =MDIWindow()
mdi.show()
app.exec_()