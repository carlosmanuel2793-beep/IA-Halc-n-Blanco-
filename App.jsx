import React, { useEffect, useState } from 'react'

export default function App() {
  const [health, setHealth] = useState(null)
  const [pred, setPred] = useState(null)

  useEffect(() => {
    fetch('/api/health').then(r => r.json()).then(setHealth).catch(console.error)
    fetch('/api/prediccion/demo').then(r => r.json()).then(setPred).catch(console.error)
  }, [])

  return (
    <div style={{fontFamily:'system-ui, sans-serif', padding: 24, maxWidth: 900, margin: '0 auto'}}>
      <h1>🦅 Halcón Blanco AI</h1>
      <p>Fullstack en un solo servicio (Render).</p>

      <section style={{padding:16, border:'1px solid #ddd', borderRadius:8, marginTop:12}}>
        <h2>Estado del backend</h2>
        <pre>{health ? JSON.stringify(health, null, 2) : 'Cargando...'}</pre>
      </section>

      <section style={{padding:16, border:'1px solid #ddd', borderRadius:8, marginTop:12}}>
        <h2>Predicción demo</h2>
        <pre>{pred ? JSON.stringify(pred, null, 2) : 'Cargando...'}</pre>
      </section>

      <footer style={{marginTop:24, opacity:0.7}}>
        <small>Halcón Blanco AI – Plataforma unificada</small>
      </footer>
    </div>
  )
}
