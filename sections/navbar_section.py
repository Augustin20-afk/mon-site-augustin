# sections/navbar_section.py

import streamlit as st

def render_navbar() -> None:
    st.markdown(
        """
        <div style="position:fixed;top:0;left:0;right:0;z-index:99999;
                    background:rgba(255,255,255,0.97);
                    border-bottom:1px solid #e2e8f0;
                    padding:0.8rem 2rem;
                    display:flex;align-items:center;justify-content:space-between;
                    box-shadow:0 2px 12px rgba(0,0,0,0.06);">
            <span style="font-size:1rem;font-weight:700;color:#0f172a;">
                Le Site Web d'<span style="color:#2563eb;">Augustin Leclercq</span>
            </span>
            <div style="display:flex;align-items:center;gap:1.5rem;">
                <a href="#accueil" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">Accueil</a>
                <a href="#apropos" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">À propos</a>
                <a href="#experiences" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">Expériences</a>
                <a href="#projets" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">Projets</a>
                <a href="#quiz" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">Quiz</a>
                <a href="#contact" style="font-size:0.85rem;font-weight:600;color:#475569;text-decoration:none;">Contact</a>
            </div>
        </div>
        <div style="text-align:center;padding:5rem 2rem 2rem 2rem;
                    max-width:960px;margin:0 auto;">
            <h1 style="font-size:2.8rem;font-weight:800;color:#0f172a;
                       letter-spacing:-0.02em;line-height:1.1;margin-bottom:0.6rem;">
                Le Site Web d'<span style="color:#2563eb;">Augustin Leclercq</span>
            </h1>
            <p style="font-size:1rem;font-weight:600;color:#64748b;
                      letter-spacing:0.15em;text-transform:uppercase;">
                Rigueur · Terrain · Ambition
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
