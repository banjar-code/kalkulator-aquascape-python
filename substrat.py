import tkinter as tk

def is_valid_input(input_str):
    try:
        input_num = float(input_str)
        if input_num <= 0:
            return False
        return True
    except ValueError:
        return False

def validate_input():
    if not is_valid_input(panjang_entry.get()):
        return False
    if not is_valid_input(lebar_entry.get()):
        return False
    if not is_valid_input(tinggi_entry.get()):
        return False
    return True

def hitung_volume():
    if not validate_input():
        volume_label.config(text="Harap masukkan nilai numerik lebih besar dari 0")
        return
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi_sub = float(tinggi_entry.get())

    volume = panjang * lebar * tinggi_sub
    volume1 = volume / 1000

    volume_label.config(text="Volume Total Substrat: {:.2f} Liter".format(volume1))

    soil_kebutuhan = volume * 0.1 / 100
    malang_kebutuhan = volume * 0.06 / 100
    silika_kebutuhan = volume * 0.12 / 100
    bali_kebutuhan = soil_kebutuhan

    soil_label.config(text="Soil: {:.2f} Liter".format(soil_kebutuhan))
    malang_label.config(text="Pasir Malang: {:.2f} Liter".format(malang_kebutuhan))
    silika_label.config(text="Pasir Silika: {:.2f} Liter".format(silika_kebutuhan))
    bali_label.config(text="Pasir Bali: {:.2f} Liter".format(bali_kebutuhan))

def reset_all_entries():
    panjang_entry.delete(0, tk.END)
    lebar_entry.delete(0, tk.END)
    tinggi_entry.delete(0, tk.END)
    volume_label.config(text="Volume Total Substrat: ")
    soil_label.config(text="Soil: ")
    malang_label.config(text="Pasir Malang: ")
    silika_label.config(text="Pasir Silika: ")
    bali_label.config(text="Pasir Bali: ")

window = tk.Tk()
window.title("Kalkulator Substrat Aquascape")

panjang_label = tk.Label(window, text="Panjang (cm):")
panjang_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
panjang_entry = tk.Entry(window)
panjang_entry.grid(row=0, column=1, padx=5, pady=5)

lebar_label = tk.Label(window, text="Lebar (cm):")
lebar_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
lebar_entry = tk.Entry(window)
lebar_entry.grid(row=1, column=1, padx=5, pady=5)

tinggi_label = tk.Label(window, text="Tinggi Substrat (cm):")
tinggi_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
tinggi_entry = tk.Entry(window)
tinggi_entry.grid(row=2, column=1, padx=5, pady=5)

volume_button = tk.Button(window, text="Hitung Volume", command=hitung_volume)
volume_button.grid(row=3, column=0, padx=5, pady=5)

reset_button = tk.Button(window, text="Reset", command=reset_all_entries)
reset_button.grid(row=3, column=1, padx=5, pady=5)

volume_label = tk.Label(window, text="Volume Total Substrat: ")
volume_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="W")

soil_label = tk.Label(window, text="Soil: ")
soil_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")

malang_label = tk.Label(window, text="Pasir Malang: ")
malang_label.grid(row=6, column=0, padx=5, pady=5, sticky="W")

silika_label = tk.Label(window, text="Pasir Silika: ")
silika_label.grid(row=7, column=0, padx=5, pady=5, sticky="W")

bali_label = tk.Label(window, text="Pasir Bali: ")
bali_label.grid(row=8, column=0, padx=5, pady=5, sticky="W")

window.mainloop()