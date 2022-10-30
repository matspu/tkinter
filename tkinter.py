from tkinter import *


canvas = Canvas()
canvas.pack()

x = 50
y = 50
s = 1

# house
canvas.create_rectangle(x, y, x+50, y+50, fill="green")
canvas.create_polygon(x, y, x+25, y-25, x+50, y, fill="red")








mainloop()


