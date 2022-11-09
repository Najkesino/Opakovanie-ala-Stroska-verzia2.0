import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

x1 = -100
x2 = 600

def titulky():
    global x1, x2
    canvas.delete('all')
    x1 += 5
    x2 += 5
    canvas.create_text(x1, 650, text=entry1.get(), font='Arial 15 bold', fill='red')
    canvas.create_text(x2, 650, text=entry1.get(), font='Arial 15 bold', fill='red')
    if x1 >= 1300:
        x1 = -100
    if x2 >= 1300:
        x2 = -100
    canvas.update()
    canvas.after(10, titulky)

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Start', command=titulky)
button1.pack()
