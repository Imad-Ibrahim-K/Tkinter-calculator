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


but_frame = Frame(window, width=312, height=272.5, bg="grey")
#
Bt1 = Button(window, text=" 1 ", command=lambda: on_click("1"))
Bt2 = Button(window, text=" 2 ", command=lambda: on_click("2"))
Bt3 = Button(window, text=" 3 ", command=lambda: on_click("3"))
Bt4 = Button(window, text=" 4 ", command=lambda: on_click("4"))
Bt5 = Button(window, text=" 5 ", command=lambda: on_click("5"))
Bt6 = Button(window, text=" 6 ", command=lambda: on_click("6"))
Bt7 = Button(window, text=" 7 ", command=lambda: on_click("7"))
Bt8 = Button(window, text=" 8 ", command=lambda: on_click("8"))
Bt9 = Button(window, text=" 9 ", command=lambda: on_click("9"))
Bt0 = Button(window, text=" 0 ", command=lambda: on_click("0"))

Btdiv = Button(window, text=" / ", command=lambda: on_click("/"))
Btadd = Button(window, text=" + ", command=lambda: on_click("+"))
Btminus = Button(window, text=" - ", command=lambda: on_click("-"))

Btc = Button(window, text=" C ", command=lambda: clear())

#
text_display.grid(row=0, column=0, columnspan=20, padx=10, pady=10)
Bt1.grid(row=1, column=0, padx=10, pady=10)
Bt2.grid(row=2, column=0, padx=10, pady=10)
Btm.grid(row=2, column=1, padx=10, pady=10)
Btc.grid(row=2, column=2, padx=10, pady=10)

window.mainloop()
