# sections/hero.py

import streamlit as st
from components.photo import display_profile_photo
from config.settings import (
    HERO_TITLE,
    HERO_SUBTITLE,
    HERO_INTRO,
    PHOTO_PATH,
    LINKEDIN_URL,
    EMAIL,
    CV_PATH,
)
from core.helpers import get_file_as_base64


def render_hero() -> None:
    """Affiche la section Hero complète."""
    st.markdown('<div id="accueil"></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-wrapper">', unsafe_allow_html=True)
    col_photo, col_text = st.columns([1, 2], gap="large")
    with col_photo:
        st.markdown('<div class="hero-photo-container">', unsafe_allow_html=True)
        display_profile_photo(PHOTO_PATH, css_class="profile-photo")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_text:
        st.markdown(f'<h1 class="hero-title">{HERO_TITLE}</h1>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-subtitle">{HERO_SUBTITLE}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="hero-intro">{HERO_INTRO}</p>', unsafe_allow_html=True)

        st.markdown('<div class="hero-buttons">', unsafe_allow_html=True)
        _render_buttons()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def _render_buttons() -> None:
    cv_b64 = get_file_as_base64(CV_PATH)
    cv_button = (
        f'<a href="data:application/pdf;base64,{cv_b64}" '
        f'download="CV_Augustin.pdf" class="hero-btn btn-cv">Télécharger mon CV</a>'
        if cv_b64
        else ""
    )

    st.markdown(
        f"""
        <div class="hero-buttons">
            <a href="{LINKEDIN_URL}" target="_blank" class="hero-btn btn-linkedin">LinkedIn</a>
            <a href="mailto:{EMAIL}" class="hero-btn btn-mail">📧 augustin.leclercq.ci@gmail.com</a>            {cv_button}
        </div>
        <p class="hero-tagline">
            Rigueur dans le travail. Énergie dans l'action. Humain dans l'approche.
        </p>
        """,
        unsafe_allow_html=True,
    )

    if st.button("📋 Voir mon parcours", key="parcours_btn"):
        st.session_state.show_parcours = True
        st.rerun()
