import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  // Public assets are imported explicitly by the application. Disabling the
  // public directory prevents the local evidence symlink from being copied
  // wholesale into a production build.
  publicDir: false,
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://localhost:8001',
    },
    fs: {
      allow: ['.', '..'],
    },
  },
})
