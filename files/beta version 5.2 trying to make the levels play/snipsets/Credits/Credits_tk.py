from tkinter import *
import sys
from webbrowser import *

def web(url):
    webbrowser.open_new("{}".format(url))
 
def affichehl(e):
    #web(e)
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
t.tag_bind(1, '<Button-1>', affichehl)
#
t.insert(END, ".")
t.pack()
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()

#Credits of Wolf Escape
#
#Programed by:
#Henry Letellier
#Github (link: https://bit.ly/2YcQ4ce)
#Facebook (link: http://bit.ly/2EieENH)
#Instagram (http://bit.ly/2PRGBkG)
#
#Graphics By:
#Irina Marchand
#Instagram: (https://bit.ly/2EmmERy)
#
#Feedback:
#Tell us what you think about the game:
#Tell us on:
#Discord: (link: http://bit.ly/wolfesc)
#Answer a survey form: (link: http://bit.ly/wolfescf)
#
#Support Us:
#
#On Tipyee: (link: https://bit.ly/3cqnOYV)
#
#
#Many Thenks To all the beta testers
#
# Monosis (link: discordlink)
# Suxene (link:discordlink )
# Totopo (link:discordlink)
# Gabin (link:discordlink)
# Defucota (color: #AE20FF, link:discordlink )
# Marina (link:discordlink)
# Caroline (link:discordlink)


# No name: rgaby013@gmail.com Axel sarasin: aksel.sarrazin@gmail.com Madamme Gofford (svt): fgifford@hattemer.fr Madame martinez: a voir: gmartinez@hattemer.fr Tom Veller: vellertom@gmail.com Louis ledauphin: ledauphinlouis@gmail.com Sasha Deniset:sashadeniset@gmail.com Kwame: KwMK@outlook.fr Jean-maxime: djanettjm@gmail.com
