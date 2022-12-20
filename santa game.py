import random
import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Sledge Game")

# Create the canvas
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()

# Create the sledge
sledge_size = 50
sledge_x = 200
sledge_y = 250
sledge = canvas.create_rectangle(sledge_x - sledge_size / 2, sledge_y - sledge_size / 2,
                                 sledge_x + sledge_size / 2, sledge_y + sledge_size / 2,
                                 fill="red")

# Create the presents
present_size = 20
presents = []

def create_present():
    x = random.randint(0, 400)
    y = 0
    present = canvas.create_rectangle(x - present_size / 2, y - present_size / 2,
                                     x + present_size / 2, y + present_size / 2,
                                     fill="red")
    presents.append(present)
    window.after(1000, create_present)  # Schedule the next present to be created in 1 second

# Create the balls
ball_size = 20
balls = []

def create_ball():
    x = random.randint(0, 400)
    y = 0
    ball = canvas.create_oval(x - ball_size / 2, y - ball_size / 2,
                              x + ball_size / 2, y + ball_size / 2,
                              fill="green")
    balls.append(ball)
    window.after(1000, create_ball)  # Schedule the next ball to be created in 1 second

# Move the sledge
def move_sledge(event):
    if event.keysym == "Left":
        canvas.move(sledge, -20, 0)
    elif event.keysym == "Right":
        canvas.move(sledge, 20, 0)

canvas.bind_all("<KeyPress-Left>", move_sledge)
canvas.bind_all("<KeyPress-Right>", move_sledge)

# Move the presents and balls
def move_items():
    for present in presents:
        canvas.move(present, 0, 5)
    for ball in balls:
        canvas.move(ball, 0, 5)
    window.after(50, move_items)

# Start the present and ball spawning and movement
create_present()
create_ball()
move_items()

# Run the game loop
window.mainloop()






