from datetime import datetime

LOG_FILE = "sort_log.txt"

def log_file_move(filename, target_folder):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] {filename} -> {target_folder}\n")