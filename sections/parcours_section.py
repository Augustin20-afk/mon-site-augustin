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
    return (
        f'<img src="data:image/{mime};base64,{b64}"'
        f' style="width:{size}px;height:{size}px;object-fit:cover;'
        f'border-radius:50%;border:3px solid #2563eb;'
        f'box-shadow:0 4px 16px rgba(37,99,235,0.2);" alt="">'
    )


def _logo(path: str) -> str:
    b64 = get_image_base64(path)
    if not b64:
        return ""
    return (
        f'<img src="data:image/png;base64,{b64}"'
        f' style="height:40px;width:auto;object-fit:contain;" alt="logo">'
    )


def render_parcours() -> None:
    """Affiche le flow chart parcours en pleine page."""

    st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

    if st.button("← Retour au site", key="back_btn"):
        st.session_state.show_parcours = False
        st.rerun()

    st.markdown(
        """
        ...
        """,
        unsafe_allow_html=True,
    )
    steps = [
        {
            "num": "01",
            "visual": _img_circle(PHOTO_PATH, 80),
            "title": "Qui je suis aujourd'hui",
            "text": (
                "Étudiant, engagé sur le terrain, curieux, impliqué et tourné vers l'action. "
                "Un profil qui avance avec énergie, méthode et envie de construire."
            ),
            "tags": ["profil", "énergie", "action"],
            "color": "#2563eb",
        },
        {
            "num": "02",
            "visual": _img_circle(PHOTO_CAMPING, 80),
            "title": "Mes bases",
            "text": (
                "Le sens du travail, l'esprit de famille, le terrain, l'autonomie "
                "et le goût des choses concrètes ont beaucoup construit ma manière d'avancer."
            ),
            "tags": ["famille", "terrain", "rigueur", "simplicité", "implication"],
            "color": "#16a34a",
        },
        {
            "num": "03",
            "visual": (
                '<div style="width:80px;height:80px;border-radius:50%;'
                'background:#eff6ff;border:3px solid #2563eb;'
                'display:flex;align-items:center;justify-content:center;'
                'font-size:2rem;">🎯</div>'
            ),
            "title": "Mon orientation",
            "text": (
                "Au fil de mes études, j'ai compris que j'aimais les environnements "
                "dynamiques, concrets et transverses, où il faut comprendre vite, "
                "s'adapter, structurer et faire avancer les sujets."
            ),
            "tags": ["business", "concret", "progression"],
            "color": "#7c3aed",
        },
        {
            "num": "04",
            "visual": _logo(COLOPLAST_LOGO),
            "title": "Le terrain professionnel",
            "text": (
                "Mon expérience chez Coloplast a marqué une étape clé. J'y évolue "
                "dans un environnement exigeant, au croisement des achats, des projets "
                "et de la coordination transverse."
            ),
            "tags": ["achats projets", "coordination", "exigence", "progression"],
            "color": "#0077b5",
        },
        {
            "num": "05",
            "visual": (
                '<div style="width:80px;height:80px;border-radius:50%;'
                'background:#f0fdf4;border:3px solid #16a34a;'
                'display:flex;align-items:center;justify-content:center;'
                'font-size:2rem;">🌍</div>'
            ),
            "title": "Expériences qui m'ont façonné",
            "text": (
                "Audit fournisseur en Pologne, présence au salon Compamed, "
                "échanges avec des fournisseurs et environnements internationaux : "
                "autant d'expériences qui ont renforcé ma maturité professionnelle "
                "et mon ouverture."
            ),
            "tags": ["audit", "Compamed", "international"],
            "color": "#16a34a",
        },
        {
            "num": "06",
            "visual": (
                '<div style="width:80px;height:80px;border-radius:50%;'
                'background:#fef3c7;border:3px solid #f59e0b;'
                'display:flex;align-items:center;justify-content:center;'
                'font-size:2rem;">🚀</div>'
            ),
            "title": "Ce que je recherche maintenant",
            "text": (
                "Aujourd'hui, je recherche une alternance à partir de septembre 2026, "
                "dans un environnement ambitieux, formateur et stimulant, "
                "où je pourrai continuer à apprendre, m'investir pleinement "
                "et contribuer concrètement."
            ),
            "tags": ["alternance", "ambition", "suite"],
            "color": "#f59e0b",
        },
    ]

    for i, step in enumerate(steps):
        tags_html = "".join([
            f'<span style="background:{step["color"]}18;color:{step["color"]};'
            f'font-size:0.75rem;font-weight:600;padding:0.25rem 0.7rem;'
            f'border-radius:999px;">{t}</span>'
            for t in step["tags"]
        ])

        connector = ""
        if i < len(steps) - 1:
            next_color = steps[i + 1]["color"]
            connector = (
                f'<div style="display:flex;justify-content:center;margin:0;">'
                f'<div style="width:3px;height:40px;'
                f'background:linear-gradient({step["color"]},{next_color});'
                f'border-radius:2px;"></div></div>'
            )

        st.markdown(
            f"""
            <div style="max-width:700px;margin:0 auto;
                        background:#ffffff;border:1px solid #e2e8f0;
                        border-left:5px solid {step["color"]};
                        border-radius:16px;padding:1.8rem;
                        box-shadow:0 4px 16px rgba(0,0,0,0.05);">
                <div style="display:flex;align-items:center;gap:1.5rem;">
                    <div style="flex-shrink:0;">{step["visual"]}</div>
                    <div style="flex:1;">
                        <div style="display:flex;align-items:center;
                                    gap:0.8rem;margin-bottom:0.5rem;">
                            <span style="font-size:0.75rem;font-weight:800;
                                         color:{step["color"]};
                                         background:{step["color"]}18;
                                         padding:0.2rem 0.6rem;border-radius:6px;
                                         letter-spacing:0.1em;">{step["num"]}</span>
                        </div>
                        <h3 style="font-size:1.1rem;font-weight:700;
                                   color:#0f172a;margin-bottom:0.5rem;">
                            {step["title"]}
                        </h3>
                        <p style="font-size:0.9rem;color:#475569;
                                  line-height:1.65;margin-bottom:0.8rem;">
                            {step["text"]}
                        </p>
                        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">
                            {tags_html}
                        </div>
                    </div>
                </div>
            </div>
            {connector}
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="max-width:700px;margin:2rem auto 3rem auto;text-align:center;
                    font-style:italic;font-size:1rem;color:#334155;
                    padding:1.5rem 2rem;background:rgba(255,255,255,0.8);
                    border-left:4px solid #2563eb;border-radius:0 12px 12px 0;">
            "Construire la suite avec sérieux, énergie et envie."
        </div>
        """,
        unsafe_allow_html=True,
    )
