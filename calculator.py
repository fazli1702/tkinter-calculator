import tkinter as tk

win = tk.Tk()

win.title('Calculator')
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

entry = tk.Entry(width = 30, textvariable = entry_text)
entry.grid(row = 0, column = 0, columnspan = 3)

# buttons
button_clear = tk.Button(text = 'C', width = 20, height = 4, command = lambda: clear())
button_clear.grid(row = 1, column = 0, columnspan = 2)

button_delete = tk.Button(text = u'\u232b', width = 10, height = 4, command = lambda: delete())
button_delete.grid(row = 1, column = 2)

# row 2
row = 2
button_1 = tk.Button(text = '1', width = 10, height = 4, command = lambda: click(1))
button_1.grid(row = row, column = 0)

button_2 = tk.Button(text = '2', width = 10, height = 4, command = lambda: click(2))
button_2.grid(row = row, column = 1)

button_3 = tk.Button(text = '3', width = 10, height = 4, command = lambda: click(3))
button_3.grid(row = row, column = 2)

# row 3
row = 3
button_4 = tk.Button(text = '4', width = 10, height = 4, command = lambda: click(4))
button_4.grid(row = row, column = 0)

button_5 = tk.Button(text = '5', width = 10, height = 4, command = lambda: click(5))
button_5.grid(row = row, column = 1)

button_6 = tk.Button(text = '6', width = 10, height = 4, command = lambda: click(6))
button_6.grid(row = row, column = 2)

# row 4
row = 4
button_7 = tk.Button(text = '7', width = 10, height = 4, command = lambda: click(7))
button_7.grid(row = row, column = 0)

button_8 = tk.Button(text = '8', width = 10, height = 4, command = lambda: click(8))
button_8.grid(row = row, column = 1)

button_9 = tk.Button(text = '9', width = 10, height = 4, command = lambda: click(9))
button_9.grid(row = row, column = 2)

# row 5
row = 5
button_0 = tk.Button(text = '0', width = 20, height = 4, command = lambda: click(0))
button_0.grid(row = row, column = 0, columnspan = 2)

button_dot = tk.Button(text = '.', width = 10, height = 4, command = lambda: click('.'))
button_dot.grid(row = row, column = 2)

# operators
col = 3
button_equal = tk.Button(text = '=', width = 10, height = 4, command = lambda: get_answer())
button_equal.grid(row = 5, column = col)

button_plus = tk.Button(text = '+', width = 10, height = 4, command = lambda: click('+'))
button_plus.grid(row = 4, column = col)

button_minus = tk.Button(text = '-', width = 10, height = 4, command = lambda: click('-'))
button_minus.grid(row = 3, column = col)

button_plus = tk.Button(text = '*', width = 10, height = 4, command = lambda: click('*'))
button_plus.grid(row = 2, column = col)

button_plus = tk.Button(text = u'\u00F7', width = 10, height = 4, command = lambda: click('/'))
button_plus.grid(row = 1, column = col)

win.mainloop()