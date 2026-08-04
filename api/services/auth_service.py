# atentificacion de usuarios
from database import get_connection_usuarios
import logging 
logger = logging.getLogger(__name__)

def autenticar_usuario(correo: str, password: str, rol: str) -> dict:
    if rol.lower() == "admin":
        tabla = "tb_admins"
        col_correo = "correo_admin"
        col_nombre = "nombre_admin"
    elif rol.lower() == "estudiante":
        tabla = "tb_estudiantes"
        col_correo = "correo_estudiante"
        col_nombre = "nombre_completo"
    else:
        return{
            "success": False,
            "mensaje": "Rol invalido",
            "nombre": None,
            "rol": None
        }
    conexion = None

    try:
        conexion = get_connection_usuarios()
        with conexion.cursor() as cursor:
            sql = f"""

            SELECT {col_nombre}
            FROM {tabla}
            WHERE {col_correo} = %s
            AND password = %s
            """
            
            
            cursor.execute(sql, (correo, password))
            usuario = cursor.fetchone()
            if usuario:
                logger.info("inicio de sesion exitoso (%s): %s",
                rol,
                correo
                )
                return{
                    "success": True,
                    "mensaje": "inicio de sesion exitoso.",
                    "nombre": usuario[col_nombre],
                    "rol": rol 
                }
            logger.warning("Intento de inicio de sesion fallido (%s): %s", rol, correo)
            return{
                "success": False,
                "mensaje": "correo o contraseña incorrecta",
                "nombre": None,
                "rol": rol
            }
    except Exception as e:
        logger.exception("Error durante la autentificacion del usuario")
        return{
            "success": False,
            "mensaje": "Error interno en el servidor",
            "nombre": None,
            "rol": None
        }
    finally:
        if conexion:
            conexion.close()