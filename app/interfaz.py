import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QStackedWidget, QLineEdit
from PySide6.QtGui import QFont, QPixmap
from pathlib import Path


if getattr(sys, "frozen", False):
    DIR_ACTUAL = Path(sys._MEIPASS)
else:
    DIR_ACTUAL = Path(__file__).parent
RUTA_IMAG = DIR_ACTUAL / "iconos" / "logo.png"



class imagEscalable(QLabel):
    def __init__(self, RUTA_IMAG, alto_max=220, parent=None):
        super().__init__(parent)
        self.pixmap_original = QPixmap(str(RUTA_IMAG))
        self.alto_max = alto_max
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background: transparent;")
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.actualizar_imagen()
    
    def actualizar_imagen(self):
        if self.pixmap_original.isNull():
            return
        ancho = self.width()
        alto = min(self.height(), self.alto_max)
        if ancho <= 0:
            ancho = 250
        if alto < 40:
            alto = self.alto_max
        pixmap_escalado = self.pixmap_original.scaled(
            ancho,
            alto,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(pixmap_escalado)
    
    def resizeEvent(self, event):
        self.actualizar_imagen()
        super().resizeEvent(event)
 
   
   

class Ui_VentanaPresentacion(object):
    def setupUi(self, VentanaPresentacion):
        VentanaPresentacion.setObjectName("VentanaPresentacion")
        VentanaPresentacion.setWindowTitle("  ")
        VentanaPresentacion.setGeometry(100, 100, 400, 300)
        
        VentanaPresentacion.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    x1: 0, x2: 0, y2: 1,
                    stop: 0 #020616,
                    stop: 1 #071144
                );
            }
            QLabel {
                color: white;
                font-family: 'Segoe UI' , Arial;
            }
            QPushButton{
                background-color: white;
                color: #000080;
                border-radius: 15px;
                padding: 12px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover{
                background-color: #b7d8e0;
            }
        """)
        
        self.cambiarSeleccion = QStackedWidget(VentanaPresentacion)
        
        # Pagina de inicio
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.logo = imagEscalable(RUTA_IMAG, alto_max=220)
        layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignCenter)
        
        titulo = QLabel("Bienvenid@")
        titulo.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo.setStyleSheet("margin-bottom: 20px;")
        layout.addStretch()
        layout.addWidget(titulo)
        
        subtitulo =QLabel("Selecciona tu usuario")
        subtitulo.setFont(QFont("Arial", 12))
        layout.addWidget(subtitulo)
        
        botones_layout = QHBoxLayout()
        self.btn_estudiante = QPushButton("Estudiante")
        self.btn_admin = QPushButton("Administrativo")
        
        estilo_botones = "padding: 15px; font-size: 14px; min-width: 120px;"
        self.btn_estudiante.setStyleSheet(estilo_botones)
        self.btn_admin.setStyleSheet(estilo_botones)
        
        botones_layout.addWidget(self.btn_estudiante)
        botones_layout.addWidget(self.btn_admin)
        layout.addLayout(botones_layout)
        layout.addStretch()
        
        self.pantalla_inicio =QWidget()
        self.pantalla_inicio.setLayout(layout)
        
        #Formulario del login
        self.pantalla_login =QWidget()
        layout_login =QVBoxLayout()
        layout_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_rol = QLabel("LOGIN")
        self.label_rol.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        
        self.input_correo = QLineEdit()
        self.input_correo.setPlaceholderText("Correo electrónico")
        self.input_correo.setFixedWidth(250)
        self.input_correo.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        
        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Contraseña")
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pass.setFixedWidth(250)
        self.input_pass.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        
        
        # advertencia de de datos incorrectos en admin y estudiante
        self.label_error = QLabel("")
        self.label_error.setStyleSheet("color: #ff4d4d; font-weight: bold; background: transparent;")
        self.label_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_login.addWidget(self.label_error)
        
        # advertencia de de llenar ambos campoos en admin y estudiabte
        self.label_error = QLabel("")
        self.label_error.setStyleSheet("color: #ff4d4d; font-weight: bold; background: transparent;")
        self.label_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_login.addWidget(self.label_error)
        
        self.btn_iniciar = QPushButton("Iniciar Sesion")
        self.btn_regresar = QPushButton("Regresar")
        self.btn_regresar.setStyleSheet("background-color: transparent; color: white; border: 0px solid white; ")
        self.btn_regresar.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btn_olvido = QPushButton("¿Olvidaste tu contraseña?")
        self.btn_crear = QPushButton("¿No tienes cuenta? Regístrate")
        estilo_ayuda = (" background-color: transparent; color: #a0a0a0; font-size: 11px; text-decoration: underline; border: none;")
        self.btn_olvido.setStyleSheet(estilo_ayuda)
        self.btn_crear.setStyleSheet(estilo_ayuda)
        self.btn_olvido.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_crear.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btn_ver_pass_login = QPushButton("Mostrar contraseña")
        self.btn_ver_pass_login.setFixedWidth(120)
        self.btn_ver_pass_login.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_ver_pass_login.setStyleSheet("""
            QPushButton{
                background-color: transparent;
                color: #3498db;
                font-size: 8px;
                border: none;
                text-decoration: underline;
                margin-top: -15px;    
            }
            QPushButton:hover{
                color: white; }
        """)
        
        
        layout_login.addWidget(self.label_rol, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addSpacing(20)
        layout_login.addWidget(self.input_correo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.input_pass, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.btn_ver_pass_login, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addSpacing(15)
        
        #layout_login.addWidget(self.label_error, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        layout_login.addWidget(self.btn_iniciar, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.btn_olvido, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.btn_crear, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addSpacing(10)
        layout_login.addWidget(self.btn_regresar, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.pantalla_login.setLayout(layout_login)
        
        #Formulario de registro
        self.pantalla_registro = QWidget()
        layout_registro = QVBoxLayout()
        layout_registro.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_registro = QLabel("Crear cuenta")
        self.label_registro.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        
        self.reg_nombre_completo = QLineEdit()
        self.reg_nombre_completo.setPlaceholderText("Nombre Completo")
        self.reg_nombre_completo.setFixedWidth(250)
        self.reg_nombre_completo.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        
        self.reg_codigo_estudiante = QLineEdit()
        self.reg_codigo_estudiante.setPlaceholderText("Codigo")
        self.reg_codigo_estudiante.setFixedWidth(250)
        self.reg_codigo_estudiante.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        self.reg_codigo_estudiante.setMaxLength(9)
        
        self.reg_correo_estudiante = QLineEdit()
        self.reg_correo_estudiante.setPlaceholderText("Correo institucional")
        self.reg_correo_estudiante.setFixedWidth(250)
        self.reg_correo_estudiante.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        
        self.reg_password = QLineEdit()
        self.reg_password.setPlaceholderText("Crea una contraseña")
        self.reg_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.reg_password.setFixedWidth(250)
        self.reg_password.setMaxLength(16)
        self.reg_password.setStyleSheet("background-color: white; color: black; border-radius: 5px; padding: 5px;")
        
        self.btn_ver_pass = QPushButton("Mostrar contraseña")
        self.btn_ver_pass.setFixedWidth(120)
        self.btn_ver_pass.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_ver_pass.setStyleSheet("""
            QPushButton{
                background-color: transparent;
                color: #3498db;
                font-size: 8px;
                border: none;
                text-decoration: underline;
                margin-top: -15px;    
            }
            QPushButton:hover{
                color: white; }
        """)
        
        self.btn_registrar_final = QPushButton("Registrarme")
        self.btn_cancelar_reg = QPushButton("Regresar")
        self.btn_cancelar_reg.setStyleSheet(" background-color: transparent; color: white; border: solid white;")
        
        layout_registro.addWidget(self.label_registro, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addSpacing(15)
        layout_registro.addWidget(self.reg_nombre_completo, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.reg_codigo_estudiante, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.reg_correo_estudiante, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.reg_password, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.btn_ver_pass, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addSpacing(15)
        layout_registro.addWidget(self.btn_registrar_final, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.btn_cancelar_reg, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        self.pantalla_registro.setLayout(layout_registro)
        
        #advertencia de llenar todos los campos en registro
        self.label_error_reg = QLabel("")
        self.label_error_reg.setStyleSheet("color: #ff4d4d; font-weight: bold; background: transparent;")
        self.label_error_reg.setWordWrap(True)
        self.label_error_reg.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout_registro.addWidget(self.label_error_reg)
        
        self.pantalla_registro.setLayout(layout_registro)
        
        #Añadir al stackewidget
        self.cambiarSeleccion.addWidget(self.pantalla_inicio)
        self.cambiarSeleccion.addWidget(self.pantalla_login)
        self.cambiarSeleccion.addWidget(self.pantalla_registro)
        
        layout_final = QVBoxLayout(VentanaPresentacion)
        layout_final.addWidget(self.cambiarSeleccion)
        
