Here i used pycham.
First i import Tkinter module (Tkinter is a GUI library for Python),
after that i used Tk() (Tk is interface) Then 

![alt text](https://github.com/Imad-Ibrahim-K/Tkinter-calculator/blob/main/images/Tkinter1.png)

Then i added mainloop() for loop the window,
and Window size sett to (350 x 500), Added text height and width [window = tk.Text(window, height=1, width=30)]
and also i added font size (60) [font="size=60"]

![alt text](https://github.com/Imad-Ibrahim-K/Tkinter-calculator/blob/main/images/Tkinter2.png)

and i give padding to text 
[wind = tk.Text(window, height=1, width=30, font="size=60")
wind.pack(pady=10)]

![alt text](https://github.com/Imad-Ibrahim-K/Tkinter-calculator/blob/main/images/Tkinter3.png)

after i (added padx =20)

![alt text](https://github.com/Imad-Ibrahim-K/Tkinter-calculator/blob/main/images/Tkinter4.png)

Set tex state to DISABLE to make Tkinter text read only
window.configure(state='DISABLE')]

Final igot pass the value to screen by using lambda function
Python Lambda Functions are anonymous function means that the function is
 without a name. As we already know that the def keyword is used to define
 a normal function in Python. Similarly, the lambda keyword is used to 
define an anonymous function in Python.

[

def on_click(text):
    text_display.insert(0, text)


Bt1 = Button(window, text=" 1 ", command=lambda: on_click("1"))
Bt1.pack()

]

set text left to right (justify = right)

added minimum and maximum size of window (350 x 500)
i change minimun and maximum size of window (350 x 500) to resizable(0, 0) so we 
can't change window size,created textvariable as text_values to set output to display values

last output

![alt text](https://github.com/Imad-Ibrahim-K/Tkinter-calculator/blob/main/images/Screeshort(21).png)









