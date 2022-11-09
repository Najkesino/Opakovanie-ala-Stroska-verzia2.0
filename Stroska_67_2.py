import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

canvas.create_rectangle(0, 400, 700, 700, fill='blue', outline='')
def lodka_balon(event):
    x = event.x
    y = event.y
    if y <= 300:
        canvas.create_oval(x-25, y-25, x+25, y+25)
        canvas.create_rectangle(x-20, y+50, x+20, y+70)
        canvas.create_line(x-25, y+8, x, y+50, x+25, y+8)
    elif y > 400:
        canvas.create_line(x-30, y, x+30, y, x+15, y+20, x-15, y+20, x-30, y)
        canvas.create_line(x, y, x, y-30, x+15, y-15, x, y)


canvas.bind_all('<Button-3>', lodka_balon)
