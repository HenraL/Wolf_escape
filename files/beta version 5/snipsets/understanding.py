from tkinter import *
import sys
 
 
def affiche(e):
    top = Toplevel(root)
    top.title("View")
    text = Text(top)
    with open(sys.argv[0], "r") as fp:
        text.insert(END, fp.read())
    text.pack()
 
 
root = Tk()
root.title("tkinter.Text sample")
t = Text(root)
t.insert(END, " Text et les tags.")
t.insert(END, " Voir le ")
#
t.insert(END, "code", 1)
t.tag_config(1, foreground="blue")
t.tag_bind(1, '<Button-1>', affiche)
#
t.insert(END, ".")
t.pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
