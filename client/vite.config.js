import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

const resolveDir = dir => path.resolve(__dirname, dir);

// https://vitejs.dev/config/
export default defineConfig({
    base: '/client/',
    plugins: [vue()],
    build: {
        outDir: 'dist/',
    },
    resolve: {
        alias: {
            '@': resolveDir('./src'),
            'vue': 'vue/dist/vue.esm-bundler.js',
        },
    },
    server: {
        host: '0.0.0.0',
        port: 3000,
        hmr: {
            clientPort: 8443,
        },
    },
})
