import tkinter as tk
import os

root = tk.Tk()
root.title("Kalkulator Aquascape")
root.geometry("400x350")

# Header
header = tk.Label(root, text="Kalkulator Aquascape", font=("Arial", 16))
header.pack(pady=10)

# Gambar
image = tk.PhotoImage(file="image/tanaman-aquascape.png")  # Ganti "aquascape.png" dengan nama file gambar Anda
image_label = tk.Label(root, image=image)
image_label.pack(pady=10)

# Sub-Header
sub_header = tk.Label(root, text="Developer By Banjar Smart Digital", font=("Arial", 12))
sub_header.pack()

def run_watt_p():
    os.system('python3 watt-p.py')

def run_watt_t():
    os.system('python3 watt-t.py')

def run_intensitas():
    os.system('python3 intensitas.py')

def run_par():
    os.system('python3 par.py')

def run_filter():
    os.system('python3 filter.py')

def run_subtrat():
    os.system('python3 substrat.py')

def run_co2():
    os.system('python3 co2.py')

# membuat menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Pilih Menu", menu=file_menu)

file_menu.add_command(label="Hitung Kebutuhan Lampu (P)", command=run_watt_p)
file_menu.add_command(label="Hitung Kebutuhan Lampu (T)", command=run_watt_t)
file_menu.add_command(label="Hitung Intensitas Cahaya", command=run_intensitas)
file_menu.add_command(label="Hitung Kebutuhan Par", command=run_par)
file_menu.add_command(label="Hitung Kebutuhan Filter", command=run_filter)
file_menu.add_command(label="Hitung Kebutuhan Substrate", command=run_subtrat)
file_menu.add_command(label="Hitung Kebutuhan CO2", command=run_co2)

root.mainloop()
