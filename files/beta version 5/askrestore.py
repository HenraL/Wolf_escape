from tkinter import *
def retorelevel():
    fentre = Tk()
    Frame1 = Frame(fentre, borderwidth=2, relief=FLAT)
    Frame1.pack(side=LEFT, padx=10, pady=10)

    label = Label(Frame1, text="Choose you're level:")
    label.pack()
    bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    bouton.pack(side=RIGHT, padx=5)
    bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    bouton.pack(side=RIGHT, padx=5)
    fentre.mainloop()

retorelevel()
