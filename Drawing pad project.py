from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()
root.title("Drawing Pad")
root.geometry("900x600")

current_color = "black"
brush_size = 5

canvas = Canvas(root, bg="white", width=800, height=500)
canvas.pack(pady=20)

last_x = None
last_y = None

def set_color(color):
    global current_color
    current_color = color

def choose_color():
    global current_color
    color = askcolor()[1]
    if color:
        current_color = color

def set_brush_size(size):
    global brush_size
    brush_size = size

def start_draw(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(
        last_x,
        last_y,
        event.x,
        event.y,
        fill=current_color,
        width=brush_size,
        capstyle=ROUND,
        smooth=True
    )
    last_x = event.x
    last_y = event.y

def clear_canvas():
    canvas.delete("all")

frame = Frame(root)
frame.pack()

Button(frame, text="Black", bg="black", fg="white",
       command=lambda: set_color("black")).grid(row=0, column=0)

Button(frame, text="Red", bg="red",
       command=lambda: set_color("red")).grid(row=0, column=1)

Button(frame, text="Blue", bg="blue", fg="white",
       command=lambda: set_color("blue")).grid(row=0, column=2)

Button(frame, text="Green", bg="green", fg="white",
       command=lambda: set_color("green")).grid(row=0, column=3)

Button(frame, text="Choose Color",
       command=choose_color).grid(row=0, column=4)

Button(frame, text="Eraser",
       command=lambda: set_color("white")).grid(row=0, column=5)

Button(frame, text="Clear",
       command=clear_canvas).grid(row=0, column=6)

Scale(frame, from_=1, to=20,
      orient=HORIZONTAL,
      label="Brush Size",
      command=lambda x: set_brush_size(int(x))).grid(row=0, column=7)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()