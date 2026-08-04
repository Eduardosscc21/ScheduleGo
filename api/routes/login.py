from fastapi import APIRouter
from models import loginRequest, loginResponse
from services.auth_service import autenticar_usuario

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post(
    "/",
    response_model=loginResponse
)

def login(datos : loginRequest):
    respuesta = autenticar_usuario(
        correo=datos.correo,
        password=datos.password,
        rol=datos.rol
    )
    return loginResponse(**respuesta)
    