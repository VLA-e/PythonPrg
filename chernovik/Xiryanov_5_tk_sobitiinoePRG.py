from tkinter import *


def handler1(event):
    print('Hello World!! x=', event.x, 'y=', event.y)


def handler2(event):
    exit()  # vixod iz programmi


# inicializacia
root = Tk()  # root - kornevoi widget i knemu privyazan interpretator Tk tisel
hello_label = Label(root, text="Hello, world!", font="Times 30")  # sozdali okno(widget) s tekstom i shriftom 30
hello_label.pack()  # ypakovali eto okno v megaokne;)

# Privyazka obrabot4ikov - k pare sobitie i obrabot4ik
# widget.bind(sobitie, obrabot4ik)
hello_label.bind('<Button-1>', handler1)  # sobitie handler1 po nagatiy mouse1
hello_label.bind('<Button-3>', handler2)  # sobitie handler2 po nagatiu po mouse3

# glavnii cikel (project)
root.mainloop()
