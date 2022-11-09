import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

def panacikovia(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x-20, y-25, x+20, y+25)
    canvas.create_oval(x-20, y-65, x+20, y-25)
    canvas.create_text(x, y+35, text=entry1.get())

entry1 = tkinter.Entry()
entry1.pack()
canvas.bind_all('<Button-3>', panacikovia)
