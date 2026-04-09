# sections/work_style_section.py

import streamlit as st


def render_work_style() -> None:
    """Affiche la section Manière de travailler."""

    st.markdown('<div class="work-style-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Méthode</span>
            <h2 class="section-title">Une manière de travailler fondée sur la rigueur</h2>
            <p class="section-desc">
                Ce que j'essaie d'apporter au quotidien, c'est une implication réelle,
                de la fiabilité et une vraie exigence dans l'exécution.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="work-style-grid">
            <div class="work-style-card">
                <div class="work-style-icon">⚙️</div>
                <h3 class="work-style-title">Rigueur</h3>
                <p class="work-style-text">J'aime les sujets cadrés, suivis et structurés. La qualité de l'exécution compte autant que la vision.</p>
            </div>
            <div class="work-style-card">
                <div class="work-style-icon">🔥</div>
                <h3 class="work-style-title">Implication</h3>
                <p class="work-style-text">Je m'investis pleinement quand un sujet a du sens. L'engagement n'est pas une option, c'est une manière d'être.</p>
            </div>
            <div class="work-style-card">
                <div class="work-style-icon">🤝</div>
                <h3 class="work-style-title">Fiabilité</h3>
                <p class="work-style-text">Je veux être quelqu'un sur qui l'on peut compter. Tenir ses engagements, aller au bout des choses, rester présent.</p>
            </div>
            <div class="work-style-card">
                <div class="work-style-icon">📈</div>
                <h3 class="work-style-title">Progression</h3>
                <p class="work-style-text">J'apprends vite et je cherche à m'améliorer en continu. Chaque sujet est une opportunité de comprendre mieux et de faire mieux.</p>
            </div>
        </div>

        <div class="work-style-quote">
            "J'aime les environnements exigeants, les sujets concrets et les projets
            qui demandent de vraiment s'impliquer."
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
