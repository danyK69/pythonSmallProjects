import tkinter as tk

ob = tk.Tk()

ob.title('Calculator')
text = tk.Entry(ob, width=120, borderwidth=2)
text.grid(row=0, column=0, columnspan=4)


def on_click(n):
    first = text.get()
    text.delete(0,tk.END)
    text.insert(0,str(first) + str(n))

def addition():
    first = text.get()
    global first_num
    global label
    label = 'add'
    first_num = int(first)
    text.delete(0,tk.END)

def substraction():
    first = text.get()
    global first_num
    global label
    label = 'sub'
    first_num = int(first)
    text.delete(0,tk.END)
    return

def multiply():
    first = text.get()
    global first_num
    global label
    label = 'multiply'
    first_num = int(first)
    text.delete(0,tk.END)
    return

def divide():
    first = text.get()
    global first_num
    global label
    label = 'divide'
    first_num = int(first)
    text.delete(0,tk.END)
    return

def calculate():
    next_num = text.get()
    text.delete(0,tk.END)
    if label =='add':
        text.insert(0, first_num + int(next_num))
    elif  label == 'sub':
        text.insert(0, first_num - int(next_num))
    elif label == 'multiply':
        text.insert(0, first_num * int(next_num))
    elif label == 'divide':
        text.insert(0, first_num / int(next_num))
    else:
        pass

#creating the various buttons

number1 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(1))
number1.grid(row=1, column=0, columnspan=1)
tk.Label(ob, text="1").grid(row=1, column=0)

number2 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(2))
number2.grid(row=1, column=1, columnspan=1)
tk.Label(ob, text="2").grid(row=1, column=1)

number3 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(3))
number3.grid(row=1, column=2, columnspan=1)
tk.Label(ob, text="3").grid(row=1, column=2)

number4 = tk.Button(ob,height=2, width=25, borderwidth=2, command=addition)
number4.grid(row=1, column=3, columnspan=1)
tk.Label(ob, text="+").grid(row=1, column=3)

number5 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(4))
number5.grid(row=2, column=0, columnspan=1)
tk.Label(ob, text="4").grid(row=2, column=0)

number6 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(5))
number6.grid(row=2, column=1, columnspan=1)
tk.Label(ob, text="5").grid(row=2, column=1)

number7 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(6))
number7.grid(row=2, column=2, columnspan=1)
tk.Label(ob, text="6").grid(row=2, column=2)

number8 = tk.Button(ob,height=2, width=25, borderwidth=2, command= substraction)
number8.grid(row=2, column=3, columnspan=1)
tk.Label(ob, text="-").grid(row=2, column=3)


number9 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(7))
number9.grid(row=3, column=0, columnspan=1)
tk.Label(ob, text="7").grid(row=3, column=0)

number10 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(8))
number10.grid(row=3, column=1, columnspan=1)
tk.Label(ob, text="8").grid(row=3, column=1)

number11 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(9))
number11.grid(row=3, column=2, columnspan=1)
tk.Label(ob, text="9").grid(row=3, column=2)

number12 = tk.Button(ob,height=2, width=25, borderwidth=2, command= multiply)
number12.grid(row=3, column=3, columnspan=1)
tk.Label(ob, text="X").grid(row=3, column=3)

number13 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : on_click(0))
number13.grid(row=4, column=0, columnspan=1)
tk.Label(ob, text="0").grid(row=4, column=0)

number14 = tk.Button(ob,height=2, width=25, borderwidth=2, command= divide)
number14.grid(row=4, column=1, columnspan=1)
tk.Label(ob, text="/").grid(row=4, column=1)

number15 = tk.Button(ob,height=2, width=25, borderwidth=2, command= calculate)
number15.grid(row=4, column=2, columnspan=1)
tk.Label(ob, text="=").grid(row=4, column=2)

number16 = tk.Button(ob,height=2, width=25, borderwidth=2, command=lambda : text.delete(0, tk.END))
number16.grid(row=4, column=3, columnspan=1)
tk.Label(ob, text="C").grid(row=4, column=3)

ob.mainloop()