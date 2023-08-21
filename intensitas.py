import math
import tkinter as tk

# fungsi untuk menghitung nilai lux pada permukaan air
def hitung_lux_p():
    try:
        # mengambil nilai input dari user
        wattage = float(wattage_entry.get())
        jarak = float(jarak_entry.get()) / 100
        angle = float(angle_entry.get())
        jarak_pengukuran = float(jarak_pengukuran_entry.get()) / 100

        # validasi input
        if wattage <= 0 or jarak <= 0 or angle <= 0 or jarak_pengukuran <= 0:
            raise ValueError("Input tidak valid")

        # menghitung intensitas cahaya pada permukaan air
        intensitas_p = wattage / (4 * math.pi * jarak**2)

        # menampilkan hasil perhitungan
        intensitas_p_label.config(text=f"Lumen pada permukaan air: {intensitas_p:.2f} lm/m^2")

        # menghitung nilai lux pada permukaan air
        lux_p = intensitas_p * jarak_pengukuran**2 * 10000

        # menampilkan hasil perhitungan
        lux_p_label.config(text=f"Lux pada permukaan air: {lux_p:.2f} lux")

    except ValueError as e:
        # menampilkan pesan error jika input tidak valid
        lux_p_label.config(text="Error: " + str(e))
        intensitas_p_label.config(text="")


# fungsi untuk menghitung nilai lux pada kedalaman tertentu
def hitung_lux_k():
    try:
        # mengambil nilai input dari user
        wattage = float(wattage_entry.get())
        jarak = float(jarak_entry.get()) / 100
        angle = float(angle_entry.get())
        kedalaman = float(kedalaman_entry.get()) / 100
        jarak_pengukuran = float(jarak_pengukuran_entry.get()) / 100

        # validasi input
        if wattage <= 0 or jarak <= 0 or angle <= 0 or kedalaman <= 0 or jarak_pengukuran <= 0:
            raise ValueError("Input tidak valid")

        # menghitung intensitas cahaya pada permukaan air
        intensitas_p = wattage / (4 * math.pi * jarak**2)

        # menghitung koefisien penyebaran cahaya
        koefisien = math.log(2) / (kedalaman * math.tan(math.radians(angle / 2)))

        # menampilkan hasil perhitungan
        koefisien_label.config(text=f"Koefisien penyebaran cahaya: {koefisien:.2f}")

        # menghitung intensitas cahaya pada kedalaman tertentu
        intensitas_k = intensitas_p * math.exp(-koefisien * kedalaman)

        # menampilkan hasil perhitungan
        intensitas_k_label.config(text=f"Lumen pada kedalaman {kedalaman:.2f} m: {intensitas_k:.2f} lm/m^2")

        # menghitung nilai lux pada kedalaman tertentu
        lux_k = intensitas_k * jarak_pengukuran**2 * 10000

        # menampilkan hasil perhitungan
        lux_k_label.config(text=f"Lux pada kedalaman {kedalaman:.2f} m: {lux_k:.2f} lux")

    except ValueError as e:
        # menampilkan pesan error jika input tidak valid
        lux_k_label.config(text="Error: " + str(e))
        intensitas_k_label.config(text="")
        koefisien_label.config(text="")

root = tk.Tk()
root.title("Kalkulator Lux Meter")

# membuat frame untuk input
input_frame = tk.LabelFrame(root, text="Input", padx=10, pady=10)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

wattage_label = tk.Label(input_frame, text="Wattage:")
wattage_label.grid(row=0, column=0, padx=5, pady=5)
wattage_entry = tk.Entry(input_frame)
wattage_entry.grid(row=0, column=1, padx=5, pady=5)

jarak_label = tk.Label(input_frame, text="Jarak lampu ke permukaan air (cm):")
jarak_label.grid(row=1, column=0, padx=5, pady=5)
jarak_entry = tk.Entry(input_frame)
jarak_entry.grid(row=1, column=1, padx=5, pady=5)

angle_label = tk.Label(input_frame, text="Sudut pancaran cahaya (derajat):")
angle_label.grid(row=2, column=0, padx=5, pady=5)
angle_entry = tk.Entry(input_frame)
angle_entry.grid(row=2, column=1, padx=5, pady=5)

kedalaman_label = tk.Label(input_frame, text="Kedalaman air (cm):")
kedalaman_label.grid(row=3, column=0, padx=5, pady=5)
kedalaman_entry = tk.Entry(input_frame)
kedalaman_entry.grid(row=3, column=1, padx=5, pady=5)

jarak_pengukuran_label = tk.Label(input_frame, text="Jarak pengukuran (cm):")
jarak_pengukuran_label.grid(row=4, column=0, padx=5, pady=5)
jarak_pengukuran_entry = tk.Entry(input_frame)
jarak_pengukuran_entry.grid(row=4, column=1, padx=5, pady=5)

# membuat frame untuk output
output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10)
output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

intensitas_p_label = tk.Label(output_frame, text="")
intensitas_p_label.grid(row=0, column=0, padx=5, pady=5)

lux_p_label = tk.Label(output_frame, text="")
lux_p_label.grid(row=1, column=0, padx=5, pady=5)

koefisien_label = tk.Label(output_frame, text="")
koefisien_label.grid(row=2, column=0, padx=5, pady=5)

intensitas_k_label = tk.Label(output_frame, text="")
intensitas_k_label.grid(row=3, column=0, padx=5, pady=5)

lux_k_label = tk.Label(output_frame, text="")
lux_k_label.grid(row=4, column=0, padx=5, pady=5)

# membuat tombol untuk menghitung lux pada permukaan air
lux_p_button = tk.Button(input_frame, text="Hitung Lux pada Permukaan Air", command=hitung_lux_p)
lux_p_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# membuat tombol untuk menghitung lux pada kedalaman tertentu
lux_k_button = tk.Button(input_frame, text="Hitung Lux pada Kedalaman Tertentu", command=hitung_lux_k)
lux_k_button.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="e")

# fungsi untuk mereset nilai pada input dan output
def reset():
    wattage_entry.delete(0, tk.END)
    jarak_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)
    kedalaman_entry.delete(0, tk.END)
    jarak_pengukuran_entry.delete(0, tk.END)
    intensitas_p_label.config(text="")
    lux_p_label.config(text="")
    intensitas_k_label.config(text="")
    lux_k_label.config(text="")
    koefisien_label.config(text="")

# membuat tombol reset
reset_button = tk.Button(input_frame, text="Reset", command=reset)
reset_button.grid(row=4, column=2, padx=5, pady=5, sticky="e")


root.mainloop()
