# SERVITEK — Sitio web

Landing page de una sola sección para **Servitek · Servicio Técnico Eléctrico** (Kemsa Inversiones, Tacna).
HTML, CSS y JavaScript puros. Sin build, sin dependencias, sin backend.

## Ver el sitio

```bash
python3 -m http.server 8080
# abrir http://localhost:8080
```

## Publicar

El sitio ya está en vivo en **GitHub Pages**: https://codekadigital.github.io/servitek/
Cada `git push` a `main` lo actualiza solo en 1-2 minutos.

Para verlo con dominio propio (ej. `servitek.pe`):

1. Compra el dominio (Punto.pe para `.pe`, o Namecheap/GoDaddy para `.com`).
2. Crea un archivo `CNAME` en la raíz del repo con el dominio (ej. `servitek.pe`).
3. En el panel de tu proveedor de dominio, apunta los DNS a GitHub Pages
   (4 registros `A` a las IP de GitHub, o un `CNAME` a `codekadigital.github.io`).
4. En GitHub → Settings → Pages, escribe el dominio y activa "Enforce HTTPS".

GitHub emite el certificado HTTPS gratis. Alternativa sin tocar DNS a mano:
subir la carpeta a **Netlify** (arrastrar y soltar) y conectar el dominio ahí.

## Estructura

```
index.html              Página principal
blog.html               Listado del blog
blog/*.html             Artículos individuales
css/styles.css          Diseño completo
js/main.js              Scroll reveal, contadores, menú, formulario
assets/                 Logo, fotos (WebP) e imagen de compartir
tools/gen_blog.py       Generador del blog (fuente de las páginas del blog)
sitemap.xml, robots.txt Para indexación en Google
```

## Blog: cómo agregar un artículo

Las páginas del blog se generan desde un solo archivo para que el encabezado,
el pie y el estilo sean idénticos en todas. Para publicar un artículo nuevo:

1. Abre `tools/gen_blog.py` y copia uno de los bloques de la lista `POSTS`.
2. Cambia `slug` (nombre del archivo, sin espacios ni tildes), `title`,
   `cat`, `date`, `read`, `cover` (una foto de `assets/`), `excerpt` y `body`
   (el texto en HTML: `<p>`, `<h2>`, `<ul>`, etc.).
3. Ejecuta `python3 tools/gen_blog.py`. Regenera `blog.html` y los artículos.
4. Agrega la URL nueva a `sitemap.xml` y sube los cambios.

Si prefieres no tocar Python, también puedes **duplicar un archivo de `blog/`**,
renombrarlo y editar el texto a mano. Recuerda actualizar también la tarjeta
correspondiente en `blog.html` y en la sección Blog de `index.html`.

## Cómo funciona el formulario

No hay servidor. Al enviarlo, `js/main.js` valida los campos y abre WhatsApp
con el mensaje ya redactado hacia el número definido en la constante `WHATSAPP`
(línea 4 de `js/main.js`). Los datos nunca se almacenan.

Si más adelante quieren recibir los mensajes por correo, se puede conectar a
Formspree o Web3Forms cambiando solo el `submit` handler.

## Qué falta reemplazar antes de publicar

Estos valores son **estimaciones de relleno**, no datos reales. Confírmalos con el
cliente antes de que el sitio salga a producción:

| Dónde | Qué revisar |
|---|---|
| `index.html` → sección `.stats` | 12 años, 1500 motores, 24 h, 6 meses de garantía |
| `index.html` → sección `.quotes` | Los 3 testimonios son inventados. Usar reseñas reales de Facebook |
| `index.html` → `.faq` | Plazos y política de garantía |
| `index.html` → `<link rel="canonical">` y `og:image` | Apuntan a `servitek.pe`, cambiar al dominio real |

Los dos afiches muestran páginas de Facebook distintas (`serelectacna` y
`servitek.reparaciones`). El sitio usa `servitek.reparaciones`; confirmar cuál es la vigente.

## Imágenes

El sitio usa fotos reales del cliente, optimizadas a WebP:

| Archivo | Dónde aparece |
|---|---|
| `logo-servitek.png` | Logo real, recortado en círculo con fondo transparente (header y footer) |
| `foto-diagnostico.webp` | Hero — técnico midiendo un tablero |
| `foto-motores.webp` | Tarjeta "Motores y bombas" y marco de Rebobinado |
| `foto-tableros.webp` | Tarjeta "Instalaciones y tableros" |
| `foto-electrodomesticos.webp` | Tarjeta "Electrodomésticos" |
| `og-servitek.png` | Vista previa al compartir (1200×630) |

Para reemplazar cualquiera: sustituye el `.webp` por otro con el mismo nombre (o cambia
el `src` en `index.html`) y actualiza los atributos `width`/`height` a las dimensiones
reales de la nueva foto. Las fotos se optimizaron con `sharp` (WebP calidad 80).

## Accesibilidad y rendimiento

- Respeta `prefers-reduced-motion`: todas las animaciones se desactivan.
- Navegable por teclado, con `skip-link` y `:focus-visible` visible.
- Marcado `ElectricalContractor` de Schema.org para búsqueda local.
- Único recurso externo: Google Fonts (Anton, Barlow, IBM Plex Mono).
  Para máxima velocidad, descargar los `.woff2` a `assets/fonts/` y auto-alojarlos.
