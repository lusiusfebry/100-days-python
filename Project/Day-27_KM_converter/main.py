from tkinter import *


def miles_to_KM():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

#windows
windows = Tk()
windows.title("Mile to KM Converter")
windows.config(padx=20,pady=20)

#input
miles_input = Entry(width=8)
miles_input.grid(column=1,row=0)

#label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

km_label = Label(text="KM")
km_label.grid(column=3,row=1)

#button
calculate_button = Button(text="Calculate",command=miles_to_KM)
calculate_button.grid(row=2,column=1)



windows.mainloop()
