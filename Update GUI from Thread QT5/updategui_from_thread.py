from PyQt5 import QtWidgets, uic, QtCore
from datetime import datetime
import sys

class UpdateThread(QtCore.QThread):
    str_signal=QtCore.pyqtSignal(str) #declare the custom signal
    progress=QtCore.pyqtSignal(int)

    def __init__(self,  parent=None): #init class - as far as i know is not mandatory ... but ok
        QtCore.QThread.__init__(self, parent)
        self.running = False

    def run(self):   #define a method that would emit a str signal from time to time (3 sec apart)
        pvalue=0
        self.running = True
        self.str_signal.emit('Thread id is: ' + str(int(QtCore.QThread.currentThreadId())))
        while self.running:
            pvalue=pvalue+1
            self.sleep(3)
            self.str_signal.emit('Thread ran at: ' + str(datetime.now()))
            self.progress.emit(pvalue)

    def stop(self):
        self.str_signal.emit('Background thread will be terminated after its outstanding work will be done')
        self.running=False
        

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mt.ui', self) #load the UI file that contains a text edit box named textEdit

        self.statusTh = UpdateThread() #declare a new instance of the update thread
        self.statusTh.str_signal.connect(self.textEdit.append) #connect te signal of the update thread to the append signal of the textEdit object in GUI
        self.statusTh.start() #start the thread 
        self.stopRefresh.clicked.connect(self.statusTh.stop)
        self.startRefresh.clicked.connect(self.statusTh.start)
        self.statusTh.progress.connect(self.progressBar.setValue)
        self.show() #show the GUI


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()