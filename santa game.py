from tkinter import *
from random import *


def vytvorStrom():
    global stromy
    global poradie

    znacka = f"strom-{poradie}"

    tree_size = 80
    x = randint(0, SIRKA-tree_size)
    y = -150
    tree_1 = canvas.create_oval(x, y, x+tree_size, y+tree_size, fill="#485e52", outline="", tag=znacka)
    tree_2 = canvas.create_oval(x+(tree_size//6), y+(tree_size//6), x+(tree_size*5//6), y+(tree_size*5//6), fill="#587e60", outline="", tag=znacka)
    tree_3 = canvas.create_oval(x+(tree_size//3), y+(tree_size//3), x+(tree_size*2//3), y+(tree_size*2//3), fill="#5f926a", outline="", tag=znacka)
    stromy.append(znacka)
    poradie += 1


def zmazStrom(znacka):
    canvas.delete(znacka)
    stromy.remove(znacka)

def vytvorDarcek():
    global darceky
    global poradie

    znacka = f"darcek-{poradie}"

    present_size = 80
    x = randint(0, SIRKA-present_size)
    y = -150
    canvas.create_rectangle(x, y, x+75, y+75, fill="#FF3D4E", outline="", tag=znacka)
    canvas.create_rectangle(x, y+32, x+75, y+43, fill="white", outline="", tag=znacka)
    canvas.create_rectangle(x+32, y+0, x+43, y+75, fill="white", outline="", tag=znacka)

    darceky.append(znacka)
    poradie += 1


def zmazDarcek(znacka):
    canvas.delete(znacka)
    darceky.remove(znacka)


def vytvorGulu():
    global gule
    global poradie

    znacka = f"darcek-{poradie}"
    ball_size = 30
    x = randint(0, SIRKA-ball_size)
    y = -50
    canvas.create_oval(x, y, x+ball_size, y+ball_size, outline="black", tag=znacka);
    gule.append(znacka)
    poradie += 1


def zmazGulu(znacka):
    canvas.delete(znacka)
    gule.remove(znacka)


def animacia():
    global tick
    global score

    tick += 1
    if tick > 30:
        tick = 0
        vytvorStrom()
        vytvorDarcek()
        vytvorGulu()


    for strom in stromy.copy():
        canvas.move(strom, 0, KROK)
        x1, y1, x2, y2 = canvas.coords(strom)
        x1Sane, y1Sane, x2Sane, y2Sane = canvas.coords("collider")
        if x1 < x2Sane and x2 > x1Sane and y1 < y2Sane and y2 > y1Sane:
            canvas.create_text(SIRKA // 2, VYSKA // 2, text="Koniec hry", font="Arial 50", fill="red")
            return
        
        if y1 > VYSKA:
            zmazStrom(strom)

    for darcek in darceky.copy():
        canvas.move(darcek, 0, KROK)
        x3, y3, x4, y4 = canvas.coords(darcek)
        x1Sane, y1Sane, x2Sane, y2Sane = canvas.coords("collider")
        if x3 < x2Sane and x4 > x1Sane and y3 < y2Sane and y4 > y1Sane:
            scoreText = canvas.create_text(SIRKA-50, 50, text=score, font="Arial 40", fill="red")
            score+=1

        if y3 > VYSKA:
            zmazDarcek(darcek)

    for gula in gule.copy():
        canvas.move(gula, 0, KROK)
        x5, y5, x6, y6 = canvas.coords(gula)
        x1Sane, y1Sane, x2Sane, y2Sane = canvas.coords("collider")
        if x5 < x2Sane and x6 > x1Sane and y5 < y2Sane and y6 > y1Sane:
            canvas.create_text(SIRKA // 2, VYSKA // 2, text="Koniec hry", font="Arial 50", fill="red")
            return
        if y5 > VYSKA:
            zmazGulu(gula)
        


    canvas.after(40, animacia)


def saneVpravo(event):
    canvas.move("sane", 10, 0)
    canvas.move("collider", 10, 0)

def saneVlavo(event):
    canvas.move("sane", -10, 0)
    canvas.move("collider", -10, 0)


# Hlavn?? program (Odtia??to sa spust?? program)
SIRKA = 700
VYSKA = 900
canvas = Canvas(width=SIRKA, height=VYSKA, bg="lightblue")
canvas.pack()

KROK = 10



stromy = []   
darceky = []
gule = []
tick = 0        
poradie = 1    
score = 0

scoreText = canvas.create_text(SIRKA-50, 50, text=score, font="Arial 40", fill="red")


# Vytvor sane
x = SIRKA // 2 -50
y = VYSKA - 220
# hlavne ??iary
canvas.create_rectangle(x-30, y-20, x+120, y+180, tag="collider")
canvas.create_line(x-30, y-20, x-30, y+180, fill="#003049", width="10", tag="sane")
canvas.create_line(x+120, y-20, x+120, y+180, fill="#003049", width="10", tag="sane")
#lines 
canvas.create_line(x-30, y+20, x+120, y+20, fill="#20639B", width="8", tag="sane")
canvas.create_line(x-30, y+72, x+120, y+72, fill="#20639B", width="8", tag="sane")
canvas.create_line(x-30, y+132, x+120, y+132, fill="#20639B", width="8", tag="sane")
# sledge
canvas.create_rectangle(x, y, x+90, y+160, fill="#FCBF49", outline="", tag="sane")

canvas.create_line(x+10, y+85, x+10, y+150, fill="#F77F00", width="7", tag="sane")
canvas.create_line(x+7, y+150, x+80, y+150, fill="#F77F00", width="7", tag="sane")
canvas.create_line(x+80, y+154, x+80, y+85, fill="#F77F00", width="7", tag="sane")

canvas.create_rectangle(x+20, y+90, x+70, y+140, fill="#EAE287", outline="", tag="sane")


canvas.bind_all("<Right>", saneVpravo)
canvas.bind_all("<Left>", saneVlavo)


vytvorStrom()
vytvorDarcek()
vytvorGulu()

# Spusti anim??ciu
animacia()

mainloop()
