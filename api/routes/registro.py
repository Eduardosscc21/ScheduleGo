from fastapi import APIRouter
from pydantic import BaseModel

from services.registro_service import registrar_estudiante

router = APIRouter(
    prefix="/registro",
    tags=["Registro"]
)

class registroRequest(BaseModel):
    nombre_completo: str
    codigo_estudiante: str
    correo_estudiante: str
    password: str

@router.post("/")
def registrar(datos: registroRequest):
    return registrar_estudiante(
        nombre_completo=datos.nombre_completo,
        codigo_estudiante=datos.codigo_estudiante,
        correo_estudiante=datos.correo_estudiante,
        password=datos.password
    )
    