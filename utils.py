import os
from config import CATEGORIES, FRONTEND_EXT, BACKEND_EXT

def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    name = name.lower().replace(" ", "_")
    return f"{name}{ext}"

def get_file_category(file_ext):
    """Erkennen Kategorie + Frontend/Backend"""
    for category, ext_list in CATEGORIES.items():
        if file_ext.lower() in ext_list:
            return category
    if file_ext.lower() in FRONTEND_EXT:
        return "frontend"
    elif file_ext.lower() in BACKEND_EXT:
        return "backend"
    return "others"