# sections/vision_section.py

import streamlit as st


def render_vision() -> None:
    """Affiche la section Ma vision."""

    st.markdown('<div class="vision-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Ma vision</span>
            <h2 class="section-title">La valeur se construit sur le terrain</h2>
        </div>

        <div class="vision-content">
            <p class="vision-text">
                Je crois aux profils capables d'allier <strong>rigueur, énergie et bon sens terrain</strong>.
                Dans un monde où tout va vite, la différence se fait souvent dans la qualité
                de l'implication, la capacité à comprendre concrètement les enjeux et la volonté
                de faire avancer les choses proprement.
            </p>
            <p class="vision-text">
                Mon ambition est de continuer à grandir sur des <strong>projets à impact</strong>,
                avec une forte exigence de travail, une ouverture internationale et une envie
                constante d'apprendre et de contribuer.
            </p>
            <div class="vision-quote">
                "Le terrain m'a appris une chose simple : la valeur ne se raconte pas,
                elle se construit."
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
