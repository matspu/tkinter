from tkinter import *


canvas = Canvas(height="1000", width="1000")
canvas.pack()

#x = int(input("x: "))
#y = int(input("y: "))
x = 10
y = 10
s = int(input("size: "))

# house
def house(x, y):
    # wall
    canvas.create_rectangle(x, y, x+(s/2), y+(s/2), fill="green")
    # roof
    canvas.create_polygon(x, y, x+(s/4), y-(s*(2/6)), x+s/2, y, fill="red")
    # door
    canvas.create_rectangle(x+s*(1/8), y+s*(1/2), x+s*(3/8), y+s*(1/4), fill="blue")
    # 3d roof
    canvas.create_polygon(x+s/2, y, x+s, y-s*(1/6), x+s*(3/4), y-s*(3/6), x+(s/4), y-(s*(2/6)))
    #3d wall
    canvas.create_polygon(x+(s/2), y, x+(s/2), y+(s/2), x+s, y+s*(2/6), x+s, y-s*(1/6), fill="pink")
    # window
    canvas.create_polygon(x+s*(5/9), y+s*(1/15), x+s*(5/9), y+s*(2/8), x+s*(14/15), y+s*(1/8), x+s*(14/15), y-s*(1/15),  fill="orange")

for i in range(8):
    house(x, y)
    x += 100
    y += 100





mainloop()


