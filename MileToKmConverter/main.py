from tkinter import *

def calculate():
    km = float(input.get()) * 1.609344
    kilo_result.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=270, height=100)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(row=0, column=1)

miles_label = Label(text='miles')
miles_label.grid(row=0, column=2)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

kilo_result = Label(text='0')
kilo_result.grid(row=1,column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(row=2, column=1)


window.mainloop()