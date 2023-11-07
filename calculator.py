from tkinter import *
from tkinter import ttk
import tkinter as tk

build = ""
def number_pressed(num):
    build_string(num)
    return num

def operator_pressed(operator):
    build_string(operator)
    return operator

def build_string(button):
    global build 
    build = build + (str(button))
    entry_text.set(str(build))
    
    return build

def equals_pressed():
    try:
        global build
        answer = (str(eval(build)))
    except:
        Exception
        answer = 0

    build = answer
    entry_text.set(str(build))
    return answer


if __name__ =='__main__':
    root = Tk()
    root.title("Calculator.py")
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    
    entry_text = tk.StringVar()
    screen = Entry(frm, textvariable = entry_text, width=50, justify=RIGHT)
    screen.grid(column=1, row=0, columnspan=4, pady=10)

    button_7 = ttk.Button(frm, text="7", command=lambda: number_pressed(7)).grid(column=1, row=1)
    button_8 = ttk.Button(frm, text="8", command=lambda: number_pressed(8)).grid(column=2, row=1)
    button_9 = ttk.Button(frm, text="9", command=lambda: number_pressed(9)).grid(column=3, row=1)
    button_div = ttk.Button(frm, text="/", command=lambda: operator_pressed("/")).grid(column=4, row=1)

    button_4 = ttk.Button(frm, text="4", command=lambda: number_pressed(4)).grid(column=1, row=2)
    button_5 = ttk.Button(frm, text="5", command=lambda: number_pressed(5)).grid(column=2, row=2)
    button_6 = ttk.Button(frm, text="6", command=lambda: number_pressed(6)).grid(column=3, row=2)
    button_mult = ttk.Button(frm, text="*", command=lambda: operator_pressed("*")).grid(column=4, row=2)

    button_1 = ttk.Button(frm, text="1", command=lambda: number_pressed(1)).grid(column=1, row=3)
    button_2 = ttk.Button(frm, text="2", command=lambda: number_pressed(2)).grid(column=2, row=3)
    button_3 = ttk.Button(frm, text="3", command=lambda: number_pressed(3)).grid(column=3, row=3)
    button_min = ttk.Button(frm, text="-", command=lambda: operator_pressed("-")).grid(column=4, row=3)
    
    button_0 = ttk.Button(frm, text="0", command=lambda: number_pressed(0)).grid(column=1, row=4)
    button_dec = ttk.Button(frm, text=".", command=lambda: operator_pressed(".")).grid(column=2, row=4)
    button_plus = ttk.Button(frm, text="+", command=lambda: operator_pressed("+")).grid(column=4, row=4)
    

    
    button_equals = ttk.Button(frm, text="=", command=lambda: equals_pressed()).grid(column=3, row=4)

    root.mainloop()