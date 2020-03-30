""""
Digital clock using python and tkinter """

# import the required libraries

import sys
import tkinter as tk
import time

# define Function
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)

digit_clock = tk.Tk()
clock = tk.Label(digit_clock, font=("times", 50, "bold"), bg="cyan")
clock.grid(row=0, column=1)
tick()

digit_clock.mainloop()
