from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from services.materia_service import obtener_materias, buscar_materia, actualizar_materia, eliminar_materia, cargar_csv as cargar_csv_service, buscar_choques, crear_horarios, obtener_materias_horario
import os
import tempfile

class MateriaUpdate(BaseModel):
    nrc: int
    clave: str
    materia: str
    sec: str
    cr: int
    cup: int
    dis: int
    hora_dia: str
    profesor: str

class MateriaHorario(BaseModel):
    materias: list[str]
    ciclo: str=""

class CrearHorarioRequest(BaseModel):
    materias: list[str]
    ciclo: str=""

router = APIRouter(
    prefix="/materias",
    tags=["Materias"]
)
# mostrar materias
@router.get("/")
def mostrar_materias():
    return obtener_materias()

# metodos actualizar materia
@router.get("/{nrc}")
def buscar_materia_router(nrc: str):
    return buscar_materia(nrc)

@router.get("/choques/{nrc}")
def buscar_choques_route(nrc:int, ciclo: str = ""):
    return buscar_choques(nrc, ciclo)


@router.put("/")
def actualizar_materia_route(datos: MateriaUpdate):
    return actualizar_materia(
        datos.nrc,
        datos.clave,
        datos.materia,
        datos.sec,
        datos.cr,
        datos.cup,
        datos.dis,
        datos.hora_dia,
        datos.profesor
    )

@router.delete("/{nrc}")
def eliminar_materia_route(nrc: int):
    return eliminar_materia(nrc)

@router.post("/crear-horario/datos")
def obtener_datos_horario(datos: MateriaHorario):
    return obtener_materias_horario(
        datos.materias,
        datos.ciclo
    )

@router.post("/cargar-csv")
async def cargar_csv(archivo: UploadFile = File(...)):
    archivo_temporal = None
    try:
        with tempfile.NamedTemporaryFile(delete=False,suffix=".csv") as temporal:
            archivo_temporal = temporal.name
            contenido = await archivo.read()
            temporal.write(contenido)
        respuesta = cargar_csv_service(
            archivo_temporal
        )
        return respuesta
    finally:
        if archivo_temporal and os.path.exists(archivo_temporal):
            os.remove(archivo_temporal)

@router.post("/crear-horario")
def crear_horario_route(datos: CrearHorarioRequest):
    return crear_horarios(
        datos.materias,
        datos.ciclo
    )




