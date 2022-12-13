from tkinter import *

window = Tk()
window.geometry("350x500")
# window.maxsize(350, 500)
# window.minsize(350, 500)
window.resizable(0, 0)
window.title("Tkinter-Calculator")


expression = ""
text_values = StringVar()

text_display = Entry(window, width=30, textvariable=text_values, font="size=60", justify="right")


def on_click(text):
    global expression
    expression = expression + str(text)
    text_values.set(expression)


#
Bt1 = Button(window, text=" 1 ", command=lambda: on_click(1))
Bt2 = Button(window, text=" 2 ", command=lambda: on_click(2))
Btm = Button(window, text=" - ", command=lambda: on_click("-"))
# # Bt3 = Button(window, text= " 2 ", command=lambda: on_click("2"))

#
text_display.grid(row=0, column=0, columnspan=20, padx=10, pady=10)
Bt1.grid(row=1, column=0, padx=10, pady=10)
Bt2.grid(row=2, column=0, padx=10, pady=10)
Btm.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
