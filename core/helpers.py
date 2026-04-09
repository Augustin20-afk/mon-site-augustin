def get_file_as_base64(file_path: str) -> str | None:
    from pathlib import Path
    import base64
    path = Path(file_path)
    if not path.exists():
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_image_base64_resized(file_path: str, size: int = 80) -> str | None:
    """Convertit une image en base64 en la redimensionnant d'abord."""
    from pathlib import Path
    import base64
    try:
        from PIL import Image
        import io
        path = Path(file_path)
        if not path.exists():
            return None
        img = Image.open(path)
        img = img.convert("RGB")
        img.thumbnail((size, size))
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=85)
        return base64.b64encode(buffer.getvalue()).decode()
    except ImportError:
        return get_file_as_base64(file_path)
