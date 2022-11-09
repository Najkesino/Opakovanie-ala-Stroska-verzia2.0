import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

uhol = 0

def setric_obrazovky():
    global uhol
    x = random.randint(20, 680)
    y = random.randint(20, 680)
    farba = random.choice(('red', 'blue', 'green', 'black', 'lime', 'pink', 'yellow', 'aqua'))
    canvas.create_text(x, y, text=entry1.get(), font='Arial 15 bold', fill=farba, angle = uhol, tags='pismo')
    uhol += 10
    if uhol >= 90:
        uhol = 10
    canvas.update()
    canvas.after(1000, setric_obrazovky)

def vymaz_to_uz_do_psej_matere_lebo_mam_nervy_uz(event):
    canvas.delete('all')
    
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Start', command=setric_obrazovky)
button1.pack()
canvas.bind_all('Button-3', vymaz_to_uz_do_psej_matere_lebo_mam_nervy_uz)

