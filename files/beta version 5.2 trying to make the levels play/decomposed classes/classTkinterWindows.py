from pygame import *
from tkinter import *
from os import *
from classImporter import *
class tkinterWindows:
    def choselevels():
        def LEVEL():
            Levelnumber = int(level.get())
            Cevel.destroy()
            print(Levelnumber)
            trackProgress.refreshlevels("levels")#levelfiles
            maxlevel=len(levelfiles)
            global choix
            choix=levelfiles[Levelnumber-1]
            print("choix= ",choix)
            Choix=1
            global CREDIT
            CREDIT=False
            # MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix)#niveau,
            return choix, Choix, maxlevel, CREDIT
        trackProgress.refreshlevels("levels")#levelfiles
        maxlevel=len(levelfiles)
        Cevel = Tk()
        Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
        Frame1.pack(side=LEFT, padx=10, pady=10)
        label = Label(Frame1, text="Choose you're level:")
        label.pack()
        level=Spinbox(Frame1, from_=1, to=maxlevel, increment=1)
        level.pack(side=LEFT, padx=5)
        bouton=Button(Frame1, text="Jouer!", command=LEVEL)
        bouton.pack(side=RIGHT, padx=5)
        Cevel.mainloop()
        # return choix, Choix, maxlevel, CREDIT
    def retorelevel(FileProgress):
        def Yes():
            print("yes")
            choix=FileProgress
            fenetre.destroy()
            return choix, FileProgress
        def No():
            print("No")
            choix=0
            FileProgress=0
            fenetre.destroy()
            return choix, FileProgress
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
    def web(url):open_new("{}".format(url))
    def Githubh():tkinterWindows.web("https://bit.ly/2YcQ4ce")
    def Facebookh():tkinterWindows.web("http://bit.ly/2EieENH")
    def Instagramh():tkinterWindows.web("http://bit.ly/2PRGBkG")
    def InstagramI():tkinterWindows.web("https://bit.ly/2EmmERy")
    def discord():tkinterWindows.web("http://bit.ly/wolfesc")
    def Answerasurveyform():tkinterWindows.web("http://bit.ly/wolfescf")
    def tipyee():tkinterWindows.web("https://bit.ly/3cqnOYV")
    def utip():tkinterWindows.web("https://github.com/404")
    def monosis():tkinterWindows.web("https://github.com/")
    def suxene():tkinterWindows.web("https://github.com/Suxene?tab=repositories")
    def totopoo():tkinterWindows.web("https://www.instagram.com/haiko_hana/")
    def gabin():tkinterWindows.web("https://github.com/")
    def defucoa():tkinterWindows.web("https://www.instagram.com/quentin.defu/")
    def marina():tkinterWindows.web("https://www.instagram.com/marinamarraskuu/")#https://www.facebook.com/marina.toussaint.5201
    def marinaF():tkinterWindows.web("https://www.facebook.com/marina.toussaint.5201")
    def caroline():tkinterWindows.web("https://github.com/")


    def main_credits():
        pfonty="Times New Roman"
        pfontw="bold"
        pfonts=9
        F1=FLAT
        bgColor="White"
        root = Tk()
        root['bg']=bgColor
        root.title("tkinter.Text sample")
        root.geometry("900x600")
        Frame1 = Frame(root, borderwidth=2, relief=F1, bg=bgColor)
        Frame1Scroolbar = Frame(Frame1, borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP2=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP =Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP3=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOPMarina=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP4=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP5=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP6=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1.pack(side=TOP, padx=10, pady=10, fill=X)
        Frame1Scroolbar.pack(side=TOP, padx=0, pady=0, fill=X)
        Frame1TOP.pack(side=TOP, padx=0, pady=0, fill=X)
        Frame1TOP2.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP3.pack(anchor=CENTER, side=TOP, padx=0, pady=0, fill=X)
        Frame1TOPMarina.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP4.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP5.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP6.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Credits=Label(Frame1TOP, text="Credits of Wolf Escape", font=(pfonty,pfonts,pfontw), bg=bgColor)
        Programmed=Label(Frame1TOP, text="Programmed by:", bg=bgColor)
        Henry=Label(Frame1TOP, text="Henry Letellier", bg=bgColor)
        Credits.pack(anchor=CENTER)
        Programmed.pack(anchor=CENTER,side=TOP)#,fill=X
        Henry.pack(anchor=CENTER,side=TOP)#,fill=X
        git=Button(Frame1TOP2, text="Github", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Githubh)
        fac=Button(Frame1TOP2, text="Facebook", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Facebookh)
        insth=Button(Frame1TOP2, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Instagramh)
        git.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        fac.pack(anchor=CENTER,side=LEFT) #,fill=X, border=FLAT
        insth.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        Graphics=Label(Frame1TOP3, text="Graphics by:", bg=bgColor)
        Graphics.pack(anchor=CENTER,side=TOP,fill=X)
        Irina=Label(Frame1TOP3, text="Irina Marchand", bg=bgColor)
        Irina.pack(anchor=CENTER,side=TOP,fill=X)
        insti=Button(Frame1TOP3, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.InstagramI)
        insti.pack(anchor=CENTER,side=TOP)#,fill=X, relief=FLAT
        Marina=Label(Frame1TOP3, text="Marina Toussain", bg=bgColor)
        Marina.pack(anchor=CENTER,side=TOP)#,fill=X
        git=Button(Frame1TOPMarina, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.marina)
        fac=Button(Frame1TOPMarina, text="Facebook", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.marinaF)
        git.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        fac.pack(anchor=CENTER,side=LEFT) #,fill=X, border=FLAT
        Feedback=Label(Frame1TOP4, text="Feedback:", bg=bgColor)
        Feedback.pack(anchor=CENTER, side=TOP)
        TUWYTATG=Label(Frame1TOP4, text="Tell us what you think about the game:", bg=bgColor)
        TUWYTATG.pack(anchor=CENTER, side=TOP)
        TUO=Label(Frame1TOP4, text="Tell us on:", bg=bgColor)
        TUO.pack(anchor=CENTER, side=TOP)
        Discord=Button(Frame1TOP4, text="Discord", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.discord)
        Discord.pack(anchor=CENTER, side=LEFT)#,fill=X
        Form=Button(Frame1TOP4, text="Answer a survey form", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Answerasurveyform)
        Form.pack(anchor=CENTER, side=LEFT)#,fill=X
        SU=Label(Frame1TOP5, text="Support us:", bg=bgColor)
        SU.pack(anchor=CENTER, side=TOP)
        Tipyee=Button(Frame1TOP5, text="On Tipyee", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.tipyee)
        Tipyee.pack(anchor=CENTER, side=LEFT)#,fill=X
        Utip=Button(Frame1TOP5, text="On Utip", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.utip)
        Utip.pack(anchor=CENTER, side=LEFT)#,fill=X
        MT=Label(Frame1TOP6, text="Many Thanks To all the beta testers:", bg=bgColor)
        MT.pack(anchor=CENTER, side=TOP)
        Monosis=Button(Frame1TOP6, text="Monosis", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.monosis)
        Monosis.pack(anchor=CENTER, side=TOP)#,fill=X
        Suxene=Button(Frame1TOP6, text="Suxene", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.suxene)
        Suxene.pack(anchor=CENTER, side=TOP)#,fill=X
        Totopoo=Button(Frame1TOP6, text="Totopoo", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.totopoo)
        Totopoo.pack(anchor=CENTER, side=TOP)#,fill=X
        Gabin=Button(Frame1TOP6, text="Gabin", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.gabin)
        Gabin.pack(anchor=CENTER, side=TOP)#,fill=X
        Defucoa=Button(Frame1TOP6, text="Defucoa", font=(pfonty, pfonts, pfontw), relief=F1, fg="#AE20FF", bg=bgColor, command=tkinterWindows.defucoa)
        Defucoa.pack(anchor=CENTER, side=TOP)#,fill=X
        Caroline=Button(Frame1TOP6, text="Caroline", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.caroline)
        Caroline.pack(anchor=CENTER, side=TOP)#,fill=X
        Quit=Button(root, text="Exit", command=root.destroy)
        Quit.pack()
        
        root.mainloop()
    def accueil(continuer_jeu,continuer_accueil):
        #Chargement et affichage de l'écran d'accueil
        accueil = pygame.image.load(image_accueil).convert()
        fenetre.blit(accueil, (0,0))
        #Rafraichissement
        pygame.display.flip()
        #On remet ces variables à 1 à chaque tour de boucle
        #global continuer_jeu,continuer_accueil
        continuer_jeu = 1
        continuer_accueil = 1
        return continuer_jeu,continuer_accueil
