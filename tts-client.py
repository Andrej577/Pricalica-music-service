import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os

SERVER_URL = "http://localhost:5000"

def generate_audio():
    text = text_input.get("1.0", tk.END).strip()
    lang = lang_entry.get()
    filename = filename_entry.get()

    if not text or not filename:
        messagebox.showerror("Greška", "Tekst i naziv datoteke su obavezni.")
        return

    data = {
        "text": text,
        "lang": lang,
        "filename": filename
    }

    try:
        response = requests.post(f"{SERVER_URL}/generate", json=data)
        response.raise_for_status()
        result = response.json()

    except Exception as e:
        messagebox.showerror("Greška", f"Došlo je do greške: {e}")

# GUI setup
root = tk.Tk()
root.title("Text-to-MP3 Generator (gTTS)")

tk.Label(root, text="Unesi tekst:").pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

tk.Label(root, text="Jezik (npr. fr, es, en):").pack()
lang_entry = tk.Entry(root)
lang_entry.insert(0, "en")
lang_entry.pack()

tk.Label(root, text="Naziv datoteke (bez .mp3):").pack()
filename_entry = tk.Entry(root)
filename_entry.insert(0, "output")
filename_entry.pack()

tk.Button(root, text="Generiraj MP3", command=generate_audio).pack(pady=10)

root.mainloop()

