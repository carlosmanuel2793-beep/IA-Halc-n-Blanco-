import os
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Halcón Blanco AI – Fullstack")

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend", "dist")
INDEX_FILE = os.path.join(FRONTEND_DIR, "index.html")

# Servir archivos estáticos del build de React (Vite)
if os.path.isdir(FRONTEND_DIR):
    app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIR, "assets")), name="assets")

# ----------- Endpoints API -----------
@app.get("/api/health")
def health():
    return {"status": "ok", "app": "Halcón Blanco AI Fullstack"}

@app.get("/api/version")
def version():
    return {"version": "1.0.0", "mode": "fullstack"}

@app.get("/api/prediccion/demo")
def prediccion_demo():
    # Aquí integrarías tus modelos reales (mercado, lotería, arbitraje, etc.)
    return {"symbol": "AAPL", "prediction": 0.73, "signal": "buy"}

# ----------- Rutas del frontend (SPA) -----------
@app.get("/{full_path:path}")
async def serve_spa(full_path: str, request: Request):
    # Enrutado tipo SPA: cualquier ruta no-API devuelve index.html
    if request.url.path.startswith("/api"):
        return JSONResponse({"detail": "Not Found"}, status_code=404)

    if os.path.exists(INDEX_FILE):
        return FileResponse(INDEX_FILE, media_type="text/html")
    return JSONResponse({"detail": "Frontend build no encontrado. Despliega con npm run build en /frontend."}, status_code=500)