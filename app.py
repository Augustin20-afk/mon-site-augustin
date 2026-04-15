# app.py

import streamlit as st
from sections.navbar_section import render_navbar
from core.page_config import setup_page
from core.session_state import init_session_state
from styles.css import load_css
from sections.hero import render_hero
from sections.game_section import render_game, render_runner
from sections.current_section import render_current
from sections.world_section import render_world
from sections.work_style_section import render_work_style
from sections.project_section import render_projects
from sections.experiences_section import render_experiences
from sections.vision_section import render_vision
from sections.footer import render_footer
from sections.parcours_section import render_parcours

setup_page()
init_session_state()
load_css()

if st.session_state.get("show_parcours", False):
    render_parcours()
else:
    render_navbar()
    render_hero()
    render_game()
    render_current()
    render_world()
    render_work_style()
    render_projects()
    render_experiences()
    render_vision()
    render_runner()
    render_footer()
