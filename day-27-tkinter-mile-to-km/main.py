from tkinter import *

def calculate_km():
    km = float(input.get()) * 1.609
    label_km["text"] = round(km, 2)

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

# Miles entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(END, string="0")

# Miles label
label = Label(text="Miles")
label.grid(column=2, row=0)

# is equal to
label = Label(text="is equal to")
label.grid(column=0, row=1)

# Output km
label_km = Label(text=("0"))
label_km.grid(column=1, row=1)

# Km label
label = Label(text="Km")
label.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()