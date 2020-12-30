import tkinter as tk

win = tk.Tk()

win.title('Calculator')
win.geometry('330x343')
win.resizable(0, 0)  # prevent resizing of window

EXPRESSION = ''  # math expression on screen

def click(item):
    global EXPRESSION
    EXPRESSION += str(item)
    set_entry()

def delete():
    global EXPRESSION
    EXPRESSION = EXPRESSION[:-1]
    set_entry()

def clear():
    global EXPRESSION
    EXPRESSION = ''
    set_entry()

def get_answer():
    global EXPRESSION
    try:
        answer = eval(EXPRESSION)
    except:
        EXPRESSION = 'ERROR'
        set_entry()
    else:
        EXPRESSION = str(answer)
        set_entry()

def set_entry():
    global EXPRESSION
    entry_text.set(EXPRESSION)


# input text - display user math expression
entry_text = tk.StringVar()

entry_frame = tk.Frame(win, width = 312, height = 50, bd = 0)
entry_frame.pack(side = tk.TOP)

entry = tk.Entry(entry_frame, font = ('arial', 18, 'bold') , width = 50, textvariable = entry_text, justify = tk.RIGHT)
entry.grid(row = 0, column = 0)
entry.pack(ipady = 10)

# buttons
padx, pady = 1, 1

button_frame = tk.Frame(win, width = 312, height = 272.5, bg = 'grey')
button_frame.pack()

button_clear = tk.Button(button_frame, text = 'C', width = 22, height = 3, bg = 'lightgrey', command = lambda: clear()).grid(row = 1, column = 0, columnspan = 2, padx = padx, pady = pady)

button_delete = tk.Button(button_frame, text = u'\u232b', width = 10, height = 3, bg = 'lightgrey', command = lambda: delete()).grid(row = 1, column = 2, padx = padx, pady = pady)

# row 2
row = 2
button_1 = tk.Button(button_frame, text = '1', width = 10, height = 3, bg = 'white', command = lambda: click(1)).grid(row = row, column = 0, padx = padx, pady = pady)

button_2 = tk.Button(button_frame, text = '2', width = 10, height = 3, bg = 'white', command = lambda: click(2)).grid(row = row, column = 1, padx = padx, pady = pady)

button_3 = tk.Button(button_frame, text = '3', width = 10, height = 3, bg = 'white', command = lambda: click(3)).grid(row = row, column = 2, padx = padx, pady = pady)

# row 3
row = 3
button_4 = tk.Button(button_frame, text = '4', width = 10, height = 3, bg = 'white', command = lambda: click(4)).grid(row = row, column = 0, padx = padx, pady = pady)

button_5 = tk.Button(button_frame, text = '5', width = 10, height = 3, bg = 'white', command = lambda: click(5)).grid(row = row, column = 1, padx = padx, pady = pady)

button_6 = tk.Button(button_frame, text = '6', width = 10, height = 3, bg = 'white', command = lambda: click(6)).grid(row = row, column = 2, padx = padx, pady = pady)

# row 4
row = 4
button_7 = tk.Button(button_frame, text = '7', width = 10, height = 3, bg = 'white', command = lambda: click(7)).grid(row = row, column = 0, padx = padx, pady = pady)

button_8 = tk.Button(button_frame, text = '8', width = 10, height = 3, bg = 'white', command = lambda: click(8)).grid(row = row, column = 1, padx = padx, pady = pady)

button_9 = tk.Button(button_frame, text = '9', width = 10, height = 3, bg = 'white', command = lambda: click(9)).grid(row = row, column = 2, padx = padx, pady = pady)

# row 5
row = 5
button_0 = tk.Button(button_frame, text = '0', width = 22, height = 3, bg = 'white', command = lambda: click(0)).grid(row = row, column = 0, columnspan = 2, padx = padx, pady = pady)

button_dot = tk.Button(button_frame, text = '.', width = 10, height = 3, bg = 'white', command = lambda: click('.')).grid(row = row, column = 2, padx = padx, pady = pady)

# operators
col = 3
button_equal = tk.Button(button_frame, text = '=', width = 10, height = 3, bg = 'lightgrey', command = lambda: get_answer()).grid(row = 5, column = col, padx = padx, pady = pady)

button_plus = tk.Button(button_frame, text = '+', width = 10, height = 3, bg = 'lightgrey', command = lambda: click('+')).grid(row = 4, column = col, padx = padx, pady = pady)

button_minus = tk.Button(button_frame, text = '-', width = 10, height = 3, bg = 'lightgrey', command = lambda: click('-')).grid(row = 3, column = col, padx = padx, pady = pady)

button_multiply = tk.Button(button_frame, text = '*', width = 10, height = 3, bg = 'lightgrey', command = lambda: click('*')).grid(row = 2, column = col, padx = padx, pady = pady)

button_divide = tk.Button(button_frame, text = u'\u00F7', width = 10, height = 3, bg = 'lightgrey', command = lambda: click('/')).grid(row = 1, column = col, padx = padx, pady = pady)

win.mainloop()