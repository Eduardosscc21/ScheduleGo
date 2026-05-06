from PySide6.QtWidgets import  QApplication
from mainwindow import MainWindow
import sys


#Inicar aplicacion
app = QApplication(sys.argv)
# cargar archivos .ui

window = MainWindow()

window.show()

exit(app.exec_())
