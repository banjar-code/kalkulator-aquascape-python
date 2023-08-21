import tkinter as tk
# Create a function to calculate the volume of water
def calculate_volume():
    # Get the input values from the user
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        height = float(height_entry.get())

        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Input harus lebih besar dari 0")

        # Calculate the volume of water using the formula
        volume = length * width * height * 0.001

        # Update the volume label with the calculated value
        volume_label.config(text="Volume air: {:.2f} liter".format(volume))

        # Calculate the wattage required based on the volume of water
        low_light = volume * 0.25
        medium_light = volume * 0.5
        high_light = volume * 1

        # Update the wattage label with the calculated values
        low_light_label.config(text="Low light:{:.1f} watt".format(low_light))
        medium_light_label.config(text="Medium light:{:.1f} watt".format(medium_light))
        high_light_label.config(text="High light:{:.1f} watt".format(high_light))
        
    except ValueError as e:
        volume_label.config(text=str(e))
        low_light_label.config(text="")
        medium_light_label.config(text="")
        high_light_label.config(text="")
        
# Create the main window
root = tk.Tk()
root.title("Kalkulator Lampu Aquascape")

# Create the input labels and entries
length_label = tk.Label(root, text="Panjang (cm):")
length_entry = tk.Entry(root)

width_label = tk.Label(root, text="Lebar (cm):")
width_entry = tk.Entry(root)

height_label = tk.Label(root, text="Tinggi (cm):")
height_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Hitung", command=calculate_volume)

# Create the volume label
volume_label = tk.Label(root, text="Volume air: 0 liter", anchor='w')

# Create the wattage labels
low_light_label = tk.Label(root, text="Low light: 0 watt", anchor='w')
medium_light_label = tk.Label(root, text="Medium light: 0 watt", anchor='w')
high_light_label = tk.Label(root, text="High light: 0 watt", anchor='w')

# Lay out the widgets in the window
length_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)

width_label.grid(row=1, column=0)
width_entry.grid(row=1, column=1)

height_label.grid(row=2, column=0)
height_entry.grid(row=2, column=1)

calculate_button.grid(row=3, column=0)

volume_label.grid(row=4, column=0, columnspan=2, sticky='w')
low_light_label.grid(row=5, column=0, columnspan=2, sticky='w')
medium_light_label.grid(row=6, column=0, columnspan=2, sticky='w')
high_light_label.grid(row=7, column=0, columnspan=2, sticky='w')

# Create a function to reset the output
def reset_output():
    # Clear the input fields
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    # Reset the output labels to default values
    volume_label.config(text="Volume air: 0 liter")
    low_light_label.config(text="Low light: 0 watt")
    medium_light_label.config(text="Medium light: 0 watt")
    high_light_label.config(text="High light: 0 watt")

# Create the reset button
reset_button = tk.Button(root, text="Reset", command=reset_output)
# Lay out the reset button in the window
reset_button.grid(row=3, column=1)

root.mainloop()
