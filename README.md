Here i used pycham.
First i import Tkinter module (Tkinter is a GUI library for Python),
after that i used Tk() (Tk is interface) Then 

add pic Tkinter1.png

Then i added mainloop() for loop the window,
and Window size sett to (350 x 500), Added text height and width [window = tk.Text(window, height=1, width=30)]
and also i added font size (60) [font="size=60"]

picture Tkinter2.png

and i give padding to text 
[wind = tk.Text(window, height=1, width=30, font="size=60")
wind.pack(pady=10)]

picture Tkinter.3

after i (added padx =20)

picture Tkinter4.png

Set tex state to DISABLE to make Tkinter text read only
[text_display.configure(state='disabled')]












