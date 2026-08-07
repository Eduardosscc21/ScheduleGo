from pydantic import BaseModel

class loginRequest(BaseModel):
    correo: str
    password: str
    rol: str

class loginResponse(BaseModel):
    success: bool
    mensaje: str 
    nombre: str | None = None
    rol: str | None = None