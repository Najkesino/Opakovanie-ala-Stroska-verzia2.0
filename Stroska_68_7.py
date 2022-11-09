import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

stop = 0
cas = 60
spravny = random.choice(('blue', 'red', 'yellow', 'green'))

def casovac():
    global cas
    canvas.delete('odpocet')
    canvas.create_text(350, 350, text=str(cas), font='Arial 30 bold', fill='red', tags='odpocet')
    cas -= 1
    if stop == 0:
        canvas.update()
        canvas.after(1000, casovac)
casovac()

def bomba_jako_RYTMUS(farba):
    if cas <= 0:
        canvas.delete('all')
        canvas.create_text(350, 200, text='Vybuchol si', fill='red', font='Arial 20 bold')
        stop = 1
    if farba == spravny:
        canvas.delete('all')
        canvas.create_text(350, 200, text='Nice cock BRO', fill='red', font='Arial 20 bold')
        stop = 1

button1 = tkinter.Button(text='Modrý káblik', command=bomba_jako_RYTMUS('blue'))
button1.pack()
button2 = tkinter.Button(text='Červený káblik', command=bomba_jako_RYTMUS('red'))
button2.pack()
button3 = tkinter.Button(text='Žltý káblik', command=bomba_jako_RYTMUS('yellow'))
button3.pack()
button4 = tkinter.Button(text='Zelený káblik', command=bomba_jako_RYTMUS('green'))
button4.pack()
