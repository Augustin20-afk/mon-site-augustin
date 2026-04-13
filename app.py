# app.py

import streamlit as st
from core.page_config import setup_page
from core.session_state import init_session_state
from styles.css import load_css
from sections.hero import render_hero
from sections.game_section import render_game
from sections.world_section import render_world
from sections.project_section import render_projects
from sections.footer import render_footer
from sections.work_style_section import render_work_style
from sections.experiences_section import render_experiences
from sections.vision_section import render_vision
from sections.game_section import render_game, render_runner
from sections.current_section import render_current

setup_page()
init_session_state()
load_css()



# Ordre mis à jour :
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
