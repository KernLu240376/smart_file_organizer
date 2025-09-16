# Smart File Organizer Pro – Beta

A powerful Python-based file organizer designed for developers, designers, and everyday users who want a clean, structured workspace. This Beta version features **Drag & Drop support**, automatic sorting by file type, and a clear **Frontend/Backend folder hierarchy** for web development projects.

---

## Features

- **Drag & Drop Support**: Simply drop files or folders into the application window, and they are automatically sorted.
- **Frontend & Backend Categorization**:
  - **Frontend**: HTML, CSS, JavaScript, TypeScript, JSON, YAML, XML
  - **Backend**: Python, Java, C++, C#, PHP, SQL
- **Automatic Folder Structure**:
  - `frontend/html`, `frontend/css`, `frontend/javascript`, etc.
  - `backend/python`, `backend/java`, `backend/sql`, etc.
- **Clean File Naming**: All files are automatically renamed to `snake_case` for consistency.
- **Multi-Select Sorting**: Choose specific files to sort or organize the entire folder at once.
- **Auto-Cleanup**: Organize all files in a folder with a single click.
- **Logging**: Tracks all file movements in `sort_log.txt` for accountability.

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. Tkinter is required (usually included with Python).
3. Optional: If using Drag & Drop on Windows, ensure `tkdnd` is installed.

---

## Usage

1. Launch `main.py`.
2. Select a folder or drag and drop files/folders into the GUI.
3. Click **"Sort Selected / All Files"** or **"Auto Cleanup"** to organize your files automatically.
4. Check the folder structure: Files are now neatly organized by type and Frontend/Backend classification.

---

## Supported File Types

**Frontend**:  
`.html`, `.htm`, `.css`, `.js`, `.ts`, `.json`, `.yml`, `.yaml`, `.xml`  

**Backend**:  
`.py`, `.java`, `.cpp`, `.cs`, `.php`, `.sql`  

**Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`  
**Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`  
**Music**: `.mp3`, `.wav`, `.flac`, `.aac`  
**Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`  
**Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`  

---



## License

This project is open-source under the MIT License. Feel free to use, modify, and distribute.
