import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from sorter import sort_files_in_folder

folder_path = None
file_listbox = None
progress_bar = None

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        list_files(folder)

def list_files(folder):
    file_listbox.delete(0, tk.END)
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, f)):
            file_listbox.insert(tk.END, f)

def sort_selected():
    folder = folder_path.get()
    if not folder:
        messagebox.showwarning("Warning", "Please select a folder first!")
        return
    selected_files = [file_listbox.get(i) for i in file_listbox.curselection()]
    if not selected_files:
        selected_files = None
    sort_files_in_folder(folder, selected_files)
    list_files(folder)
    messagebox.showinfo("Done", "Files sorted successfully!")

def auto_cleanup():
    folder = folder_path.get()
    if folder:
        sort_files_in_folder(folder)
        list_files(folder)
        messagebox.showinfo("Done", "Auto Cleanup completed!")

def drag_and_drop(event):
    paths = root.tk.splitlist(event.data)
    for path in paths:
        if os.path.isdir(path):
            folder_path.set(path)
            sort_files_in_folder(path)
            list_files(path)

def setup_gui():
    global folder_path, file_listbox, progress_bar, root

    root = tk.Tk()
    root.title("Smart File Organizer Pro – Drag&Drop")
    root.geometry("700x400")
    root.resizable(False, False)

    folder_path = tk.StringVar()

    frame_top = tk.Frame(root)
    frame_top.pack(pady=10)

    tk.Label(frame_top, text="Select Folder to Organize:").pack(side=tk.LEFT, padx=5)
    tk.Entry(frame_top, textvariable=folder_path, width=50).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_top, text="Browse", command=select_folder).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_top, text="Auto Cleanup", command=auto_cleanup).pack(side=tk.LEFT, padx=5)

    frame_middle = tk.Frame(root)
    frame_middle.pack(pady=10, fill=tk.BOTH, expand=True)

    file_listbox = tk.Listbox(frame_middle, width=90, height=15, selectmode=tk.MULTIPLE)
    file_listbox.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_middle)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    file_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=file_listbox.yview)

    frame_bottom = tk.Frame(root)
    frame_bottom.pack(pady=10)

    tk.Button(frame_bottom, text="Sort Selected / All Files", command=sort_selected, width=25).pack(pady=5)
    progress_bar = ttk.Progressbar(frame_bottom, orient="horizontal", length=550, mode="determinate")
    progress_bar.pack(pady=5)

    # Drag-and-Drop Unterstützung (Windows)
    try:
        import tkdnd
        tkdnd.TkinterDnD(root)
        root.drop_target_register(tkdnd.DND_FILES)
        root.dnd_bind('<<Drop>>', drag_and_drop)
    except ImportError:
        pass  # Drag-and-Drop nur, wenn tkdnd verfügbar

    root.mainloop()

if __name__ == "__main__":
    setup_gui()