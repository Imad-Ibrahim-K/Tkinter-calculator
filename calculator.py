from tkinter import *

window = Tk()
window.geometry("350x500")
text_display = Entry(window, width=30, font="size=60")
# text_display.configure(state='disabled')


def on_click(text):
    text_display.insert(0, text)


text_display.pack(padx=20, pady=10)

Bt1 = Button(window, text=" 1 ", command=lambda: on_click("1"))
Bt1.pack()


window.mainloop()
