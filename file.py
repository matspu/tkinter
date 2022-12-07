from tkinter import *
from random import randint
import time


width = 1000
height = 1000
canvas = Canvas(width=width, height=height, bg="lightblue")

canvas.pack()

x = 0
y = 0

tree_size = randint(30, 70)
present_size = 50


def present_animation():
    canvas.move("present", 0, 1)
    canvas.after(20, present_animation)

def tree_animation():
    canvas.move("tree", 0, 1)
    canvas.after(20, tree_animation)

def player(x, y):
    x = width // 2
    y = height // 2
    canvas.create_rectangle(x, y, x+100, y+180, fill="red", tag="player")




def tree(x, y):
    for i in range(5):
        y = 100
        x = randint(0, width-tree_size)
        canvas.create_oval(x, y, x+tree_size, y+tree_size, fill="green", outline="", tag="tree")
        tree_animation()

def present(x, y):
    for i in range(5):
        x = randint(0, width-present_size)
        canvas.create_rectangle(x, y, x+50, y+50, fill="red", outline="", tag="present")
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