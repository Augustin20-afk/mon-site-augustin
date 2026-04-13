# sections/parcours_section.py

import streamlit as st
from components.photo import get_image_base64
from config.settings import (
    PHOTO_PATH,
    PHOTO_CAMPING,
    COLOPLAST_LOGO,
)


def _img_circle(path: str, size: int = 80) -> str:
    b64 = get_image_base64(path)
    if not b64:
        return ""
    ext = path.split(".")[-1].lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    return f"""
    <img src="data:image/{mime};base64,{b64}"
         style="width:{size}px;height:{size}px;object-fit:cover;
                border-radius:50%;border:3px solid #2563eb;
                box-shadow:0 4px 16px rgba(37,99,235,0.2);"
         alt="">
    """


def _logo(path: str) -> str:
    b64 = get_image_base64(path)
    if not b64:
        return ""
    return f'<img src="data:image/png;base64,{b64}" style="height:40px;width:auto;object-fit:contain;" alt="logo">'


def render_parcours() -> None:
    """Affiche le flow chart parcours en pleine page."""

    # Bouton retour
    st.markdown(
        """
        <style>
        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
            font-weight: 600;
            color: #0f172a;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            margin-bottom: 2rem;
            transition: all 0.2s ease;
        }
        .back-btn:hover { background: #f1f5f9; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button("← Retour au site", key="back_btn"):
        st.session_state.show_parcours = False
        st.rerun()

    # Titre
    st.markdown(
        """
        <div style="text-align:center;padding:1rem 2rem 3rem 2rem;max-width:800px;margin:0 auto;">
            <span class="section-tag">Flow Chart</span>
            <h1 style="font-size:2.2rem;font-weight:700;color:#0f172a;margin:0.8rem 0 0.5rem 0;">
                Comment je me suis construit
            </h1>
            <p style="font-size:1rem;color:#64748b;line-height:1.7;">
                Au-delà d'un parcours linéaire, voici les étapes, les environnements et les expériences
                qui ont façonné ma manière de travailler, d'avancer et de me projeter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Étapes
    steps = [
        {
            "num": "01",
            "visual": _img_circle(PHOTO_PATH, 80),
            "tag": "profil · énergie · action",
            "title": "Qui je suis aujourd'hui",
            "text": "Étudiant, engagé sur le terrain, curieux, impliqué et tourné vers l'action. Un profil qui avance avec énergie, méthode et envie de construire.",
            "tags": ["profil", "énergie", "action"],
            "color": "#2563eb",
        },
        {
            "num": "02",
            "visual": _img_circle(PHOTO_CAMPING, 80),
            "tag": "famille · terrain · rigueur",
            "title": "Mes bases",
            "text": "Le sens du travail, l'esprit de famille, le terrain, l'autonomie et le goût des choses concrètes ont beaucoup construit ma manière d'avancer.",
            "tags": ["famille", "terrain", "rigueur", "simplicité", "implication"],
            "color": "#16a34a",
        },
        {
            "num": "03",
            "visual": '<div style="width:80px;height:80px;border-radius:50%;background:#eff6ff;border:3px solid #2563eb;display:flex;align-items:center;justify-content:center;font-size:2rem;">🎯</div>',
            "tag": "business · concret · progression",
            "title": "Mon orientation",
            "text": "Au fil de mes études, j'ai compris que j'aimais les environnements dynamiques, concrets et transverses, où il faut comprendre vite, s'adapter, structurer et faire avancer les sujets.",
            "tags": ["business", "concret", "progression"],
            "color": "#7c3aed",
        },
        {
            "num": "04",
            "visual": _logo(COLOPLAST_LOGO),
            "tag": "achats · projets · coordination",
            "title": "Le terrain professionnel",
            "text": "Mon expérience chez Coloplast a marqué une étape clé. J'y évolue dans un environnement exigeant, au croisement des achats, des projets et de la coordination transverse.",
            "tags": ["achats projets", "coordination", "exigence", "progression", "concret"],
            "color": "#0077b5",
        },
        {
            "num": "05",
            "visual": '<div style="width:80px;height:80px;border-radius:50%;background:#f0fdf4;border:3px solid #16a34a;display:flex;align-items:center;justify-content:center;font-size:2rem;">🌍</div>',
            "tag": "audit · Compamed · international",
            "title": "Expériences qui m'ont façonné",
            "text": "Audit fournisseur en Pologne, présence au salon Compamed, échanges avec des fournisseurs et environnements internationaux : autant d'expériences qui ont renforcé ma maturité professionnelle et mon ouverture.",
            "tags": ["audit", "Compamed
