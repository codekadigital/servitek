# -*- coding: utf-8 -*-
import os

ROOT = "/home/codeka/proyectos-codekadigital/servitek"
BASE = "https://codekadigital.github.io/servitek"
WA = "https://wa.me/51977220049?text=Hola%20SERVITEK%2C%20le%C3%AD%20su%20blog%20y%20necesito%20ayuda"

WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 0 0 4.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96S17.54 2 12.04 2Zm5.83 14.06c-.24.68-1.42 1.31-1.96 1.36-.5.05-.96.24-3.24-.68-2.73-1.1-4.46-3.9-4.6-4.09-.13-.19-1.1-1.46-1.1-2.78 0-1.32.7-1.97.94-2.24.25-.27.54-.34.72-.34.18 0 .36 0 .52.01.17.01.39-.06.61.47.24.55.8 1.9.87 2.04.07.14.12.3.02.49-.1.19-.15.3-.29.46-.15.17-.31.37-.44.5-.15.14-.3.3-.13.59.17.29.75 1.24 1.61 2.01 1.11.99 2.04 1.3 2.33 1.44.29.15.46.12.63-.07.17-.19.73-.85.93-1.14.19-.29.39-.24.65-.15.26.1 1.61.76 1.89.9.27.14.46.22.53.34.06.12.06.7-.18 1.38Z"/></svg>')


def head(title, desc, canonical, p, og_img):
    return f'''<!doctype html>
<html lang="es-PE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0C">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="es_PE">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Poppins:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/styles.css">'''


def header(p, home):
    return f'''<a class="skip-link" href="#main">Saltar al contenido</a>
<div class="grain" aria-hidden="true"></div>
<div class="spotlight" aria-hidden="true"></div>

<header class="hdr hdr--stuck" id="hdr">
  <div class="hdr__inner">
    <a class="brand" href="{home}" aria-label="Servitek, inicio">
      <img src="{p}assets/logo-servitek.png" alt="" width="48" height="48" class="brand__mark">
      <span class="brand__text"><strong>SERVITEK</strong><em>Kemsa Inversiones</em></span>
    </a>
    <nav class="nav" id="nav" aria-label="Principal">
      <a href="{home}#servicios">Servicios</a>
      <a href="{home}#rebobinado">Rebobinado</a>
      <a href="{home}#proceso">Proceso</a>
      <a href="{p}blog.html">Blog</a>
      <a href="{home}#faq">Preguntas</a>
      <a href="{home}#contacto" class="nav__cta">Cotizar ahora</a>
    </nav>
    <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
  </div>
  <div class="hdr__hazard" aria-hidden="true"></div>
  <div class="hdr__progress" id="progress" aria-hidden="true"></div>
</header>'''


def footer(p, home):
    return f'''<footer class="ftr">
  <div class="ftr__hazard" aria-hidden="true"></div>
  <div class="wrap ftr__grid">
    <div class="ftr__brand">
      <img src="{p}assets/logo-servitek.png" alt="Servitek" width="72" height="72">
      <p><strong>SERVITEK</strong> — Servicio Técnico Eléctrico<br>
      <span>Kemsa Inversiones · Tacna, Perú</span></p>
    </div>
    <nav class="ftr__nav" aria-label="Pie de página">
      <a href="{home}#servicios">Servicios</a>
      <a href="{home}#rebobinado">Rebobinado</a>
      <a href="{home}#proceso">Proceso</a>
      <a href="{p}blog.html">Blog</a>
      <a href="{home}#contacto">Contacto</a>
    </nav>
    <div class="ftr__contact">
      <a href="tel:+51977220049">977 220 049</a>
      <a href="tel:+51975321706">975 321 706</a>
      <div class="ftr__social">
        <a href="https://www.facebook.com/servitek.reparaciones" target="_blank" rel="noopener" aria-label="Facebook">FB</a>
        <a href="https://www.tiktok.com/@servitek.pe" target="_blank" rel="noopener" aria-label="TikTok">TT</a>
      </div>
    </div>
  </div>
  <div class="wrap ftr__bottom">
    <p>© <span id="year">2026</span> Servitek · Kemsa Inversiones. Todos los derechos reservados.</p>
    <p class="ftr__made">Solución al instante ⚡</p>
  </div>
</footer>

<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
  {WA_SVG}<span class="wa__ping" aria-hidden="true"></span>
</a>
<button class="totop" id="totop" aria-label="Volver arriba">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5m0 0-6 6m6-6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
</button>
<script src="{p}js/main.js" defer></script>
</body>
</html>'''


# ─────────────────────────────────────────── ARTÍCULOS
POSTS = [
    {
        "slug": "senales-motor-necesita-rebobinado",
        "title": "5 señales de que tu motor necesita rebobinado",
        "cat": "Motores",
        "date": "2026-07-01", "date_h": "1 de julio, 2026", "read": "5 min",
        "cover": "foto-motores.webp",
        "excerpt": "Ruidos, olor a quemado o disparos del térmico. Aprende a detectar a tiempo una falla antes de que el motor muera por completo.",
        "body": """
<p>Un motor eléctrico rara vez se quema de un momento a otro: casi siempre avisa. Reconocer esas señales a tiempo puede ser la diferencia entre un rebobinado económico y comprar un motor nuevo. Estas son las cinco alertas que vemos todos los días en el taller.</p>

<h2>1. Huele a quemado o a barniz</h2>
<p>Es la señal más clara. Ese olor característico proviene del <strong>esmalte del alambre de cobre</strong> sobrecalentándose. Cuando el aislamiento se degrada, las espiras empiezan a hacer cortocircuito entre sí. Si lo hueles, apaga el equipo de inmediato: seguir usándolo solo agrava el daño.</p>

<h2>2. El térmico o la llave se dispara al arrancar</h2>
<p>Si cada vez que enciendes el motor salta la protección, no es capricho de la llave: está haciendo su trabajo. Un bobinado con fuga a tierra o en corto consume más corriente de la normal, y la protección corta para evitar un incendio.</p>

<h2>3. Cuesta arrancar o pierde fuerza</h2>
<p>Un motor que antes arrancaba al instante y ahora "le cuesta", zumba sin girar o mueve menos carga, probablemente tiene espiras dañadas. En motores monofásicos, muchas veces el problema empieza en el capacitor, pero si ya lo cambiaste y sigue igual, el bobinado es el sospechoso.</p>

<blockquote>Un motor que zumba pero no arranca está consumiendo corriente sin hacer trabajo. Cada segundo así lo acerca a la falla total.</blockquote>

<h2>4. Se calienta más de lo normal</h2>
<p>Todos los motores trabajan tibios, pero si no puedes mantener la mano sobre la carcasa unos segundos, hay un problema. El sobrecalentamiento acelera la muerte del aislamiento y suele venir acompañado de las señales anteriores.</p>
<h3>¿Cómo saber si es normal?</h3>
<ul>
  <li><strong>Tibio y constante:</strong> normal.</li>
  <li><strong>Muy caliente en minutos:</strong> revisar ventilación, carga y bobinado.</li>
  <li><strong>Caliente + ruido + olor:</strong> apagar y llamar al técnico.</li>
</ul>

<h2>5. Hace ruidos o vibra distinto</h2>
<p>No todo ruido es bobinado —muchas veces son <strong>rodamientos gastados</strong>— pero un zumbido eléctrico grave, chispazos o vibración nueva ameritan una revisión. Cambiar un rodamiento a tiempo evita que el eje dañe el estátor.</p>

<h2>¿Rebobinar o comprar nuevo?</h2>
<p>Depende de la potencia y del estado del núcleo. Como regla general, en motores medianos y grandes <strong>el rebobinado cuesta bastante menos que uno nuevo</strong> y queda como de fábrica si se hace bien. En motores muy pequeños, a veces conviene reemplazar. Por eso nuestro diagnóstico es gratuito: medimos, te decimos la verdad y tú decides.</p>
""",
    },
    {
        "slug": "alargar-vida-refrigeradora-lavadora",
        "title": "Cómo alargar la vida de tu refrigeradora y lavadora",
        "cat": "Electrodomésticos",
        "date": "2026-06-20", "date_h": "20 de junio, 2026", "read": "4 min",
        "cover": "foto-electrodomesticos.webp",
        "excerpt": "Pequeños hábitos de mantenimiento que evitan reparaciones caras y hacen que tus electrodomésticos duren años más.",
        "body": """
<p>La mayoría de las reparaciones que atendemos se pudieron evitar con un poco de mantenimiento. No necesitas ser técnico: con estos hábitos sencillos, tu refrigeradora y tu lavadora te durarán muchos años más.</p>

<h2>Refrigeradora: el frío bien cuidado</h2>
<h3>Limpia la parte de atrás</h3>
<p>El serpentín trasero (esas rejillas negras) acumula polvo y pelusa. Cuando está sucio, el <strong>compresor trabaja el doble</strong> para enfriar, gasta más luz y se desgasta antes. Desconéctala y pásale una brocha o aspiradora cada 3 o 4 meses.</p>
<h3>Deja espacio a los lados</h3>
<p>La refrigeradora necesita ventilar. Pegada a la pared o encajonada, no disipa el calor y el motor sufre. Deja al menos 10 cm libres por detrás y a los costados.</p>
<h3>Revisa el empaque de la puerta</h3>
<p>Si la goma está dura o rota, entra aire caliente y el motor no descansa nunca. Prueba fácil: cierra la puerta atrapando una hoja de papel. Si sale sin resistencia, el empaque ya no sella.</p>

<blockquote>El 80% de las fallas de compresor que vemos empiezan por un serpentín sucio o mala ventilación. Son cinco minutos que te ahorran una reparación cara.</blockquote>

<h2>Lavadora: cuídala del maltrato</h2>
<ul>
  <li><strong>No la sobrecargues.</strong> Meter más ropa de la cuenta fuerza el motor, los rodamientos y la faja. Respeta la capacidad.</li>
  <li><strong>Revisa los bolsillos.</strong> Monedas, clavos y llaves rompen el tambor y atascan la bomba de desagüe.</li>
  <li><strong>Nivélala.</strong> Si vibra y "camina", ajusta las patas. El desbalance destroza los rodamientos con el tiempo.</li>
  <li><strong>Deja la puerta abierta</strong> tras cada lavada para que seque y no crezca moho ni malos olores.</li>
</ul>

<h2>Estabiliza el voltaje</h2>
<p>En zonas donde la luz "baja y sube", las variaciones de voltaje son enemigas de las tarjetas electrónicas. Un <strong>estabilizador</strong> para la refrigeradora y equipos con tablero digital es una inversión pequeña que protege lo caro.</p>

<h2>Cuándo llamar al técnico</h2>
<p>Si notas ruidos nuevos, que no enfría, que no centrifuga, agua donde no debe o un olor a quemado, no esperes a que empeore. Una revisión a tiempo casi siempre sale más barata. En Tacna atendemos electrodomésticos a domicilio y el diagnóstico es gratuito.</p>
""",
    },
    {
        "slug": "tablero-electrico-seguro-casa-negocio",
        "title": "Tablero eléctrico seguro: qué debe tener el tuyo",
        "cat": "Seguridad",
        "date": "2026-06-05", "date_h": "5 de junio, 2026", "read": "6 min",
        "cover": "foto-tableros.webp",
        "excerpt": "Llaves térmicas, diferencial y puesta a tierra. Lo mínimo que tu instalación necesita para proteger a tu familia o tu negocio.",
        "body": """
<p>El tablero eléctrico es el corazón de tu instalación y, cuando está mal armado, es también la causa más común de incendios y descargas en casas y negocios. Esto es lo que un tablero seguro debe tener, explicado sin tecnicismos.</p>

<h2>1. Llave general (interruptor principal)</h2>
<p>Es la que corta toda la energía de golpe. Debe ser accesible y del amperaje correcto para tu acometida. En una emergencia, todos en casa deberían saber dónde está y cómo bajarla.</p>

<h2>2. Llaves termomagnéticas por circuito</h2>
<p>No basta con una sola llave para todo. Cada zona —tomacorrientes, iluminación, cocina, termas— debe tener <strong>su propia llave térmica</strong>. Así, si falla un circuito, solo ese se corta y puedes ubicar el problema rápido. Además protegen los cables contra sobrecarga y cortocircuito.</p>

<h2>3. Interruptor diferencial</h2>
<p>Este es el que <strong>salva vidas</strong>. El diferencial detecta fugas de corriente mínimas —las que ocurren cuando una persona toca algo energizado— y corta en milésimas de segundo. Es obligatorio especialmente en circuitos de baños, cocina y exteriores. Si tu tablero no tiene uno, es la primera mejora que deberías hacer.</p>

<blockquote>Una llave térmica protege tus cables. Un diferencial te protege a ti. No son lo mismo, y tu tablero necesita ambos.</blockquote>

<h2>4. Puesta a tierra</h2>
<p>El pozo a tierra da un camino seguro para que la corriente de falla se vaya al suelo en lugar de pasar por tu cuerpo o por los equipos. Sin puesta a tierra, el diferencial no trabaja bien y tus electrodomésticos quedan expuestos. Es especialmente crítico para equipos con carcasa metálica.</p>

<h2>5. Cables y borneras en orden</h2>
<p>Un tablero seguro también se reconoce a la vista:</p>
<ul>
  <li>Cables ordenados y del <strong>calibre correcto</strong> para cada carga.</li>
  <li>Conexiones firmes en las borneras (las flojas se calientan y queman).</li>
  <li>Sin empalmes improvisados ni "puentes" con cable pelado.</li>
  <li>Tapa cerrada y, en lo posible, un directorio que indique qué controla cada llave.</li>
</ul>

<h2>Señales de que tu tablero necesita revisión</h2>
<p>Llama a un técnico si notas alguna de estas: olor a quemado o plástico derretido, llaves que se calientan, chispas al conectar, la instalación "tira" corrientazos leves, o tu tablero todavía usa los antiguos tapones de rosca (fusibles de loza).</p>

<h2>Hazlo con un profesional</h2>
<p>Un tablero es barato comparado con un incendio o un accidente. Nosotros armamos e instalamos tableros para casa, comercio e industria, con protecciones certificadas y puesta a tierra. Te dejamos todo probado y con su directorio. La asesoría es gratuita: escríbenos y revisamos tu caso.</p>
""",
    },
]


def render_article(post):
    p = "../"
    home = "../index.html"
    canonical = f"{BASE}/blog/{post['slug']}.html"
    og_img = f"{BASE}/assets/{post['cover']}"
    schema = (
        '{"@context":"https://schema.org","@type":"Article",'
        f'"headline":"{post["title"]}",'
        f'"datePublished":"{post["date"]}",'
        f'"image":"{og_img}",'
        '"author":{"@type":"Organization","name":"SERVITEK"},'
        '"publisher":{"@type":"Organization","name":"SERVITEK — Servicio Técnico Eléctrico"}}'
    )
    return f'''{head(post["title"] + " · SERVITEK", post["excerpt"], canonical, p, og_img)}
<script type="application/ld+json">{schema}</script>
</head>
<body>
{header(p, home)}

<main id="main">
<article class="article">
  <div class="article__wrap">
    <a class="article__back" href="{p}blog.html"><span aria-hidden="true">←</span> Volver al blog</a>
    <p class="article__meta">{post["cat"]} · {post["date_h"]} · {post["read"]} de lectura</p>
    <h1 class="article__title">{post["title"]}</h1>
  </div>

  <div class="article__wrap">
    <figure class="article__cover">
      <img src="{p}assets/{post["cover"]}" alt="{post["title"]}" width="900" height="500">
    </figure>

    <div class="prose">
      {post["body"].strip()}
    </div>

    <div class="article__cta">
      <h2>¿Tienes un caso así?</h2>
      <p>Diagnóstico y asesoría gratuita en Tacna. Cuéntanos qué pasa y te ayudamos.</p>
      <a class="btn btn--volt" href="{WA}" target="_blank" rel="noopener">
        <svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2c-5.5 0-9.96 4.46-9.96 9.96 0 1.76.46 3.48 1.34 5L2 22l5.2-1.36a9.9 9.9 0 0 0 4.84 1.24h.01c5.5 0 9.96-4.46 9.96-9.96S17.54 2 12.04 2Zm5.83 14.06c-.24.68-1.42 1.31-1.96 1.36-.5.05-.96.24-3.24-.68-2.73-1.1-4.46-3.9-4.6-4.09-.13-.19-1.1-1.46-1.1-2.78 0-1.32.7-1.97.94-2.24.25-.27.54-.34.72-.34.18 0 .36 0 .52.01.17.01.39-.06.61.47.24.55.8 1.9.87 2.04.07.14.12.3.02.49-.1.19-.15.3-.29.46-.15.17-.31.37-.44.5-.15.14-.3.3-.13.59.17.29.75 1.24 1.61 2.01 1.11.99 2.04 1.3 2.33 1.44.29.15.46.12.63-.07.17-.19.73-.85.93-1.14.19-.29.39-.24.65-.15.26.1 1.61.76 1.89.9.27.14.46.22.53.34.06.12.06.7-.18 1.38Z"/></svg>
        Escríbenos por WhatsApp
      </a>
    </div>
  </div>

  <div class="article__foot">
    <p>SERVITEK · Servicio Técnico Eléctrico · Tacna, Perú</p>
  </div>
</article>
</main>

{footer(p, home)}'''


def render_listing():
    p = ""
    home = "index.html"
    canonical = f"{BASE}/blog.html"
    og_img = f"{BASE}/assets/og-servitek.png"
    cards = []
    for post in POSTS:
        cards.append(f'''      <article class="post" data-reveal>
        <div class="post__art">
          <img src="assets/{post["cover"]}" alt="{post["title"]}" width="481" height="640" loading="lazy">
          <span class="post__cat">{post["cat"]}</span>
        </div>
        <div class="post__body">
          <p class="post__meta">{post["date_h"]} · {post["read"]} de lectura</p>
          <h3><a href="blog/{post["slug"]}.html">{post["title"]}</a></h3>
          <p>{post["excerpt"]}</p>
          <span class="post__link">Leer artículo <span aria-hidden="true">→</span></span>
        </div>
      </article>''')
    cards_html = "\n".join(cards)
    return f'''{head("Blog · Consejos eléctricos | SERVITEK Tacna", "Consejos prácticos sobre motores, bombas, tableros eléctricos y electrodomésticos del equipo técnico de SERVITEK en Tacna.", canonical, p, og_img)}
</head>
<body>
{header(p, home)}

<main id="main">
<section class="blog-hero">
  <div class="hero__grid" aria-hidden="true"></div>
  <div class="wrap">
    <p class="kicker" data-reveal>Blog · Consejos</p>
    <h1 class="sec-title" data-reveal>El blog de <span class="hl">SERVITEK</span></h1>
    <p class="sec-lead" data-reveal>Guías claras y sin tecnicismos para cuidar tus motores, bombas, tableros y electrodomésticos. Escrito por quienes los reparan todos los días.</p>
  </div>
</section>

<section class="blog" style="border-top:0">
  <div class="wrap">
    <div class="posts">
{cards_html}
    </div>
  </div>
</section>
</main>

{footer(p, home)}'''


os.makedirs(f"{ROOT}/blog", exist_ok=True)
with open(f"{ROOT}/blog.html", "w", encoding="utf-8") as f:
    f.write(render_listing())
print("blog.html")
for post in POSTS:
    path = f"{ROOT}/blog/{post['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_article(post))
    print(f"blog/{post['slug']}.html")
