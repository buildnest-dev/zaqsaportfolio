import re, base64, os, json, shutil

SITE = os.environ.get('SITE_URL', 'https://www.zaqsa.com')
EMAIL = 'zyqotech@gmail.com'
PHONE = '+91 95707 52983'
ADDR = 'Mahavir Enclave, New Delhi – 110045, India'

BASE_DIR = '/Users/adityarajput/Downloads/files'
SRC_FILE = os.path.join(BASE_DIR, 'aditya.html')
src = open(SRC_FILE, encoding='utf-8').read()

O = BASE_DIR
os.makedirs(os.path.join(O, 'public', 'assets'), exist_ok=True)
A = os.path.join(O, 'public', 'assets') + os.sep

def b64(p, n):
    m = re.search(p, src)
    if m:
        open(A + n, 'wb').write(base64.b64decode(m.group(1)))

b64(r'<img src="data:image/png;base64,([A-Za-z0-9+/=]+)"', 'logo.png')
b64(r'rel="icon" type="image/png" sizes="32x32" href="data:image/png;base64,([A-Za-z0-9+/=]+)"', 'favicon.png')

# Ensure team photos exist
def extract_team_photos():
    if os.path.exists(A + 'team1.jpg') and os.path.exists(A + 'team2.jpg') and os.path.getsize(A + 'team1.jpg') != os.path.getsize(A + 'team2.jpg'):
        return
    for i, m in enumerate(re.findall(r'<img src="data:image/jpeg;base64,([A-Za-z0-9+/=]+)"', src)[:2]):
        open(A + 'team%d.jpg' % (i + 1), 'wb').write(base64.b64decode(m))

extract_team_photos()

# World-class modern dark stylesheet
CSS = """
/* ===================================================================
   ZAQSA TECH & SOLUTIONS — PREMIER DESIGN SYSTEM
   Modern, High-Tech, Elite Dark Aesthetics
   =================================================================== */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg: #07090e;
  --bg-card: rgba(15, 23, 42, 0.65);
  --border: rgba(255, 255, 255, 0.08);
  --border-hover: rgba(56, 189, 248, 0.4);
  --ice: #F8FAFC;
  --mute: #94A3B8;
  --text-muted: #64748B;
  --cyan: #38BDF8;
  --blue: #2563EB;
  --indigo: #6366F1;
  --purple: #8B5CF6;
  --emerald: #10B981;
  --amber: #F59E0B;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color-scheme: dark;
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
  background: var(--bg);
  color: var(--ice);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: clip;
}

body {
  background: var(--bg);
  color: var(--ice);
  font-family: var(--font-sans);
  line-height: 1.6;
  overflow-x: clip;
  min-height: 100vh;
}

a {
  color: inherit;
}

:focus-visible {
  outline: 2px solid var(--cyan);
  outline-offset: 3px;
}

/* Background Atmosphere */
.bg {
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background: 
    radial-gradient(circle at 15% 15%, rgba(37, 99, 235, 0.15), transparent 45%),
    radial-gradient(circle at 85% 25%, rgba(56, 189, 248, 0.12), transparent 40%),
    radial-gradient(circle at 50% 80%, rgba(99, 102, 241, 0.1), transparent 50%),
    #07090e;
}

.bg::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px);
  background-size: 32px 32px;
  opacity: 0.6;
}

/* Scroll progress */
.prog {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC);
  transform: scaleX(0);
  transform-origin: left;
  z-index: 1000;
}

/* Typography Overhauls */
.d, h1, h2, h3, h4, .ph {
  font-family: var(--font-sans) !important;
  letter-spacing: -0.025em;
  text-transform: none;
}

/* Global Section Headings */
.d.big, .sec h2.big {
  font-size: clamp(2rem, 3.8vw, 3.1rem) !important;
  font-weight: 800 !important;
  line-height: 1.2 !important;
  text-align: center;
  margin: 0 auto 0.75rem !important;
  max-width: 900px;
  background: linear-gradient(180deg, #FFFFFF 15%, #E2E8F0 60%, #94A3B8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none !important;
}

.w i {
  display: inline-block;
  font-style: normal;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.6s ease;
}

.sec:not(.in) .w i {
  opacity: 0;
  transform: translateY(16px);
}

.sec.in .w i {
  opacity: 1;
  transform: translateY(0);
}

/* Page Hero Headings */
h1.ph {
  font-size: clamp(2.4rem, 5vw, 4rem) !important;
  font-weight: 800 !important;
  line-height: 1.15 !important;
  text-align: center;
  margin: 0 auto 1.25rem !important;
  max-width: 950px;
  background: linear-gradient(135deg, #FFFFFF 30%, #BAE6FD 75%, #38BDF8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 4px 30px rgba(56, 189, 248, 0.15) !important;
}

.phero {
  padding-top: clamp(6.5rem, 11vw, 9rem) !important;
  padding-bottom: clamp(2.5rem, 5vw, 4rem) !important;
  text-align: center;
}

.phero p {
  font-size: clamp(1.05rem, 1.8vw, 1.25rem) !important;
  color: var(--mute) !important;
  max-width: 680px;
  margin: 0 auto 1.75rem !important;
  line-height: 1.65;
}

/* Sub-labels and badges */
.sub {
  text-align: center;
  color: var(--cyan) !important;
  font-size: 0.8rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.15em !important;
  text-transform: uppercase !important;
  margin: 0 auto 2.5rem !important;
  display: block;
}

.contact-tag {
  display: inline-flex !important;
  align-items: center;
  gap: 8px;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: var(--cyan) !important;
  background: rgba(56, 189, 248, 0.08) !important;
  border: 1px solid rgba(56, 189, 248, 0.25) !important;
  border-radius: 9999px !important;
  padding: 6px 16px !important;
  margin-bottom: 1.25rem !important;
  text-shadow: none !important;
}

.lead, .sec p.lead {
  font-size: clamp(1.05rem, 1.4vw, 1.2rem) !important;
  line-height: 1.7 !important;
  color: var(--mute) !important;
  max-width: 780px !important;
  margin: 0 auto 1.75rem !important;
  text-align: center;
}

/* Navigation */
.top-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
  background: rgba(7, 9, 14, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  transition: all 0.3s ease;
}

.nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0.9rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo-img {
  height: 32px;
  width: auto;
  object-fit: contain;
}

.nav-links-wrap {
  position: relative;
  display: flex;
  align-items: center;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.07);
  padding: 4px 6px;
  border-radius: 9999px;
}

.nav-item {
  color: var(--mute);
  font-size: 0.9rem;
  font-weight: 500;
  text-decoration: none;
  padding: 0.45rem 1rem;
  border-radius: 9999px;
  transition: all 0.2s ease;
  position: relative;
  z-index: 2;
  white-space: nowrap;
}

.nav-item:hover {
  color: #FFFFFF;
  background: rgba(255, 255, 255, 0.08);
}

.nav-indicator {
  position: absolute;
  top: 4px;
  height: calc(100% - 8px);
  background: rgba(56, 189, 248, 0.15);
  border: 1px solid rgba(56, 189, 248, 0.3);
  border-radius: 9999px;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
  opacity: 0;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.contact-pill-btn {
  display: inline-flex;
  align-items: center;
  background: linear-gradient(135deg, #2563EB, #0284C7);
  color: #FFFFFF;
  font-size: 0.88rem;
  font-weight: 600;
  padding: 0.55rem 1.25rem;
  border-radius: 9999px;
  text-decoration: none;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 16px -2px rgba(37, 99, 235, 0.5);
  transition: all 0.25s ease;
  white-space: nowrap;
}

.contact-pill-btn:hover {
  box-shadow: 0 6px 24px 0 rgba(56, 189, 248, 0.6);
  transform: translateY(-1px);
}

.menu-toggle {
  display: none;
  background: transparent;
  border: 1px solid var(--border);
  color: #FFFFFF;
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
  flex-direction: column;
  gap: 5px;
}

.menu-toggle span {
  display: block;
  width: 20px;
  height: 2px;
  background: #FFFFFF;
  transition: all 0.3s ease;
}

/* Mobile Nav */
.mobile-nav {
  position: fixed;
  left: 0;
  right: 0;
  background: rgba(7, 9, 14, 0.98);
  backdrop-filter: blur(24px);
  border-bottom: 1px solid var(--border);
  padding: 1.5rem;
  display: none;
  z-index: 998;
}

.mobile-nav.open {
  display: block;
}

.mobile-nav-inner {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mobile-item {
  color: var(--mute);
  font-size: 1.1rem;
  text-decoration: none;
  padding: 0.5rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.mobile-item:hover {
  color: #FFFFFF;
}

.mobile-contact-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #2563EB, #0284C7);
  color: #FFFFFF;
  font-weight: 600;
  padding: 0.75rem;
  border-radius: 12px;
  text-decoration: none;
  margin-top: 0.5rem;
}

/* Home Hero */
.hero {
  min-height: 90vh;
  padding: clamp(6.5rem, 12vw, 8.5rem) clamp(1.25rem, 4vw, 3rem) 3rem;
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--mute);
  font-size: 0.88rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 1rem;
  margin-bottom: 2rem;
}

.top i {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--emerald);
  margin-left: 8px;
  box-shadow: 0 0 10px var(--emerald);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.title {
  text-align: center;
  margin: 1rem 0 2rem;
}

h1#h1 {
  font-size: clamp(3.5rem, 14vw, 9.5rem) !important;
  font-weight: 900 !important;
  letter-spacing: -0.04em !important;
  line-height: 0.95;
  display: flex;
  justify-content: center;
  background: linear-gradient(135deg, #FFFFFF 20%, #BAE6FD 60%, #38BDF8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 10px 40px rgba(56, 189, 248, 0.25));
}

.ch i {
  display: inline-block;
  font-style: normal;
}

.row {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 3rem;
  align-items: center;
  margin-top: 1.5rem;
}

.row h2 {
  font-size: clamp(1.8rem, 3.2vw, 2.75rem) !important;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1rem;
  background: linear-gradient(180deg, #FFFFFF 30%, #CBD5E1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.row p {
  color: var(--mute);
  font-size: 1.1rem;
  line-height: 1.65;
  margin-bottom: 1.75rem;
}

.btns {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.85rem 1.85rem;
  border-radius: 9999px;
  background: linear-gradient(135deg, #2563EB, #0284C7);
  color: #FFFFFF;
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 4px 20px -2px rgba(37, 99, 235, 0.5);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px 0 rgba(56, 189, 248, 0.5);
}

.btn.g {
  background: rgba(255, 255, 255, 0.05);
  color: #FFFFFF;
  border: 1px solid var(--border);
  box-shadow: none;
}

.btn.g:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: rgba(56, 189, 248, 0.4);
}

.stats {
  list-style: none;
  display: grid;
  gap: 1rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 1.75rem;
  border-radius: 20px;
  backdrop-filter: blur(12px);
}

.stats li {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  font-size: 1rem;
  color: var(--ice);
  font-weight: 500;
}

.stats li b {
  color: var(--cyan);
  font-size: 1.2rem;
}

/* Marquee */
.marq {
  overflow: hidden;
  background: rgba(15, 23, 42, 0.5);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  padding: 0.85rem 0;
  margin: 3rem 0;
}

.marq div {
  display: flex;
  width: max-content;
}

.marq span {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mute);
  padding: 0 2rem;
  display: inline-flex;
  align-items: center;
  gap: 2rem;
}

.marq span::after {
  content: "✦";
  color: var(--cyan);
  font-size: 0.8rem;
}

/* Sections */
.wrap {
  max-width: 1280px;
  margin: 0 auto;
  padding: clamp(3.5rem, 6vw, 6rem) clamp(1.25rem, 4vw, 2.5rem);
}

.sec {
  position: relative;
}

.center {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

/* Cards & Grid */
.solutions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.75rem;
  margin-top: 2.5rem;
}

.solution-card {
  background: var(--bg-card);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 2.25rem 2rem;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
}

.solution-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #38BDF8, #818CF8);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.solution-card:hover {
  transform: translateY(-6px);
  border-color: var(--border-hover);
  box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6), 0 0 25px rgba(56, 189, 248, 0.12);
}

.solution-card:hover::before {
  opacity: 1;
}

.sol-icon {
  width: 54px;
  height: 54px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.12), rgba(139, 92, 246, 0.12));
  border: 1px solid rgba(56, 189, 248, 0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--cyan);
  margin-bottom: 1.4rem;
}

.sol-title {
  font-size: 1.28rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0 0 0.85rem;
  letter-spacing: -0.02em;
}

.sol-desc {
  font-size: 0.98rem;
  color: var(--mute);
  line-height: 1.65;
  margin: 0 0 1.5rem;
  flex-grow: 1;
}

.panel-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--cyan);
  text-decoration: none;
  transition: gap 0.2s ease, color 0.2s ease;
}

.panel-cta:hover {
  gap: 10px;
  color: #7DD3FC;
}

/* Team Section (FIXING SCREENSHOT 2) */
.team {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 360px));
  gap: 2.5rem;
  justify-content: center;
  margin: 3rem auto 0;
  max-width: 820px;
}

.pt {
  position: relative;
  aspect-ratio: 4/5;
  border-radius: 24px;
  overflow: hidden;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.6);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.pt:hover {
  transform: translateY(-8px);
  border-color: rgba(56, 189, 248, 0.45);
  box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.7), 0 0 30px rgba(56, 189, 248, 0.15);
}

.pt img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 12%;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.pt:hover img {
  transform: scale(1.05);
}

.pt::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 40%, rgba(7, 9, 14, 0.65) 70%, rgba(7, 9, 14, 0.95) 100%);
  pointer-events: none;
}

.pi {
  position: absolute;
  left: 1.25rem;
  right: 1.25rem;
  bottom: 1.25rem;
  padding: 1.2rem 1.4rem;
  border-radius: 18px;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #FFFFFF;
  z-index: 2;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  text-align: left;
}

.pi h3, .pi b {
  font-size: 1.25rem !important;
  font-weight: 700 !important;
  color: #FFFFFF !important;
  margin: 0 0 0.25rem !important;
  letter-spacing: -0.01em !important;
  text-transform: none !important;
}

.pi small, .pi span {
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  color: var(--cyan) !important;
  display: block;
}

/* Process Steps */
.steps.six {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
  margin-top: 2.5rem;
}

.step {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 2rem 1.75rem;
  position: relative;
  transition: all 0.3s ease;
}

.step:hover {
  border-color: var(--border-hover);
  transform: translateY(-4px);
}

.step h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0 0 0.75rem;
}

.step p {
  font-size: 0.95rem;
  color: var(--mute);
  line-height: 1.6;
}

/* Tech Categories */
.tech-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2.5rem;
}

.tech-cat-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 1.75rem;
  transition: all 0.3s ease;
}

.tech-cat-card:hover {
  border-color: var(--border-hover);
  transform: translateY(-4px);
}

.tech-cat-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0 0 1rem;
}

.tech-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tech-pill {
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--mute);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  transition: all 0.2s ease;
}

.tech-pill:hover {
  color: #FFFFFF;
  border-color: var(--cyan);
  background: rgba(56, 189, 248, 0.1);
}

/* Call to Action Banner */
.cta, .sec.cta {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(15, 23, 42, 0.8)), var(--bg-card);
  border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 28px;
  padding: clamp(3.5rem, 7vw, 5.5rem) clamp(1.5rem, 5vw, 4rem);
  text-align: center;
  margin: 4rem auto;
  max-width: 1200px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 35px rgba(56, 189, 248, 0.1);
}

.cta h2 {
  font-size: clamp(2.2rem, 4.5vw, 3.5rem) !important;
  font-weight: 800 !important;
  margin-bottom: 1.25rem !important;
  background: linear-gradient(180deg, #FFFFFF 20%, #E2E8F0 60%, #94A3B8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: none !important;
}

.cta p {
  font-size: clamp(1.05rem, 1.6vw, 1.2rem);
  color: var(--mute);
  max-width: 640px;
  margin: 0 auto 2rem;
  line-height: 1.65;
}

/* Contact Page & Forms */
.sec-contact {
  padding-top: clamp(5rem, 9vw, 7.5rem) !important;
  padding-bottom: 4rem !important;
}

.contact-container {
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: 3.5rem;
  max-width: 1240px;
  margin: 0 auto;
}

.contact-heading {
  font-size: clamp(2rem, 3.8vw, 3rem);
  font-weight: 800;
  line-height: 1.2;
  margin: 0.5rem 0 1rem;
  background: linear-gradient(180deg, #FFFFFF 20%, #E2E8F0 60%, #94A3B8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.contact-subtext {
  font-size: 1.05rem;
  color: var(--mute);
  line-height: 1.65;
  margin-bottom: 2rem;
}

.contact-cards-stack {
  display: grid;
  gap: 1rem;
}

.info-card {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.25rem 1.5rem;
  text-decoration: none;
  color: inherit;
  transition: all 0.25s ease;
}

.info-card:hover {
  border-color: var(--border-hover);
  transform: translateY(-2px);
}

.info-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--cyan);
}

.info-label {
  display: block;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
}

.info-value {
  font-size: 1.05rem;
  font-weight: 600;
  color: #FFFFFF;
}

.project-form {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 2.5rem;
  backdrop-filter: blur(16px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
}

.form-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.25rem;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--ice);
  margin-bottom: 0.5rem;
}

.form-group input, .form-group select, .form-group textarea {
  width: 100%;
  background: rgba(11, 15, 25, 0.8);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 0.85rem 1rem;
  color: #FFFFFF;
  font-family: inherit;
  font-size: 0.95rem;
  transition: all 0.2s ease;
  outline: none;
}

.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
  border-color: var(--cyan);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
}

.form-error-msg {
  display: none;
  font-size: 0.8rem;
  color: #F87171;
  margin-top: 0.35rem;
}

.form-error-msg.visible {
  display: block;
}

.form-consent-wrap {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  margin: 1.5rem 0 1.25rem;
  font-size: 0.88rem;
  color: var(--mute);
}

.form-consent-wrap input[type="checkbox"] {
  margin-top: 0.2rem;
  accent-color: var(--cyan);
}

.form-msg {
  padding: 0.9rem 1.1rem;
  border-radius: 12px;
  font-weight: 600;
  display: none;
  margin-bottom: 1rem;
}

.form-msg.ok {
  display: block;
  background: rgba(16, 185, 129, 0.15);
  color: #6EE7B7;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.form-msg.err {
  display: block;
  background: rgba(239, 68, 68, 0.15);
  color: #FCA5A5;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.hp {
  position: absolute;
  left: -9999px;
  opacity: 0;
}

.form-submit-btn {
  width: 100%;
  padding: 1rem;
  border-radius: 12px;
  background: linear-gradient(135deg, #2563EB, #0284C7);
  color: #FFFFFF;
  font-size: 1rem;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.2);
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 4px 20px -2px rgba(37, 99, 235, 0.5);
}

.form-submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px 0 rgba(56, 189, 248, 0.5);
}

/* Legal Pages */
.legal {
  max-width: 840px;
  margin: 0 auto;
  color: var(--mute);
  line-height: 1.8;
}

.legal h3 {
  color: #FFFFFF;
  margin: 2rem 0 0.5rem;
  font-size: 1.3rem;
  font-weight: 700;
}

.legal p {
  margin-bottom: 1rem;
}

/* Footer */
footer.site {
  border-top: 1px solid var(--border);
  padding: 4.5rem clamp(1.25rem, 4vw, 3rem) 2.5rem;
  background: rgba(7, 9, 14, 0.95);
  margin-top: 4rem;
}

.fgrid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1.2fr 1.2fr;
  gap: 3rem;
  max-width: 1280px;
  margin: 0 auto;
}

.fgrid h4 {
  font-size: 1rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 1.25rem;
}

.fgrid a, .fgrid p {
  display: block;
  color: var(--mute);
  text-decoration: none;
  font-size: 0.92rem;
  margin-bottom: 0.65rem;
  line-height: 1.6;
  transition: color 0.2s ease;
}

.fgrid a:hover {
  color: var(--cyan);
}

.fcopy {
  text-align: center;
  color: var(--text-muted);
  font-size: 0.85rem;
  border-top: 1px solid var(--border);
  padding-top: 2rem;
  margin-top: 3.5rem;
}

/* Responsive adjustments */
@media (max-width: 960px) {
  .row {
    grid-template-columns: 1fr;
  }
  .contact-container {
    grid-template-columns: 1fr;
  }
  .fgrid {
    grid-template-columns: 1fr 1fr;
  }
  .nav-links-wrap {
    display: none;
  }
  .menu-toggle {
    display: flex;
  }
}

@media (max-width: 600px) {
  .fgrid {
    grid-template-columns: 1fr;
  }
  .form-grid-2 {
    grid-template-columns: 1fr;
  }
  .btns {
    flex-direction: column;
  }
}
"""

open(A + 'site.css', 'w').write(CSS)

JS = r'''
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
      msg.textContent = "We couldn't submit your enquiry right now. Please try again or contact us directly at ''' + EMAIL + '''.";
    }
    busy = false;
    btn.classList.remove('submitting');
    bt.textContent = 'Send My Enquiry';
  };
}
'''

open(A + 'site.js', 'w').write(JS)

IC = [
    '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    '<path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.2 16.2l2.9 2.8M2 12h4M18 12h4"/>',
    '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/>',
    '<path d="M3 11v2a1 1 0 0 0 1 1h2l5 4V6L6 10H4a1 1 0 0 0-1 1zM15 9a4 4 0 0 1 0 6"/>',
    '<circle cx="12" cy="12" r="10"/><path d="m16 8-2 6-6 2 2-6z"/>'
]

def ico(i):
    return '<div class="sol-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg></div>' % IC[i % 6]

SV = [
    ('website-development', 'Website Design & Development', 'High-performance responsive websites, corporate portals, e-commerce stores, landing pages, and bespoke web applications built for speed, SEO, and conversion.', "Websites That Do More Than Look Good.", "Build My Website", ['Business websites', 'Corporate websites', 'E-commerce websites', 'Landing pages', 'Custom web applications', 'Website redesign', 'Website maintenance', 'API integrations'], 'We design and build fast, accessible and maintainable websites that present your business clearly and help visitors take action.'),
    ('mobile-app-development', 'Mobile App Development', 'Native and cross-platform mobile applications for iOS and Android engineered for performance, delightful UX, and business velocity.', "Powerful Mobile Experiences. Built Around Your Users.", "Discuss My App Idea", ['Android applications', 'iOS applications', 'Cross-platform applications', 'Business applications', 'Customer-facing applications', 'API and backend integration', 'App maintenance'], 'From idea to store release, we build mobile applications that are smooth, reliable and designed around how your users actually work.'),
    ('ai-automation', 'AI & Automation', 'Intelligent AI agents, automated workflow pipelines, LLM integrations, and custom neural systems that eliminate repetitive operations.', "Work Smarter With Intelligent Automation.", "Automate My Business", ['AI chatbots & assistants', 'Workflow automation pipelines', 'Customer support automation', 'Business process automation', 'LLM & AI API integrations', 'Data processing automation', 'Custom AI-enabled internal tools'], 'We apply AI and automation to practical problems: repetitive work, slow support and scattered data.'),
    ('custom-software', 'Custom Software & CRM', 'Tailor-made CRM, ERP, business management dashboards, and enterprise platforms architected to match your exact business logic.', "Software Built for the Way Your Business Works.", "Request Custom Software", ['Custom CRM systems', 'ERP solutions', 'Admin dashboards', 'Business management platforms', 'Internal workflow systems', 'Customer and partner portals', 'Reporting dashboards', 'SaaS applications'], 'When off-the-shelf tools do not fit, we build software around your processes, users and growth plans.'),
    ('digital-marketing', 'Digital Marketing & Branding', 'Data-driven SEO, brand identity, performance marketing, and creative growth strategies that turn visibility into recurring revenue.', "Creative Thinking. Smarter Digital Growth.", "Grow My Brand", ['Social media management', 'Digital advertising', 'Search engine optimization', 'Brand identity & design', 'Creative content marketing', 'Marketing strategy', 'Campaign planning'], 'We help you look consistent, be found and communicate clearly across digital channels.'),
    ('it-consulting', 'IT Consulting & Digital Transformation', 'Strategic technology advisory, system integration, cloud infrastructure, and modern architecture planning.', "Better Technology Decisions Start With the Right Strategy.", "Talk to an Expert", ['IT strategy & architecture', 'Digital transformation planning', 'Technology assessment', 'System integration', 'Cloud consultation', 'Process optimization', 'Software architecture guidance'], 'We help you choose the right technology, plan the change and connect the systems you already use.')
]

WHY = [
    ('Innovation-Driven Thinking', 'We challenge standard defaults to build smarter, future-proof software architectures.'),
    ('Business-Focused Engineering', 'Every line of code and feature is directly aligned with your commercial growth.'),
    ('Scalable Cloud Architecture', 'High-throughput systems engineered to scale reliably as your users and data multiply.'),
    ('Human-Centric Experiences', 'Intuitive, fluid interfaces built to minimize user friction and boost productivity.'),
    ('Transparent Partnership', 'Direct communication, milestone visibility, and proactive consultation at every stage.'),
    ('Long-Term Maintainability', 'Clean code, modern tech stacks, and structured documentation that lasts for years.')
]

SOL = [
    ('Enterprise Management Systems', 'Centralize enterprise records, resource planning, and approvals in one unified platform.'),
    ('Customer Relationship Management', 'Empower sales and support teams with unified pipeline tracking and customer histories.'),
    ('AI-Powered Business Tools', 'Deploy intelligent assistants and automated agents that eliminate manual busywork.'),
    ('Cloud-Based Applications', 'Secure, responsive web applications engineered for seamless accessibility anywhere.'),
    ('Digital Commerce Solutions', 'Modern digital storefronts, friction-free checkouts, and integrated payment flows.'),
    ('Custom Business Portals', 'Dedicated high-security portals designed for clients, vendors, and internal teams.')
]

SOL2 = [
    ('Business Operations Management', 'Records, workflows and approvals organized into streamlined digital hubs.'),
    ('Customer Engagement Platforms', 'Tools to capture, manage, nurture, and support customer relationships seamlessly.'),
    ('Workflow Automation Pipelines', 'Automating repetitive, rule-based operations with intelligent triggers.'),
    ('Digital Commerce & Billing', 'Modern online selling experiences, from product catalogues to checkout & payouts.'),
    ('Data Analytics & Dashboards', 'Executive dashboards that convert operational metrics into actionable clarity.'),
    ('Custom Enterprise Applications', 'Tailor-made software designed specifically around your organizational structure.')
]

TECH = [
    ('Frontend', ['React.js', 'Next.js', 'TypeScript', 'Tailwind CSS', 'HTML5 & CSS3']),
    ('Backend', ['Node.js', 'Python', 'FastAPI', 'Express', 'REST & GraphQL']),
    ('Mobile', ['Flutter', 'React Native', 'iOS (Swift)', 'Android (Kotlin)']),
    ('Databases', ['PostgreSQL', 'MySQL', 'MongoDB', 'Redis']),
    ('AI & Automation', ['OpenAI APIs', 'Anthropic Claude', 'LangChain', 'Workflow Automation']),
    ('Cloud & DevOps', ['AWS', 'Google Cloud', 'Docker', 'Vercel', 'CI/CD Pipelines']),
    ('Design & Prototyping', ['Figma', 'UI/UX Prototyping', 'Design Systems', 'User Research']),
    ('Integrations & APIs', ['Stripe', 'Razorpay', 'Twilio', 'CRM Integrations', 'Custom Webhooks'])
]

PR = [
    ('Discovery & Alignment', 'We dive deep into your business objectives, technical constraints, and end-user personas.'),
    ('Architecture & Planning', 'We define technical scope, database schemas, feature milestones, and system architecture.'),
    ('UI/UX Design & Prototyping', 'We craft interactive prototypes and design systems tailored for your review and feedback.'),
    ('Agile Development', 'We build in iterative milestones with continuous integration, sharing live staging progress.'),
    ('Rigorous QA & Security', 'We test performance, security vulnerabilities, edge cases, and cross-device responsiveness.'),
    ('Deployment & Ongoing Support', 'We execute zero-downtime launches, train your team, and provide dedicated maintenance.')
]

def sec(t, s, inner, cls='', id=''):
    return '<section class="sec wrap %s"%s><h2 class="d big" data-t="%s"></h2><p class="sub">%s</p>%s</section>' % (cls, ' id="%s"' % id if id else '', t, s, inner)

def cards(it, link=None):
    h = ''
    for i, x in enumerate(it):
        h += '<div class="solution-card" style="--d:%.2fs">%s<h3 class="sol-title">%s</h3><p class="sol-desc">%s</p>%s</div>' % (i * .1, ico(i), x[0], x[1], ('<a class="panel-cta" href="%s">Learn More →</a>' % link[i]) if link else '')
    return '<div class="solutions-grid">%s</div>' % h

def btn(t, h, g=0):
    return '<a class="btn%s" href="%s">%s</a>' % (' g' if g else '', h, t)

def ph(tag, h, p, b=''):
    return '<header class="phero wrap"><span class="contact-tag">%s</span><h1 class="ph">%s</h1><p>%s</p>%s</header>' % (tag, h, p, ('<div class="center">%s</div>' % b) if b else '')

def tech(cats):
    return '<div class="tech-categories">' + ''.join('<div class="tech-cat-card"><h3 class="tech-cat-title">%s</h3><div class="tech-pills">%s</div></div>' % (c, ''.join('<span class="tech-pill">%s</span>' % t for t in ts)) for i, (c, ts) in enumerate(cats)) + '</div>'

def steps(p=PR):
    return '<div class="steps six">' + ''.join('<div class="step"><h3>%02d — %s</h3><p>%s</p></div>' % (i + 1, a, b) for i, (a, b) in enumerate(p)) + '</div>'

def cta(h, p, b):
    return '<section class="sec cta"><h2 class="d" data-t="%s"></h2><p>%s</p><div class="center">%s</div></section>' % (h, p, b)

INTRO = 'ZAQSA is a premier technology firm based in New Delhi, specializing in high-performance web development, mobile applications, AI workflow automation, and custom enterprise software for ambitious companies.'

slug_link = ['/services/' + s[0] for s in SV]
P = {}

mq = lambda a: '<div class="marq" aria-hidden="true"><div>%s</div></div>' % ''.join('<span>%s</span>' % x for _ in range(6) for x in a)

hero = '''<header class="hero"><div class="top"><span>ZAQSA Tech and Solutions Private Limited</span><span>New Delhi, India<i></i></span></div>
<div class="title"><h1 id="h1" aria-label="ZAQSA">%s</h1></div>
<div class="row"><div><span class="contact-tag">WELCOME TO ZAQSA</span><h2 class="d">Your Vision. Our Innovation.</h2><p>We build technology that moves businesses forward. From powerful web platforms and mobile apps to intelligent AI automation and custom software, ZAQSA transforms bold ideas into scalable digital reality.</p><div class="btns">%s%s</div></div>
<ul class="stats"><li><b>✦</b><span>Intelligent Digital Solutions</span></li><li><b>✦</b><span>Scalable Cloud Software</span></li><li><b>✦</b><span>AI-Powered Workflow Automation</span></li></ul></div></header>''' % (''.join('<span class="ch" aria-hidden="true"><i style="--i:%d">%s</i></span>' % (i, c) for i, c in enumerate('ZAQSA')), btn('Start Your Project', '/contact'), btn('Explore Our Services', '#services', 1))

P[''] = (
    'ZAQSA | Your Vision. Our Innovation. Software, AI & Automation',
    'ZAQSA Tech and Solutions builds websites, mobile apps, AI automation, custom software and CRM for ambitious businesses.',
    hero + mq(['Websites', 'Mobile Apps', 'AI & Automation', 'Custom Software', 'Digital Marketing', 'IT Consulting']) + '<main>'
    + sec('Innovation Is at the Heart of Everything We Build', 'WHO WE ARE', '<p class="lead">%s</p><div class="center">%s</div>' % (INTRO, btn('Discover ZAQSA', '/about')))
    + sec('Everything You Need to Build, Grow, and Transform Digitally', 'WHAT WE DO', cards([(s[1], s[2]) for s in SV], slug_link) + '<div class="center">%s</div>' % btn('View All Services', '/services'), id='services')
    + sec('More Than Technology. A Partner in Your Growth.', 'THE ZAQSA ADVANTAGE', cards(WHY))
    + sec('Smart Solutions for Modern Business Challenges.', 'OUR SOLUTIONS', cards(SOL) + '<div class="center">%s</div>' % btn('Discuss Your Requirements', '/contact'))
    + sec('Built With Modern Technology. Designed for Tomorrow.', 'OUR TECHNOLOGY APPROACH', tech(TECH[:7]))
    + sec('From Your First Idea to Your Digital Launch.', 'HOW WE WORK', steps() + '<div class="center">%s</div>' % btn('Start Your Journey', '/contact'))
    + cta('Ready to Build Something Extraordinary?', "Whether you are starting from scratch or scaling an existing system, let's explore how our engineering and AI capabilities can accelerate your vision.", btn("Let's Talk", '/contact') + btn('Request a Proposal', '/contact', 1)) + '</main>'
)

VAL = [
    ('Innovation First', 'We question default solutions to engineer smarter, higher-leverage outcomes for our clients.'),
    ('Uncompromising Integrity', 'Transparent roadmaps, honest architectural advice, and delivery commitments we stand behind.'),
    ('Engineering Excellence', 'High-speed performance, clean maintainable code, and attention to every interaction detail.'),
    ('Deep Collaboration', 'We work as an embedded extension of your leadership team, aligned with your commercial goals.'),
    ('Customer Outcome Driven', 'Every feature is measured against business value, operational efficiency, and user satisfaction.'),
    ('Continuous Evolution', 'We stay at the frontier of AI, modern cloud architectures, and digital design trends.')
]

# Team Section with Real Founders
team = '''<div class="team">
  <article class="pt">
    <img src="/assets/team1.jpg" alt="Drona Singh Rajpoot" loading="lazy">
    <div class="pi">
      <h3>Drona Singh Rajpoot</h3>
      <small>Founder & Director</small>
    </div>
  </article>
  <article class="pt">
    <img src="/assets/team2.jpg" alt="Chinmay Anand" loading="lazy">
    <div class="pi">
      <h3>Chinmay Anand</h3>
      <small>Co-Founder & Head of Technology</small>
    </div>
  </article>
</div>'''

OUR_STORY = '''<div style="max-width:840px;margin:0 auto;text-align:left;color:var(--mute);line-height:1.8;font-size:1.05rem">
<p style="margin-bottom:1.25rem">Founded in New Delhi, <strong>ZAQSA Tech and Solutions Private Limited</strong> was established with a singular conviction: technology should accelerate business velocity, not complicate it. We saw ambitious businesses struggling with disjointed off-the-shelf software, brittle legacy systems, and slow development cycles that drained momentum.</p>
<p style="margin-bottom:1.25rem">ZAQSA bridges the gap between deep technical engineering and real-world business outcomes. Our multidisciplinary team combines full-stack software architecture, mobile engineering, and modern artificial intelligence to build software that is robust, beautiful, and built for scale.</p>
<p>Today, we partner with startups, growing enterprises, and established institutions across India and internationally, delivering mission-critical applications, automated operations, and modern digital experiences that give our clients an unfair competitive advantage.</p>
</div>'''

P['about'] = (
    'About ZAQSA | Technology Company in New Delhi',
    'Learn about ZAQSA Tech and Solutions: our journey, vision, mission, core values, and executive team.',
    ph('ABOUT US', 'Driven by Ideas. Powered by Technology.', INTRO) + '<main>'
    + sec('Our Journey & Roots', 'WHO WE ARE', OUR_STORY)
    + sec('Vision & Mission', 'WHERE WE ARE HEADED', cards([
        ('Our Vision', 'To become a globally trusted technology and AI innovation partner, empowering forward-thinking companies to scale fearlessly with world-class digital systems.'),
        ('Our Mission', 'To engineer scalable, human-centric software and intelligent automation that solve deep operational bottlenecks and unlock exponential business value.')
    ]))
    + sec('Our Core Principles', 'WHAT GUIDES US', cards(VAL))
    + sec('Technology Should Work for People, Not the Other Way Around.', 'OUR PHILOSOPHY', '<p class="lead">We believe great technology feels invisible. We obsess over the humans using our systems—crafting frictionless interfaces and reliable architectures so your teams can focus on growth.</p>')
    + sec('Leadership & Engineering Team', 'THE MINDS BEHIND ZAQSA', team)
    + cta('Partner With ZAQSA', 'Have a project in mind? Let us show you what modern engineering can do for your business.', btn('Start the Conversation', '/contact')) + '</main>'
)

P['services'] = (
    'Services | Websites, Apps, AI, Software & Marketing | ZAQSA',
    'Explore ZAQSA services: website development, mobile apps, AI automation, custom software and CRM, digital marketing and IT consulting.',
    ph('OUR SERVICES', 'Everything You Need to Build, Scale, and Transform.', 'Six specialized engineering and digital capabilities under one accountable team.') + '<main>'
    + sec('Full-Lifecycle Capabilities', 'WHAT WE DO', cards([(s[1], s[2]) for s in SV], slug_link))
    + cta('Not sure where to start?', 'Tell us your core operational challenge and we will architect the right approach.', btn('Get a Free Consultation', '/contact')) + '</main>'
)

for i, s in enumerate(SV):
    rel = ''.join('<a class="btn g" href="/services/%s">%s</a>' % (r[0], r[1]) for r in SV if r[0] != s[0])
    P['services/' + s[0]] = (
        s[1] + ' | ZAQSA',
        s[2],
        ph('CAPABILITY', s[3], s[6], btn(s[4], '/contact?service=' + s[1].split(' &')[0].replace(' ', '+'))) + '<main>'
        + sec('What We Deliver', 'INCLUDED IN THIS SERVICE', cards([(x, '') for x in s[5]]).replace('<p class="sol-desc"></p>', ''))
        + sec('Why It Matters', 'KEY ADVANTAGES', '<p class="lead">Transparent scoping, modern technology choices, and a solution engineered to scale seamlessly as your operations expand.</p>')
        + sec('Explore Other Capabilities', 'RELATED SERVICES', '<div class="center">%s</div>' % rel)
        + cta('Ready to get started?', 'Share your project details with our team and receive a structured technical roadmap.', btn(s[4], '/contact')) + '</main>'
    )

P['solutions'] = (
    'Business Solutions | ZAQSA',
    'Intelligent solution categories for business operations, customer engagement, automation, commerce, data and custom enterprise applications.',
    ph('SOLUTIONS', 'Intelligent Architectures for Modern Businesses.', 'Custom solution frameworks we engineer for evolving organizations.') + '<main>'
    + sec('What We Build', 'SOLUTION DOMAINS', cards(SOL2) + '<div class="center">%s</div>' % btn('Explore a Custom Solution', '/contact')) + '</main>'
)

P['technologies'] = (
    'Technologies | ZAQSA',
    'The modern technology stack ZAQSA uses: frontend, backend, mobile, databases, AI, cloud and design.',
    ph('TECHNOLOGY STACK', 'Modern Tools for Demanding Engineering Challenges.', 'We deliberately select best-of-breed technologies suited for speed, reliability, and security.') + '<main>'
    + sec('Our Technical Capabilities', 'TOOLS & FRAMEWORKS', tech(TECH)) + '</main>'
)

P['process'] = (
    'Our Process | From Idea to Launch | ZAQSA',
    'ZAQSA six-stage engineering process: discovery, planning, design, development, testing, launch and support.',
    ph('OUR PROCESS', 'From First Concept to Scaled Digital Launch.', 'A disciplined, transparent delivery framework with verifiable milestones at every phase.') + '<main>'
    + sec('The Six-Stage Delivery Framework', 'HOW WE WORK', steps())
    + cta('Ready to begin your journey?', 'Schedule an initial discovery workshop with our engineering leadership.', btn('Book a Discovery Call', '/contact')) + '</main>'
)

card = lambda ic, l, v, h='': '<%s class="info-card"%s><div class="info-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">%s</svg></div><div class="info-body"><span class="info-label">%s</span><b class="info-value">%s</b></div></%s>' % ('a' if h else 'div', ' href="%s"' % h if h else '', ic, l, v, 'a' if h else 'div')
opt = lambda l: ''.join('<option>%s</option>' % x for x in l)

form = '''<section class="sec-contact"><div class="contact-container"><div class="contact-info-col"><span class="contact-tag">START THE CONVERSATION</span><h2 class="contact-heading">Let's Create Something Remarkable.</h2><p class="contact-subtext">Tell us what you're building, the operational bottleneck you're solving, or the idea you want to explore. Our team will review your requirements and respond within 24 hours.</p><div class="contact-cards-stack">%s%s%s</div></div>
<div class="contact-form-col"><form class="project-form" id="projectForm" novalidate>
<div class="form-grid-2"><div class="form-group"><label for="name">Full Name *</label><input id="name" autocomplete="name" placeholder="Aditya Rajput"><span class="form-error-msg" id="nameErr">Please enter your name.</span></div><div class="form-group"><label for="company">Company / Organization</label><input id="company" autocomplete="organization" placeholder="Your Company Ltd."></div></div>
<div class="form-grid-2"><div class="form-group"><label for="email">Work Email *</label><input id="email" type="email" autocomplete="email" placeholder="name@company.com"><span class="form-error-msg" id="emailErr">Enter a valid email address.</span></div><div class="form-group"><label for="phone">Phone Number *</label><input id="phone" type="tel" autocomplete="tel" placeholder="+91 98765 43210"><span class="form-error-msg" id="phoneErr">Enter a valid phone number.</span></div></div>
<div class="form-grid-2"><div class="form-group"><label for="service">Service of Interest *</label><select id="service"><option value="">Select a service</option>%s</select><span class="form-error-msg" id="serviceErr">Please select a service.</span></div><div class="form-group"><label for="budget">Estimated Budget</label><select id="budget"><option value="">Select (optional)</option>%s</select></div></div>
<div class="form-group"><label for="details">Project Description *</label><textarea id="details" rows="4" placeholder="Briefly describe your objectives, timeline, or current challenges..."></textarea><span class="form-error-msg" id="detailsErr">Please describe your project (minimum 10 characters).</span></div>
<div class="form-group"><label for="contactMethod">Preferred Contact Channel</label><select id="contactMethod"><option value="">No preference</option><option>Email</option><option>Phone</option><option>WhatsApp</option></select></div>
<input class="hp" id="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="form-consent-wrap"><input type="checkbox" id="consent"><label for="consent">I agree to the processing of my enquiry and have read the <a href="/privacy-policy" style="color:var(--cyan);text-decoration:underline">Privacy Policy</a>.</label></div><span class="form-error-msg" id="consentErr">Please accept the policy to continue.</span>
<div class="form-msg" id="formMsg" role="status" aria-live="polite"></div>
<button type="submit" class="form-submit-btn" id="formSubmitBtn"><span class="btn-text">Send My Enquiry</span></button></form></div></div></section>''' % (
    card('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-10 6L2 7"/>', 'Email', EMAIL, 'mailto:' + EMAIL),
    card('<path d="M22 16.9v3a2 2 0 0 1-2.2 2A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>', 'Phone', PHONE, 'tel:' + PHONE.replace(' ', '')),
    card('<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>', 'Registered Office', ADDR),
    opt(['Website Development', 'Mobile App Development', 'AI & Automation', 'Custom Software / CRM', 'Digital Marketing', 'IT Consulting', 'Other']),
    opt(['Under ₹50,000', '₹50,000 – ₹1,50,000', '₹1,50,000 – ₹5,00,000', 'Above ₹5,00,000', 'Flexible / Not Sure'])
)

P['contact'] = ('Contact ZAQSA | Get a Free Consultation', 'Contact ZAQSA Tech and Solutions in New Delhi to discuss your custom website, application, AI automation or software project.', form)

def legal(h, secs):
    return '<main class="wrap"><div class="legal">' + ''.join('<h3>%s</h3><p>%s</p>' % x for x in secs) + '</div></main>'

P['privacy-policy'] = (
    'Privacy Policy | ZAQSA',
    'How ZAQSA collects, uses and protects information submitted through this website.',
    ph('LEGAL DISCLOSURE', 'Privacy Policy', 'Last updated: November 2026') + legal('', [
        ('Information We Collect', 'When you submit an enquiry through our contact form, we collect your full name, email address, phone number, company name, service interest, budget estimates, and project description.'),
        ('How We Use Your Information', 'We use the collected information exclusively to respond to your project requirements, prepare custom technical and commercial proposals, and coordinate project consultations.'),
        ('Storage and Data Security', 'Your submitted data is stored securely on protected servers with strict access controls. We adhere to industry best practices and never sell, lease, or monetize your contact details.'),
        ('Cookies and Analytics', 'We may use essential session cookies and aggregated analytics to measure performance, uptime, and user navigation patterns on our web pages.'),
        ('Data Retention and Your Rights', 'We retain customer enquiry data as long as necessary to fulfill project proposals and commercial obligations. You have the right to request access to, correction of, or deletion of your information by contacting %s.' % EMAIL)
    ])
)

P['terms-and-conditions'] = (
    'Terms & Conditions | ZAQSA',
    'Terms governing the use of the ZAQSA website and client enquiries.',
    ph('LEGAL DISCLOSURE', 'Terms & Conditions', 'Last updated: November 2026') + legal('', [
        ('Acceptance of Terms', 'By accessing or browsing this website, you agree to comply with and be bound by these Terms and Conditions and our Privacy Policy.'),
        ('Intellectual Property', 'All content, branding, designs, code, graphics, and proprietary methodologies displayed on this website are the intellectual property of ZAQSA Tech and Solutions Private Limited unless stated otherwise.'),
        ('Informational Purpose Only', 'Service descriptions, case references, and technical outlines presented on this website are informational. Specific project scope, timelines, deliverables, and service levels are defined strictly in executed Master Services Agreements or Statements of Work.'),
        ('Limitation of Liability', 'ZAQSA Tech and Solutions shall not be liable for any indirect, incidental, or consequential damages resulting from the use or inability to use the materials on this website.')
    ])
)

NAV = [
    ('Home', '/'),
    ('About Us', '/about'),
    ('Services', '/services'),
    ('Solutions', '/solutions'),
    ('Technologies', '/technologies'),
    ('Our Process', '/process'),
    ('Contact', '/contact')
]

def layout(r, t, d, body):
    u = SITE + ('/' + r if r else '/')
    ld = '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "ZAQSA Tech and Solutions Private Limited",
        "url": SITE,
        "email": EMAIL,
        "telephone": PHONE
    })
    nav = '<nav class="top-nav" id="topNav"><div class="nav-inner"><a href="/" class="nav-logo" aria-label="ZAQSA home"><img class="logo-img" src="/assets/logo.png" alt="ZAQSA"></a><div class="nav-links-wrap" id="navLinksWrap"><div class="nav-indicator" id="navIndicator"></div><div class="nav-links" id="navLinks">%s</div></div><div class="nav-actions"><a class="contact-pill-btn magnetic" href="/contact">Get a Free Consultation</a><button type="button" class="menu-toggle" id="menuToggle" aria-label="Toggle menu"><span></span><span></span><span></span></button></div></div></nav>' % ''.join('<a class="nav-item" href="%s">%s</a>' % (h, n) for n, h in NAV)
    mob = '<div class="mobile-nav" id="mobileNav" aria-hidden="true"><div class="mobile-nav-inner">%s<a class="mobile-contact-pill" href="/contact">Get a Free Consultation</a></div></div>' % ''.join('<a class="mobile-item" href="%s">%s</a>' % (h, n) for n, h in NAV)
    ft = '<footer class="site"><div class="fgrid"><div><img src="/assets/logo.png" alt="ZAQSA" style="height:36px;margin-bottom:1rem"><p>ZAQSA builds intelligent, scalable and user-centric digital solutions. Engineering Ideas. Empowering Businesses.</p></div><div><h4>Quick Links</h4>%s</div><div><h4>Services</h4>%s</div><div><h4>Direct Contact</h4><a href="mailto:%s">%s</a><a href="tel:%s">%s</a><p>%s</p><a href="/privacy-policy">Privacy Policy</a><a href="/terms-and-conditions">Terms & Conditions</a></div></div><div class="fcopy">© 2026 ZAQSA Tech and Solutions Private Limited. All Rights Reserved.</div></footer>' % (''.join('<a href="%s">%s</a>' % (h, n) for n, h in NAV), ''.join('<a href="/services/%s">%s</a>' % (s[0], s[1]) for s in SV), EMAIL, EMAIL, PHONE.replace(' ', ''), PHONE, ADDR)
    return '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:type" content="website"><meta name="twitter:card" content="summary"><link rel="icon" href="/assets/favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="/assets/site.css">%s<noscript><style>.solution-card,.tech-cat-card,.step,.pt,.contact-info-col,.contact-form-col{opacity:1!important;transform:none!important}.pt img{clip-path:none!important}.pi{translate:none!important}</style></noscript></head><body><div class="bg" aria-hidden="true"></div><div class="prog" id="prog"></div>%s%s%s%s<script src="/assets/site.js"></script></body></html>' % (t, d, u, t, d, u, ld if r == '' else '', nav, mob, body, ft)

for r, (t, d, b) in P.items():
    p_dir = os.path.join(O, 'public', r)
    os.makedirs(p_dir, exist_ok=True)
    open(os.path.join(p_dir, 'index.html'), 'w', encoding='utf-8').write(layout(r, t, d, b))

# Also copy index.html to root for consistency
shutil.copy2(os.path.join(O, 'public', 'index.html'), os.path.join(O, 'index.html'))

open(os.path.join(O, 'public', 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join('<url><loc>%s/%s</loc></url>' % (SITE, r) for r in P) + '</urlset>')
open(os.path.join(O, 'public', 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /admin\nDisallow: /api/\nSitemap: %s/sitemap.xml\n' % SITE)
print(len(P), 'pages compiled successfully.')
