import requests

API_URL = "https://schedulego.onrender.com"

def autenticar(correo: str, password: str, rol: str) -> dict:
    # sirve ára enviar crednciales a la api  y devolver respuesta
    url = f"{API_URL}/login/"

    datos = {
        "correo": correo,
        "password": password,
        "rol": rol
    }

    try:
        respuesta = requests.post(
            url,
            json=datos,
            timeout=10
        )
        respuesta.raise_for_status()
        return respuesta.json()

    except requests.exceptions.ConnectionError:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api",
            "nombre": None,
            "rol": None
        }
    
    except requests.exceptions.Timeout:
        return{
            "success": False,
            "mensaje": "La api tardo demasiado en responder",
            "nombre": None,
            "rol": None
        }
    except requests.exceptions.HTTPError:
        return{
            "success": False,
            "mensaje": "La api devolvio un error",
            "nombre": None,
            "rol": None
        }
    
    except Exception as e:
        return{
            "success": False,
            "mensaje": f"Error inesperado: {e}",
            "nombre": None,
            "rol": None
        }

def registrar_estudiante(nombre_completo: str,codigo_estudiante: str,correo_estudiante: str,password: str) -> dict:
    url = f"{API_URL}/registro/"
    datos= {
        "nombre_completo": nombre_completo,
        "codigo_estudiante": codigo_estudiante,
        "correo_estudiante": correo_estudiante,
        "password": password
    }

    try:
        respuesta = requests.post(
            url,
            json=datos,
            timeout=10
        )
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.ConnectionError:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse a la api"
        }
    except requests.exceptions.timeout:
        return{
            "success": False,
            "mensaje": "La api tardo demasiado en responder"
        }
    except requests.exceptions.HTTPError:
        return{
            "success": False,
            "mensaje": "La api devolvio un error"
        }
    except Exception as e:
        return{
            "success": False,
            "mensaje": f"Error inesperado: {e}"
        }

def obtener_materias():
    try:
        respuesta = requests.get(
            f"{API_URL}/materias/",
            timeout=5
        )
        return respuesta.json()
    except requests.exceptions.RequestException:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api"
        }

def buscar_materia(nrc):
    try:
        respuesta = requests.get(
            f"{API_URL}/materias/{nrc}",
            timeout=5
        )
        return respuesta.json()
    except requests.exception.RequestException:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api"
        }

def actualizar_materia(nrc,clave,materia,sec,cr,cup,dis,hora_dia,profesor):
    try:
        datos = {
            "nrc": nrc,
            "clave": clave,
            "materia": materia,
            "sec": sec,
            "cr": cr,
            "cup": cup,
            "dis": dis,
            "hora_dia": hora_dia,
            "profesor": profesor
        }
        respuesta = requests.put(
            f"{API_URL}/materias/",
            json=datos,
            timeout=5
        )
        return respuesta.json()
        
    except requests.exception.RequestException:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api"
        }

def eliminar_materia(nrc):
    try:
        respuesta = requests.delete(
            f"{API_URL}/materias/{nrc}",
            timeout=5
        )
        return respuesta.json()
    except requests.exceptions.RequestException:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api"
        }

def cargar_csv(ruta_archivo):
    try:
        with open(ruta_archivo,"rb") as archivo:
            archivos = {
                "archivo": (
                    ruta_archivo,
                    archivo,
                    "text/csv"
                )
            }
            respuesta = requests.post(
                f"{API_URL}/materias/cargar-csv",
                files=archivos,
                timeout=30
            )
        return respuesta.json()
    except requests.exceptions.RequestException:
        return{
            "sucess": False,
            "mensaje": "No fue posible conectarse con la api"
        }
    except Exception as e:
        return {
            "sucess": False,
            "mensaje": "Error inesperado: {e}"
        }

def buscar_choques(nrc, ciclo_buscado=""):
    try:
        url = f"{API_URL}/materias/choques/{nrc}"
        params = {}
        if ciclo_buscado:
            params["ciclo_buscada"] = ciclo_buscado
        respuesta = requests.get(
            url,
            params=params,
            timeout=10
        )
        return respuesta.json()
    except requests.RequestException as e:
        return{
            "success": False,
            "mensaje": f"No fue posible consultar los choques: {str(e)}"
        }
    except Exception as e:
        return{
            "success": False,
            "mensaje": f"Error al consultar los choques: {str(e)}"
        }

def crear_horarios(materias, ciclo=""):
    try:
        datos = {
            "materias": materias,
            "ciclo": ciclo
        }
        respuesta = requests.post(
            f"{API_URL}/materias/crear-horario",
            json=datos,
            timeout=60
        )
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.ConnectionError:
        return{
            "success": False,
            "mensaje": "No fue posible conectarse con la api"
        }
    except requests.exceptions.Timeout:
        return{
            "success": False,
            "mensaje": "La api tardo demasiado en generar los horarios"
        }
    except requests.exceptions.HTTPError as e:
        return{
            "success": False,
            "mensaje": f"La api devolvio un error http: {e}"
        }
    except requests.exceptions.RequestException as e:
        return{
            "success": False,
            "mensaje": f"Error de la comunicacion con la api: {e}"
        }
    except Exception as e:
        return{
            "success": False,
            "mensaje": f"Error inesperado: {e}"
        }

