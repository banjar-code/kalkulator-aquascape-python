import tkinter as tk

def calculate_PAR():
    try:
        lux_value = float(lux_entry.get())
        if lux_value <= 0:
            raise ValueError
        PAR_value = round(lux_value * 0.22, 2)
        PAR_result.config(text=f"PAR value: {PAR_value} micromol m^-2 s^-1")
    except ValueError:
        PAR_result.config(text="Invalid input. Please enter a positive number.")

def reset():
    lux_entry.delete(0, tk.END)
    PAR_result.config(text="PAR value: ")
    PAR_button.config(state=tk.DISABLED)

def check_lux_value(*args):
    lux_value = lux_entry.get()
    if lux_value:
        try:
            lux_value = float(lux_value)
            if lux_value <= 0:
                raise ValueError
            PAR_button.config(state=tk.NORMAL)
            return
        except ValueError:
            pass
    PAR_button.config(state=tk.DISABLED)

# create the GUI window
root = tk.Tk()
root.title("PAR Calculator")

# create the GUI widgets
lux_label = tk.Label(root, text="Lux value:")
lux_entry = tk.Entry(root)
lux_entry.bind("<KeyRelease>", check_lux_value)
PAR_button = tk.Button(root, text="Calculate PAR", command=calculate_PAR, state=tk.DISABLED)
reset_button = tk.Button(root, text="Reset", command=reset)
PAR_result = tk.Label(root, text="PAR value: ")

# arrange the widgets in the GUI window
lux_label.grid(row=0, column=0)
lux_entry.grid(row=0, column=1)
PAR_button.grid(row=1, column=0)
reset_button.grid(row=1, column=1)
PAR_result.grid(row=2, column=0, columnspan=2)

# start the GUI event loop
root.mainloop()
