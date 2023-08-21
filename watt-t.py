import tkinter as tk
import math

# Create a function to calculate the volume and surface area of aquarium
def calculate():
    # Get the input values from the user
    diameter = diameter_entry.get()
    height = height_entry.get()

    # Validate the input values
    try:
        diameter = float(diameter)
        height = float(height)
        if diameter <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        # Display an error message if the input is not valid
        volume_label.config(text="Volume air: input tidak valid")
        surface_area_label.config(text="Luas Permukaan: input tidak valid")
        low_light_label.config(text="Low light: input tidak valid")
        medium_light_label.config(text="Medium light: input tidak valid")
        high_light_label.config(text="High light: input tidak valid")
        return

    # Calculate the volume of water using the formula for cylinder
    volume = math.pi * (diameter / 2) ** 2 * height * 0.001

    # Calculate the surface area using the formula for cylinder
    surface_area = 2 * math.pi * (diameter / 2) ** 2 + math.pi * diameter * height

    # Update the volume label with the calculated value
    volume_label.config(text="Volume air: {:.2f} liter".format(volume))

    # Update the surface area label with the calculated value
    surface_area_label.config(text="Luas Permukaan: {:.2f} cm²".format(surface_area))

    # Calculate the wattage required based on the volume of water
    low_light = volume * 0.25
    medium_light = volume * 0.5
    high_light = volume * 1

    # Update the wattage label with the calculated values
    low_light_label.config(text="Low light: {:.1f} watt".format(low_light))
    medium_light_label.config(text="Medium light: {:.1f} watt".format(medium_light))
    high_light_label.config(text="High light: {:.1f} watt".format(high_light))

# Create the main window
root = tk.Tk()
root.title("Kalkulator Lampu Aquascape")

# Create the input labels and entries
diameter_label = tk.Label(root, text="Diameter (cm):")
diameter_entry = tk.Entry(root)

height_label = tk.Label(root, text="Tinggi (cm):")
height_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Hitung", command=calculate)

# Create the volume and surface area labels
volume_label = tk.Label(root, text="Volume air: 0 liter", anchor='w')
surface_area_label = tk.Label(root, text="Luas Permukaan: 0 cm²", anchor='w')

# Create the wattage labels
low_light_label = tk.Label(root, text="Low light: 0 watt", anchor='w')
medium_light_label = tk.Label(root, text="Medium light: 0 watt", anchor='w')
high_light_label = tk.Label(root, text="High light: 0 watt", anchor='w')

# Lay out the widgets in the window
diameter_label.grid(row=0, column=0)
diameter_entry.grid(row=0, column=1)

height_label.grid(row=1, column=0)
height_entry.grid(row=1, column=1)

calculate_button.grid(row=2, column=0)

volume_label.grid(row=3, column=0, columnspan=2, sticky='w')
surface_area_label.grid(row=4, column=0, columnspan=2, sticky='w')
low_light_label.grid(row=5, column=0, columnspan=2, sticky='w')
medium_light_label.grid(row=6, column=0, columnspan=2, sticky='w')
high_light_label.grid(row=7, column=0, columnspan=2, sticky='w')

# Create a function to reset the output
def reset_output():
    # Clear the input fields
    diameter_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    # Reset the output labels
    volume_label.config(text="Volume air: 0 liter")
    surface_area_label.config(text="Luas Permukaan: 0 cm²")
    low_light_label.config(text="Low light: 0 watt")
    medium_light_label.config(text="Medium light: 0 watt")
    high_light_label.config(text="High light: 0 watt")

reset_button = tk.Button(root, text="Reset", command=reset_output)

reset_button.grid(row=2, column=1)

root.mainloop()

