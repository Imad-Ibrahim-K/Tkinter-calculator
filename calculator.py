import tkinter as tk

window = tk.Tk()
window.geometry("350x500")
text_display = tk.Text(window, height=1, width=30, font="size=60")
text_display.configure(state='disabled')
text_display.pack(padx=20, pady=10)
window.mainloop()


