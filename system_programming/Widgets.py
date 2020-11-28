from tkinter import *

root = Tk()
kekw = Label(width=20)
lol = Entry(text='Нажмите на цвет', width=20)
lol.insert(0, 'Нажмите на цвет')
kekw['text'] = 'Определение цвета'

def cvet1():
    lol.delete(0, END)
    lol.insert(0, "#ff0000")
    kekw['text'] = 'Красный'

def cvet2():
    lol.delete(0, END)
    lol.insert(0, "#FFA500")
    kekw['text'] = 'Оранжевый'

def cvet3():
    lol.delete(0, END)
    lol.insert(0, "#FFFF00")
    kekw['text'] = 'Жёлтый'

def cvet4():
    lol.delete(0, END)
    lol.insert(0, "#00FF00")
    kekw['text'] = 'Зелёный'

def cvet5():
    lol.delete(0, END)
    lol.insert(0, "#00FFFF")
    kekw['text'] = 'Голубой'

def cvet6():
    lol.delete(0, END)
    lol.insert(0, "#0000FF")
    kekw['text'] = 'Синий'

def cvet7():
    lol.delete(0, END)
    lol.insert(0, "#800080")
    kekw['text'] = 'Фиолетовый'


button1 = Button(bg='#ff0000', command=cvet1, width=18,)
button2 = Button(bg='#FFA500', command=cvet2, width=18)
button3 = Button(bg='#FFFF00', command=cvet3, width=18)
button4 = Button(bg='#00FF00', command=cvet4, width=18)
button5 = Button(bg='#00FFFF', command=cvet5, width=18)
button6 = Button(bg='#0000FF', command=cvet6, width=18)
button7 = Button(bg='#800080', command=cvet7, width=18)
kekw.pack()
lol.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
root.mainloop()