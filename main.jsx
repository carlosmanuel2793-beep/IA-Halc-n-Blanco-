
import React from 'react'
import ReactDOM from 'react-dom/client'

function App() {
  const [status, setStatus] = React.useState(null)

  React.useEffect(() => {
    fetch(import.meta.env.VITE_API_BASE + "/api/health")
      .then(r => r.json())
      .then(setStatus)
  }, [])

  return (
    <div>
      <h1>Halcon Blanco Platform</h1>
      <pre>{JSON.stringify(status, null, 2)}</pre>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
