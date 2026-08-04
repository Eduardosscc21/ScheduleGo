from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QSizeGrip, QFileDialog
from PySide6.QtCore import Slot, QPropertyAnimation,QEasingCurve,Qt
from PySide6 import QtCore, QtWidgets
from mainwindow_ui import Ui_MainWindow
#from conexionsql_ventanacargar import Comunicacion
#from cre_horarios import HorarioGenetico
#from PySide6.QtUiTools import QUiLoader
import sys
import re 
from datetime import datetime
import random
from itertools import product
import csv
import os 
from openpyxl import Workbook
from api_client import obtener_materias, buscar_materia, actualizar_materia, eliminar_materia, cargar_csv, buscar_choques, crear_horarios

# modificar ui en caso de self en caso de no server y viceversa
class MainWindow(QMainWindow):
#Funciones
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()   ### loadUi(mainwindow.ui,self)
        self.ui.setupUi(self)
        #ui.pushButton.clicked.connect(self.clci)
        ###################### Movilidad de la pantalla ######################
        self.ui.pushButton_menu.clicked.connect(self.mover_menu)
        # comunicacion con la base de datos
        #self.base_datos = Comunicacion()
        #self.cargar_csv = Boton_cargar()
        

        #ocultamos los botones
        self.ui.pushButton_ampliar.hide()
        
        #control barra de titulos
        self.ui.pushButton_minimizar.clicked.connect(self.control_minimizar)
        self.ui.pushButton_ampliar.clicked.connect(self.control_ampliar)
        self.ui.pushButton_cerrar.clicked.connect(self.close)
         
        #eliinar barra y titulo - opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #sizeGrip
        self.ui.gripSize = 10
        self.ui.grip = QSizeGrip(self.ui.centralwidget)
        self.ui.grip.resize(self.ui.gripSize, self.ui.gripSize)

        # mover ventana
        self.ui.frame_S.mouseMoveEvent = self.mover_ventana

        

        # ancho de columna adaptable
        self.ui.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Tabla_materias.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        ####################### botones uso funciones ######################
        self.ui.pushButton_datos.clicked.connect(self.mostrar_materias)
#        self.ui.pushButton_registrar.clicked.connect(self.registrar_materias)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar_materias)
        self.ui.bt_buscar_eliminar.clicked.connect(self.buscar_eliminar)
        self.ui.pushButton_actualizar.clicked.connect(self.modificar_materias)
        self.ui.bt_buscar_actializar.clicked.connect(self.buscar_actualiza)
        self.ui.signal_carga_csv.clicked.connect(self.cargar_csv)
        self.ui.signal_choque_materias.clicked.connect(self.choque_materias)
        self.ui.signal_crear_horario.clicked.connect(self.crear_horario)
        self.ui.bt_descargar_csv.clicked.connect(self.descargar_horarios_csv)
        self.horarios_generados = []
        

                                               #coneccion botones del menu/
        ####aqui me quede en error
        self.ui.pushButton_datos.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_datos))
        self.ui.pushButton_actualizar.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_actualizar))
        self.ui.pushButton_eliminar.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar))
        self.ui.bt_cargar.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_cargar))
        self.ui.bt_choque_materias.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_choque_materias))
        self.ui.pushButton_crear_horarios.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_crea_horarios))


    
    def control_minimizar(self):
        self.showMinimized()
    
    # control_normal ponerlo mas adelante

    def control_normal(self):
        self.showNormal()
        #self.pushButton_normal.hide()
        self.pushButton_ampliar.hide()
    
    def control_ampliar(self):
        self.showMaximized()
        self.pushButton_ampliar.hide()
        #self.pushButton_normal.hide()
    
    #SizeGrip
    def resizeEvent(self,event):
        rect = self.rect()
        self.ui.grip.move(rect.right() - self.ui.gripSize, rect.bottom() - self.ui.gripSize)

    #mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        if  event.globalPos().y() <=10:
            self.showMaximized()
            self.pushButton_ampliar.hide()
            #self.pushButton_restaurar.show()
        else:
            self.showNormal()
            #self.pushButton_restaurar.hide()
            #self.pushButton_ampliar.show()
    
    # metodo para mover menu lateral
    def mover_menu(self):
        width = self.ui.frame_control.width()
        normal = 0
        if width == 0:
            extender = 200
        else:
            extender = normal
        self.animacion = QPropertyAnimation(
            self.ui.frame_control, b'minimumWidth'
        )
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.InQuart)
        self.animacion.start()
    #########################
    @Slot()
    #mostrar materias
    def mostrar_materias(self): # modificar ui por self en caso de que de error
        respuesta = obtener_materias()
        if not respuesta.get("success"):
            QMessageBox.warning(
                self,
                "Error",
                respuesta.get(
                    "mensaje",
                    "No fue posible obtener materias"
                )
            )
            return
        datos = respuesta["materias"]
        self.ui.Tabla_materias.setRowCount(len(datos))
        for fila, materia in enumerate(datos):
            self.ui.Tabla_materias.setItem(
                fila, 0,
                QtWidgets.QTableWidgetItem(str(materia["nrc"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 1,
                QtWidgets.QTableWidgetItem(str(materia["clave"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 2,
                QtWidgets.QTableWidgetItem(str(materia["materia"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 3,
                QtWidgets.QTableWidgetItem(str(materia["sec"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 4,
                QtWidgets.QTableWidgetItem(str(materia["cr"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 5,
                QtWidgets.QTableWidgetItem(str(materia["cup"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 6,
                QtWidgets.QTableWidgetItem(str(materia["dis"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 7,
                QtWidgets.QTableWidgetItem(str(materia["hora_dia"]))
            )
            self.ui.Tabla_materias.setItem(
                fila, 8,
                QtWidgets.QTableWidgetItem(str(materia["profesor"]))
            )
        
   
    @Slot()
    def buscar_actualiza(self):
        nrc = self.ui.act_buscar.text().upper()
        respuesta = buscar_materia(nrc)
        if respuesta.get("success"):
            self.nrc_actual = nrc
            materia = respuesta["materia"]

            self.ui.act_nrc_2.setText(str(materia["nrc"]))
            self.ui.act_clave_2.setText(str(materia["clave"]))
            self.ui.act_materia_2.setText(str(materia["sec"]))
            self.ui.act_sec_2.setText(str(materia["sec"]))
            self.ui.act_cr_2.setText(str(materia["cr"]))
            self.ui.act_cup_2.setText(str(materia["cup"]))
            self.ui.act_dis_2.setText(str(materia["dis"]))
            self.ui.act_hora.setText(str(materia["hora_dia"]))
            self.ui.act_profesor_2.setText(str(materia["profesor"]))

            self.ui.signal_actualizar.setText("Encontrado")
        else:
            self.ui.signal_actualizar.setText("No existe")

            
    @Slot()
    def modificar_materias(self):
        if not hasattr(self, "nrc_actual"):
            self.ui.signal_actualizar.setText("Busque una materia")

        nrc = self.ui.act_nrc_2.text().strip().upper()
        clave = self.ui.act_clave_2.text().strip().upper()
        materia = self.ui.act_materia_2.text().strip().upper()
        sec = self.ui.act_sec_2.text().strip().upper()

        cr = int(self.ui.act_cr_2.text().strip().upper())
        cup = int(self.ui.act_cup_2.text().strip().upper())
        dis = int(self.ui.act_dis_2.text().strip().upper())

        hora_dia = self.ui.act_hora.text().strip().upper()
        profesor = self.ui.act_profesor_2.text().strip().upper()

        respuesta = actualizar_materia(
            nrc,
            clave,
            materia,
            sec,
            cr,
            cup,
            dis,
            hora_dia,
            profesor
        )
        if respuesta.get("success"):
            self.ui.signal_actualizar.setText("Actualizado")
        else:
            self.ui.signal_actualizar.setText("Incorrecto")

           
    @Slot()
    def buscar_eliminar(self):
        nrc = self.ui.materia_eliminar.text().strip().upper()
        respuesta = buscar_materia(nrc)
        self.ui.tabla_borrar.setRowCount(0)

        if not respuesta.get("success"):
            self.ui.signal_eliminar.setText("No existe")
            return

        materia = respuesta["materia"]
        self.ui.tabla_borrar.setRowCount(1)
        self.ui.tabla_borrar.setItem(
            0, 0,
            QtWidgets.QTableWidgetItem(str(materia["nrc"]))
        )
        self.ui.tabla_borrar.setItem(
            0, 1,
            QtWidgets.QTableWidgetItem(materia["clave"])
        )
        self.ui.tabla_borrar.setItem(
            0, 2,
            QtWidgets.QTableWidgetItem(materia["materia"])
        )
        self.ui.tabla_borrar.setItem(
            0, 3,
            QtWidgets.QTableWidgetItem(materia["sec"])
        )
        self.ui.tabla_borrar.setItem(
            0, 4,
            QtWidgets.QTableWidgetItem(str(materia["cr"]))
        )
        self.ui.tabla_borrar.setItem(
            0, 5,
            QtWidgets.QTableWidgetItem(str(materia["cup"]))
        )
        self.ui.tabla_borrar.setItem(
            0, 6,
            QtWidgets.QTableWidgetItem(str(materia["dis"]))
        )
        self.ui.tabla_borrar.setItem(
            0, 7,
            QtWidgets.QTableWidgetItem(materia["hora_dia"])
        )
        self.ui.tabla_borrar.setItem(
            0, 8,
            QtWidgets.QTableWidgetItem(materia["profesor"])
        )
        self.ui.signal_eliminar.setText("materia seleccionada")

        
                
    @Slot()
    def eliminar_materias(self):
        fila = self.ui.tabla_borrar.currentRow()
        if fila < 0:
            self.ui.signal_eliminar.setText("Selecciona una fila")
            return
        nrc = self.ui.tabla_borrar.item(fila, 0).text()
        respuesta = eliminar_materia(nrc)
        if respuesta.get("success"):
            self.ui.tabla_borrar.removeRow(fila)
            self.ui.signal_eliminar.setText("Materia eliminada")
        else:
            self.ui.signal_eliminar.setText(
                respuesta.get(
                    "mensaje",
                    "No fue posible eliminar la materia"
                )
            )

    @Slot()
    def cargar_csv(self):
        archivo, _= QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo csv",
            "",
            "Archivo csv (*.csv)"
        )

        if archivo:
            try:
                respuesta = cargar_csv(archivo)
                if respuesta.get("success"):
                    total = respuesta.get("total", 0)
                    self.ui.signal_carga_csv.setText(f"{total} registros cargados")
                    self.mostrar_materias()
                else:
                    self.ui.signal_carga_csv.setText(
                        respuesta.get(
                            "mensaje",
                            "Error al cargar"
                        )
                    )
            except Exception as e:
                self.ui.signal_carga_csv.setText(f"Error: {str(e)[:50]}")

  # #################### elementos de choque de materias  
    
    @Slot()
    def choque_materias(self):
        nrc = self.ui.materia_choque.text().upper().strip()
        ciclo_buscado = self.ui.materia_choque_2.text().replace(" ", "")

        resultado = buscar_choques(nrc, ciclo_buscado)

        if not resultado.get("success"):
            self.ui.tabla_materias_chocando.clearContents()
            self.ui.tabla_materias_chocando.setRowCount(0)
            self.ui.signal_choque_materias.setText(
                resultado.get(
                    "mensaje",
                    "No fue posible buscar los choques"
                )
            )
            return

        coincidencias = resultado.get(
            "materias",
            []
        )
        self.ui.tabla_materias_chocando.clearContents()
        self.ui.tabla_materias_chocando.setRowCount(len(coincidencias))

        for fila, materia in enumerate(coincidencias):
            datos =[
                materia.get("nrc", ""),
                materia.get("clave", ""),
                materia.get("materia", ""),
                materia.get("sec", ""),
                materia.get("cr", ""),
                materia.get("cup", ""),
                materia.get("dis", ""),
                materia.get("hora_dia", ""),
                materia.get("profesor", "")
            ]

            for columna, valor in enumerate(datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.ui.tabla_materias_chocando.setItem(fila, columna, item)
        self.ui.signal_choque_materias.setText(f"{len(coincidencias)} choque encontrado")
        

            
        
############### elementos crear horarios 
    def limpiar_hora_dia(texto): # este ya estaba asi        
        dias = []
        horarios = []
        patrones = re.findall(r'(\d{2})\s+(\d{4}-\d{4})\s+([LMIJVS\. ]+)'),
        texto
        mapa_dias = ["L", "M", "I", "J", "V", "S"]
        for _, hora, dias_raw in patrones:
            dias_encontrados = [
                dia for dia, marca in zip(
                    mapa_dias,
                    dias_raw.split()
                )
                if marca == dia
            ]
            dias.extend(dias_encontrados)
            horarios.append(hora)
        if not horarios:
            return "", ""
        return "".join(dict.fromkeys(dias)), horarios[0]
        
    def parsear_ciclo(self,ciclo):
        try:
            inicio, fin = ciclo.split('-')
            inicio = datetime.strptime(inicio, "%d/%m/%y")
            fin = datetime.strptime(fin, "%d/%m/%y")
            return inicio, fin
        except:
            return None, None

    

    def obtener_columna_dia(self, dia):
        mapa = {
            "L":0,
            "M":1,
            "I":2,
            "J":3,
            "V":4,
            "S":5
        }
        return [mapa[d] for d in dia if d in mapa]
    
    def obtener_fila_hora(self, hora, tabla):
        #borara una vez se confirme sirve para confirmar lineas
        print("\nBuscand0:", hora)
        for fila in range(tabla.rowCount()):
            item = tabla.verticalHeaderItem(fila)
            #borrar este una vez se confirme
            if item:
                print("fila", fila, "=", item.text())
            #################################
            if item and hora in item.text():
                return fila
        return None
    # intento de correccion del congelamient que se da al ingresar mas e 4
    
    """"
    # algoritmo backtracking
    def generar_horarios(self, materias_dict, materias_ordenadas, max_horarios):
        horarios_validos = []
        def backtrack(indice, horario_actual):
            if len(horarios_validos) >= max_horarios:
                return
            if indice == len(materias_ordenadas):
                horario = sorted(horario_actual, key=self.obtener_inicio)
                horarios_validos.append(horario)
                return
            materia = materias_ordenadas[indice]

            for opcion in materias_dict[materia]:
                if self.es_valido(opcion, horario_actual):
                    horario_actual.append(opcion)
                    backtrack(indice + 1, horario_actual)
                    horario_actual.pop()
        backtrack(0, [])
        return horarios_validos
        """


    @Slot()
    def crear_horario(self):
        #obtener materias ingresdas
        materias_usuario = [
            self.ui.materia1.text().strip().upper(),
            self.ui.materia2.text().strip().upper(),
            self.ui.materia3.text().strip().upper(),
            self.ui.materia4.text().strip().upper(),
            self.ui.materia5.text().strip().upper(),
            self.ui.materia6.text().strip().upper(),
            self.ui.materia7.text().strip().upper()
        ]
        materias_usuario = [m for m in materias_usuario if m]
        #validar minimo de materias
        if len(materias_usuario) < 4:
            self.ui.signal_crear_horario.setText("Ingresa minimo 4 materias")
            return
        #obtner ciclo
        ciclo_usuario = self.ui.linea_ciclo.text().replace(" ", "")
        #solicitar generacion de la api
        respuesta = crear_horarios(
            materias_usuario,
            ciclo_usuario
        )
        #validar respuesta de la api
        if not respuesta.get("success", False):
            self.ui.signal_crear_horario.setText(
                respuesta.get(
                    "mensaje",
                    "No fue posible generar los horarios"
                )
            )
            return
        #guardar horarios recibidos
        horarios_generados = respuesta.get("horarios", [])
        self.horarios_generados = horarios_generados
        #mostrar mensaje
        self.ui.signal_crear_horario.setText(
            f"Generacion exitosa: {len(horarios_generados)} horarios"
        )
        #tablas de la interfaz
        tablas = [
            self.ui.horario1,
            self.ui.horario2,
            self.ui.horario3,
            self.ui.horario4,
            self.ui.horario5,
            self.ui.horario6,
        ]
        #limpiar tablas
        for tabla in tablas:
            tabla.clearContents()
            tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # mostrar respuestas de la api
        for indice, horario in enumerate(horarios_generados):
            if indice >= len(tablas):
                break
            tabla = tablas[indice]
            for materia in horario:
                nrc = str(materia.get("nrc","")).strip()
                nombre = str(materia.get("materia","")).strip()
                hora_dia = str(materia.get("hora_dia","")).strip()
                profesor = str(materia.get("profesor","")).strip()
                texto = (f"{nrc}-{nombre}")

                if not hora_dia:
                    continue
                coincidencia_hora = re.search(r'\d{4}-\d{4}', hora_dia)
                if not coincidencia_hora:
                    continue
                hora = coincidencia_hora.group()
                dias_encontrados = []

                mapa_dias = [
                    "L",
                    "M",
                    "I",
                    "J",
                    "V",
                    "S"
                ]
                # buscar las marcas de dia dentro del registro
                for dia in mapa_dias:
                    if re.search(rf'\b{dia}\b', hora_dia):
                        dias_encontrados.append(dia)
                dias = "".join(dias_encontrados)
                fila = self.obtener_fila_hora(hora,tabla)
                columnas = (self.obtener_columna_dia(dias))
                if fila is None:
                    continue
                for columna in columnas:
                    item = QTableWidgetItem(texto)
                item.setToolTip(
                    f"NRC: {nrc}\n"
                    f"Materia: {nombre}\n"
                    f"Horario: {hora_dia}\n"
                    f"Profesor: {profesor}\n"
                )
                tabla.setItem(
                    fila,
                    columna,
                    item
                )

           

    def descargar_horarios_csv(self):
        if not hasattr(self, "horarios_generados") or len(self.horarios_generados) == 0:
            self.ui.bt_descargar_csv.setText("Aun no generas un horario")
            return
        archivo, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar horarios",
            "Horarios.xlsx",
            "Archivos de excel (*.xlsx)"
        )
        if not archivo:
            return
        if not archivo.endswith(".xlsx"):
            archivo += ".xlsx"
        wb = Workbook()
        wb.remove(wb.active)
        encabezados = [
            "NRC",
            "Clave",
            "Seccion",
            "CR",
            "Cupo",
            "Disponibles",
            "Horario",
            "Profesor"
        ]
        for indice, horario in enumerate(self.horarios_generados, start=1):
            ws = wb.create_sheet(title=f"Horario {indice}")
            ws.append(encabezados)
            for materia in horario:
                ws.append([
                    materia.get("nrc", ""),
                    materia.get("clave", ""),
                    materia.get("sec", ""),
                    materia.get("cr", ""),
                    materia.get("cup", ""),
                    materia.get("dis", ""),
                    materia.get("hora_dia", ""),
                    materia.get("profesor", ""),
                ])
            
            #ajusztar el anchi
            for columna in ws.columns:
                longitud = 0
                letra = columna[0].column_letter
                for celda in columna:
                    try:
                        longitud = max(longitud, len(str(celda.value)))
                    except:
                        pass
                ws.column_dimensions[letra].width = longitud + 3
        wb.save(archivo)
        self.ui.signal_carga_csv.setText("Horarios exportados")
        







