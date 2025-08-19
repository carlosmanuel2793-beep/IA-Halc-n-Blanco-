
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "halcon-blanco-backend"}

@app.post("/api/predict")
def predict(data: dict):
    series = data.get("series", [])
    if not series:
        return {"error": "Serie vacía"}
    pred = sum(series)/len(series)
    return {"prediction": pred}

@app.post("/api/biorritmo")
def biorritmo(data: dict):
    nacimiento = data.get("nacimiento")
    if not nacimiento:
        return {"error": "Falta fecha"}
    fecha_nac = datetime.strptime(nacimiento, "%Y-%m-%d")
    dias = (datetime.now() - fecha_nac).days
    ciclos = {
        "fisico": math.sin(2*math.pi*dias/23),
        "emocional": math.sin(2*math.pi*dias/28),
        "intelectual": math.sin(2*math.pi*dias/33)
    }
    return {"dias": dias, "ciclos": ciclos}
