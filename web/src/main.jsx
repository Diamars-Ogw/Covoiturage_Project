import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Messag from './messag.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Messag />
  </StrictMode>,
)
