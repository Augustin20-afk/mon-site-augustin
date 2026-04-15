# sections/navbar_section.py

import streamlit as st


def render_navbar() -> None:
    """Affiche la barre de navigation fixe et le grand titre."""
    st.markdown(
    """
    <nav class="navbar">
        <span class="navbar-brand">
            Le Site Web d'<span>Augustin Leclercq</span>
        </span>
        <div class="navbar-links">
            <a href="#accueil" class="navbar-link" onclick="document.getElementById('accueil').scrollIntoView({behavior:'smooth'});return false;">Accueil</a>
            <a href="#apropos" class="navbar-link" onclick="document.getElementById('apropos').scrollIntoView({behavior:'smooth'});return false;">À propos</a>
            <a href="#experiences" class="navbar-link" onclick="document.getElementById('experiences').scrollIntoView({behavior:'smooth'});return false;">Expériences</a>
            <a href="#projets" class="navbar-link" onclick="document.getElementById('projets').scrollIntoView({behavior:'smooth'});return false;">Projets</a>
            <a href="#quiz" class="navbar-link" onclick="document.getElementById('quiz').scrollIntoView({behavior:'smooth'});return false;">Quiz</a>
            <a href="#contact" class="navbar-link" onclick="document.getElementById('contact').scrollIntoView({behavior:'smooth'});return false;">Contact</a>
        </div>
    </nav>
    <div class="page-title-wrapper">
        <h1 class="page-title-main">
            Le Site Web d'<span>Augustin Leclercq</span>
        </h1>
        <p class="page-title-sub">Rigueur · Terrain · Ambition</p>
    </div>
    """,
    unsafe_allow_html=True,
)
