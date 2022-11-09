import tkinter, random
canvas = tkinter.Canvas(width = 500, height = 500, bg='white')
canvas.pack()

stopka = 0
pocet = 0
mx = 300
my = 350
y = 0
priemer = 0

def miska():
    canvas.create_oval(150, 300, 450, 400)
    canvas.create_oval(150, 250, 450, 350)
    canvas.create_line(150, 350, 150, 300)
    canvas.create_line(450, 350, 450, 300)
miska()

def mlaka():
    canvas.delete('vodiška', 'textik')
    canvas.create_text(100, 10, text='Počet kvapiek je : '+str(pocet), tags='textik')
    canvas.create_oval(mx-priemer, my-priemer/3, mx+priemer, my+priemer/3, fill='blue', tags='vodiška')
    
def kvapkanie():
    canvas.delete('kvapka')
    global my, mx, priemer, y, pocet
    canvas.create_oval(290, y-10, 310, y+10, fill='blue', tags='kvapka')
    y += 10
    if y >= 350:
        y = 0
        if priemer < 150:
            priemer += 10
        pocet += 1
        mlaka()
    if stopka == 0:
        canvas.update()
        canvas.after(10, kvapkanie)
kvapkanie()

def stop(event):
    global stopka
    if stopka == 0:
        stopka = 1
    elif stopka == 1:
        stopka = 0
        kvapkanie()
     
canvas.bind_all('<Button-1>', stop)
