# styles/css.py

import streamlit as st

def load_css():
    st.markdown(
        """
        <style>
.stApp {
    background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 40%, #e2e8f0 100%);
    color: #0f172a;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
}

/* reste du CSS... */
        * ── NAVBAR FIXE ──────────────────────────────────────── */
.navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 9999 !important;
    background: rgba(255,255,255,0.97) !important;
    backdrop-filter: blur(10px) !important;
    border-bottom: 1px solid #e2e8f0 !important;
    padding: 0.8rem 2rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
}
.navbar-links a {
    display: inline-block !important;
    visibility: visible !important;
    opacity: 1 !important;
    color: #475569 !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    margin: 0 0.5rem !important;
}

.navbar-brand {
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    text-decoration: none !important;
}

.navbar-brand span {
    color: #2563eb !important;
}

.navbar-links {
    display: flex !important;
    align-items: center !important;
    gap: 1.5rem !important;
}

.navbar-link {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: #475569 !important;
    text-decoration: none !important;
    transition: color 0.2s ease !important;
}

.navbar-link:hover {
    color: #2563eb !important;
    text-decoration: none !important;
}
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }
        /* ── CURRENT SECTION ──────────────────────────────────── */
.current-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}
/* ── BOUTON PARCOURS ──────────────────────────────────── */
div[data-testid="stButton"] button {
    background: #2563eb !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.2rem !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
}

div[data-testid="stButton"] button:hover {
    background: #1d4ed8 !important;
}
.footer-subdesc {
    font-size: 0.95rem;
    color: #64748b;
    line-height: 1.7;
    max-width: 600px;
    margin: 0.8rem auto 0 auto;
}

.current-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #2563eb;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
}

.current-card-header {
    display: flex;
    align-items: center;
    gap: 1.2rem;
    margin-bottom: 1.5rem;
}

.current-logo {
    height: 48px;
    width: auto;
    object-fit: contain;
}

.current-company {
    font-size: 1.3rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.2rem;
}

.current-role {
    font-size: 0.95rem;
    color: #2563eb;
    font-weight: 600;
}

.current-text {
    font-size: 0.95rem;
    color: #334155;
    line-height: 1.75;
    margin-bottom: 1rem;
}

.current-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 1.2rem;
    padding-top: 1.2rem;
    border-top: 1px solid #f1f5f9;
}

.current-tag {
    background: #eff6ff;
    color: #2563eb;
    font-size: 0.82rem;
    font-weight: 600;
    padding: 0.35rem 0.8rem;
    border-radius: 999px;
}
        .hero-box {
            background: rgba(255,255,255,0.78);
            border: 1px solid rgba(255,255,255,0.6);
            backdrop-filter: blur(12px);
            border-radius: 28px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
            height: 100%;
        }
        .small-muted {
            color: #64748b;
            font-size: 0.95rem;
        }
        .pill {
            display: inline-block;
            padding: 0.45rem 0.8rem;
            margin: 0 0.35rem 0.45rem 0;
            background: #ffffff;
            border-radius: 999px;
            font-size: 0.9rem;
            border: 1px solid #e2e8f0;
        }
        /* ── CACHER LES ANCRES ────────────────────────────────── */
div[id="accueil"],
div[id="apropos"],
div[id="experiences"],
div[id="projets"],
div[id="quiz"],
div[id="contact"] {
    display: block;
    height: 0;
    overflow: hidden;
}

a[href^="#"] {
    text-decoration: none !important;
}
/* ── CACHER ICÔNES ANCRES STREAMLIT ──────────────────── */
.world-card-title a,
.section-title a,
h1 a, h2 a, h3 a {
    display: none !important;
}

[data-testid="stMarkdownContainer"] a[href^="#"] {
    display: none !important;
}
        /* ── HERO WRAPPER ─────────────────────────────────────── */
        .hero-wrapper {
            padding: 3rem 2rem 2rem 2rem;
            max-width: 960px;
            margin: 0 auto;
        }

        /* ── PHOTO ────────────────────────────────────────────── */
        .hero-photo-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding-top: 0.5rem;
        }
        .profile-photo {
    width: 260px;
    height: 320px;
    object-fit: cover;
    object-position: center top;
    border-radius: 16px;
    border: 3px solid #e2e8f0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    transition: transform 0.3s ease;
}
        .profile-photo:hover {
            transform: scale(1.03);
        }
        .photo-placeholder {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: #1e2230;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            border: 3px solid #ffffff20;
        }
        
        .hero-tagline {
    font-size: 0.88rem;
    font-weight: 600;
    color: #3b82f6;
    letter-spacing: 0.04em;
    margin-top: 1.2rem;
    font-style: italic;
}
 .btn-parcours {
    background: #2563eb;
    color: #ffffff !important;
}
.btn-parcours:hover { background: #1d4ed8; color: #ffffff !important; }

.btn-linkedin {
    background: #0077b5;
    color: #ffffff !important;
}
.btn-linkedin:hover { background: #005f91; color: #ffffff !important; }

.btn-mail {
    background: #2d3748;
    color: #ffffff !important;
    border: 1px solid #4a5568;
}
.btn-mail:hover { background: #3a4a60; color: #ffffff !important; }

.btn-cv {
    background: #38a169;
    color: #ffffff !important;
}
.btn-cv:hover { background: #2f855a; color: #ffffff !important; }

/* ── TEXTE HERO ───────────────────────────────────────── */
        .hero-title {
            font-size: 2.6rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.4rem;
            line-height: 1.2;
        }
        .hero-subtitle {
            font-size: 1.15rem;
            color: #475569;
            margin-bottom: 1rem;
            font-weight: 400;
            letter-spacing: 0.02em;
        }
        .hero-intro {
            font-size: 0.97rem;
            color: #334155;
            line-height: 1.7;
            margin-bottom: 1.8rem;
            max-width: 520px;
        }
        /* ── PROJECTS GRID ────────────────────────────────────── */
.projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
}

.projects-col {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
}

/* ── WORK STYLE ───────────────────────────────────────── */
.work-style-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}
/* ── NAVBAR FIXE ──────────────────────────────────────── */
.navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 9999 !important;
    background: rgba(255,255,255,0.97) !important;
    backdrop-filter: blur(10px) !important;
    border-bottom: 1px solid #e2e8f0 !important;
    padding: 0.8rem 2rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06) !important;
}

.navbar-brand {
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    text-decoration: none !important;
}

.navbar-brand span {
    color: #2563eb !important;
}

.navbar-links {
    display: flex !important;
    align-items: center !important;
    gap: 1.5rem !important;
}

.navbar-link {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    color: #475569 !important;
    text-decoration: none !important;
    transition: color 0.2s ease !important;
}

.navbar-link:hover {
    color: #2563eb !important;
    text-decoration: none !important;
}

/* ── PAGE TITLE ───────────────────────────────────────── */
.page-title-wrapper {
    text-align: center !important;
    padding: 6rem 2rem 2rem 2rem !important;
    max-width: 960px !important;
    margin: 0 auto !important;
}

.page-title-main {
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    color: #0f172a !important;
    letter-spacing: -0.02em !important;
    line-height: 1.1 !important;
    margin-bottom: 0.6rem !important;
}

.page-title-main span {
    color: #2563eb !important;
}

.page-title-sub {
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: #64748b !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
}

/* Cacher la barre noire Streamlit */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
}

.work-style-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
    margin-bottom: 2rem;
}

.work-style-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-left: 4px solid #2563eb;
    border-radius: 0 12px 12px 0;
    padding: 1.4rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04);
}

.work-style-icon {
    font-size: 1.6rem;
    margin-bottom: 0.6rem;
}

.work-style-title {
    font-size: 1rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.4rem;
}

.work-style-text {
    font-size: 0.88rem;
    color: #475569;
    line-height: 1.6;
}

.work-style-quote {
    text-align: center;
    font-style: italic;
    font-size: 1rem;
    color: #334155;
    padding: 1.5rem 2rem;
    background: rgba(255,255,255,0.7);
    border-left: 4px solid #2563eb;
    border-radius: 0 12px 12px 0;
    max-width: 640px;
    margin: 0 auto;
}

/* ── EXPERIENCES ──────────────────────────────────────── */
.experiences-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}

.exp-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
    margin-bottom: 1.5rem;
}

.exp-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.6rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
}

.exp-card-top {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 0.8rem;
}

.exp-icon { font-size: 1.4rem; }

.exp-tag {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #2563eb;
    background: #eff6ff;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
}

.exp-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.6rem;
}

.exp-text {
    font-size: 0.88rem;
    color: #475569;
    line-height: 1.65;
}

.exp-conclusion {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    background: #eff6ff;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
}

.exp-conclusion-icon { font-size: 1.4rem; }

.exp-conclusion p {
    font-size: 0.9rem;
    color: #1e40af;
    line-height: 1.65;
    font-style: italic;
}

/* ── VISION ───────────────────────────────────────────── */
.vision-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}

.vision-content {
    max-width: 720px;
    margin: 0 auto;
    text-align: center;
}

.vision-text {
    font-size: 1rem;
    color: #334155;
    line-height: 1.8;
    margin-bottom: 1.2rem;
}

.vision-quote {
    font-style: italic;
    font-size: 1.1rem;
    color: #0f172a;
    font-weight: 600;
    padding: 1.5rem 2rem;
    background: rgba(255,255,255,0.8);
    border-left: 4px solid #2563eb;
    border-radius: 0 12px 12px 0;
    text-align: left;
    margin-top: 1.5rem;
}
        /* ── BOUTONS ──────────────────────────────────────────── */
        .hero-buttons {
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
            margin-top: 0.5rem;
        }
        .hero-btn {
            display: inline-block;
            padding: 0.55rem 1.2rem;
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 600;
            text-decoration: none;
            text-align: center;
            transition: all 0.2s ease;
            cursor: pointer;
            white-space: nowrap;
        }
        .btn-linkedin {
            background: #0077b5;
            color: #ffffff;
        }
        .btn-linkedin:hover { background: #005f91; color: #ffffff; }
        .btn-mail {
            background: #2d3748;
            color: #e2e8f0;
            border: 1px solid #4a5568;
        }
        .btn-mail:hover { background: #3a4a60; color: #ffffff; }
        .btn-cv {
            background: #38a169;
            color: #ffffff;
        }
        .btn-cv:hover { background: #2f855a; color: #ffffff; }
        .btn-disabled {
            background: #2d3748;
            color: #718096;
            cursor: default;
            opacity: 0.6;
        }
        /* ── WORLD SECTION ────────────────────────────────────── */
.world-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}

.section-header {
    text-align: center;
    margin-bottom: 2rem;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.section-tag {
    display: inline-block;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #3b82f6;
    background: #eff6ff;
    padding: 0.3rem 0.8rem;
    border-radius: 999px;
    margin-bottom: 0.8rem;
}

.section-title {
    font-size: 2rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.5rem;
}

.section-desc {
    font-size: 1rem;
    color: #64748b;
    max-width: 600px;
    margin: 0 auto;
    text-align: center;
}

/* ── PILLS IDENTITÉ ───────────────────────────────────── */
.identity-pills {
    display: flex;
    justify-content: center;
    gap: 0.8rem;
    flex-wrap: wrap;
    margin-bottom: 2.5rem;
}

.identity-pill {
    display: inline-block;
    padding: 0.5rem 1.1rem;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 999px;
    font-size: 0.9rem;
    font-weight: 600;
    color: #0f172a;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* ── WORLD CARDS ──────────────────────────────────────── */
.world-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.6rem;
    height: 100%;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.world-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.world-card-icon {
    font-size: 2rem;
    margin-bottom: 0.8rem;
}

.world-card-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.6rem;
}

.world-card-text {
    font-size: 0.9rem;
    color: #475569;
    line-height: 1.65;
}

/* ── CITATION ─────────────────────────────────────────── */
.world-quote {
    margin: 2.5rem auto 0 auto;
    max-width: 640px;
    text-align: center;
    font-size: 1.05rem;
    font-style: italic;
    color: #334155;
    padding: 1.5rem 2rem;
    background: rgba(255,255,255,0.7);
    border-left: 4px solid #3b82f6;
    border-radius: 0 12px 12px 0;
}
/* ── PROJECTS SECTION ─────────────────────────────────── */
.projects-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}

.project-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
}

.project-card-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 0.8rem;
}

.project-icon {
    font-size: 1.4rem;
}

.project-tag {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
}

.project-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.5rem;
}

.project-desc {
    font-size: 0.9rem;
    color: #475569;
    line-height: 1.65;
    margin-bottom: 1rem;
}

.project-skill {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding-top: 0.8rem;
    border-top: 1px solid #f1f5f9;
}

.skill-label {
    font-size: 0.75rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.skill-value {
    font-size: 0.82rem;
    font-weight: 600;
    color: #334155;
}
/* ── FOOTER ───────────────────────────────────────────── */
.footer-wrapper {
    padding: 3rem 2rem 2rem 2rem;
    max-width: 960px;
    margin: 0 auto;
}

.footer-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #cbd5e0, transparent);
    margin-bottom: 3rem;
}

.footer-content {
    text-align: center;
    margin-bottom: 2rem;
}

.footer-title {
    font-size: 2rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.8rem;
}

.footer-desc {
    font-size: 1rem;
    color: #64748b;
    line-height: 1.7;
}

.footer-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 3rem;
}

.footer-btn {
    display: inline-block;
    padding: 0.65rem 1.4rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none;
    text-align: center;
    transition: all 0.2s ease;
    cursor: pointer;
    white-space: nowrap;
}

.footer-btn.btn-mail {
    background: #2d3748;
    color: #ffffff !important;
    border: 1px solid #4a5568;
}
.footer-btn.btn-mail:hover { background: #3a4a60; color: #ffffff !important; }

.footer-btn.btn-linkedin {
    background: #0077b5;
    color: #ffffff;
}
.footer-btn.btn-linkedin:hover { background: #005f91; color: #ffffff; }

.footer-btn.btn-cv {
    background: #38a169;
    color: #ffffff;
}
.footer-btn.btn-cv:hover { background: #2f855a; color: #ffffff; }

.footer-btn.btn-disabled {
    background: #f1f5f9;
    color: #94a3b8;
    cursor: default;
    opacity: 0.6;
}

.footer-signature {
    text-align: center;
    font-size: 0.8rem;
    color: #94a3b8;
    padding-bottom: 2rem;
    letter-spacing: 0.04em;
}
/* ── GAME SECTION ─────────────────────────────────────── */
.game-wrapper {
    padding: 3rem 2rem;
    max-width: 960px;
    margin: 0 auto;
    }
    
    /* ── LOGO PROJET ──────────────────────────────────────── */
.project-logo {
    height: 24px;
    width: auto;
    margin-left: auto;
    object-fit: contain;
    opacity: 0.85;

}
/* ── WORLD CARDS AVEC PHOTOS ──────────────────────────── */
.world-card-photo {
    position: relative;
    overflow: hidden;
    border-radius: 16px;
    height: 260px;
    margin-bottom: 1.2rem;
    cursor: default;
}

.world-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
}

.world-card-photo:hover .world-photo {
    transform: scale(1.05);
}

.world-card-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(0deg, rgba(10,15,30,0.85) 0%, rgba(10,15,30,0.3) 70%, transparent 100%);
    padding: 1.2rem;
    color: #ffffff;
}

.world-card-overlay-icon {
    font-size: 1.4rem;
    display: block;
    margin-bottom: 0.3rem;
}

.world-card-overlay .world-card-title {
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.3rem;
}

.world-card-overlay .world-card-text {
    font-size: 0.82rem;
    color: rgba(255,255,255,0.85);
    line-height: 1.5;
}
        </style>
        """,
        unsafe_allow_html=True,
    )
