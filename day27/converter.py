from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# label miles
label_miles = Label(text="Miles", font=("Arial", 15))
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)  # bringt ein bisschen abstand

# label is equal to
label_equal = Label(text="Is equal to", font=("Arial", 15))
label_equal.grid(column=0, row=1)

# label output
label_output = Label(text="0", font=("Arial", 15))
label_output.grid(column=1, row=1)

# label kilometer
label_km = Label(text="km", font=("Arial", 15))
label_km.grid(column=2, row=1)

# Button


def convert():
    miles = float(entry.get())
    km = round(miles*1.609, 2)  # auf zwei nachkommastellen gerundet
    label_output.config(text=km)


button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

window.mainloop()
