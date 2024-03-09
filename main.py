from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)

num_label = Label(text="is equal to")
num_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

calculation = Label(text="0")
calculation.grid(column=1, row=1)
def calculate_button():
    mile = float(input.get())
    calc = int(mile * 1.609344)
    calculation.config(text=calc,font=("Arial",24,"bold"))

button = Button(text="Calculate", font=("Arial", 10, "bold"),command=calculate_button)
button.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1,row=0)
input.get()

window.mainloop()
