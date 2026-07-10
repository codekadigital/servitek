# SERVITEK — Sitio web

Landing page de una sola sección para **Servitek · Servicio Técnico Eléctrico** (Kemsa Inversiones, Tacna).
HTML, CSS y JavaScript puros. Sin build, sin dependencias, sin backend.

## Ver el sitio

```bash
python3 -m http.server 8080
# abrir http://localhost:8080
```

Para publicarlo basta con subir la carpeta completa a Netlify, Vercel, GitHub Pages
o cualquier hosting compartido (Hostinger, cPanel). No requiere Node ni PHP.

## Estructura

```
index.html              Todo el contenido
css/styles.css          Diseño completo
js/main.js              Scroll reveal, contadores, menú, formulario
assets/*.svg            Ilustraciones vectoriales (generadas, no fotos)
```

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

Las ilustraciones de `assets/` son SVG que dibujé a mano (estátor, electrobomba,
tablero, electrodomésticos, logo). Sirven como referencia y funcionan bien en producción
porque escalan sin pixelarse y pesan poco.

Dicho esto, **para un negocio de servicios técnicos las fotos reales convierten mucho más**.
Recomiendo reemplazar, en este orden de prioridad:

1. `.hero__art` → foto de un estátor rebobinado por ustedes, fondo oscuro.
2. `.card__art` (3) → una foto por servicio: motor en el banco, tablero armado, técnico en domicilio.
3. `.rewind__frame` → un antes/después de un rebobinado.

Al cambiar a `<img>` con fotos, usar `loading="lazy"` y `width`/`height` explícitos, y
quitar la animación `spin` del estátor (se ve rara en una foto).

## Accesibilidad y rendimiento

- Respeta `prefers-reduced-motion`: todas las animaciones se desactivan.
- Navegable por teclado, con `skip-link` y `:focus-visible` visible.
- Marcado `ElectricalContractor` de Schema.org para búsqueda local.
- Único recurso externo: Google Fonts (Anton, Barlow, IBM Plex Mono).
  Para máxima velocidad, descargar los `.woff2` a `assets/fonts/` y auto-alojarlos.
