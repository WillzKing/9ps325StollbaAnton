from tkinter import *
from tkinter import messagebox

global lol, lel

def checkvvod():
    try:
        global lol, lel
        lol = ent.get()
        lol = int(lol)
        lel = ent1.get()
        lel = int(lel)
    except ValueError:
        messagebox.showerror("ОШИБКА", "Введите корректные значения")

def summa(event):
    checkvvod()
    kek = lol+lel
    kek = str(kek)
    lab['text'] = ' '.join(kek)

def vichit(event):
    checkvvod()
    kek = lol-lel
    kek = str(kek)
    lab['text'] = ' '.join(kek)

def umn(event):
    checkvvod()
    kek = lol*lel
    kek = str(kek)
    lab['text'] = ' '.join(kek)

def delen(event):
    checkvvod()
    kek = lol/lel
    kek = str(kek)
    lab['text'] = ' '.join(kek)

root = Tk()

ent = Entry(root, width=20)
ent1 = Entry(root, width=20)
but = Button(root, text="+", width=20)
but2 = Button(root, text="-", width=20)
but3 = Button(root, text="*", width=20)
but4 = Button(root, text="/", width=20)
lab = Label(root, width=20, bg='black', fg='white')


but.bind('<Button-1>', summa)
but2.bind('<Button-1>', vichit)
but3.bind('<Button-1>', umn)
but4.bind('<Button-1>', delen)

ent.pack()
ent1.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()
root.mainloop()