import os
import shutil
from utils import clean_filename, get_file_category
from logger import log_file_move

def sort_files_in_folder(folder, files=None):
    """Sortiert Dateien direkt in Frontend/Backend Unterordner"""
    if files is None:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for f in files:
        src_path = os.path.join(folder, f)
        file_ext = os.path.splitext(f)[1]
        category = get_file_category(file_ext)

        # Zielordner bestimmen
        if category in ["html", "css", "javascript"]:
            parent_folder = os.path.join(folder, "frontend")
        elif category in ["python", "java", "cpp", "php", "cs"]:
            parent_folder = os.path.join(folder, "backend")
        else:
            parent_folder = folder  # andere Kategorien bleiben direkt im Hauptordner

        target_folder = os.path.join(parent_folder, category) if category not in ["documents", "images", "music", "videos", "archives"] else os.path.join(parent_folder, category)
        os.makedirs(target_folder, exist_ok=True)

        new_name = clean_filename(f)
        shutil.move(src_path, os.path.join(target_folder, new_name))
        log_file_move(new_name, target_folder)