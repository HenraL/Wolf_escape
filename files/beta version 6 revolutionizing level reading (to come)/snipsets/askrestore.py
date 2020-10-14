from tkinter import *
def retorelevel():
    def Yes():
        print("yes")
        fenetre.destroy()
    def No():
        print("No")
        fenetre.destroy()
    fenetre = Tk()
    Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
    Frame1.pack(side=TOP, padx=10, pady=10)
    FrameButt=Frame(fenetre, borderwidth=2, relief=FLAT)
    FrameButt.pack(side=TOP, padx=0, pady=10)

    label = Label(Frame1, text="Une sauvegarde a été trouvée.")
    label.pack()
    label = Label(Frame1, text="Voulez-vous contiunuer la partie déjà entamée?")
    label.pack()
    bouton=Button(FrameButt, text="Oui", command=Yes)
    bouton.pack(side=RIGHT, padx=5)
    bouton=Button(FrameButt, text="Non", command=No)
    bouton.pack(side=RIGHT, padx=5)
    fenetre.mainloop()

retorelevel()
