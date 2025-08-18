# 🦅 Halcón Blanco AI – Fullstack (Render listo)

Plataforma unificada **backend + frontend** en un único servicio para Render.

## 🚀 ¿Qué incluye?
- **Backend**: FastAPI con endpoints de ejemplo (`/api/*`).
- **Frontend**: React + Vite, compilado y servido por FastAPI desde `/frontend/dist`.
- **Blueprint (render.yaml)** para despliegue automático en Render como **un solo servicio**.
- **Procfile** por si quisieras desplegar en Heroku/Railway.

---

## 🔧 Despliegue 1‑click en Render (recomendado)
1. Sube este repo a GitHub.
2. En Render: **New + → Blueprint → selecciona el repo**.
3. Acepta el plano: creará **un Web Service**.
4. Render ejecutará automáticamente:
   ```
   pip install -r requirements.txt
   cd frontend && npm ci || npm install
   npm run build
   uvicorn app:app --host 0.0.0.0 --port 10000
   ```
5. Abre la **URL pública**. El frontend y la API estarán en la misma dirección.

> Si prefieres hacerlo manual: New + → Web Service → Python → usa el `buildCommand` y `startCommand` mostrados arriba.

---

## 🖥️ Ejecución local
```bash
# 1) Backend
pip install -r requirements.txt
# 2) Frontend
cd frontend && npm install && npm run build && cd ..
# 3) Ejecutar
uvicorn app:app --reload
# Visita: http://localhost:8000
```

> Desarrollo de frontend en caliente:
```bash
cd frontend
npm install
npm run dev
# Vite en http://localhost:5173
```
En ese modo, el backend sigue en `http://localhost:8000` y el frontend consume `/api/*` con fetch relativo.

---

## 🗂️ Estructura
```
/
├─ app.py                 # FastAPI que sirve API + build del frontend
├─ requirements.txt
├─ render.yaml            # Plano de despliegue (Blueprint) para Render
├─ Procfile               # Arranque alternativo
└─ frontend/              # React + Vite
   ├─ index.html
   ├─ package.json
   └─ src/
      ├─ main.jsx
      └─ App.jsx
```

---

## 🔗 Endpoints de ejemplo
- `GET /api/health` → estado
- `GET /api/version` → versión
- `GET /api/prediccion/demo` → demo de predicción

---

## 📝 Notas
- Puedes reemplazar el contenido de `App.jsx` y añadir llamadas reales a tus módulos de IA.
- Si Render no detecta `npm ci`, usará `npm install`.
- El build del frontend queda en `frontend/dist` y lo sirve FastAPI.

¡Listo para producción ligera en Render Free! ✨
