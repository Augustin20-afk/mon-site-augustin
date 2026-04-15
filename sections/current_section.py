# sections/current_section.py

import streamlit as st
import streamlit.components.v1 as components
from components.photo import get_image_base64
from config.settings import COLOPLAST_LOGO


def render_current() -> None:
    """Affiche la section alternance actuelle."""

    st.markdown(
        """
        <div class="section-header" style="padding: 3rem 2rem 1rem 2rem;
             max-width:960px; margin:0 auto; text-align:center;">
            <span class="section-tag">Aujourd&#39;hui</span>
            <h2 class="section-title">Ce que je fais aujourd&#39;hui</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    logo_html = ""
    b64 = get_image_base64(COLOPLAST_LOGO)
    if b64:
        logo_html = (
            f'<img src="data:image/png;base64,{b64}" '
            f'style="height:48px;width:auto;object-fit:contain;" alt="Coloplast">'
        )

    html = f"""
    <div style="max-width:960px;margin:0 auto;padding:0 2rem 3rem 2rem;
                font-family:'Inter',sans-serif;">
        <div style="background:#ffffff;border:1px solid #e2e8f0;
                    border-left:5px solid #2563eb;border-radius:16px;
                    padding:2rem;box-shadow:0 4px 24px rgba(0,0,0,0.06);">

            <div style="display:flex;align-items:center;gap:1.2rem;margin-bottom:1.5rem;">
                {logo_html}
                <div>
                    <h3 style="font-size:1.3rem;font-weight:700;color:#0f172a;
                               margin-bottom:0.2rem;">Coloplast</h3>
                    <p style="font-size:0.95rem;color:#2563eb;font-weight:600;">
                        Alternant Acheteur Projet
                    </p>
                </div>
            </div>

            <p style="font-size:0.95rem;color:#334155;line-height:1.75;margin-bottom:1rem;">
                J&#39;évolue chez Coloplast dans un environnement exigeant, au croisement des achats,
                des projets et de la coordination transverse. Cette expérience me permet de travailler
                sur des sujets concrets, d&#39;interagir avec plusieurs interlocuteurs, et de développer
                une manière de travailler fondée sur la rigueur, l&#39;adaptation et le sens du collectif.
            </p>
            <p style="font-size:0.95rem;color:#334155;line-height:1.75;margin-bottom:1.5rem;">
                Au quotidien, j&#39;apprends à structurer, suivre, relancer, analyser et faire avancer
                des sujets avec sérieux. C&#39;est ce terrain qui m&#39;a donné le goût des environnements
                où l&#39;on construit vraiment.
            </p>

            <div style="display:flex;flex-wrap:wrap;gap:0.6rem;
                        padding-top:1.2rem;border-top:1px solid #f1f5f9;">
                <span style="background:#eff6ff;color:#2563eb;font-size:0.82rem;
                             font-weight:600;padding:0.35rem 0.8rem;border-radius:999px;">
                    ⚙️ Achats projets
                </span>
                <span style="background:#eff6ff;color:#2563eb;font-size:0.82rem;
                             font-weight:600;padding:0.35rem 0.8rem;border-radius:999px;">
                    🤝 Coordination transverse
                </span>
                <span style="background:#eff6ff;color:#2563eb;font-size:0.82rem;
                             font-weight:600;padding:0.35rem 0.8rem;border-radius:999px;">
                    📊 Analyse &amp; structuration
                </span>
                <span style="background:#eff6ff;color:#2563eb;font-size:0.82rem;
                             font-weight:600;padding:0.35rem 0.8rem;border-radius:999px;">
                    🌍 Environnement international
                </span>
            </div>
        </div>
    </div>
    """

    components.html(html, height=500, scrolling=False)
