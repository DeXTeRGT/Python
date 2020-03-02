from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTextEdit
from PyQt5 import uic, QtWidgets
import sys
 
 
 
class MDIWindow(QMainWindow):
 
    count = 0

    def __init__(self):
        super().__init__()
 
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
 
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.WindowTrig)
        self.setWindowTitle("MDI Application")

    def WindowTrig(self, p):
  
        if p.text() == "New":
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