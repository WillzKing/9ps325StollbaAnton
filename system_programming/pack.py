from tkinter import *

root = Tk()
lel = Frame(root)
kekw = Label(width=20)
lol = Entry(text='Нажмите на цвет', width=20)
lol.insert(0, 'Нажмите на цвет')
kekw['text'] = 'Определение цвета'

def cvet():
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


button1 = Button(bg='#ff0000', command=cvet, width=9)
button2 = Button(bg='#FFA500', command=cvet2, width=9)
button3 = Button(bg='#FFFF00', command=cvet3, width=9)
button4 = Button(bg='#00FF00', command=cvet4, width=9)
button5 = Button(bg='#00FFFF', command=cvet5, width=9)
button6 = Button(bg='#0000FF', command=cvet6, width=9)
button7 = Button(bg='#800080', command=cvet7, width=9)
kekw.pack(padx=4, pady=4)
lol.pack(padx=4, pady=4)
lel.pack(padx=4, pady=4)
button1.pack(side=LEFT, padx=4, pady=4)
button2.pack(side=LEFT, padx=4, pady=4)
button3.pack(side=LEFT, padx=4, pady=4)
button4.pack(side=LEFT, padx=4, pady=4)
button5.pack(side=LEFT, padx=4, pady=4)
button6.pack(side=LEFT, padx=4, pady=4)
button7.pack(side=LEFT, padx=4, pady=4)
root.mainloop()