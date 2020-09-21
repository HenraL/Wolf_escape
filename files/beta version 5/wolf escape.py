#!/usr/bin/python3
# -*- coding: Utf-8 -*
levels=4
#levelfiles=[]
"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame, os
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from tkinter import *
from webbrowser import *

from classes import *
from constantes import *

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
    git=Button(Frame1TOP2, text="Github", relief=FLAT, fg="blue", bg="White", command=affichehl)
    fac=Button(Frame1TOP2, text="Facebook", relief=FLAT, fg="blue", bg="White", command=affichehl)
    insth=Button(Frame1TOP2, text="Instagram", relief=FLAT, fg="blue", bg="White", command=affichehl)
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

def refreshlevels():#levelfiles
    global levelfiles
    levelfiles=os.listdir("levels")
    
    return levelfiles

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

def choselevels():
    def LEVEL():
        Levelnumber = int(level.get())
        Cevel.destroy()
        print(Levelnumber)
        refreshlevels()#levelfiles
        maxlevel=len(levelfiles)
        global choix
        choix=levelfiles[Levelnumber-1]
        return choix
    refreshlevels()#levelfiles
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
    # return choix

def check(image_fond,image_fond_credits,fenetre,choix): #niveau,
    if choix != 0:
        pygame.display.set_caption("{}{}".format(titre_fenetre,choix))
        CHOIX=choix
        choix='levels/{}'.format(choix)
        #Chargement du fond
        global fond
        if CHOIX=="016_credits":
            fond = pygame.image.load(image_fond_credits).convert()
        else:
            fond = pygame.image.load(image_fond).convert()
        #Génération d'un niveau à partir d'un fichier
        global niveau
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)
        #Création du loup
        global dk
        dk = Perso("img/sprite/w/w_rigth.png", "img/sprite/w/w_left.png", "img/sprite/w/w_up.png", "img/sprite/w/w_down.png", niveau)
        #Creating the ennemi (The gardian)
        global gardien
        gardien=Perso("img/sprite/gardien/Gardien_Droite.png", "img/sprite/gardien/Gardien_Gauche.png", "img/sprite/gardien/Gardien_haut.png", "img/sprite/gardien/Gardien_bas.png", niveau)
    return dk, gardien, fond, choix, niveau, fenetre



def boucledejeu(continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien): #				
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					dk.deplacer('droite')
				elif event.key == K_LEFT:
					dk.deplacer('gauche')
				elif event.key == K_UP:
					dk.deplacer('haut')
				elif event.key == K_DOWN:
					dk.deplacer('bas')			
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()

		#Victoire -> Retour à l'accueil
		if niveau.structure[dk.case_y][dk.case_x] == '3' or niveau.structure[dk.case_y][dk.case_x] == '4':continuer_jeu = 0
        #return continuer_jeu, continuer

def play(continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels):
    #continuer_accueil = 0
    refreshlevels()#levelfiles
    maxlevel=len(levelfiles)
    print(levelfiles)
    for i in range(len(levelfiles)):
        print(levelfiles)
        print(i)
        #global continuer_jeu
        continuer_jeu = 1
        #global choix
        choix=levelfiles[i]
        pygame.display.set_caption("{}{}".format(titre_fenetre,choix))
        if choix=="014_m1" or choix=="015_m2" or choix=="017_h" or choix=="018_I":
            continuer_jeu=0
        elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_q:
            continuer_jeu = 0
            i=maxlevel
            continuer = 0
            #Variable de choix du niveau
            choix = 0
            break
        else:
            print (choix)
            #choix = 'l{}'.format(i+1)
            check(image_fond,image_fond_credits,fenetre,choix)#niveau,
            boucledejeu(continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)
            #print("tour = {}\ncontinuer_jeu = {}\nchoix={}\ncontinuer={}\nniveau={}".format(i,continuer_jeu,choix,continuer,niveau))

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetrex, cote_fenetrey))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)
#rendre le déplacement fluide
pygame.key.set_repeat(400, 30)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
    #Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))
	#Titre
	pygame.display.set_caption(titre_fenetre)

	#Rafraichissement
	pygame.display.flip()
	
	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_q:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_SPACE:
					continuer_accueil=0
					play(continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels)						
				elif event.key == K_BACKSPACE or event.key == K_RETURN:
					continuer_accueil = 0
					choselevels()
					check(image_fond,image_fond_credits,fenetre,choix)#niveau,
					
					boucledejeu(continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)#
					print(choix)
				#elif event.key == K_s:
				#	continuer_accueil = 0
				#	choix = ''
				elif event.key == K_c:
					continuer_accueil = 0
					main_credits()
					continuer_accueil=1
				elif event.key == K_c:continuer_accueil,choix=0,"credits"
				if event.key == K_F1:continuer_accueil,choix = 0,'m1'
				#Lancement du niveau 2
				elif event.key == K_F2:continuer_accueil,choix =0,'m2'
	
