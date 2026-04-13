# sections/current_section.py

import streamlit as st
from components.photo import get_image_base64
from config.settings import COLOPLAST_LOGO


def render_current() -> None:
    """Affiche la section alternance actuelle."""

    st.markdown('<div class="current-wrapper">', unsafe_allow_html=True)

    logo_html = ""
    b64 = get_image_base64(COLOPLAST_LOGO)
    if b64:
        logo_html = f'<img src="data:image/png;base64,{b64}" class="current-logo" alt="Coloplast">'

    st.markdown(
        f"""
        <div class="section-header">
            <span class="section-tag">Aujourd'hui</span>
            <h2 class="section-title">Ce que je fais aujourd'hui</h2>
        </div>

        <div class="current-card">
            <div class="current-card-header">
                {logo_html}
                <div class="current-card-meta">
                    <h3 class="current-company">Coloplast</h3>
                    <p class="current-role">Alternant Acheteur Projet</p>
                </div>
            </div>

            <div class="current-card-body">
                <p class="current-text">
                    J'évolue chez Coloplast dans un environnement exigeant, au croisement des achats,
                    des projets et de la coordination transverse. Cette expérience me permet de travailler
                    sur des sujets concrets, d'interagir avec plusieurs interlocuteurs, et de développer
                    une manière de travailler fondée sur la rigueur, l'adaptation et le sens du collectif.
                </p>
                <p class="current-text">
                    Au quotidien, j'apprends à structurer, suivre, relancer, analyser et faire avancer
                    des sujets avec sérieux. C'est ce terrain qui m'a donné le goût des environnements
                    où l'on construit vraiment.
                </p>
            </div>

            <div class="current-tags">
                <span class="current-tag">⚙️ Achats projets</span>
                <span class="current-tag">🤝 Coordination transverse</span>
                <span class="current-tag">📊 Analyse & structuration</span>
                <span class="current-tag">🌍 Environnement international</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
