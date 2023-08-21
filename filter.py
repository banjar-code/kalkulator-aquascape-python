import tkinter as tk

# membuat fungsi untuk menghitung kebutuhan pompa filter
def hitung_pompa():
    # mendapatkan nilai panjang, lebar, dan tinggi dari input
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())
        kecepatan_aliran = float(entry_kecepatan_aliran.get())

        if panjang <= 0 or lebar <= 0 or tinggi <= 0 or kecepatan_aliran <= 0:
            raise ValueError("Input harus lebih dari 0")
    except ValueError:
        label_hasil.config(text="Input harus berupa angka dan lebih dari 0")
    else:
        # menghitung volume akuarium dalam liter
        volume = panjang * lebar * tinggi / 1000

        # menghitung laju aliran air yang dibutuhkan dalam liter per jam
        laju = volume * kecepatan_aliran

        # menampilkan hasil kebutuhan pompa filter
        label_hasil.config(text="Kebutuhan pompa filter: " + str(round(laju)) + " liter per jam")

# membuat fungsi untuk mereset nilai input dan hasil
def reset():
    entry_panjang.delete(0, tk.END)
    entry_lebar.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    entry_kecepatan_aliran.delete(0, tk.END)
    label_hasil.config(text="")

# membuat GUI dengan tkinter
root = tk.Tk()
root.title("Kalkulator Pompa Filter")

# membuat label dan input untuk panjang, lebar, tinggi akuarium, dan kecepatan aliran
label_panjang = tk.Label(root, text="Panjang (cm): ")
label_panjang.grid(row=0, column=0, padx=5, pady=5)
entry_panjang = tk.Entry(root)
entry_panjang.grid(row=0, column=1, padx=5, pady=5)

label_lebar = tk.Label(root, text="Lebar (cm): ")
label_lebar.grid(row=1, column=0, padx=5, pady=5)
entry_lebar = tk.Entry(root)
entry_lebar.grid(row=1, column=1, padx=5, pady=5)

label_tinggi = tk.Label(root, text="Tinggi (cm): ")
label_tinggi.grid(row=2, column=0, padx=5, pady=5)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1, padx=5, pady=5)

label_kecepatan_aliran = tk.Label(root, text="Kecepatan Aliran (x volume): ")
label_kecepatan_aliran.grid(row=3, column=0, padx=5, pady=5)
entry_kecepatan_aliran = tk.Entry(root)
entry_kecepatan_aliran.grid(row=3, column=1, padx=5, pady=5)

# membuat tombol untuk menghitung kebutuhan pompa filter
button_hitung = tk.Button(root, text="Hitung", command=hitung_pompa)
button_hitung.grid(row=4, column=0, padx=5, pady=5)

# membuat tombol untuk mereset input dan hasil
button_reset= tk.Button(root, text="Reset", command=reset)
button_reset.grid(row=4, column=1, padx=5, pady=5)

label_hasil = tk.Label(root, text="")
label_hasil.grid(row=5, columnspan=2, padx=5, pady=5)

root.mainloop()