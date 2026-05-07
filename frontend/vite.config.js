import { defineConfig } from 'vite'
import react, { reactCompilerPreset } from '@vitejs/plugin-react'
import babel from '@rolldown/plugin-babel'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    babel({ presets: [reactCompilerPreset()] })
  ],
  server:{
    proxy:{
      "/api":{
        target:'http://127.0.0.1:8000',
        changeOrigin:true,

      },
      "/ask":{
        target:'http://127.0.0.1:8000',
        changeOrigin:true,
      },
      '/trending': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true,
      },
      '/video': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true,
      },
      '/search': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/generate-script': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/run-workflow': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    }
  },
})
