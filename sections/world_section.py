# sections/world_section.py

import streamlit as st
from components.photo import get_image_base64
from config.settings import (
    PHOTO_RUNNER,
    PHOTO_VIBES,
    PHOTO_CAMPING,
    PHOTO_TENT,
    PHOTO_NATURE,
    PHOTO_DOG,
)


def _img(path: str, css_class: str = "world-photo", alt: str = "") -> str:
    b64 = get_image_base64(path)
    if not b64:
        return ""
    ext = path.split(".")[-1].lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    return f'<img src="data:image/{mime};base64,{b64}" class="{css_class}" alt="{alt}">'


def render_world() -> None:
    """Affiche la section Mon monde."""

    st.markdown('<div class="world-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Mon monde</span>
            <h2 class="section-title">Au-delà du profil : ce qui me construit</h2>
<p class="section-desc">Une énergie forgée par le terrain, la famille, le sport et l'envie constante d'avancer.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="identity-pills">
         <span class="identity-pill">🌍 Terrain</span>
<span class="identity-pill">⚡ Rigueur</span>
<span class="identity-pill">🎯 Ambition</span>
<span class="identity-pill">🤝 Engagement</span>
<span class="identity-pill">🔍 Curiosité</span>
<span class="identity-pill">🔥 Énergie</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Ligne 1 : Sport + Camping ---
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            f"""
            <div class="world-card world-card-photo">
                {_img(PHOTO_RUNNER, "world-photo", "Marathon Barcelone")}
                <div class="world-card-overlay">
                    <span class="world-card-overlay-icon">⚽</span>
                   <h3 class="world-card-title">Le sport, école d'exigence</h3>
<p class="world-card-text">
    Marathon de Barcelone, marathon du Médoc déguisé, pratique régulière —
    au-delà de l'effort, j'y retrouve une logique qui me ressemble :
    discipline, constance, dépassement de soi et capacité à garder le cap.
</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="world-card world-card-photo">
                {_img(PHOTO_CAMPING, "world-photo", "Camping")}
                <div class="world-card-overlay">
                    <span class="world-card-overlay-icon">🏕️</span>
                   <h3 class="world-card-title">Le camping familial, mon premier terrain</h3>
<p class="world-card-text">
    Grandir dans un business familial, c'est comprendre tôt que rien n'avance tout seul.
    Le camping m'a transmis une culture du terrain, du service, de l'énergie et du concret.
    C'est là que s'est construit une partie essentielle de ma façon de travailler aujourd'hui.
</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- Ligne 2 : Good vibes + Chien ---
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        st.markdown(
            f"""
            <div class="world-card world-card-photo">
                {_img(PHOTO_VIBES, "world-photo", "Good vibes")}
                <div class="world-card-overlay">
                    <span class="world-card-overlay-icon">🚀</span>
                    <h3 class="world-card-title">Construire des choses concrètes</h3>
<p class="world-card-text">
    J'ai toujours aimé créer, tester, structurer et faire avancer des projets.
    Du terrain familial aux outils que je développe aujourd'hui, j'aime transformer
    une idée en quelque chose d'utile, lisible et concret.
</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="world-card world-card-photo">
                {_img(PHOTO_DOG, "world-photo", "Mon chien")}
                <div class="world-card-overlay">
                    <span class="world-card-overlay-icon">🐾</span>
                    <h3 class="world-card-title">Voyages, ouverture et recul</h3>
<p class="world-card-text">
    Voyager, c'est sortir de ses repères, observer et apprendre autrement.
    J'y trouve une ouverture qui nourrit ma curiosité et ma façon d'aborder
    les situations : avec adaptabilité, écoute et envie de comprendre plus large.
</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- Citation ---
    st.markdown(
        """
        <div class="world-quote">
    "Le terrain m'a appris une chose simple : la valeur ne se raconte pas, elle se construit."
</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
