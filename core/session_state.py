# core/session_state.py

import streamlit as st

def init_session_state():
    defaults = {
        "site_ready": True,
        "show_parcours": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
