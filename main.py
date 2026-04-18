import tkinter as tk
import turtle

window = tk.Tk()
window.title("Turtle Control")

button_panel = tk.Frame(window)
button_panel.pack(side="left", padx=10, pady=10)

canvas = tk.Canvas(window, width=600, height=500)
canvas.pack(side="right")

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.speed(0)

def reset_turtle():
    t.clear()
    t.penup()
    t.home()
    t.setheading(0)
    t.pensize(1)
    t.pencolor("black")
    t.pendown()

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

def move_forward():
    t.forward(50)

def reset():
    reset_turtle()

def draw_square():
    reset_turtle()
    size = 120
    small = 22

    # Big square - black
    t.pencolor("black")
    t.pensize(2)
    t.penup()
    t.goto(-size/2, -size/2)
    t.setheading(0)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.left(90)

    # Small squares - red, starting exactly from each corner outward
    t.pencolor("red")
    t.pensize(2)
    corners = [
        (-size/2 - small, -size/2 - small),  # bottom left
        ( size/2,         -size/2 - small),  # bottom right
        ( size/2,          size/2),           # top right
        (-size/2 - small,  size/2),           # top left
    ]
    for corner in corners:
        t.penup()
        t.goto(corner[0], corner[1])
        t.setheading(0)
        t.pendown()
        for i in range(4):
            t.forward(small)
            t.left(90)

def draw_star():
    reset_turtle()
    t.pencolor("red")
    t.pensize(4)
    for i in range(5):
        t.forward(180)
        t.right(144)

def koch_edge(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch_edge(length / 3, depth - 1)
        t.left(60)
        koch_edge(length / 3, depth - 1)
        t.right(120)
        koch_edge(length / 3, depth - 1)
        t.left(60)
        koch_edge(length / 3, depth - 1)

def draw_snowflake():
    reset_turtle()
    t.pensize(1)
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()
    for i in range(3):
        koch_edge(300, 3)
        t.right(120)

def tree1(length, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(30)
    tree1(length * 0.7, depth - 1)
    t.right(60)
    tree1(length * 0.7, depth - 1)
    t.left(30)
    t.backward(length)

def draw_tree1():
    reset_turtle()
    t.pensize(1)
    t.penup()
    t.goto(-80, -180)
    t.setheading(90)
    t.pendown()
    tree1(80, 6)

def tree2(length, depth):
    if depth == 0:
        return
    t.pensize(1)
    t.forward(length)
    t.left(25)
    tree2(length * 0.65, depth - 1)
    t.right(50)
    tree2(length * 0.65, depth - 1)
    t.left(25)
    t.backward(length)

def draw_tree2():
    reset_turtle()
    t.pensize(1)
    t.penup()
    t.goto(80, -180)
    t.setheading(90)
    t.pendown()
    tree2(80, 7)

tk.Label(button_panel, text="Control", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(button_panel, text="Turn Left", width=15, command=turn_left).pack(pady=3)
tk.Button(button_panel, text="Turn Right", width=15, command=turn_right).pack(pady=3)
tk.Button(button_panel, text="Move Forward", width=15, command=move_forward).pack(pady=3)
tk.Button(button_panel, text="Reset", width=15, command=reset).pack(pady=3)

tk.Label(button_panel, text="Shapes", font=("Arial", 10, "bold")).pack(pady=5)
tk.Button(button_panel, text="Square", width=15, command=draw_square).pack(pady=3)
tk.Button(button_panel, text="Star", width=15, command=draw_star).pack(pady=3)
tk.Button(button_panel, text="Snowflake", width=15, command=draw_snowflake).pack(pady=3)
tk.Button(button_panel, text="Tree 1", width=15, command=draw_tree1).pack(pady=3)
tk.Button(button_panel, text="Tree 2", width=15, command=draw_tree2).pack(pady=3)

window.mainloop()
