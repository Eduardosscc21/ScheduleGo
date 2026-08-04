# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(781, 581)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(0, 0, 0)")
        self.gridLayout_9 = QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_S = QFrame(self.frame)
        self.frame_S.setObjectName(u"frame_S")
        self.frame_S.setMinimumSize(QSize(0, 42))
        self.frame_S.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#000000ff;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgb(61,61,61);\n"
"border-radius: 20px;\n"
"}")
        self.frame_S.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_S.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_S)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_menu = QPushButton(self.frame_S)
        self.pushButton_menu.setObjectName(u"pushButton_menu")
        self.pushButton_menu.setMinimumSize(QSize(200, 38))
        icon = QIcon()
        icon.addFile(u"../../../../../../../../../root/.designer/crear_horarios/barra.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_menu.setIcon(icon)
        self.pushButton_menu.setIconSize(QSize(38, 28))

        self.horizontalLayout.addWidget(self.pushButton_menu)

        self.horizontalSpacer = QSpacerItem(189, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_minimizar = QPushButton(self.frame_S)
        self.pushButton_minimizar.setObjectName(u"pushButton_minimizar")
        self.pushButton_minimizar.setMinimumSize(QSize(38, 38))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../../../../root/.designer/crear_horarios/minimizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_minimizar.setIcon(icon1)
        self.pushButton_minimizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton_minimizar)

        self.pushButton_ampliar = QPushButton(self.frame_S)
        self.pushButton_ampliar.setObjectName(u"pushButton_ampliar")
        self.pushButton_ampliar.setMinimumSize(QSize(38, 38))
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../../../root/.designer/crear_horarios/ampliar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_ampliar.setIcon(icon2)
        self.pushButton_ampliar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton_ampliar)

        self.pushButton_cerrar = QPushButton(self.frame_S)
        self.pushButton_cerrar.setObjectName(u"pushButton_cerrar")
        self.pushButton_cerrar.setMinimumSize(QSize(38, 38))
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../../../../root/.designer/crear_horarios/cerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_cerrar.setIcon(icon3)
        self.pushButton_cerrar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.pushButton_cerrar)


        self.verticalLayout_2.addWidget(self.frame_S)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_control = QFrame(self.frame_contenido)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(200, 0))
        self.frame_control.setStyleSheet(u"QFrame{\n"
"background-color:rgb(0,206,151);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_datos = QPushButton(self.frame_control)
        self.pushButton_datos.setObjectName(u"pushButton_datos")
        self.pushButton_datos.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_datos)

        self.bt_cargar = QPushButton(self.frame_control)
        self.bt_cargar.setObjectName(u"bt_cargar")
        self.bt_cargar.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.bt_cargar)

        self.pushButton_actualizar = QPushButton(self.frame_control)
        self.pushButton_actualizar.setObjectName(u"pushButton_actualizar")
        self.pushButton_actualizar.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_actualizar)

        self.pushButton_eliminar = QPushButton(self.frame_control)
        self.pushButton_eliminar.setObjectName(u"pushButton_eliminar")
        self.pushButton_eliminar.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_eliminar)

        self.bt_choque_materias = QPushButton(self.frame_control)
        self.bt_choque_materias.setObjectName(u"bt_choque_materias")
        self.bt_choque_materias.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.bt_choque_materias)

        self.pushButton_crear_horarios = QPushButton(self.frame_control)
        self.pushButton_crear_horarios.setObjectName(u"pushButton_crear_horarios")
        self.pushButton_crear_horarios.setMinimumSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.pushButton_crear_horarios)


        self.horizontalLayout_2.addWidget(self.frame_control)

        self.frame_paginas = QFrame(self.frame_contenido)
        self.frame_paginas.setObjectName(u"frame_paginas")
        self.frame_paginas.setStyleSheet(u"QFrame{\n"
"background-color:rgb(61,61,61);\n"
"}\n"
"\n"
"QLabel{\n"
"font:87 12pt\"Arial Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(0,206,151);\n"
"border:0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:0px;\n"
"color:rgb(255,255,255);\n"
"border-bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt\"Times New Roman\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-radius:15px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(0,206,151);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);\n"
"font: 77 10pt\"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"gridline-color:rgb(0,206,151);\n"
"font-size: 12pt;\n"
"color:#000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color:rgb(0,206,151);\n"
"border:1px solid rgb(0,0,0);\n"
"font-size:12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color:rgb(0,0,0);\n"
"bo"
                        "rder:1px solid rgb(0,206,151);\n"
"}")
        self.frame_paginas.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_paginas.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.stackedWidget = QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_cargar = QWidget()
        self.page_cargar.setObjectName(u"page_cargar")
        self.gridLayout_4 = QGridLayout(self.page_cargar)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.signal_carga_csv = QPushButton(self.page_cargar)
        self.signal_carga_csv.setObjectName(u"signal_carga_csv")

        self.gridLayout.addWidget(self.signal_carga_csv, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.page_cargar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_cargar)
        self.page_eliminar = QWidget()
        self.page_eliminar.setObjectName(u"page_eliminar")
        self.verticalLayout_13 = QVBoxLayout(self.page_eliminar)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.page_eliminar)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_nrc_eliminar = QLabel(self.page_eliminar)
        self.label_nrc_eliminar.setObjectName(u"label_nrc_eliminar")

        self.horizontalLayout_9.addWidget(self.label_nrc_eliminar)

        self.materia_eliminar = QLineEdit(self.page_eliminar)
        self.materia_eliminar.setObjectName(u"materia_eliminar")

        self.horizontalLayout_9.addWidget(self.materia_eliminar)

        self.bt_buscar_eliminar = QPushButton(self.page_eliminar)
        self.bt_buscar_eliminar.setObjectName(u"bt_buscar_eliminar")
        self.bt_buscar_eliminar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_9.addWidget(self.bt_buscar_eliminar)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.tabla_borrar = QTableWidget(self.page_eliminar)
        if (self.tabla_borrar.columnCount() < 9):
            self.tabla_borrar.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabla_borrar.setObjectName(u"tabla_borrar")

        self.verticalLayout_13.addWidget(self.tabla_borrar)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.page_eliminar)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_10.addWidget(self.label_16)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.signal_eliminar = QPushButton(self.page_eliminar)
        self.signal_eliminar.setObjectName(u"signal_eliminar")

        self.horizontalLayout_10.addWidget(self.signal_eliminar)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_actualizar = QWidget()
        self.page_actualizar.setObjectName(u"page_actualizar")
        self.verticalLayout_12 = QVBoxLayout(self.page_actualizar)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_13 = QLabel(self.page_actualizar)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_13)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.page_actualizar)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.act_buscar = QLineEdit(self.page_actualizar)
        self.act_buscar.setObjectName(u"act_buscar")

        self.horizontalLayout_8.addWidget(self.act_buscar)

        self.bt_buscar_actializar = QPushButton(self.page_actualizar)
        self.bt_buscar_actializar.setObjectName(u"bt_buscar_actializar")
        self.bt_buscar_actializar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_8.addWidget(self.bt_buscar_actializar)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.page_actualizar)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_11 = QLabel(self.page_actualizar)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_8 = QLabel(self.page_actualizar)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_6 = QLabel(self.page_actualizar)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.page_actualizar)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_5 = QLabel(self.page_actualizar)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_4 = QLabel(self.page_actualizar)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_3 = QLabel(self.page_actualizar)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_2 = QLabel(self.page_actualizar)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.act_nrc_2 = QLineEdit(self.page_actualizar)
        self.act_nrc_2.setObjectName(u"act_nrc_2")

        self.verticalLayout_11.addWidget(self.act_nrc_2)

        self.act_clave_2 = QLineEdit(self.page_actualizar)
        self.act_clave_2.setObjectName(u"act_clave_2")

        self.verticalLayout_11.addWidget(self.act_clave_2)

        self.act_materia_2 = QLineEdit(self.page_actualizar)
        self.act_materia_2.setObjectName(u"act_materia_2")

        self.verticalLayout_11.addWidget(self.act_materia_2)

        self.act_sec_2 = QLineEdit(self.page_actualizar)
        self.act_sec_2.setObjectName(u"act_sec_2")

        self.verticalLayout_11.addWidget(self.act_sec_2)

        self.act_cr_2 = QLineEdit(self.page_actualizar)
        self.act_cr_2.setObjectName(u"act_cr_2")

        self.verticalLayout_11.addWidget(self.act_cr_2)

        self.act_cup_2 = QLineEdit(self.page_actualizar)
        self.act_cup_2.setObjectName(u"act_cup_2")

        self.verticalLayout_11.addWidget(self.act_cup_2)

        self.act_dis_2 = QLineEdit(self.page_actualizar)
        self.act_dis_2.setObjectName(u"act_dis_2")

        self.verticalLayout_11.addWidget(self.act_dis_2)

        self.act_hora = QLineEdit(self.page_actualizar)
        self.act_hora.setObjectName(u"act_hora")

        self.verticalLayout_11.addWidget(self.act_hora)

        self.act_profesor_2 = QLineEdit(self.page_actualizar)
        self.act_profesor_2.setObjectName(u"act_profesor_2")

        self.verticalLayout_11.addWidget(self.act_profesor_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.page_actualizar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(129, 30))

        self.horizontalLayout_4.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.signal_actualizar = QPushButton(self.page_actualizar)
        self.signal_actualizar.setObjectName(u"signal_actualizar")
        self.signal_actualizar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_4.addWidget(self.signal_actualizar)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page_actualizar)
        self.page_choque_materias = QWidget()
        self.page_choque_materias.setObjectName(u"page_choque_materias")
        self.gridLayout_11 = QGridLayout(self.page_choque_materias)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.nrc_choque_materias = QLabel(self.page_choque_materias)
        self.nrc_choque_materias.setObjectName(u"nrc_choque_materias")

        self.gridLayout_5.addWidget(self.nrc_choque_materias, 0, 0, 1, 1)

        self.materia_choque = QLineEdit(self.page_choque_materias)
        self.materia_choque.setObjectName(u"materia_choque")

        self.gridLayout_5.addWidget(self.materia_choque, 0, 1, 1, 1)

        self.nrc_choque_materias_2 = QLabel(self.page_choque_materias)
        self.nrc_choque_materias_2.setObjectName(u"nrc_choque_materias_2")

        self.gridLayout_5.addWidget(self.nrc_choque_materias_2, 0, 2, 1, 1)

        self.materia_choque_2 = QLineEdit(self.page_choque_materias)
        self.materia_choque_2.setObjectName(u"materia_choque_2")

        self.gridLayout_5.addWidget(self.materia_choque_2, 0, 3, 1, 1)

        self.signal_choque_materias = QPushButton(self.page_choque_materias)
        self.signal_choque_materias.setObjectName(u"signal_choque_materias")
        self.signal_choque_materias.setMinimumSize(QSize(120, 30))

        self.gridLayout_5.addWidget(self.signal_choque_materias, 0, 4, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabla_materias_chocando = QTableWidget(self.page_choque_materias)
        if (self.tabla_materias_chocando.columnCount() < 9):
            self.tabla_materias_chocando.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_materias_chocando.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.tabla_materias_chocando.setObjectName(u"tabla_materias_chocando")

        self.gridLayout_11.addWidget(self.tabla_materias_chocando, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_choque_materias)
        self.page_crea_horarios = QWidget()
        self.page_crea_horarios.setObjectName(u"page_crea_horarios")
        self.gridLayout_8 = QGridLayout(self.page_crea_horarios)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_18 = QLabel(self.page_crea_horarios)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 3, 0, 1, 1)

        self.label_17 = QLabel(self.page_crea_horarios)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)

        self.materia5 = QLineEdit(self.page_crea_horarios)
        self.materia5.setObjectName(u"materia5")

        self.gridLayout_6.addWidget(self.materia5, 0, 3, 1, 1)

        self.materia6 = QLineEdit(self.page_crea_horarios)
        self.materia6.setObjectName(u"materia6")

        self.gridLayout_6.addWidget(self.materia6, 1, 3, 2, 1)

        self.label_24 = QLabel(self.page_crea_horarios)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 4, 2, 1, 1)

        self.materia7 = QLineEdit(self.page_crea_horarios)
        self.materia7.setObjectName(u"materia7")

        self.gridLayout_6.addWidget(self.materia7, 3, 3, 1, 1)

        self.materia3 = QLineEdit(self.page_crea_horarios)
        self.materia3.setObjectName(u"materia3")

        self.gridLayout_6.addWidget(self.materia3, 3, 1, 1, 1)

        self.materia1 = QLineEdit(self.page_crea_horarios)
        self.materia1.setObjectName(u"materia1")

        self.gridLayout_6.addWidget(self.materia1, 0, 1, 2, 1)

        self.materia2 = QLineEdit(self.page_crea_horarios)
        self.materia2.setObjectName(u"materia2")

        self.gridLayout_6.addWidget(self.materia2, 2, 1, 1, 1)

        self.label_19 = QLabel(self.page_crea_horarios)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 4, 0, 1, 1)

        self.materia4 = QLineEdit(self.page_crea_horarios)
        self.materia4.setObjectName(u"materia4")

        self.gridLayout_6.addWidget(self.materia4, 4, 1, 1, 1)

        self.label_20 = QLabel(self.page_crea_horarios)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_21 = QLabel(self.page_crea_horarios)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 1, 2, 2, 1)

        self.label_15 = QLabel(self.page_crea_horarios)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_22 = QLabel(self.page_crea_horarios)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 3, 2, 1, 1)

        self.linea_ciclo = QLineEdit(self.page_crea_horarios)
        self.linea_ciclo.setObjectName(u"linea_ciclo")

        self.gridLayout_6.addWidget(self.linea_ciclo, 4, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.signal_crear_horario = QPushButton(self.page_crea_horarios)
        self.signal_crear_horario.setObjectName(u"signal_crear_horario")

        self.gridLayout_7.addWidget(self.signal_crear_horario, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_crea_horarios)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horario1 = QTableWidget(self.groupBox)
        if (self.horario1.columnCount() < 6):
            self.horario1.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.horario1.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        if (self.horario1.rowCount() < 7):
            self.horario1.setRowCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.horario1.setVerticalHeaderItem(6, __qtablewidgetitem30)
        self.horario1.setObjectName(u"horario1")

        self.gridLayout_10.addWidget(self.horario1, 0, 0, 1, 1)

        self.horario2 = QTableWidget(self.groupBox)
        if (self.horario2.columnCount() < 6):
            self.horario2.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.horario2.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        if (self.horario2.rowCount() < 7):
            self.horario2.setRowCount(7)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.horario2.setVerticalHeaderItem(6, __qtablewidgetitem43)
        self.horario2.setObjectName(u"horario2")

        self.gridLayout_10.addWidget(self.horario2, 0, 1, 1, 1)

        self.horario3 = QTableWidget(self.groupBox)
        if (self.horario3.columnCount() < 6):
            self.horario3.setColumnCount(6)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.horario3.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        if (self.horario3.rowCount() < 7):
            self.horario3.setRowCount(7)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(3, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(5, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.horario3.setVerticalHeaderItem(6, __qtablewidgetitem56)
        self.horario3.setObjectName(u"horario3")

        self.gridLayout_10.addWidget(self.horario3, 0, 2, 1, 1)

        self.horario4 = QTableWidget(self.groupBox)
        if (self.horario4.columnCount() < 6):
            self.horario4.setColumnCount(6)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.horario4.setHorizontalHeaderItem(5, __qtablewidgetitem62)
        if (self.horario4.rowCount() < 7):
            self.horario4.setRowCount(7)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.horario4.setVerticalHeaderItem(6, __qtablewidgetitem69)
        self.horario4.setObjectName(u"horario4")

        self.gridLayout_10.addWidget(self.horario4, 1, 0, 1, 1)

        self.horario5 = QTableWidget(self.groupBox)
        if (self.horario5.columnCount() < 6):
            self.horario5.setColumnCount(6)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.horario5.setHorizontalHeaderItem(5, __qtablewidgetitem75)
        if (self.horario5.rowCount() < 7):
            self.horario5.setRowCount(7)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(5, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.horario5.setVerticalHeaderItem(6, __qtablewidgetitem82)
        self.horario5.setObjectName(u"horario5")

        self.gridLayout_10.addWidget(self.horario5, 1, 1, 1, 1)

        self.horario6 = QTableWidget(self.groupBox)
        if (self.horario6.columnCount() < 6):
            self.horario6.setColumnCount(6)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(4, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.horario6.setHorizontalHeaderItem(5, __qtablewidgetitem88)
        if (self.horario6.rowCount() < 7):
            self.horario6.setRowCount(7)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(0, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(1, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(2, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(3, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(4, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(5, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.horario6.setVerticalHeaderItem(6, __qtablewidgetitem95)
        self.horario6.setObjectName(u"horario6")

        self.gridLayout_10.addWidget(self.horario6, 1, 2, 1, 1)

        self.bt_descargar_csv = QPushButton(self.groupBox)
        self.bt_descargar_csv.setObjectName(u"bt_descargar_csv")

        self.gridLayout_10.addWidget(self.bt_descargar_csv, 2, 2, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_crea_horarios)
        self.page_datos = QWidget()
        self.page_datos.setObjectName(u"page_datos")
        self.verticalLayout_5 = QVBoxLayout(self.page_datos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_datos)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.Tabla_materias = QTableWidget(self.page_datos)
        if (self.Tabla_materias.columnCount() < 9):
            self.Tabla_materias.setColumnCount(9)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(0, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(1, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(2, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(3, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(4, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(5, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(6, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(7, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.Tabla_materias.setHorizontalHeaderItem(8, __qtablewidgetitem104)
        self.Tabla_materias.setObjectName(u"Tabla_materias")

        self.verticalLayout_5.addWidget(self.Tabla_materias)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(188, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bt_refrescar = QPushButton(self.page_datos)
        self.bt_refrescar.setObjectName(u"bt_refrescar")
        self.bt_refrescar.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_3.addWidget(self.bt_refrescar)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_datos)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_paginas)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.frame_contenido)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.gridLayout_9.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_menu.setText("")
        self.pushButton_minimizar.setText("")
        self.pushButton_ampliar.setText("")
        self.pushButton_cerrar.setText("")
        self.pushButton_datos.setText(QCoreApplication.translate("MainWindow", u"Base de datos", None))
        self.bt_cargar.setText(QCoreApplication.translate("MainWindow", u"Cargar archivos", None))
        self.pushButton_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.pushButton_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.bt_choque_materias.setText(QCoreApplication.translate("MainWindow", u"Choque materias", None))
        self.pushButton_crear_horarios.setText(QCoreApplication.translate("MainWindow", u"Crear horarios", None))
        self.signal_carga_csv.setText(QCoreApplication.translate("MainWindow", u"Cargar csv", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Eliminar materia", None))
        self.label_nrc_eliminar.setText(QCoreApplication.translate("MainWindow", u"Nrc", None))
        self.bt_buscar_eliminar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nrc", None));
        ___qtablewidgetitem1 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem2 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Materia", None));
        ___qtablewidgetitem3 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sec", None));
        ___qtablewidgetitem4 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CR", None));
        ___qtablewidgetitem5 = self.tabla_borrar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cup", None));
        ___qtablewidgetitem6 = self.tabla_borrar.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Dis", None));
        ___qtablewidgetitem7 = self.tabla_borrar.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"S/H/D/E", None));
        ___qtablewidgetitem8 = self.tabla_borrar.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Ses/Profesor", None));
        self.label_16.setText("")
        self.signal_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NRC de la materia", None))
        self.bt_buscar_actializar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nrc", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Clave", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Materia", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sec", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cr", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cup", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dis", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"S/H/D/E/A", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sec/Profesor", None))
        self.label_10.setText("")
        self.signal_actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.nrc_choque_materias.setText(QCoreApplication.translate("MainWindow", u"Nrc", None))
        self.nrc_choque_materias_2.setText(QCoreApplication.translate("MainWindow", u"ciclo", None))
        self.signal_choque_materias.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem9 = self.tabla_materias_chocando.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nrc", None));
        ___qtablewidgetitem10 = self.tabla_materias_chocando.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem11 = self.tabla_materias_chocando.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Materia", None));
        ___qtablewidgetitem12 = self.tabla_materias_chocando.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sec", None));
        ___qtablewidgetitem13 = self.tabla_materias_chocando.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CR", None));
        ___qtablewidgetitem14 = self.tabla_materias_chocando.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cup", None));
        ___qtablewidgetitem15 = self.tabla_materias_chocando.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Dis", None));
        ___qtablewidgetitem16 = self.tabla_materias_chocando.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"S/H/D/E", None));
        ___qtablewidgetitem17 = self.tabla_materias_chocando.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Ses/Profesor", None));
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Materia 3", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Materia 2", None))
        self.materia5.setText("")
        self.materia6.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Ciclo", None))
        self.materia7.setText("")
        self.materia1.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Materia 4", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Materia 5", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Materia 6", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Materia 1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Materia 7", None))
        self.linea_ciclo.setText("")
        self.signal_crear_horario.setText(QCoreApplication.translate("MainWindow", u"Crear horario", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Horarios", None))
        ___qtablewidgetitem18 = self.horario1.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem19 = self.horario1.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem20 = self.horario1.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem21 = self.horario1.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem22 = self.horario1.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem23 = self.horario1.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem24 = self.horario1.verticalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem25 = self.horario1.verticalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem26 = self.horario1.verticalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem27 = self.horario1.verticalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem28 = self.horario1.verticalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem29 = self.horario1.verticalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem30 = self.horario1.verticalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        ___qtablewidgetitem31 = self.horario2.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem32 = self.horario2.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem33 = self.horario2.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem34 = self.horario2.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem35 = self.horario2.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem36 = self.horario2.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem37 = self.horario2.verticalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem38 = self.horario2.verticalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem39 = self.horario2.verticalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem40 = self.horario2.verticalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem41 = self.horario2.verticalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem42 = self.horario2.verticalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem43 = self.horario2.verticalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        ___qtablewidgetitem44 = self.horario3.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem45 = self.horario3.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem46 = self.horario3.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem47 = self.horario3.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem48 = self.horario3.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem49 = self.horario3.horizontalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem50 = self.horario3.verticalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem51 = self.horario3.verticalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem52 = self.horario3.verticalHeaderItem(2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem53 = self.horario3.verticalHeaderItem(3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem54 = self.horario3.verticalHeaderItem(4)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem55 = self.horario3.verticalHeaderItem(5)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem56 = self.horario3.verticalHeaderItem(6)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        ___qtablewidgetitem57 = self.horario4.horizontalHeaderItem(0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem58 = self.horario4.horizontalHeaderItem(1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem59 = self.horario4.horizontalHeaderItem(2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem60 = self.horario4.horizontalHeaderItem(3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem61 = self.horario4.horizontalHeaderItem(4)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem62 = self.horario4.horizontalHeaderItem(5)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem63 = self.horario4.verticalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem64 = self.horario4.verticalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem65 = self.horario4.verticalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem66 = self.horario4.verticalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem67 = self.horario4.verticalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem68 = self.horario4.verticalHeaderItem(5)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem69 = self.horario4.verticalHeaderItem(6)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        ___qtablewidgetitem70 = self.horario5.horizontalHeaderItem(0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem71 = self.horario5.horizontalHeaderItem(1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem72 = self.horario5.horizontalHeaderItem(2)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem73 = self.horario5.horizontalHeaderItem(3)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem74 = self.horario5.horizontalHeaderItem(4)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem75 = self.horario5.horizontalHeaderItem(5)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem76 = self.horario5.verticalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem77 = self.horario5.verticalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem78 = self.horario5.verticalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem79 = self.horario5.verticalHeaderItem(3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem80 = self.horario5.verticalHeaderItem(4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem81 = self.horario5.verticalHeaderItem(5)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem82 = self.horario5.verticalHeaderItem(6)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        ___qtablewidgetitem83 = self.horario6.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Lunes", None));
        ___qtablewidgetitem84 = self.horario6.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Martes", None));
        ___qtablewidgetitem85 = self.horario6.horizontalHeaderItem(2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Miercoles", None));
        ___qtablewidgetitem86 = self.horario6.horizontalHeaderItem(3)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Jueves", None));
        ___qtablewidgetitem87 = self.horario6.horizontalHeaderItem(4)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Viernes", None));
        ___qtablewidgetitem88 = self.horario6.horizontalHeaderItem(5)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Sabado", None));
        ___qtablewidgetitem89 = self.horario6.verticalHeaderItem(0)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"0700-0855", None));
        ___qtablewidgetitem90 = self.horario6.verticalHeaderItem(1)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"0900-1055", None));
        ___qtablewidgetitem91 = self.horario6.verticalHeaderItem(2)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"1100-1255", None));
        ___qtablewidgetitem92 = self.horario6.verticalHeaderItem(3)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"1300-1455", None));
        ___qtablewidgetitem93 = self.horario6.verticalHeaderItem(4)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"1500-1655", None));
        ___qtablewidgetitem94 = self.horario6.verticalHeaderItem(5)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"1700-1855", None));
        ___qtablewidgetitem95 = self.horario6.verticalHeaderItem(6)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"1900-2055", None));
        self.bt_descargar_csv.setText(QCoreApplication.translate("MainWindow", u"Descargar horarios", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Materias", None))
        ___qtablewidgetitem96 = self.Tabla_materias.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"NRC", None));
        ___qtablewidgetitem97 = self.Tabla_materias.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Clave", None));
        ___qtablewidgetitem98 = self.Tabla_materias.horizontalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Materia", None));
        ___qtablewidgetitem99 = self.Tabla_materias.horizontalHeaderItem(3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Sec", None));
        ___qtablewidgetitem100 = self.Tabla_materias.horizontalHeaderItem(4)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"CR", None));
        ___qtablewidgetitem101 = self.Tabla_materias.horizontalHeaderItem(5)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Cup", None));
        ___qtablewidgetitem102 = self.Tabla_materias.horizontalHeaderItem(6)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Disp", None));
        ___qtablewidgetitem103 = self.Tabla_materias.horizontalHeaderItem(7)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Ses/Hora/Dias/Edif/Aula/Periodo", None));
        ___qtablewidgetitem104 = self.Tabla_materias.horizontalHeaderItem(8)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Ses/Profesor", None));
        self.bt_refrescar.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
    # retranslateUi

