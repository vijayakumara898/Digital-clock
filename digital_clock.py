from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")
def time():
    string=strftime("%I:%M:%S %p")
    lable.config(text = string)
    lable.after(1000,time)



lable = Label(window, font =("ds-digital",80),background = "black",foreground= "cyan")
lable.pack(anchor="center")
time()

mainloop()