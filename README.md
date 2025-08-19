
# Halcón Blanco Platform

Plataforma unificada con:
- **Backend (FastAPI)**: análisis predictivo, biorritmos.
- **Frontend (React + Vite)**: interfaz gráfica.

## Despliegue en Render (Blueprint)
1. Subir este repo a GitHub (archivos sueltos, no zip).
2. En Render → New → Blueprint → conecta tu repo.
3. Render detectará dos servicios:
   - Backend: FastAPI (puerto 10000)
   - Frontend: React (static site)
4. Agregar variable en el frontend:
   - `VITE_API_BASE` = URL pública del backend
5. Redeploy y listo 🚀

## Ejecución local
Backend:
```bash
cd backend
uvicorn main:app --reload --port 8000
```
Frontend:
```bash
cd frontend
npm install
npm run dev
```
