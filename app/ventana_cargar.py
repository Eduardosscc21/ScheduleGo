import sys
sys.path.append(r".")
from PySide6.QtWidgets import  QApplication
from main import VentanaPresentacion

#Inicar aplicacion
app = QApplication(sys.argv)
# cargar archivos .ui

window = VentanaPresentacion()

window.show()

sys.exit(app.exec())
