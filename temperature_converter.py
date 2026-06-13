import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result = f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K"

        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result = f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K"

        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result = f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F"

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature.")

# Main Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Heading
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Temperature Input
tk.Label(root, text="Enter Temperature:").pack()
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# Unit Selection
tk.Label(root, text="Select Unit:").pack()
unit_var = tk.StringVar()
unit_dropdown = ttk.Combobox(root, textvariable=unit_var)
unit_dropdown['values'] = ("Celsius", "Fahrenheit", "Kelvin")
unit_dropdown.current(0)
unit_dropdown.pack(pady=5)

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert_temperature)
convert_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
