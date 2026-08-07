import pymysql
from config import USUARIOS_DB,MATERIAS_DB
#crea y devuelve las conexiones
#

def get_connection_usuarios():
    try:
        conexion = pymysql.connect(
            host=USUARIOS_DB["host"],
            port=USUARIOS_DB["port"],
            user=USUARIOS_DB["user"],
            password=USUARIOS_DB["password"],
            database=USUARIOS_DB["database"],
           cursorclass=pymysql.cursors.DictCursor,
           autocommit=False   
        )
        return conexion
    except Exception as e:
        print(f"[ERRO] no fue posible conectar a la bd de usuarios: {e}")

def get_connection_materias():
    try:
        conexion = pymysql.connect(
            host=MATERIAS_DB["host"],
            port=MATERIAS_DB["port"],
            user=MATERIAS_DB["user"],
            password=MATERIAS_DB["password"],
            database=MATERIAS_DB["database"],
           cursorclass=pymysql.cursors.DictCursor,
           autocommit=False   
        )
        return conexion
    except Exception as e:
        print(f"[ERRO] no fue posible conectar a la bd de materias: {e}") 
