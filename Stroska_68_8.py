import tkinter, random
canvas = tkinter.Canvas(width = 400, height = 800, bg='white')
canvas.pack()

y1 = 10
y2 = 10
stop = 0

def bosorky():
    global stop, y1, y2
    minus1 = random.randint(0, 10)
    minus2 = random.randint(0, 10)
    y1 = y1+minus1
    y2 = y2+minus2
    canvas.delete('all')
    #bosorka1
    canvas.create_rectangle(100, y1, 140, y1+60)
    canvas.create_oval(100, y1-40, 140, y1)
    canvas.create_line(60, y1+40, 160, y1+40)
    canvas.create_line(40, y1-10, 60, y1+40, 40, y1, 60, y1+40, 40, y1+10, 60, y1+40, 40, y1+20, 60, y1+40, 40, y1+30, 60, y1+40, 40, y1+40, 60, y1+40, 40, y1+50, 60, y1+40, 40, y1+60, 60, y1+40, 40, y1+70, 60, y1+40, 40, y1+80)
    #bosorka2
    canvas.create_rectangle(300, y2, 340, y2+60)
    canvas.create_oval(300, y2-40, 340, y2)
    canvas.create_line(260, y2+40, 360, y2+40)
    canvas.create_line(240, y2-10, 260, y2+40, 240, y2, 260, y2+40, 240, y2+10, 260, y2+40, 240, y2+20, 260, y2+40, 240, y2+30, 260, y2+40, 240, y2+40, 260, y2+40, 240, y2+50, 260, y2+40, 240, y2+60, 260, y2+40, 240, y2+70, 260, y2+40, 240, y2+80)
    if y1 < 800 and y2 >= 800:
        stop = 1
        print('Bosorka č.2 vyhrala')
    elif y2 <= 800 and y1 > 800:
        stop = 1
        print('Bosorka č.1 vyhrala')
    if stop == 0:
        canvas.update()
        canvas.after(10, bosorky)

bosorky()
