import streamlit as st
from config.settings import SITE_TITLE, SITE_ICON, SITE_LAYOUT, SIDEBAR_STATE

def setup_page():
    st.set_page_config(
        page_title=SITE_TITLE,
        page_icon=SITE_ICON,
        layout=SITE_LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )
    # Force le thème clair + supprime la toolbar Streamlit
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        header[data-testid="stHeader"] {
            display: none !important;
            height: 0 !important;
        }
        [data-testid="stToolbar"] {display: none !important;}
        .stDeployButton {display: none !important;}
        </style>
    """, unsafe_allow_html=True)
