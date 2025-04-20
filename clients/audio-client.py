import tkinter as tk
from tkinter import simpledialog, messagebox
import requests
import pygame
import io

# Pokrećemo pygame mixer
pygame.mixer.init()

def play_stream():
    url = simpledialog.askstring("URL", "Unesi URL do MP3 stream-a:")

    if not url:
        messagebox.showerror("Greška", "Nisi uneo URL!")
        return

    try:
        # Skinemo fajl iz stream-a (ali u memoriju, ne na disk)
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Proveri da li je server vratio Partial Content ili ceo fajl
        if response.status_code not in (200, 206):
            messagebox.showerror("Greška", f"Nevalidan odgovor servera: {response.status_code}")
            return

        # Učitamo ceo stream u memorijski buffer
        mp3_data = io.BytesIO(response.content)

        # Inicijalizuj mixer da čita MP3 iz memorije
        pygame.mixer.music.load(mp3_data)
        pygame.mixer.music.play()

        messagebox.showinfo("Info", "Reprodukcija pokrenuta!")
    except Exception as e:
        messagebox.showerror("Greška", str(e))

# Tkinter GUI
root = tk.Tk()
root.title("MP3 Stream Player")
root.geometry("300x150")

btn_play = tk.Button(root, text="Pusti MP3 sa servera", command=play_stream)
btn_play.pack(pady=40)

root.mainloop()
