
document.querySelectorAll('[data-t]').forEach(h => {
  h.innerHTML = h.dataset.t.split(' ').map(w => `<span class="w"><i>${w}</i></span>`).join(' ');
});

const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) {
    e.target.classList.add('in');
    io.unobserve(e.target);
  }
}), { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.sec, .sec-contact').forEach(s => io.observe(s));

const tg = document.getElementById('menuToggle');
const mn = document.getElementById('mobileNav');
const nv = document.getElementById('topNav');

const setH = () => { if (mn && nv) mn.style.top = nv.offsetHeight + 'px'; };
setH();
addEventListener('resize', setH);

const tm = o => {
  if (!mn || !tg) return;
  mn.classList.toggle('open', o);
  tg.classList.toggle('open', o);
  mn.setAttribute('aria-hidden', !o);
};

if (tg) {
  tg.onclick = e => {
    e.stopPropagation();
    tm(!mn.classList.contains('open'));
  };
}

if (mn) {
  mn.querySelectorAll('a').forEach(a => a.onclick = () => tm(false));
  document.onclick = e => {
    if (!mn.contains(e.target) && !tg.contains(e.target)) tm(false);
  };
}

addEventListener('keydown', e => {
  if (e.key === 'Escape') tm(false);
});

const wrap = document.getElementById('navLinksWrap');
const ind = document.getElementById('navIndicator');

if (wrap && ind) {
  document.querySelectorAll('#navLinks .nav-item').forEach(i => i.addEventListener('pointerenter', () => {
    const w = wrap.getBoundingClientRect();
    const r = i.getBoundingClientRect();
    ind.style.left = r.left - w.left + 'px';
    ind.style.width = r.width + 'px';
    ind.style.opacity = '1';
  }));
  wrap.addEventListener('pointerleave', () => {
    ind.style.opacity = '0';
  });
}

const pg = document.getElementById('prog');
if (pg) {
  addEventListener('scroll', () => {
    pg.style.transform = `scaleX(${scrollY / Math.max(1, document.documentElement.scrollHeight - innerHeight)})`;
  }, { passive: true });
}

const RM = matchMedia('(prefers-reduced-motion:reduce)').matches;
const mq = [...document.querySelectorAll('.marq div')];
const ps = [0, 0];
if (!RM && mq.length) {
  (function f() {
    mq.forEach((el, j) => {
      const h = el.scrollWidth / 2;
      ps[j] = (ps[j] + 1) % h;
      el.style.transform = `translateX(${j ? ps[j] - h : -ps[j]}px)`;
    });
    requestAnimationFrame(f);
  })();
}

const q = new URLSearchParams(location.search);
const sv = document.getElementById('service');
if (sv && q.get('service')) sv.value = q.get('service');

const F = document.getElementById('projectForm');
if (F) {
  let busy = false;
  const msg = document.getElementById('formMsg');
  const btn = document.getElementById('formSubmitBtn');
  const bt = btn.querySelector('.btn-text');
  
  const bad = (el, v) => {
    el.classList.toggle('input-error', v);
    const e = document.getElementById(el.id + 'Err');
    if (e) e.classList.toggle('visible', v);
    return v;
  };
  
  F.onsubmit = async e => {
    e.preventDefault();
    if (busy) return;
    const g = id => F.querySelector('#' + id);
    const d = {};
    let x = false;
    x |= bad(g('name'), g('name').value.trim().length < 2);
    x |= bad(g('email'), !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(g('email').value.trim()));
    x |= bad(g('phone'), g('phone').value.replace(/\D/g, '').length < 10);
    x |= bad(g('service'), !g('service').value);
    x |= bad(g('details'), g('details').value.trim().length < 10);
    const c = g('consent');
    const cErr = document.getElementById('consentErr');
    if (cErr) cErr.classList.toggle('visible', !c.checked);
    if (x || !c.checked) {
      msg.className = 'form-msg err';
      msg.textContent = 'Please correct the highlighted fields.';
      return;
    }
    ['name', 'company', 'email', 'phone', 'service', 'budget', 'details', 'contactMethod', 'website'].forEach(k => d[k] = g(k).value.trim());
    d.consent = true;
    busy = true;
    btn.classList.add('submitting');
    bt.textContent = 'Sending...';
    msg.className = 'form-msg';
    try {
      const r = await fetch('/api/enquiry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(d)
      });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || !j.ok) throw 0;
      msg.className = 'form-msg ok';
      msg.textContent = 'Thank you for contacting ZAQSA! Your enquiry has been received. Our team will review your requirements and get in touch within 24 hours.';
      F.reset();
    } catch (_) {
      msg.className = 'form-msg err';
      msg.textContent = "We couldn't submit your enquiry right now. Please try again or contact us directly at zyqotech@gmail.com.";
    }
    busy = false;
    btn.classList.remove('submitting');
    bt.textContent = 'Send My Enquiry';
  };
}
