import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtGui import QIcon
from ui.ProgressDialogUI import Ui_Dialog
class ProgressDialog(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Down'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.uRLLineEdit.setText("hfhd")
        #print(self.ui.uRLLineEdit.text()=="")
        #self.ui.uRLLabel.setText("e")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProgressDialog()
    ex.show()
    sys.exit(app.exec_())
