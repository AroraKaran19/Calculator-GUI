from tkinter import *

def calculator():
    """ Main Gui """
    global gui, box
    gui = Tk()
    gui.title("Calculator")
    gui.geometry("900x600")
    gui.resizable(height=False, width=False)

    canvas = Canvas(gui, bg="grey", width="900", height="600")
    canvas.pack()

    # Entry Box
    box = Entry(canvas, width=28, font=("", 40))
    canvas.create_window(450, 70, window=box)

    # Creating Buttons(0-9)
    button_9 = Button(canvas, text="9", width=10, height=3, command=lambda: add_entry(9))
    canvas.create_window(90, 150, window=button_9)
    button_8 = Button(canvas, text="8", width=10, height=3, command=lambda: add_entry(8))
    canvas.create_window(180, 150, window=button_8)
    button_7 = Button(canvas, text="7", width=10, height=3, command=lambda: add_entry(7))
    canvas.create_window(270, 150, window=button_7)
    button_6 = Button(canvas, text="6", width=10, height=3, command=lambda: add_entry(6))
    canvas.create_window(90, 220, window=button_6)
    button_5 = Button(canvas, text="5", width=10, height=3, command=lambda: add_entry(5))
    canvas.create_window(180, 220, window=button_5)
    button_4 = Button(canvas, text="4", width=10, height=3, command=lambda: add_entry(4))
    canvas.create_window(270, 220, window=button_4)
    button_3 = Button(canvas, text="3", width=10, height=3, command=lambda: add_entry(3))
    canvas.create_window(90, 290, window=button_3)
    button_2 = Button(canvas, text="2", width=10, height=3, command=lambda: add_entry(2))
    canvas.create_window(180, 290, window=button_2)
    button_1 = Button(canvas, text="1", width=10, height=3, command=lambda: add_entry(1))
    canvas.create_window(270, 290, window=button_1)
    button_0 = Button(canvas, text="0", width=35, height=3, command=lambda: add_entry(0))
    canvas.create_window(180, 360, window=button_0)

    # Backspace Button
    backspace = Button(canvas, text="<---", width=20, height=3, command=lambda: remove_entry())
    canvas.create_window(770, 150, window=backspace)

    gui.mainloop()

def add_entry(entry):
    """ Add The passed entry to the Entry box! (Insertion at end) """
    value = box.get()
    box.insert(len(value), str(entry))

def remove_entry():
    """ Removes the last added entry! (Deletion at end) """
    # Backspace button
    value = box.get()
    box.delete(len(value)-1)

calculator()