# import tkinter
from tkinter import *

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#windows
windows = Tk()
windows.title("My gui")
windows.minsize(width=500,height=300)
windows.config(pady=20,padx=20)

#label
my_label = Label(text="Iam a label",font=("Arial",24,"bold"))
# my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

#Button
button = Button(text="Click Me",command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#entry
input = Entry(width=10)
print( input.get())
# input.pack()
input.grid(column=3,row=2)

button1 = Button(text="New Button")
button1.grid(row=0,column=2)

windows.mainloop()