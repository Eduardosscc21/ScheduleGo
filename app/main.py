import sys
import re
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
from mainwindow import MainWindow
from interfaz import Ui_VentanaPresentacion #se importa la interfaz.py
from api_client import autenticar, registrar_estudiante


#se hereda QWidget de la interfaz.py
class VentanaPresentacion(QWidget, Ui_VentanaPresentacion):
    def __init__(self):
        super().__init__()
        #Se carga la interfaz visual 
        self.setupUi(self)
        self.init_logica()
    
    def init_logica(self):
        # Conectar botones a funciones
        self.btn_estudiante.clicked.connect(self.ir_a_estudiante)
        self.btn_admin.clicked.connect(self.ir_a_admin)
        self.btn_regresar.clicked.connect(self.regresar_y_limpiar)
        self.btn_crear.clicked.connect(self.preparar_registro)
        self.btn_cancelar_reg.clicked.connect(self.cancelar_registro)
        self.btn_registrar_final.clicked.connect(self.registrar_estudiante)
        self.btn_iniciar.clicked.connect(self.login_usuario)
        self.btn_ver_pass_login.clicked.connect(self.alternar_ver_password)
        self.btn_ver_pass.clicked.connect(self.alternar_ver_password)
        
    def regresar_y_limpiar(self):
        self.input_correo.clear()
        self.input_pass.clear()
        self.cambiarSeleccion.setCurrentIndex(0)
            
    def ir_a_estudiante(self):
        self.limpiar_todo()
        self.btn_crear.show()
        self.label_error.setText("")
        print("Cambiando a login de estudiantes")
        self.label_rol.setText("Iniciar Sesión Estudiante")
        self.cambiarSeleccion.setCurrentIndex(1)

    def ir_a_admin(self):
        self.btn_crear.hide()
        self.label_error.setText("")
        print("Cambiando a login de administradores") 
        self.label_rol.setText("Iniciar Sesión Administrador")
        self.cambiarSeleccion.setCurrentIndex(1)
                
    def registrar_estudiante(self):
        self.label_error_reg.setStyleSheet("color: #ff4d4d; font-weight: bold; background: transparent;")
        nombre_completo   = self.reg_nombre_completo.text().strip()
        correo_estudiante = self.reg_correo_estudiante.text().strip()
        codigo_estudiante = self.reg_codigo_estudiante.text().strip()
        password          = self.reg_password.text().strip()
            
        if not nombre_completo or not codigo_estudiante or not correo_estudiante or not password:
            self.label_error_reg.setText("Error: Todos los campos son obligatorios")
            print("Error todos los cambpos son obligatorios")
            self.reg_nombre_completo.clear()
            self.reg_codigo_estudiante.clear()
            self.reg_correo_estudiante.clear()
            self.reg_password.clear()
            QTimer.singleShot(2000, lambda: self.label_error_reg.setText(""))
            return
        
        patron_correo = r'^[a-zA-Z0-9.]+@alumnos?\.udg\.mx$'
        if not re.match(patron_correo, correo_estudiante):
            self.label_error_reg.setText("Error: Usa tu correo institucional")
            self.reg_correo_estudiante.clear()
            QTimer.singleShot(2000, lambda: self.label_error_reg.setText(""))
            return
        
        if len (codigo_estudiante) !=9 or not codigo_estudiante.isdigit():
            self.label_error_reg.setText("Error: El código debe ser solo números")
            self.reg_codigo_estudiante.clear()
            QTimer.singleShot(2000, lambda: self.label_error_reg.setText(""))
            return
        
        patron_pass = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[.%$@!#%^&*])[A-Za-z\d.%$@!#%^&*]{6,16}$'
        if not re.match(patron_pass, password):
            self.label_error_reg.setText("Error: La contraseña debe tener 6-16 caracteres, "
                                         "incluir mayúscula, minúscula, número y caracter especial.")
            self.reg_password.clear()
            QTimer.singleShot(6000, lambda: self.label_error_reg.setText(""))
            return
        
        respuesta = registrar_estudiante(
            nombre_completo=nombre_completo,
            codigo_estudiante=codigo_estudiante,
            correo_estudiante=correo_estudiante,
            password=password
        )
        if respuesta["success"]:
            self.label_error_reg.setStyleSheet("color: #2ecc71; font-weight: bold; background: transparent;")
            self.label_error_reg.setText(respuesta["mensaje"])
            self.reg_nombre_completo.clear()
            self.reg_codigo_estudiante.clear()
            self.reg_correo_estudiante.clear()
            self.reg_password.clear()

            QTimer.singleShot(
                2000, lambda: [
                    self.label_error_reg.setText(""),
                    self.label_error_reg.setStyleSheet(
                        "color: #ff4d4d; font-weight: bold; background: transparent;"
                    )
                ]
            )
        else:
            self.label_error_reg.setStyleSheet("color: #ff4d4d; font-weight: bold; background: transparent;")
            self.label_error_reg.setText(respuesta["mensaje"])

            if "correo" in respuesta["mensaje"].lower():
                self.reg_correo_estudiante.clear()
            if "codigo" in respuesta["mensaje"].lower():
                self.reg_codigo_estudiante.clear()
                
            QTimer.singleShot(
                6000,
                lambda: self.label_error_reg.setText("")
            )
    def login_usuario(self):
        correo = self.input_correo.text().strip()
        pas = self.input_pass.text().strip()
        
        es_admin = "Administrador" in self.label_rol.text()
        
        if es_admin:
            tabla = "tb_admins"
            col_correo = "correo_admin"
            col_nombre = "nombre_admin"   
        else:
            tabla = "tb_estudiantes"
            col_correo = "correo_estudiante"
            col_nombre = "nombre_completo"
            
        if not correo or not pas:
            self.label_error.setText("Por favor, llena ambos campos")
            print("Por favor, llena ambos campos")
            self.input_correo.clear()
            self.input_pass.clear()
            QTimer.singleShot(2000, lambda: self.label_error.setText(""))
            return
        
        try:
            rol = "admin" if es_admin else "estudiante"
            respuesta = autenticar(
                correo=correo,
                password=pas,
                rol=rol
            )

            if respuesta["success"]:
                nombre_usuario = respuesta["nombre"]
                self.label_error.setText("")
                print(f"Bienvenido@ {nombre_usuario}")
                self.input_correo.clear()
                self.input_pass.clear()
                self.pantalla_horarios = MainWindow()
                self.pantalla_horarios.show()
                self.close()
            else:
                self.label_error.setText(respuesta["mensaje"])
                print(respuesta["mensaje"])
                self.input_correo.clear()
                self.input_pass.clear()

                QTimer.singleShot(
                    2000,
                    lambda: self.label_error.setText("")
                )
        except Exception as e:
            print(f"Error en el login: {e}")
                
    def limpiar_todo(self):
        self.input_correo.clear()
        self.input_pass.clear()
        self.label_error.setText("")  
        
        self.reg_nombre_completo.clear()
        self.reg_correo_estudiante.clear()
        self.reg_codigo_estudiante.clear()
        self.reg_password.clear()
        self.label_error_reg.setText("")   
        
    def preparar_registro(self):
        self.limpiar_todo()
        self.cambiarSeleccion.setCurrentIndex(2)
        
    def cancelar_registro(self):
        self.limpiar_todo()
        self.cambiarSeleccion.setCurrentIndex(1)
        
    def alternar_ver_password(self):
        boton_presionado = self.sender()
        
        if boton_presionado == self.btn_ver_pass_login:
            if self.input_pass.echoMode() == QLineEdit.EchoMode.Password:
                self.input_pass.setEchoMode(QLineEdit.EchoMode.Normal)
                self.btn_ver_pass_login.setText("Ocultar contraseña")
            else:
                self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
                self.btn_ver_pass_login.setText("Mostrar contraseña")
        
        elif boton_presionado == self.btn_ver_pass:
            if self.reg_password.echoMode() == QLineEdit.EchoMode.Password:
                self.reg_password.setEchoMode(QLineEdit.EchoMode.Normal)
                self.btn_ver_pass.setText("Ocultar contraseña")
            else:
                self.reg_password.setEchoMode(QLineEdit.EchoMode.Password)
                self.btn_ver_pass.setText("Mostrar contraseña")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPresentacion()
    sys.exit(app.exec())    
                 