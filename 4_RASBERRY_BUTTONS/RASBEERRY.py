import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("LED.ui")[0]


 
class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.pushButton_11.clicked.connect(self.Play_button_11_clicked)
  #self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
 
 
 # Eventos de botones 
 def Play_button_11_clicked(self):
 # encendido = 0
 #  if encendido == 0
    os.system("xterm -e 'bash -c \"sudo sh /etc/init.d/ssh start; exec bash\"'")
 #   encendido = 1
 #  end if
 
 # Evento del boton btn_FtoC
 # def btn_FtoC_clicked(self):
 
 
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()














    
