# stats.py
import matplotlib.pyplot as plt
from collections import defaultdict

stats_data = defaultdict(int)  # Kategorie: Anzahl Dateien

def add_stat(category):
    stats_data[category] += 1

def show_stats():
    if not stats_data:
        print("No stats to show")
        return
    categories = list(stats_data.keys())
    counts = [stats_data[c] for c in categories]
    plt.figure(figsize=(6,6))
    plt.pie(counts, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Sorted Files by Category")
    plt.show()
