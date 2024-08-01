import sys
from PyQt5 import QtGui

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ppTool.ui.FilterBox import Ui_addFilterBox
from ppTool.ui.MainBox import Ui_MainWindow
from ppTool.ui.testDialog import Ui_TestDialog
from ppTool.ui.test2 import Ui_Dialog


class NewWindow(QMainWindow,Ui_MainWindow):
   def __init__(self):

      # 继承QMainWindow
      super().__init__()
      # self.setupUi(self)
      self.setupUi(self)



class main_box(QMainWindow, Ui_MainWindow):
   """继承类"""

   def __init__(self):
      # 继承QMainWindow
      super().__init__()
      self.setupUi(self)

class test_dialog(QMainWindow,Ui_TestDialog):
   """继承类"""

   def __init__(self):
      # 继承QMainWindow
      super().__init__()
      self.setupUi(self)

class test_dialog2(QMainWindow,Ui_Dialog):
   """继承类"""

   def __init__(self, parent=None):
      # 继承QMainWindow
      super(test_dialog2, self).__init__(parent)
      self.setupUi(self)


def window():
   app = QApplication(sys.argv)
   mainBox=NewWindow()
   filterDialog=test_dialog()
   mainBox.addFilterBtn.clicked.connect(filterDialog.show)
   mainBox.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   window()