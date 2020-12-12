from tkinter import *

def load():
    f = open(entry.get())
    text.delete(1.0, END)
    text.insert(1.0, f.read())

def save():
    f = open(entry.get(), 'x')
    f.write(text.get(1.0, END))
    text.delete(1.0, END)


root = Tk()
kekw = Frame()
kekw.pack()
entry = Entry(kekw, width=20)
entry.pack(side=LEFT)
Button(kekw, text="Открыть", command=load)\
    .pack(side=LEFT)
Button(kekw, text="Сохранить", command=save)\
    .pack(side=LEFT)
kek = Frame()
kek.pack()
text = Text(kek, width=50, height=20, wrap=NONE)
text.pack(side=LEFT)
scroll = Scrollbar(kek, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

lol = Scrollbar(orient=HORIZONTAL, command=text.xview)
lol.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=lol.set)

root.mainloop()
