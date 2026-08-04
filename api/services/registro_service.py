from database import get_connection_usuarios
import logging

logger = logging.getLogger(__name__)

def registrar_estudiante(nombre_completo: str,codigo_estudiante: str,correo_estudiante: str,password: str):
    conexion = None

    try:
        conexion = get_connection_usuarios()
        with conexion.cursor() as cursor:
            sql = """
            INSERT INTO tb_estudiantes
            (
                nombre_completo,
                codigo_estudiante,
                correo_estudiante,
                password            
            )
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(
                sql,
                (
                    nombre_completo,
                    codigo_estudiante,
                    correo_estudiante,
                    password
                )
            )

            conexion.commit()
            logger.info(
                "registro exitoso: %s",
                correo_estudiante
            )
            return{
                "success": True,
                "mensaje": "Registro completado con exito"
            }
    except Exception as e:
        #duplicacio
        if hasattr(e, "args") and len(e.args) > 0:
            if e.args[0] == 1062:
                print("\n========ERROR DUPLICADO =======")
                print(e)
                print("=================================")
                mensaje = str(e)
                if "correo_estudiante" in mensaje:
                    return{
                        "success": False,
                        "mensaje": "Este correo ya esta registrado"
                    }
                if "codigo_estudiante" in mensaje:
                    return{
                        "success": False,
                        "mensaje": "Este codigo ya esta registrado"
                    }
                return{
                    "success": False,
                    "mensaje": "Los datos ya existen"
                }
        logger.error(e)
        return{
            "success": False,
            "mensaje": "Error interno del servidor"
        }
    finally:
        if conexion:
            conexion.close()

 