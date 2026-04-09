# components/photo.py

import base64
from pathlib import Path
import streamlit as st


def get_image_base64(image_path: str) -> str | None:
    """Convertit une image en base64 pour l'affichage HTML."""
    path = Path(image_path)
    if not path.exists():
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def display_profile_photo(image_path: str, css_class: str = "profile-photo") -> None:
    """Affiche la photo de profil encodée en base64."""
    b64 = get_image_base64(image_path)
    if b64:
        ext = Path(image_path).suffix.lower().replace(".", "")
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        st.markdown(
            f'<img src="data:image/{mime};base64,{b64}" class="{css_class}" alt="Photo de profil">',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="photo-placeholder">📷</div>',
            unsafe_allow_html=True,
        )
