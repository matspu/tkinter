from tkinter import *

canvas = Canvas(width=1000, height=1000)
canvas.pack()

vyska = int(input("výška: "))

a = 80
x = 500 - (a // 2)
y = 10

xStart = x
kocky = 1

def animacia():
    for j in range(vyska):
        for i in range(kocky):
            canvas.create_rectangle(x, y, x + a, y + a, fill="red", width=2)
            x += a
        y += a
        kocky += 2
        xStart -= a
        x = xStart
animacia()


mainloop()



# animacia lopty
from tkinter import *

canvas = Canvas(width=1000, height=1000)
canvas.pack()

x = 10
y = 500
a = 10

def animacia():
    global x
    canvas.delete('all')
    canvas.create_oval(x - a, y - a, x + a, y + a, fill="red", width=2)
    x += 10
    canvas.update()
    canvas.after(10, animacia)

animacia()

mainloop()




# mys
from tkinter import *

canvas = Canvas(width=1000, height=1000)
canvas.pack()

def klik(mys):
    x = mys.x
    y = mys.y
    print(mys)
    canvas.create_text(x, y, text="*", fill="red")

def hore(x):
    global x
    y -= 10


canvas.bind("<ButtonPress-1>", klik)
canvas.bind_all("<w>", hore)



#  animacia-move
from tkinter import *

canvas = Canvas(width=1000, height=1000)
canvas.pack()

x = 10
y = 500
a = 10

canvas.create_oval(
    x - a, y - a, x + a, y + a, fill="red", width=2, tag="lopta"
)
y += a
canvas.create_oval(
    x - a, y - a, x + a, y + a, fill="red", width=2, tag="lopta"
)

def animacia():
    canvas.move("lopta", 10, 0)
    a, b, c, d = canvas.coords("lopta")
    print(a)
    canvas.update()
    canvas.after(20, animacia)

animacia()

mainloop()