import tkinter as tk

def calculate():
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())

    # Konversi panjang, lebar, dan tinggi ke volume air dalam liter
    volume = length * width * height / 1000
    volume_label.config(text=f"Volume air: {volume:.2f} liter")

    # Hitung kebutuhan ppm untuk tanaman
    dosis_co2 = ppm.get() * volume / 24
    dosis_co2_label.config(text=f"Kebutuhan CO2 : {dosis_co2:.2f} mg/hari")

    # Hitung kebutuhan bps
    bps = dosis_co2 / 60
    bps_label.config(text=f"Setingan Tabung CO2: {bps:.2f} bps")

def reset():
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    ppm.set(30)
    volume_label.config(text="Volume air: ")
    dosis_co2_label.config(text="Kebutuhan CO2 : ")
    bps_label.config(text="Setingan Tabung CO2: ")

root = tk.Tk()
root.title("Kalkulator CO2 Aquascape")

length_label = tk.Label(root, text="Panjang (cm):")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = tk.Label(root, text="Lebar (cm):")
width_label.grid(row=1, column=0, padx=5, pady=5)

width_entry = tk.Entry(root)
width_entry.grid(row=1, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Tinggi (cm):")
height_label.grid(row=2, column=0, padx=5, pady=5)

height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=5, pady=5)

ppm_label = tk.Label(root, text="Kebutuhan CO2 (ppm):")
ppm_label.grid(row=3, column=0, padx=5, pady=5)

ppm = tk.Scale(root, from_=10, to=60, orient=tk.HORIZONTAL, length=200)
ppm.grid(row=3, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

volume_label = tk.Label(root, text="Volume air: ")
volume_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

dosis_co2_label = tk.Label(root, text="Kebutuhan CO2 : ")
dosis_co2_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

bps_label = tk.Label(root, text="Setingan Tabung CO2: ")
bps_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
