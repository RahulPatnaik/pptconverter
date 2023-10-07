import tkinter as tk
from tkinter import *

root = tk.Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redbutton = Button(frame, text = "Hi", fg = "red")
redbutton.pack(side = LEFT)

def open_window():
    new_window = tk.Tk()
    label = tk.Label(new_window, text = "This is a new window")
    label.pack()
    new_window.mainloop()

button = tk.Button(root, text= "Open window", command = open_window)
button.pack()



root.mainloop()