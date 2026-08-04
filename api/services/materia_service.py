import logging
import csv
import re
import sys
import random
from database import get_connection_materias
from cre_horarios import HorarioGenetico

logger = logging.getLogger(__name__)

def obtener_materias():
    conexion = None

    try:
        conexion = get_connection_materias()
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    nrc,
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor
                FROM materia
                ORDER BY materia ASC, sec ASC
            """
            cursor.execute(sql)
            materias = cursor.fetchall()

            
            logger.info("Consulta de materias exitosa (%d registrados)",len(materias))
            return{
                "success": True,
                "materias": materias
            }
    except  Exception:
        logger.exception("Error al consultar materias")
        return{
            "success": False,
            "mensaje": "No fue posible obtener las materias"
        }
    finally:
        if conexion:
            conexion.close()

def buscar_materia(nrc):
    conexion = None

    try:
        conexion = get_connection_materias()
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    nrc,
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor
                FROM materia
                WHERE nrc =%s
            """
            cursor.execute(sql,(nrc,))
            materia = cursor.fetchone()
            if materia:
                logger.info(
                    "Materia encontrada: %s",
                    nrc
                )
                return{
                    "success": True,
                    "materia": materia
                }
            logger.warning(
                "Materia no encontrada: %s",
                nrc
            )
            return{
                "success": False,
                "mensaje": "La materia no existe"
            }
    except Exception:
        logger.exception(
            "Error al buscar materia"
        )
        return{
            "success": False,
            "mensaje": "No fue posible buscar la materia"
        }
    finally:
        if conexion:
            conexion.close()

def actualizar_materia(nrc,clave,materia,sec,cr,cup,dis,hora_dia,profesor):
    conexion = None

    try:
        conexion = get_connection_materias()
        with conexion.cursor() as cursor:
            sql = """
                UPDATE materia
                SET
                    clave=%s,
                    materia=%s,
                    sec=%s,
                    cr=%s,
                    cup=%s,
                    dis=%s,
                    hora_dia=%s,
                    profesor=%s
                WHERE nrc =%s
            """

            cursor.execute(
                sql,
                (
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor,
                    nrc
                )
            )
            conexion.commit()
            if cursor.rowcount > 0:
                logger.info(
                    "Materia actualizada: %s",
                    nrc
                )
                return{
                    "success": True,
                    "mensaje": "Materia actualizada correctamente"
                }
            logger.warning(
                "No se realizaron cambios sobre la materia: %s",
                nrc
            )
            return{
                "success":False,
                "mensaje": "No se realizaron cambios"
            }
    except Exception:
        if conexion:
            conexion.rollback()
        logger.exception(
            "Error al actualizar materia"
        )
        return{
            "success": False,
            "mensaje": "No fue posible actualizar la materia"
        }
    
    finally:
        if conexion:
            conexion.close()

def eliminar_materia(nrc):
    conexion = None

    try:
        conexion = get_connection_materias()
        with conexion.cursor() as cursor:
            sql = """
                DELETE FROM materia
                WHERE nrc =%s
            """
            cursor.execute(sql, (nrc,))
            conexion.commit()
            if cursor.rowcount > 0:
                logger.info(
                    "Materia eliminada: %s",
                    nrc
                )
                return{
                    "success": True,
                    "mensaje": "Materia eliminada correctamente"
                }
        
            logger.warning(
                #
                "No existe la materia: %s",
                nrc
            )
            return{
                "success": False,
                "mensaje": "La materia no existe"
            }

    except Exception:
        if conexion:
            conexion.rollback()
        logger.exception(
            "Error al eliminar materia"
        )
        return{
            "success": False,
            "mensaje": "No fue posible eliminar la materia"
        }

    finally:
        if conexion:
            conexion.close()

def cargar_csv(ruta_archivos):
    conexion = None
    archivo = None
    registro_i = 0

    try:
        conexion = get_connection_materias()
        try:
            archivo = open(
                ruta_archivos,
                mode="r",
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            archivo = open(
                ruta_archivos,
                mode="r",
                encoding="latin-1"
            )
        
        lector = csv.reader(archivo)
        next(lector, None)

        sql = """
            INSERT INTO materia(
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
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        with conexion.cursor() as cursor:
            for fila in lector:
                if len(fila) >= 9:
                    datos_fila = fila[:9]
                    datos_fila = [
                        str(dato).strip() if dato else ""
                        for dato in datos_fila
                    ]
                    cursor.execute(
                        sql,
                        tuple(datos_fila)
                    )
                    registro_i  += 1
            conexion.commit()
        logger.info(
            "Carga csv exitosa: %s registros cargados",
            registro_i
        )

        return{
            "success": True,
            "total": registro_i,
            "mensaje": f"{registro_i} registros cargados"
        }
    
    except Exception:
        if conexion:
            conexion.rollback()
        logger.exception(
            "Error al cargar csv de materias"
        )
        return{
            "success": False,
            "total": registro_i,
            "mensaje": "No fue posible cargar el archivo"
        }
    
    finally:
        if archivo:
            archivo.close()

        if conexion:
            conexion.close()

###############elementos de choque materias

def extraer_ciclo(texto):
    texto = str(texto)
    patron = re.search(r'\d{2}/\d{2}/\d{2}\s*-\s*\d{2}/\d{2}/\d{2}',texto)
    if patron:
        return patron.group().replace(" ","")
    return ""

def limpiar_hora_dia(texto): # este ya estaba asi        
        texto = str(texto).upper()
        ####limpiar hora### 
        hora_match = re.search(r'\d{4}-\d{4}',texto)
        hora = (hora_match.group() if hora_match else "")
        ###limpiar dia###
        dias_match = re.search(r'[A-Z]+(?:-[A-Z]+)?',texto)
        dias = (dias_match.group() if dias_match else "")
        return dias,hora

def mismo_dia(dia1, dia2):
        dia1 = str(dia1)
        dia2 = str(dia2)
        for d in dia1:
            if d in dia2:
                return True
        return False

def hay_traslape(hora1, hora2):
    try:
        inicio1, fin1 = map(int, hora1.split('-'))
        inicio2, fin2 = map(int, hora2.split('-'))
        return inicio1 < fin2 and inicio2 < fin1
    except Exception:
        return False

def buscar_choques(nrc, ciclo_buscado=""):
    conexion = None
    try:
        conexion = get_connection_materias()
        with conexion.cursor() as cursor:
            sql_base = """
                SELECT
                    nrc,
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor
                FROM materia
                WHERE nrc = %s
            """
            cursor.execute(sql_base, (nrc,))
            materia_base = cursor.fetchone()
            if not materia_base:
                logger.warning(
                    "NRc no encontrado para choque: %s",
                    nrc
                )
                return{
                    "success": False,
                    "mensaje": "NRC no encontrado"
                }
            #obtener dias y hora de la materia base
            dias_base, hora_base = limpiar_hora_dia(materia_base["hora_dia"])
            #obtener ciclo de la maeria
            ciclo_base = extraer_ciclo(materia_base["hora_dia"])
            #si el usuario da ciclo - utilizar ciclo
            ciclo_buscado = str(ciclo_buscado).replace(" ", "")

            if ciclo_buscado != "":
                ciclo_base = ciclo_buscado

            #obtencion materia
            sql_todas = """
                SELECT
                    nrc,
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor
                FROM materia
            """
            cursor.execute(sql_todas)
            todas = cursor.fetchall()

            coincidencias = []

            for materia in todas:
                try:
                    #evitar compararse con el mismo
                    if str(materia["nrc"]).upper().strip() == str(nrc).upper().strip():
                        continue
                    # limpiar hora y dia
                    dias_actual, hora_actual = limpiar_hora_dia(materia["hora_dia"])
                    #obtner ciclo de la materia 
                    ciclo_actual = extraer_ciclo(materia["hora_dia"])
                    #validar ciclo
                    if ciclo_base != "":
                        if ciclo_actual != ciclo_base:
                            continue
                    #validar dias
                    if not mismo_dia(dias_base, dias_actual):
                        continue
                    #validar traslape
                    if not hay_traslape(hora_base, hora_actual):
                        continue
                    if not any(str(m["nrc"]).strip() == str(materia["nrc"]).strip()for m in coincidencias):
                        coincidencias.append(materia)
                except Exception:
                    logger.exception("Error al procesar materia durante busqueda de choque")
            logger.info(
                "Consulta de choques existosa nrc para : %s (%d encontrados)",
                nrc,
                len(coincidencias)
            )
            return{
                "success": True,
                "materias": coincidencias,
                "total": len(coincidencias)
            }
    except Exception:
        logger.exception("Error al buscar choques de materia")
        return{
            "success": False,
            "mensaje": "No fue posible buscar los choques de la materia"
        }
    finally:
        if conexion:
            conexion.close()

def obtener_materias_horario(materias_usuario, ciclo_buscado=""):
    conexion = None
    try:
        conexion = get_connection_materias()
        materias_usuario = [
            str(materia).upper().strip()
            for materia in materias_usuario
            if str(materia).strip()
        ]
        ciclo_buscado = str(ciclo_buscado).replace(" ","")
        if not materias_usuario:
            return{
                "success": False,
                "mensaje": "No se proporcionaron materias"
            }
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    nrc,
                    clave,
                    materia,
                    sec,
                    cr,
                    cup,
                    dis,
                    hora_dia,
                    profesor
                FROM materia
                WHERE UPPER(materia) IN ({})
            """.format(
                ",".join(["%s"] * len(materias_usuario))
            )
            cursor.execute(
                sql,
                tuple(materias_usuario)
            )
            materias = cursor.fetchall()
        materias_filtradas = []
        for materia in materias:
            nombre = str(materia["materia"]).upper().strip()
            if nombre not in materias_usuario:
                continue
            if ciclo_buscado:
                ciclo_materia = extraer_ciclo(materia["hora_dia"])
                if ciclo_materia != ciclo_buscado:
                    continue
            materias_filtradas.append(materia)
        logger.info(
            "Consulta de materias para horario exitoso (%d registros)",
            len(materias_filtradas)
        )
        return{
            "success": True,
            "materias": materias_filtradas,
            "total": len(materias_filtradas)
        }
    except Exception:
        logger.exception("Error al obtener materias para crear horario")
        return{
            "success": False,
            "mensaje": "No fue posible obtener las materias para crear el horario"
        }
    finally:
        if conexion:
            conexion.close()

def obtener_inicio(materia):
        try:
            hora = re.search(r'\d{4}-\d{4}', str(materia[7]))
            if hora:
                return int(hora.group().split('-')[0])
        except:
            pass
        return 9999
            
def crear_horarios(materias_usuario, ciclo_usurio=""):
    conexion = None
    try:
        #normalizar materia
        materias_usuario = [
            str(materia).upper().strip()
            for materia in materias_usuario
            if str(materia).strip()
        ]

        if not materias_usuario:
            return {
                "success": False,
                "mensaje": "No se proporcionaron materias"
            }
        ciclo_usurio = str(ciclo_usurio).replace(" ", "")
    
        #conexion de base de datos
        conexion = get_connection_materias()
        cursor = conexion.cursor()

        #buscar materias
        placeholders = ",".join(["%s"] * len(materias_usuario))
        sql =  f"""
            SELECT
                nrc,
                clave,
                materia,
                sec,
                cr,
                cup,
                dis,
                hora_dia,
                profesor
            FROM materia
            WHERE UPPER(materia) IN ({placeholders})
        """
        cursor.execute(sql,tuple(materias_usuario))
        datos = cursor.fetchall()

        # conversion a la estructura 
        datos_normalizados = []
        for d in datos:
            #si el cursor devuelve diccionarios
            if isinstance(d, dict):
                datos_normalizados.append(
                (
                d["nrc"],
                d["clave"],
                d["materia"],
                d["sec"],
                d["cr"],
                d["cup"],
                d["dis"],
                d["hora_dia"],
                d["profesor"]
                )
            )
            else:
                datos_normalizados.append(d)
        
        #filtrar materias y ciclo
        datos_filtrados = []
        for d in datos_normalizados:
            nombre = str(d[2]).upper().strip()
            if nombre not in materias_usuario:
                continue
            if ciclo_usurio:
                ciclo_materia = extraer_ciclo(d[7])
                if ciclo_materia != ciclo_usurio:
                    continue
            datos_filtrados.append(d)
    
        # agrupar por materias
        materias_dict = {}
        for d in datos_filtrados:
            nombre = str(d[2]).upper().strip()
            if nombre not in materias_dict:
                materias_dict[nombre] = []
            materias_dict[nombre].append(d)
        
    
        # buscar materias faltantes 
        faltantes = []
        for materia in materias_usuario:
            if materia not in materias_dict:
                faltantes.append(materia)
        if faltantes:
            logger.warning(
                "Materias faltantes: %s",
                faltantes
            )
            return{
                "success": False,
                "mensaje": (
                    "faltan materias en la bd: "
                    + ", ".join(faltantes)
                ),
                "faltantes": faltantes
            }
        #ordenar materias por cantidad
        materias_ordenadas = sorted(
            materias_dict.keys(),
            key=lambda materia: len(materias_dict[materia])
        )

        #ordenar materias por hora
        for materia in materias_ordenadas:
            materias_dict[materia] = sorted(
                materias_dict[materia],
                key=obtener_inicio
            )
        
        #validar opcion contra el horario
        def es_valido(nueva_materia, horario_actual):
            #obtener dia y hora
            dias_nuevo, hora_nueva = limpiar_hora_dia(nueva_materia[7])
            if not dias_nuevo or not hora_nueva:
                return False

            #validar choque directo dia y hora
            for materia_actual in horario_actual:
                dias_actual, hora_actual = limpiar_hora_dia(materia_actual[7])
                if mismo_dia(dias_nuevo,dias_actual):
                    if hay_traslape(hora_nueva, hora_actual):
                        return False

            #validacion mediante buscar_choque()
            resultado_choques = buscar_choques(nueva_materia[0], ciclo_usurio)
            if not resultado_choques.get("success",False):
                return False
            choques = resultado_choques.get("materias",[])
            nrc_actuales = {
                str(materia[0]).strip()
                for materia in horario_actual
            }
            for choque in choques:
                nrc_choque = str(choque["nrc"]).strip()
                if nrc_choque in nrc_actuales:
                    return False
            return True
        
        #ejcucion del horario genetico
        gen = HorarioGenetico(
            materias_dict,
            ventana=sys.modules[__name__],
            poblacion=200,
            generaciones=200,
            mutacion=0.15
        )
        horarios_generados = gen.ejecutar()

        #validar horarios generados
        horarios_validos = []
        MAX_HORARIOS = 6

        for horario in horarios_generados:
            if len(horarios_validos) >= MAX_HORARIOS:
                break
            horario_valido = True
            horario_actual = []
            for materia in horario:
                if not es_valido(materia, horario_actual):
                    horario_valido = False
                    break
                horario_actual.append(materia)
            if horario_valido:
                horario_final = sorted(
                    horario_actual,
                    key=obtener_inicio
                )
                horarios_validos.append(horario_final)

        #validar si existen horarios
        if not horarios_validos:
            logger.warning(
                "No se encontraron combinaciones "
                "validas de horario"
            )
            return{
                "success": False,
                "mensaje": (
                    "No fue posible generar horarios "
                    "sin choques"
                ),
                "horarios": [],
                "total": 0
            }
        
        #conversion a json
        horarios_respuesta = []
        for horario in horarios_validos:
            materias_horario = []
            for materia in horario:
                materias_horario.append(
                    {
                        "nrc": materia[0],
                        "clave": materia[1],
                        "materia": materia[2],
                        "sec": materia[3],
                        "cr": materia[4],
                        "cup": materia[5],
                        "dis": materia[6],
                        "hora_dia": materia[7],
                        "profesor": materia[8]
                    }
                )
            horarios_respuesta.append(materias_horario)
        logger.info(
            "Generacion de horarios exitosa (%d horarios)",
            len(horarios_respuesta)
        )
        return{
            "success": True,
            "horarios": horarios_respuesta,
            "total": len(horarios_respuesta)
        }
    except Exception:
        logger.exception("Error al crear horarios")
        return{
            "success": False,
            "mensaje": (
                "No fue posible generar"
                "los horarios"
            )
        }
    finally:
        if conexion:
            try:
                conexion.close()
            except Exception:
                pass

        
 

    