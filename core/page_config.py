import streamlit as st
from config.settings import SITE_TITLE, SITE_ICON, SITE_LAYOUT, SIDEBAR_STATE


def setup_page():
    st.set_page_config(
        page_title=SITE_TITLE,
        page_icon=SITE_ICON,
        layout=SITE_LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )
