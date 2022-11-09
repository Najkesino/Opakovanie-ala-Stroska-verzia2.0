import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

body = 0

def kocky():
    global cislo1, cislo2
    canvas.delete('all')
    canvas.create_text(50, 20, text='Tvoje skore je: '+str(body))
    cislo1, cislo2 = random.randint(1, 6), random.randint(1, 6)
    canvas.create_rectangle(100, 100, 250, 250)
    canvas.create_text(175, 175, text=cislo1, font='Arial 20 bold')
    canvas.create_rectangle(260, 100, 410, 250)
    canvas.create_text(335, 175, text=cislo2, font='Arial 20 bold')
    canvas.update()
    canvas.after(1000, kocky)
kocky()

def skore(event):
    global body
    if cislo1 == cislo2:
        body += 2
    elif cislo1 != cislo2:
        body -= 1

canvas.bind_all('<Button-1>', skore)
