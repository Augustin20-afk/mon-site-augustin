# sections/experiences_section.py

import streamlit as st


def render_experiences() -> None:
    """Affiche la section Expériences marquantes."""

    st.markdown('<div class="experiences-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Expériences marquantes</span>
            <h2 class="section-title">Des expériences qui m'ont marqué</h2>
            <p class="section-desc">
                Certaines expériences confirment une manière d'être : aller voir sur le terrain,
                comprendre par soi-même et apprendre au contact d'environnements exigeants.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="exp-grid">
            <div class="exp-card">
                <div class="exp-card-top">
                    <span class="exp-icon"></span>
                    <span class="exp-tag">Terrain · International</span>
                </div>
                <h3 class="exp-title">Audit fournisseur à l'étranger</h3>
                <p class="exp-text">
                    Participer à un audit fournisseur à l'étranger a été une expérience
                    particulièrement formatrice. Ce type de mission demande préparation,
                    rigueur, observation et capacité d'adaptation dans un environnement
                    technique et qualité exigeant. Une expérience qui renforce la crédibilité,
                    le sens du détail et la vision concrète du terrain industriel.
                </p>
            </div>
            <div class="exp-card">
                <div class="exp-card-top">
                    <span class="exp-icon">🇩🇪</span>
                    <span class="exp-tag">International · Marché</span>
                </div>
                <h3 class="exp-title">Salon Compamed — Düsseldorf</h3>
                <p class="exp-text">
                    La participation au salon Compamed m'a permis d'échanger avec différents
                    acteurs du secteur, d'ouvrir ma vision marché et de renforcer ma
                    compréhension des dynamiques industrielles et fournisseurs à l'international.
                    Curiosité, posture professionnelle et sens du relationnel font ici toute
                    la différence.
                </p>
            </div>
        </div>

        <div class="exp-conclusion">
            <span class="exp-conclusion-icon">💡</span>
            <p>
                Être exposé à ce type de contexte me motive particulièrement : aller sur le terrain,
                observer, questionner, analyser et revenir avec une vision plus claire,
                plus concrète et plus utile.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
