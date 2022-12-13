from tkinter import *
from random import randint
import time


width = 1000
height = 1000
canvas = Canvas(width=width, height=height, bg="lightblue")

canvas.pack()

x = 0
y = 0

tree_size = 100
present_size = 50


def present_animation():
    canvas.move("present", 0, 1)
    canvas.after(20, present_animation)

def tree_animation():
    canvas.move("tree", 0, 1)
    canvas.after(20, tree_animation)

def player(x, y):
    x = width // 2
    y = height - 200
    canvas.create_line(x-30, y-30, x-30, y+200, fill="brown", width="8", tag="player")
    canvas.create_line(x+120, y-30, x+120, y+200, fill="brown", width="8", tag="player")
    #lines 
    canvas.create_line(x-30, y+20, x+120, y+20, fill="brown", width="8", tag="player")
    canvas.create_line(x-30, y+72, x+120, y+72, fill="brown", width="8", tag="player")
    canvas.create_line(x-30, y+132, x+120, y+132, fill="brown", width="8", tag="player")
    
    canvas.create_rectangle(x, y, x+90, y+160, fill="red", tag="player")

    canvas.create_line(x+10, y+70, x+10, y+150, fill="brown", width="7", tag="player")
    canvas.create_line(x+7, y+150, x+80, y+150, fill="brown", width="7", tag="player")
    canvas.create_line(x+80, y+154, x+80, y+70, fill="brown", width="7", tag="player")

    canvas.create_rectangle(x+20, y+90, x+70, y+140, fill="yellow", tag="player")




def tree(x, y):
    for i in range(5):
        y = 100
        x = randint(0, width-tree_size)
        canvas.create_oval(x, y, x+tree_size, y+tree_size, fill="#485e52", outline="", tag="tree")
        canvas.create_oval(x+(tree_size//6), y+(tree_size//6), x+(tree_size*5//6), y+(tree_size*5//6), fill="#587e60", outline="", tag="tree")
        canvas.create_oval(x+(tree_size//3), y+(tree_size//3), x+(tree_size*2//3), y+(tree_size*2//3), fill="#5f926a", outline="", tag="tree")
        tree_animation()

def present(x, y):
    for i in range(5):
        x = randint(0, width-present_size)
        canvas.create_rectangle(x, y, x+75, y+75, fill="#FF3D4E", outline="", tag="present")
        canvas.create_rectangle(x, y+32, x+75, y+43, fill="white", outline="", tag="present")
        canvas.create_rectangle(x+32, y+0, x+43, y+75, fill="white", outline="", tag="present")
        present_animation()



player(x, y)
tree(x, y)
present(x, y)

def move_left(e):
    canvas.move("player", -20, 0)


def move_right(e):
    canvas.move("player", 20, 0)

def move_up(e):
    canvas.move("player", 0, -20)

def move_down(e):
    canvas.move("player", 0, 20)


    

canvas.bind_all("<Left>", move_left)
canvas.bind_all("<Right>", move_right)
canvas.bind_all("<Up>", move_up)
canvas.bind_all("<Down>", move_down)

    


#def move_right():



mainloop()




