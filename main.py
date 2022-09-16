from tkinter import *
from tkinter import messagebox

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
    canvas.create_window(90, 220, window=button_9)
    button_8 = Button(canvas, text="8", width=10, height=3, command=lambda: add_entry(8))
    canvas.create_window(180, 220, window=button_8)
    button_7 = Button(canvas, text="7", width=10, height=3, command=lambda: add_entry(7))
    canvas.create_window(270, 220, window=button_7)
    button_6 = Button(canvas, text="6", width=10, height=3, command=lambda: add_entry(6))
    canvas.create_window(90, 290, window=button_6)
    button_5 = Button(canvas, text="5", width=10, height=3, command=lambda: add_entry(5))
    canvas.create_window(180, 290, window=button_5)
    button_4 = Button(canvas, text="4", width=10, height=3, command=lambda: add_entry(4))
    canvas.create_window(270, 290, window=button_4)
    button_3 = Button(canvas, text="3", width=10, height=3, command=lambda: add_entry(3))
    canvas.create_window(90, 360, window=button_3)
    button_2 = Button(canvas, text="2", width=10, height=3, command=lambda: add_entry(2))
    canvas.create_window(180, 360, window=button_2)
    button_1 = Button(canvas, text="1", width=10, height=3, command=lambda: add_entry(1))
    canvas.create_window(270, 360, window=button_1)
    button_0 = Button(canvas, text="0", width=35, height=3, command=lambda: add_entry(0))
    canvas.create_window(180, 430, window=button_0)

    # Backspace Button
    backspace = Button(canvas, text="<---", width=20, height=3, command=lambda: remove_entry("end"))
    canvas.create_window(770, 150, window=backspace)

    # Clear Button
    clear_button = Button(canvas, text="C", width=10, height=3, command=lambda: remove_entry("all"))
    canvas.create_window(645, 150, window=clear_button)

    # Buttons
    addition_button = Button(canvas, text="+", width=10, height=3, command=lambda: add_entry("+"))
    canvas.create_window(800, 430, window=addition_button)
    subtraction_button = Button(canvas, text="-", width=10, height=3, command=lambda: add_entry("-"))
    canvas.create_window(800, 360, window=subtraction_button)
    multiplication_button = Button(canvas, text="x", width=10, height=3, command=lambda: add_entry("x"))
    canvas.create_window(800, 290, window=multiplication_button)
    division_button = Button(canvas, text="/", width=10, height=3, command=lambda: add_entry("/"))
    canvas.create_window(800, 220, window=division_button)

    # Calculate Button
    calculate_button = Button(canvas, text="=", width=10, height=3, command=calculate)
    canvas.create_window(710, 430, window=calculate_button)

    gui.mainloop()

def add_entry(entry):
    """ Add The passed entry to the Entry box! (Insertion at end) """
    value = box.get()
    if entry in ["+", "-", "x", "/"]:
        if value not in ["", " "]:
            if value[-1] not in ["+", "-", "x", "/"]:
                box.insert(len(value), str(entry))
            else:
                messagebox.showerror("Error!", "You can't add same symbol twice!")
        else:
            messagebox.showerror("Error!", "The Field is empty!")
    else:
        box.insert(len(value), str(entry))

def remove_entry(entry):
    """ Removes the passed entry! """
    value = box.get()
    if entry == "end": # Backspace button
        """ Removes the last added entry! (Deletion at end) """
        box.delete(len(value)-1)
    else: # Clear Button
        """ Removes everything in the entrybox! """
        box.delete(0, len(value))

def calculate():
    """ Calculate the Query """
    query = box.get().replace("x", "*")
    if query not in ("", " "):
        ans = eval(query)
        box.delete(0, len(query))
        box.insert(1, str(ans))
    

calculator()