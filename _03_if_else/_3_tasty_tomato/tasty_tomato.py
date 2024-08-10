from tkinter import *
import tkinter as tk
from tkinter import simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
name = simpledialog.askstring(title='Greeter', prompt='What color tomato do you like?')
#    You can give them up to three choices


# 2. Use if-else statements to draw the tomato in the color that they chose
if name == 'yellow':
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")

if name == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")

if name == 'green':
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
#    You can modify the code below or draw your own tomato
canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")

canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
