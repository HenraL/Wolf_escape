from tkinter import *
import sys
from webbrowser import *

def web(url):
    open_new("{}".format(url))
 
def Githubh():web("https://bit.ly/2YcQ4ce")
def Facebookh():web("http://bit.ly/2EieENH")
def Instagramh():web("http://bit.ly/2PRGBkG")
def InstagramI():web("https://bit.ly/2EmmERy")
def Discord():web("http://bit.ly/wolfesc")
def Answerasurveyform():web("http://bit.ly/wolfescf")
def Tipyee():web("https://bit.ly/3cqnOYV")
def Utip():web("https://github.com/404")
def Monosis():web("https://github.com/")
def Suxene():web("https://github.com/")
def Totopoo():web("totopo#8202")
def Gabin():web("https://github.com/")
def Defucoa():web("https://github.com/")
def Marina():web("https://github.com/")
def Caroline():web("https://github.com/")



def main_credits():
    pfonty="Times New Roman"
    pfontw="bold"
    pfonts=9
    F1=FLAT
    root = Tk()
    root['bg']='white'
    root.title("tkinter.Text sample")
    root.geometry("900x600")
    Frame1 = Frame(root, borderwidth=2, relief=FLAT, bg="White")
    Frame1Scroolbar = Frame(Frame1, borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP2=Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP =Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP3=Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP4=Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP5=Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1TOP6=Frame(Frame1Scroolbar,borderwidth=2, relief=FLAT, bg="White")
    Frame1.pack(side=TOP, padx=10, pady=10, fill=X)
    Frame1Scroolbar.pack(side=TOP, padx=0, pady=0, fill=X)
    Frame1TOP.pack(side=TOP, padx=0, pady=0, fill=X)
    Frame1TOP2.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
    Frame1TOP3.pack(side=TOP, padx=0, pady=0, fill=X)
    Frame1TOP4.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
    Frame1TOP5.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
    Frame1TOP6.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
    Credits=Label(Frame1TOP, text="Credits of Wolf Escape", bg="White")
    Programmed=Label(Frame1TOP, text="Programmed by:", bg="White")
    Henry=Label(Frame1TOP, text="Henry Letellier", bg="White")
    Credits.pack(anchor=CENTER)
    Programmed.pack(anchor=CENTER,side=TOP)#,fill=X
    Henry.pack(anchor=CENTER,side=TOP)#,fill=X
    git=Button(Frame1TOP2, text="Github", relief=FLAT, fg="blue", bg="White", command=Githubh)
    fac=Button(Frame1TOP2, text="Facebook", relief=FLAT, fg="blue", bg="White", command=Facebookh)
    insth=Button(Frame1TOP2, text="Instagram", relief=FLAT, fg="blue", bg="White", command=Instagramh)
    git.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
    fac.pack(anchor=CENTER,side=LEFT) #,fill=X, border=FLAT
    insth.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
    Graphics=Label(Frame1TOP3, text="Graphics by:", bg="White")
    Irina=Label(Frame1TOP3, text="Irina Marchand", bg="White")
    Graphics.pack(anchor=CENTER,side=TOP,fill=X)
    Irina.pack(anchor=CENTER,side=TOP,fill=X)
    insti=Button(Frame1TOP3, text="Instagram", relief=FLAT, fg="blue",  bg="White", command=affichehl)
    insti.pack(anchor=CENTER,side=TOP)#,fill=X, relief=FLAT
    Feedback=Label(Frame1TOP3, text="Feedback:", bg="White")
    Feedback.pack(anchor=CENTER, side=TOP)
    TUWYTATG=Label(Frame1TOP4, text="Tell us what you think about the game:",  bg="White")
    TUWYTATG.pack(anchor=CENTER, side=TOP)
    TUO=Label(Frame1TOP4, text="Tell us on:",  bg="White")
    TUO.pack(anchor=CENTER, side=TOP)
    Discord=Button(Frame1TOP4, text="Discord", relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Discord.pack(anchor=CENTER, side=LEFT)#,fill=X
    Form=Button(Frame1TOP4, text="Answer a survey form", relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Form.pack(anchor=CENTER, side=LEFT)#,fill=X
    SU=Label(Frame1TOP5, text="Support us:",  bg="White")
    SU.pack(anchor=CENTER, side=TOP)
    Tipyee=Button(Frame1TOP5, text="On Tipyee", relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Tipyee.pack(anchor=CENTER, side=LEFT)#,fill=X
    Utip=Button(Frame1TOP5, text="On Utip", relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Utip.pack(anchor=CENTER, side=LEFT)#,fill=X
    MT=Label(Frame1TOP6, text="Many Thanks To all the beta testers:",  bg="White")
    MT.pack(anchor=CENTER, side=TOP)
    Monosis=Button(Frame1TOP6, text="Monosis", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Monosis.pack(anchor=CENTER, side=TOP)#,fill=X
    Suxene=Button(Frame1TOP6, text="Suxene", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Suxene.pack(anchor=CENTER, side=TOP)#,fill=X
    Totopoo=Button(Frame1TOP6, text="Totopoo", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Totopoo.pack(anchor=CENTER, side=TOP)#,fill=X
    Gabin=Button(Frame1TOP6, text="Gabin", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Gabin.pack(anchor=CENTER, side=TOP)#,fill=X
    Defucoa=Button(Frame1TOP6, text="Defucoa", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="#AE20FF",  bg="White", command=affichehl)
    Defucoa.pack(anchor=CENTER, side=TOP)#,fill=X
    Marina=Button(Frame1TOP6, text="Marina", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Marina.pack(anchor=CENTER, side=TOP)#,fill=X
    Caroline=Button(Frame1TOP6, text="Caroline", font=(pfonty, pfonts, pfontw), relief=FLAT, fg="blue",  bg="White", command=affichehl)
    Caroline.pack(anchor=CENTER, side=TOP)#,fill=X
    Button(root, text="Exit", command=root.destroy).pack()
    root.mainloop()

main_credits()

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
#Utip (link:)
#
#Many Thanks To all the beta testers
#
# Monosis (link: discordlink)
# Suxene (link:discordlink )
# Totopo (link:discordlink)
# Gabin (link:discordlink)
# Defucota (color: #AE20FF, link:discordlink )
# Marina (link:discordlink)
# Caroline (link:discordlink)


# No name: rgaby013@gmail.com Axel sarasin: aksel.sarrazin@gmail.com Madamme Gofford (svt): fgifford@hattemer.fr Madame martinez: a voir: gmartinez@hattemer.fr Tom Veller: vellertom@gmail.com Louis ledauphin: ledauphinlouis@gmail.com Sasha Deniset:sashadeniset@gmail.com Kwame: KwMK@outlook.fr Jean-maxime: djanettjm@gmail.com
