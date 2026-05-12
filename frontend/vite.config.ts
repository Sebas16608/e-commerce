import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// importo tailwindcss
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  
  // Agrego tailwindcss a la config 
  plugins: 
  [
  
    react(), 
    tailwindcss(),
  
  ],

})
