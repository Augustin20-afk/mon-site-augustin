# sections/footer.py

import streamlit as st
from config.settings import LINKEDIN_URL, EMAIL, CV_PATH
from core.helpers import get_file_as_base64


def render_footer() -> None:
    """Affiche le footer du site."""

    st.markdown('<div class="footer-wrapper">', unsafe_allow_html=True)

    # --- Séparateur ---
    st.markdown('<div class="footer-divider"></div>', unsafe_allow_html=True)

    # --- Message final ---
    st.markdown(
        """
        <div class="footer-content">
            <h2 class="footer-title">Travaillons ensemble.</h2>
            <p class="footer-desc">
                Une opportunité, un projet, une idée à explorer ?<br>
                Je suis toujours partant pour une bonne conversation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Boutons contact ---
    cv_b64 = get_file_as_base64(CV_PATH)
    cv_button = (
        f'<a href="data:application/pdf;base64,{cv_b64}" '
        f'download="CV_Augustin.pdf" class="footer-btn btn-cv">Télécharger mon CV</a>'
        if cv_b64
        else '<span class="footer-btn btn-disabled">CV bientôt dispo</span>'
    )

    st.markdown(
        f"""
        <div class="footer-buttons">
            <a href="mailto:{EMAIL}" class="footer-btn btn-mail">
                ✉️ {EMAIL}
            </a>
            <a href="{LINKEDIN_URL}" target="_blank" class="footer-btn btn-linkedin">
                LinkedIn
            </a>
            {cv_button}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Signature finale ---
    st.markdown(
        """
        <div class="footer-signature">
            Augustin Leclercq · Fait avec Python & Streamlit · 2025
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('</div>', unsafe_allow_html=True)
