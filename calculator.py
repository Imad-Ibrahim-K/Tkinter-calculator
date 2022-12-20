from tkinter import *

window = Tk()
window.geometry("350x500")
window.resizable(0, 0)
window.title("Tkinter-Calculator")

text_values = StringVar()
text_display = Entry(window,
                     width=30,
                     textvariable=text_values, font="size=60",
                     justify="right")
expression = ""


def on_click(text):
    global expression
    expression = expression + text
    text_values.set(expression)


def clear():
    global expression
    expression = ""
    text_values.set("")


def equalto():
    global expression
    result = eval(expression)
    text_values.set(result)


def back():
    global expression
    back_value = expression[:-1]
    expression = back_value
    text_values.set(expression)


Bt1 = Button(window, text=" 1 ", command=lambda: on_click("1"), width=7, height=2)
Bt2 = Button(window, text=" 2 ", command=lambda: on_click("2"), width=7, height=2)
Bt3 = Button(window, text=" 3 ", command=lambda: on_click("3"), width=7, height=2)
Bt4 = Button(window, text=" 4 ", command=lambda: on_click("4"), width=7, height=2)
Bt5 = Button(window, text=" 5 ", command=lambda: on_click("5"), width=7, height=2)
Bt6 = Button(window, text=" 6 ", command=lambda: on_click("6"), width=7, height=2)
Bt7 = Button(window, text=" 7 ", command=lambda: on_click("7"), width=7, height=2)
Bt8 = Button(window, text=" 8 ", command=lambda: on_click("8"), width=7, height=2)
Bt9 = Button(window, text=" 9 ", command=lambda: on_click("9"), width=7, height=2)
Bt0 = Button(window, text=" 0 ", command=lambda: on_click("0"), width=7, height=2)
Btd = Button(window, text=" . ", command=lambda: on_click("."), width=7, height=2)
Btdel = Button(window, text=" < ", command=lambda: back(), width=16, height=2)


Btdiv = Button(window, text=" / ", command=lambda: on_click("/"), width=7, height=2)
Btadd = Button(window, text=" + ", command=lambda: on_click("+"), width=7, height=2)
Btminus = Button(window, text=" - ", command=lambda: on_click("-"), width=7, height=2)
Btx = Button(window, text=" * ", command=lambda: on_click("*"), width=7, height=2)


Btq = Button(window, text=" = ", command=lambda: equalto(), width=16, height=2)
Btc = Button(window, text=" C ", command=lambda: clear(), width=16, height=2)


text_display.grid(row=0, column=0, columnspan=20, padx=10, pady=20)

Bt7.grid(row=2, column=1, pady=3)
Bt8.grid(row=2, column=2)
Bt9.grid(row=2, column=3)

Bt4.grid(row=3, column=1, pady=3)
Bt5.grid(row=3, column=2)
Bt6.grid(row=3, column=3)

Bt1.grid(row=4, column=1, pady=3)
Bt2.grid(row=4, column=2)
Bt3.grid(row=4, column=3)

Btd.grid(row=5, column=1)
Bt0.grid(row=5, column=2)
Btq.grid(row=5, column=3, columnspan=2)

Btadd.grid(row=4, column=4)
Btminus.grid(row=3, column=4)
Btx.grid(row=2, column=4)

Btc.grid(row=1, column=1, columnspan=2)
Btdel.grid(row=1, column=3, columnspan=2)

window.mainloop()
