import tkinter
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
p1 = (400.0, 100.0),
p2 = (450, 250)
p3 = (350, 250)
p4 = (320, 160)
p5 = (470, 160)
canvas.create_line(p3, p1, p2, p4, p5, p3, fill='red')
canvas.pack()
master.mainloop()