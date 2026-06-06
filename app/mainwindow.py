from PySide6.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QSizeGrip, QFileDialog
from PySide6.QtCore import Slot, QPropertyAnimation,QEasingCurve,Qt
from PySide6 import QtCore, QtWidgets
from mainwindow_ui import Ui_MainWindow
from conexionsql_ventanacargar import Comunicacion
#from PySide6.QtUiTools import QUiLoader
import sys
import re 
from datetime import datetime
import random
from itertools import product


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
        self.base_datos = Comunicacion()
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
            self.pushButton_ampliar.show()
    
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
        datos = self.base_datos.mostrar_materias()
        self.ui.Tabla_materias.setRowCount(len(datos))

        for fila, row in enumerate(datos):
            for columna in range(len(row)):
                self.ui.Tabla_materias.setItem(
                    fila,
                    columna,
                    QtWidgets.QTableWidgetItem(str(row[columna]))
                )
        
    
    # registrar materias
    @Slot()  # cambio de nrc = self.reg_nrc.text().upper() a nrc = self.ui.reg_nrc.text().upper()
    def registrar_materias(self):
        nrc = self.ui.reg_nrc.text().upper()
        clave = self.ui.reg_clave.text().upper()
        materia = self.ui.reg_materia.text().upper()
        sec = self.ui.reg_sec.text().upper()
        cr = self.ui.reg_cr.text().upper()
        cup = self.ui.reg_cup.text().upper()
        dis = self.ui.reg_dis.text().upper()
        hora_dia = self.ui.reg_ses.text().upper()
        profesor = self.ui.reg_profesor.text().upper()

        if nrc != '' and clave !='' and materia !='' and sec !='' and cr !='' and cup !='' and dis !='' and hora_dia !='' and profesor !='':       
            self.base_datos.insertar_materia(nrc, clave, materia, sec, cr, cup, dis, hora_dia, profesor)
            self.ui.signal_registrar.setText('Materias registradas')
            self.ui.reg_nrc.clear()
            self.ui.reg_clave.clear()
            self.ui.reg_materia.clear()
            self.ui.reg_sec.clear()
            self.ui.reg_cr.clear()
            self.ui.reg_cup.clear()
            self.ui.reg_dis.clear()
            self.ui.reg_ses.clear()
            self.ui.reg_profesor.clear()
        else:
            self.ui.signal_registrar.setText("Llenar todos los campos")
   
    @Slot()
    def buscar_actualiza(self):
        nrc = self.ui.act_buscar.text().upper()
        datos = self.base_datos.buscar_materia(nrc)
        if len(datos) != 0:
            self.nrc_actual = nrc

            self.ui.act_nrc_2.setText(str(datos[0][0]))
            self.ui.act_clave_2.setText(str(datos[0][1]))
            self.ui.act_materia_2.setText(str(datos[0][2]))
            self.ui.act_sec_2.setText(str(datos[0][3]))
            self.ui.act_cr_2.setText(str(datos[0][4]))
            self.ui.act_cup_2.setText(str(datos[0][5]))
            self.ui.act_dis_2.setText(str(datos[0][6]))
            self.ui.act_hora.setText(str(datos[0][7]))
            self.ui.act_profesor_2.setText(str(datos[0][8]))

            self.ui.signal_actualizar.setText("Encontrado")
        else:
            self.ui.signal_actualizar.setText("No existe")

            
    @Slot()
    def modificar_materias(self):
        if hasattr(self, "nrc_actual"):
            nrc = self.ui.act_nrc_2.text().upper()
            clave = self.ui.act_clave_2.text().upper()
            materia = self.ui.act_materia_2.text().upper()
            sec = self.ui.act_sec_2.text().upper()
            cr = self.ui.act_cr_2.text().upper()
            cup = self.ui.act_cup_2.text().upper()
            dis = self.ui.act_dis_2.text().upper()
            hora_dia = self.ui.act_hora.text().upper()
            profesor = self.ui.act_profesor_2.text().upper()

            act = self.base_datos.actualiza_materia(nrc, clave, materia, sec, cr, cup, dis, hora_dia, profesor)
            if  act == 0:
                self.ui.signal_actualizar.setText("ACTUALIZADO")
            else:
                self.ui.signal_actualizar.setText("INCORRECTO")
    @Slot()
    def buscar_eliminar(self):
        nrc = self.ui.materia_eliminar.text().upper()
        datos = self.base_datos.buscar_materia(nrc)
        self.ui.tabla_borrar.setRowCount(len(datos))

        if len(datos) == 0:
            self.ui.signal_eliminar.setText('No existe')

        self.ui.signal_eliminar.setText('Materia seleccionada')

        for fila, row in enumerate(datos):
            for col in range(len(row)):
                self.ui.tabla_borrar.setItem(
                    fila, col, QtWidgets.QTableWidgetItem(str(row[col]))
                )
    @Slot()
    def eliminar_materias(self):
        fila = self.ui.tabla_borrar.currentRow()
        if fila >= 0:
            nrc = self.ui.tabla_borrar.item(fila,0).text()
            eliminado = self.base_datos.elimina_materia(nrc)

            if eliminado == 1:
                self.ui.tabla_borrar.removeRow(fila)
                self.ui.signal_eliminar.setText("Materia eliminada")
            else:
                self.ui.signal_eliminar.setText("Selecciona una fila")

    @Slot()
    def cargar_csv(self):
        #self.cargar_csv()
        archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo CSV",
            "Archivo csv (*.csv)"
        )
        if archivo:
            try:

                 total = self.base_datos.cargar_csv_bd(archivo)
                 if total > 0:
                      self.ui.signal_carga_csv.setText(f"{total} registros cargados")
                      self.mostrar_materias()
                 else:
                    self.ui.signal_carga_csv.setText("Error al cargar")
            except Exception as e:
                self.ui.signal_carga_csv.setText(f"Error: {str(e) [:50]}")

  # #################### elementos de choque de materias  
    def limpiar_hora_dia(self, texto): # este ya estaba asi
        texto = str(texto).upper()
        ####limpiar hora###
        hora_match = re.search(r'\d{4}-\d{4}',texto)
        hora = hora_match.group() if hora_match else ""
        ###limpiar dia###
        dias_match = re.search(r'[A-Z]+(?:-[A-Z]+)?',texto)
        dias = dias_match.group() if dias_match else ""
        return dias,hora

        '''texto = str(texto).upper()
        patron_hora = re.search(r'\d{4}-\d{4}', texto)
        patron_dias = re.search(r'[LMIWJVSD\.\-]+', texto)
        hora = patron_hora.group() if patron_hora else ""
        dias = patron_dias.group() if patron_dias else ""
        return dias, hora'''

    def mismo_dia(self, dia1, dia2):
        dia1 = str(dia1)
        dia2 = str(dia2)
        for d in dia1:
            if d in dia2:
                return True
        return False
        '''longitud = min(len(dia1), len(dia2)) desactivado 
        for i in range(longitud):
            if dia1[i] != ',' and dia2[i] != ',':
                return True
        return False'''

    def hay_traslape(self, hora1, hora2):
        try:
            inicio1, fin1 = map(int, hora1.split('-'))
            inicio2, fin2 = map(int, hora2.split('-'))
            return inicio1 < fin2 and inicio2 < fin1
        except:
            return False


    @Slot()
    def choque_materias(self):
        nrc = self.ui.materia_choque.text().upper().strip()
        ciclo_buscado = self.ui.materia_choque_2.text().replace(" ", "")
        materia_base = self.base_datos.buscar_materia(nrc)
        if len(materia_base) == 0:
            self.ui.signal_choque_materias-setText("NRC no encontrado")
            return
        
        materia_base = materia_base[0]
        dias_base, hora_base = self.limpiar_hora_dia(materia_base[7])
        #obtner ciclo base
        ciclo_base = self.extraer_ciclo(materia_base[7])
        # si el usuario lo hixo manual
        if ciclo_buscado != "":
            ciclo_base = ciclo_buscado
        
        # obtner materias
        todas = self.base_datos.obtener_datos()
        coincidencias = []

        for materia in todas:
            try:
                #evitar compararse consigo mismo
                if str(materia[0]).upper().strip() == nrc:
                    continue
                # limpiar hora actual
                dias_actual, hora_actual = self.limpiar_hora_dia(materia[7])
                #obtner ciclo actual
                ciclo_actual = self.extraer_ciclo(materia[7])
                # validar ciclo
                if ciclo_base != "":
                    if ciclo_actual != ciclo_base:
                        continue
                #validar dias
                if not self.mismo_dia(dias_base, dias_actual):
                    continue
                #validar traslape
                if not self.hay_traslape(hora_base, hora_actual):
                    continue
                coincidencias.append(materia)
            except Exception as e:
                print("Error en materia:", e)
        # resultados
        self.ui.tabla_materias_chocando.clearContents()
        self.ui.tabla_materias_chocando.setRowCount(len(coincidencias))
        for fila, row in enumerate(coincidencias):
            for columna, valor in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.ui.tabla_materias_chocando.setItem(
                    fila,
                    columna,
                    item
                )
        self.ui.signal_choque_materias.setText(
            f"{len(coincidencias)} choque encontrados"
        )

        





            
        
############### elementos crear horarios 
    def extraer_ciclo(self, texto):
        texto = str(texto)
        patron = re.search(r'\d{2}/\d{2}/\d{2}\s*-\s*\d{2}/\d{2}/\d{2}',texto)
        if patron:
            return patron.group().replace(" ","")
        return ""

    def parsear_ciclo(self,ciclo):
        try:
            inicio, fin = ciclo.split('-')
            inicio = datetime.strptime(inicio, "%d/%m/%y")
            fin = datetime.strptime(fin, "%d/%m/%y")
            return inicio, fin
        except:
            return None, None

    def obtener_inicio(self, materia):
        try:
            hora = re.search(r'\d{4}-\d{4}', str(materia[7]))
            if hora:
                return int(hora.group().split('-')[0])
        except:
            pass
        return 9999

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
        for fila in range(tabla.rowCount()):
            item = tabla.verticalHeaderItem(fila)
            if item and hora in item.text():
                return fila
        return None
    # intento de correccion del congelamient que se da al ingresar mas e 4
    def es_valido(self, nuevo, actual):
        dias1, hora1 = self.limpiar_hora_dia(nuevo[7])
        for m in actual:
            dias2, hora2 = self.limpiar_hora_dia(m[7])
            if self.mismo_dia(dias1, dias2) and self.hay_traslape(hora1, hora2):
                return False
        return True

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


    @Slot()
    def crear_horario(self):
        datos = self.base_datos.obtener_datos()
        ###input de mayerias
        materias_usuario = [
            self.ui.materia1.text().upper(),
            self.ui.materia2.text().upper(),
            self.ui.materia3.text().upper(),
            self.ui.materia4.text().upper(),
            self.ui.materia5.text().upper(),
            self.ui.materia6.text().upper(),
            self.ui.materia7.text().upper()
        ]

        materias_usuario = [m for m in materias_usuario if m]
        if len(materias_usuario) < 2:
            self.ui.signal_crear_horario.setText("ingresa materias")
            return
        ciclo_usurio = self.ui.linea_ciclo.text().replace(" ","")
        #### filtrar datos
        datos_filtrados = []

        for d in datos:
            nombre = str(d[2]).upper()
            if nombre in materias_usuario:
                if ciclo_usurio:
                    ciclo_materia = self.extraer_ciclo(d[7])
                    if ciclo_materia == ciclo_usurio:
                        datos_filtrados.append(d)
                else:
                    datos_filtrados.append(d)
        #agrupar materia
        materias_dict = {}

        for d in datos_filtrados:
            nombre = str(d[2]).upper()
            if nombre not in materias_dict:
                materias_dict[nombre] = []
            materias_dict[nombre].append(d)
                
        #elimina vacios
        materias_dict = {k: v for k,v in materias_dict.items() if v}

        if len(materias_dict) < 2:
            self.ui.signal_crear_horario.setText("faltan materias en bd")
            return

        #genrar combinaciones
        MAX_HORARIOS = 6
        materias_ordenadas = sorted(
            materias_dict.keys(),
            key=lambda k: len(materias_dict[k])
        )
        for k in materias_ordenadas:
            materias_dict[k] = sorted(
                materias_dict[k],
                key=self.obtener_inicio
            )[:5]
        
        horarios_validos = self.generar_horarios(
            materias_dict,
            materias_ordenadas,
            MAX_HORARIOS        
            )
        
        #mostrar tablas
        tablas = [
            self.ui.horario1,
            self.ui.horario2,
            self.ui.horario3,
            self.ui.horario4,
            self.ui.horario5,
            self.ui.horario6
        ]
        for i, tabla in enumerate(tablas):
            tabla.clearContents()
            # ajuste automatico
            tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            if i >= len(horarios_validos):
                continue
            horario = horarios_validos[i]
            for materia in horario:
                nrc = str(materia[0]).strip()
                nombre = str(materia[2]).strip()

                texto = f"{nrc}-{nombre}"
                dias, hora = self.limpiar_hora_dia(materia[7])

                fila = self.obtener_fila_hora(hora, tabla)
                columnas = self.obtener_columna_dia(dias)

                if fila is not None:
                    for col in columnas:
                        item = QTableWidgetItem(texto)
                        # para ver comple
                        item.setToolTip(texto)
                        tabla.setItem(fila,col,item)
                        









