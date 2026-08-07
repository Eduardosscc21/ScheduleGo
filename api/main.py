from fastapi import FastAPI
from routes.login import router as login_router
from routes.registro import router as registro_router
from routes.materias import router as materias_router
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
app = FastAPI(
    title="API",
    version="1.0.0"
)
@app.get("/")
def root():
    return{
        "mensaje de confirmacion": "API GENRADA"
    }
app.include_router(login_router)
app.include_router(registro_router)
app.include_router(materias_router)