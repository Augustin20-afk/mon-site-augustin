# sections/footer.py

import streamlit as st
import streamlit.components.v1 as components
from config.settings import LINKEDIN_URL, EMAIL, CV_PATH
from core.helpers import get_file_as_base64


def render_footer() -> None:
    """Affiche le footer du site."""

    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

    cv_b64 = get_file_as_base64(CV_PATH)
    cv_button = (
        f'<a href="data:application/pdf;base64,{cv_b64}" '
        f'download="CV_Augustin.pdf" '
        f'style="display:inline-block;padding:0.65rem 1.4rem;border-radius:8px;'
        f'font-size:0.9rem;font-weight:600;text-decoration:none;'
        f'background:#38a169;color:#ffffff;">Télécharger mon CV</a>'
        if cv_b64
        else ""
    )

    html = f"""
    <div style="max-width:960px;margin:0 auto;padding:3rem 2rem 2rem 2rem;
                font-family:'Inter',sans-serif;">

        <div style="height:1px;background:linear-gradient(90deg,transparent,#cbd5e0,transparent);
                    margin-bottom:3rem;"></div>

        <div style="text-align:center;margin-bottom:2rem;">
            <span style="display:inline-block;font-size:0.78rem;font-weight:700;
                         letter-spacing:0.12em;text-transform:uppercase;color:#3b82f6;
                         background:#eff6ff;padding:0.3rem 0.8rem;border-radius:999px;
                         margin-bottom:0.8rem;">Alternance</span>
            <h2 style="font-size:2rem;font-weight:700;color:#0f172a;margin-bottom:0.8rem;">
                À la recherche d&#39;une alternance à partir de septembre 2026
            </h2>
            <p style="font-size:1rem;color:#64748b;line-height:1.7;max-width:640px;margin:0 auto 0.8rem auto;">
                Je suis actuellement à la recherche d&#39;une alternance dans un environnement
                où je pourrai continuer à apprendre, m&#39;investir pleinement et contribuer concrètement.
                J&#39;avance avec sérieux, curiosité et envie de bien faire.
            </p>
            <p style="font-size:0.95rem;color:#64748b;line-height:1.7;max-width:600px;margin:0 auto;">
                Si mon profil, mon énergie et ma manière de travailler résonnent avec vos attentes,
                je serais ravi d&#39;échanger lors d&#39;un entretien ou d&#39;une vraie conversation.
            </p>
        </div>

        <div style="display:flex;justify-content:center;gap:1rem;flex-wrap:wrap;margin-bottom:3rem;">
            <a href="mailto:{EMAIL}"
               style="display:inline-block;padding:0.65rem 1.4rem;border-radius:8px;
                      font-size:0.9rem;font-weight:600;text-decoration:none;
                      background:#2d3748;color:#ffffff;">
                ✉️ {EMAIL}
            </a>
            <a href="{LINKEDIN_URL}" target="_blank"
               style="display:inline-block;padding:0.65rem 1.4rem;border-radius:8px;
                      font-size:0.9rem;font-weight:600;text-decoration:none;
                      background:#0077b5;color:#ffffff;">
                LinkedIn
            </a>
            {cv_button}
        </div>

        <div style="text-align:center;font-size:0.8rem;color:#94a3b8;
                    padding-bottom:2rem;letter-spacing:0.04em;">
            Augustin Leclercq · Site développé avec Python et Streamlit · 2025
        </div>

    </div>
    """

    components.html(html, height=480, scrolling=False)
