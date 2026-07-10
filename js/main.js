/* SERVITEK — interacciones */
(() => {
  'use strict';

  const WHATSAPP = '51977220049';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* ── Año actual ───────────────────────────────────────────── */
  const yearEl = $('#year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ── Tema claro / oscuro ──────────────────────────────────── */
  const themeBtn = $('#theme');
  if (themeBtn) {
    const root = document.documentElement;
    const meta = document.querySelector('meta[name="theme-color"]');
    const syncBtn = () => {
      const light = root.getAttribute('data-theme') === 'light';
      themeBtn.setAttribute('aria-pressed', String(light));
      themeBtn.setAttribute('aria-label', light ? 'Cambiar a modo oscuro' : 'Cambiar a modo claro');
      if (meta) meta.setAttribute('content', light ? '#ECEBE4' : '#0B0B0C');
    };
    syncBtn();
    themeBtn.addEventListener('click', () => {
      const light = root.getAttribute('data-theme') === 'light';
      if (light) root.removeAttribute('data-theme');
      else root.setAttribute('data-theme', 'light');
      try { localStorage.setItem('servitek-theme', light ? 'dark' : 'light'); } catch (e) {}
      syncBtn();
    });
  }

  /* ── Header: fondo al hacer scroll + barra de progreso ───── */
  const hdr = $('#hdr');
  const progress = $('#progress');
  const totop = $('#totop');

  let ticking = false;
  const onScroll = () => {
    const y = scrollY;
    hdr.classList.toggle('hdr--stuck', y > 24);
    totop.classList.toggle('is-on', y > 700);

    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.width = max > 0 ? `${(y / max) * 100}%` : '0%';
    ticking = false;
  };
  addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  totop.addEventListener('click', () =>
    scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' })
  );

  /* ── Menú móvil ───────────────────────────────────────────── */
  const burger = $('#burger');
  const nav = $('#nav');

  const setMenu = (open) => {
    nav.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    document.body.style.overflow = open ? 'hidden' : '';
  };

  burger.addEventListener('click', () =>
    setMenu(burger.getAttribute('aria-expanded') !== 'true')
  );
  nav.addEventListener('click', (e) => {
    if (e.target.tagName === 'A' && innerWidth <= 760) setMenu(false);
  });
  addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
  addEventListener('resize', () => { if (innerWidth > 760) setMenu(false); });

  /* ── Reveal on scroll ─────────────────────────────────────── */
  const reveals = $$('[data-reveal]');
  reveals.forEach((el) => {
    const d = el.dataset.delay;
    if (d) el.style.setProperty('--d', d);
  });

  if (reduced || !('IntersectionObserver' in window)) {
    reveals.forEach((el) => el.classList.add('is-in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach((el) => io.observe(el));
  }

  /* ── Contadores animados ──────────────────────────────────── */
  const counters = $$('[data-count]');
  const runCounter = (el) => {
    const target = Number(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    if (reduced) { el.textContent = target.toLocaleString('es-PE') + suffix; return; }

    const dur = 1600;
    let start = null;
    const step = (ts) => {
      if (start === null) start = ts;
      const p = Math.min((ts - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('es-PE') + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  if ('IntersectionObserver' in window) {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        runCounter(entry.target);
        cio.unobserve(entry.target);
      });
    }, { threshold: 0.6 });
    counters.forEach((el) => cio.observe(el));
  } else {
    counters.forEach(runCounter);
  }

  /* ── Spotlight que sigue al cursor ────────────────────────── */
  if (!reduced && matchMedia('(pointer: fine)').matches) {
    const spot = $('.spotlight');
    addEventListener('pointermove', (e) => {
      spot.style.setProperty('--mx', `${e.clientX}px`);
      spot.style.setProperty('--my', `${e.clientY}px`);
    }, { passive: true });
  }

  /* ── Acordeón: solo uno abierto ───────────────────────────── */
  const accs = $$('.acc');
  accs.forEach((acc) => {
    acc.addEventListener('toggle', () => {
      if (!acc.open) return;
      accs.forEach((other) => { if (other !== acc) other.open = false; });
    });
  });

  /* ── Formulario → WhatsApp ────────────────────────────────── */
  const form = $('#form');
  const note = $('#formNote');

  if (form) {

  const rules = {
    nombre: (v) => (v.trim().length >= 3 ? '' : 'Escribe tu nombre completo.'),
    telefono: (v) =>
      /^9\d{8}$/.test(v.replace(/\D/g, '')) ? '' : 'Ingresa un celular de 9 dígitos que empiece con 9.',
    servicio: (v) => (v ? '' : 'Elige el servicio que necesitas.'),
  };

  const showError = (field, msg) => {
    const wrap = field.closest('.field');
    wrap.classList.toggle('is-bad', Boolean(msg));
    const slot = wrap.querySelector('[data-err]');
    if (slot) slot.textContent = msg;
    return !msg;
  };

  const validate = (field) => {
    const rule = rules[field.name];
    return rule ? showError(field, rule(field.value)) : true;
  };

  Object.keys(rules).forEach((name) => {
    const field = form.elements[name];
    field.addEventListener('blur', () => validate(field));
    field.addEventListener('input', () => {
      if (field.closest('.field').classList.contains('is-bad')) validate(field);
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Honeypot: si un bot lo llena, fingimos éxito y no hacemos nada.
    if (form.elements.empresa.value) return;

    const fields = Object.keys(rules).map((n) => form.elements[n]);
    const ok = fields.map(validate).every(Boolean);

    if (!ok) {
      note.textContent = 'Revisa los campos marcados en rojo.';
      note.classList.remove('is-ok');
      fields.find((f) => !validate(f))?.focus();
      return;
    }

    const { nombre, telefono, servicio, mensaje } = form.elements;
    const lines = [
      'Hola SERVITEK, quiero una cotización.',
      '',
      `*Nombre:* ${nombre.value.trim()}`,
      `*Teléfono:* ${telefono.value.trim()}`,
      `*Servicio:* ${servicio.value}`,
    ];
    if (mensaje.value.trim()) lines.push(`*Detalle:* ${mensaje.value.trim()}`);

    const url = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(lines.join('\n'))}`;

    note.textContent = 'Abriendo WhatsApp con tu mensaje…';
    note.classList.add('is-ok');

    const win = open(url, '_blank', 'noopener');
    if (!win) {
      note.textContent = 'Tu navegador bloqueó la ventana. Toca aquí para abrir WhatsApp.';
      note.style.cursor = 'pointer';
      note.onclick = () => { location.href = url; };
    }
  });

  } /* fin if (form) */
})();
