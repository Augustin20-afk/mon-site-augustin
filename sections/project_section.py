# sections/project_section.py

import streamlit as st
import streamlit.components.v1 as components
from components.photo import get_image_base64


PROJECTS = [
    {
        "icon": "⚙️",
        "tag": "Achats Industriels",
        "title": "Automatisation Packaging",
        "desc": "Analyse d'un projet d'automatisation industrielle autour d'une machine de packaging, avec travail sur le process, le cadrage du besoin et l'évaluation de solutions techniques.",
        "skill": "Gestion de projet industriel",
        "color": "#3b82f6",
        "logo": "assets/images/coloplast.png",
    },
    {
        "icon": "🤝",
        "tag": "Sourcing Stratégique",
        "title": "Achats Stratégiques & Transformation",
        "desc": "Contribution à plusieurs projets achats à fort impact : changement de fournisseurs, évolution de composants et accompagnement de projets de transformation.",
        "skill": "Sourcing & négociation",
        "color": "#8b5cf6",
        "logo": "assets/images/coloplast.png",
    },
    {
        "icon": "📊",
        "tag": "Python · Streamlit",
        "title": "Forex News Intelligence Tool",
        "desc": "Développement d'un outil de veille marché permettant de trier et prioriser l'information financière utile pour un usage trading.",
        "skill": "Python / Streamlit",
        "color": "#10b981",
        "logo": "",
    },
    {
        "icon": "📈",
        "tag": "Analyse & Pilotage",
        "title": "Dashboards & Business Analysis",
        "desc": "Création d'outils d'analyse et de tableaux de bord pour rendre les décisions plus rapides, plus lisibles et plus structurées.",
        "skill": "Excel · Analyse stratégique",
        "color": "#f59e0b",
        "logo": "",
    },
]


def render_projects() -> None:
    """Affiche la section Projets."""

    st.markdown(
        """
        <div class="section-header" style="padding: 3rem 2rem 1rem 2rem; max-width:960px; margin:0 auto; text-align:center;">
            <span class="section-tag">Projets</span>
            <h2 class="section-title">Ce que je construis</h2>
            <p class="section-desc">
                Des projets concrets, à l'intersection du terrain, de l'analyse et de l'ambition.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Construire les cards
    cards_left = ""
    cards_right = ""

    for i, project in enumerate(PROJECTS):
        logo_html = ""
        if project.get("logo"):
            b64 = get_image_base64(project["logo"])
            if b64:
                logo_html = f'<img src="data:image/png;base64,{b64}" style="height:22px;width:auto;margin-left:auto;object-fit:contain;opacity:0.85;" alt="logo">'

        desc = project["desc"].replace("'", "\\'")
        title = project["title"]

        card = f"""
        <div style="
            background: rgba(255,255,255,0.92);
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 1.6rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.05);
        ">
            <div style="display:flex;align-items:center;gap:0.7rem;margin-bottom:0.8rem;">
                <span style="font-size:1.4rem;">{project["icon"]}</span>
                <span style="
                    font-size:0.75rem;font-weight:700;letter-spacing:0.08em;
                    text-transform:uppercase;padding:0.25rem 0.7rem;border-radius:999px;
                    color:{project["color"]};background:{project["color"]}18;
                ">{project["tag"]}</span>
                {logo_html}
            </div>
            <h3 style="font-size:1.05rem;font-weight:700;color:#0f172a;margin-bottom:0.5rem;">{title}</h3>
            <p style="font-size:0.9rem;color:#475569;line-height:1.65;margin-bottom:1rem;">{project["desc"]}</p>
            <div style="display:flex;align-items:center;gap:0.5rem;padding-top:0.8rem;border-top:1px solid #f1f5f9;">
                <span style="font-size:0.75rem;color:#94a3b8;text-transform:uppercase;letter-spacing:0.08em;">Compétence clé</span>
                <span style="font-size:0.82rem;font-weight:600;color:#334155;">{project["skill"]}</span>
            </div>
        </div>
        """

        if i % 2 == 0:
            cards_left += card
        else:
            cards_right += card

    html = f"""
    <div style="
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:1.2rem;
        max-width:960px;
        margin:0 auto;
        padding:0 2rem 3rem 2rem;
        font-family: 'Inter', sans-serif;
    ">
        <div>{cards_left}</div>
        <div>{cards_right}</div>
    </div>
    """

    components.html(html, height=750, scrolling=False)
