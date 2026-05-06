import mariadb
import csv

class Comunicacion():
    def __init__(self):
        self.conexion = mariadb.connect(
            user = "lalo",
            password = "1234",
            host = "localhost",
            port = 3306,
            database = "bd_materias"   
            )
    
    def insertar_materia(self, nrc, clave, materia, sec, cr, cup, dis, hora_dia, profesor):
        cursor = self.conexion.cursor()
        sql = '''
        INSERT INTO materia(nrc,clave,materia,sec,cr,cup,dis,hora_dia,profesor)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        cursor.execute(sql,(nrc, clave, materia, sec, cr, cup, dis, hora_dia, profesor))
        self.conexion.commit()
        cursor.close()


    def mostrar_materias(self):
        cursor = self.conexion.cursor()
        bd_materias = "SELECT * FROM materia"
        cursor.execute(bd_materias)
        registro = cursor.fetchall()
        return registro

    def buscar_materia(self, nrc):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM materia WHERE nrc = %s"#posiblemente modificar materia a nrc viceversa
        cursor.execute(sql,(nrc, ))
        datos = cursor.fetchall()
        cursor.close()
        return datos

    def elimina_materia(self, nrc):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM materia WHERE nrc = %s"
        cursor.execute(sql,(nrc, ))
        self.conexion.commit()
        cursor.close()

        

    def actualiza_materia(self, nrc, clave, materia, sec, cr, cup, dis, hora_dia, profesor):
        cursor = self.conexion.cursor()
        sql = '''
        UPDATE materia
        SET clave=%s,materia=%s, sec=%s, cr=%s, cup=%s, dis=%s, hora_dia=%s, profesor=%s
        WHERE nrc=%s
        '''
        cursor.execute(sql,(clave, materia, sec, cr, cup, dis, hora_dia, profesor,nrc))
        self.conexion.commit()
        filas = cursor.rowcount
        cursor.close()
        return filas

    # cargar csv
    def cargar_csv_bd(self, ruta_archivo):
        cursor = self.conexion.cursor()
        registro_i = 0
        try:
            try:
                archivo = open(ruta_archivo, mode='r', encoding='utf-8')
            except:
                archivo = open(ruta_archivo, mode='r', encoding='latin-1')
                
            lector = csv.reader(archivo)
            next(lector, None)

            sql = '''
                INSERT INTO materia(nrc,clave,materia,sec,cr,cup,dis,hora_dia,profesor)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            for fila in lector:
                    if len(fila) >= 9 :
                        datos_fila = fila[:9]
                        datos_fila = [str(dato).strip() if dato else '' for dato in datos_fila]
                        cursor.execute(sql, tuple(datos_fila))
                        registro_i += 1
                        
            self.conexion.commit()
            archivo.close()
        
        except Exception as e:
            print("Error al cargar csv: ", e)
            import traceback
            traceback.print_exc()

        finally:
            if cursor:
                 cursor.close()
        return registro_i

    def obtener_datos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM materia"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        return datos
