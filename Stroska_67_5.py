import tkinter, random
canvas = tkinter.Canvas(width = 700, height = 700, bg='white')
canvas.pack()

def semafor():
    canvas.delete('farby')
    moznost = random.randint(1, 5)
    canvas.create_rectangle(100, 100, 210, 440, fill='black', tags='farby')
    if moznost == 1:
        canvas.create_oval(105, 330, 205, 430, fill='lime', tags='farby')
    elif moznost == 2:
        canvas.create_oval(105, 220, 205, 320, fill='yellow', tags='farby')
    elif moznost == 3:
        canvas.create_oval(105, 110, 205, 210, fill='red', tags='farby')
    elif moznost == 4:
        canvas.create_oval(105, 220, 205, 320, fill='yellow', tags='farby')
        canvas.create_oval(105, 110, 205, 210, fill='red', tags='farby')
    elif moznost == 5:
        canvas.create_oval(105, 110, 205, 210, fill='red', tags='farby')
        canvas.create_oval(105, 220, 205, 320, fill='yellow', tags='farby')
        canvas.create_oval(105, 330, 205, 430, fill='lime', tags='farby')
    canvas.update()
    canvas.after(1000, semafor)
semafor()
