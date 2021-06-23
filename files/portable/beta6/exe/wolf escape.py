import pygame, os, sys,requests
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from tkinter import *
from webbrowser import open_new

from classes import *
from constantes import *
levels=4
CREDIT=False
exitSpaceGame=False
#levelfiles=[]
"""
Jeu Wolf escape Labyrinthe
Jeu dans lequel on doit déplacer un loup jusqu'à la viande à travers un labyrinthe.
Script Python
Fichiers : trop pour les lister ici
"""
links=boot.initialise_links(main_for_rec_dict)
RI=root(main=main_for_rec,main_dict=main_for_rec_dict,links=links) #initialising root
for i in RI.links:
    print(i)
boot.TKinter.window.FetchingFiles(RI)


def choselevels():
    def LEVEL():
        global choix
        choix=levelfiles[int(level.get())-1]
        Level.destroy()
        print("Wolf escape.py.choselevels.LEVEL.choix= ",choix)
        #return choix
    trackProgress.refreshlevels("levels")#levelfiles
    maxlevel=len(levelfiles)
    Level = Tk()
    Frame1 = Frame(Level, borderwidth=2, relief=FLAT)
    Frame1.pack(side=LEFT, padx=10, pady=10)
    label = Label(Frame1, text="Choose you're level:")
    label.pack()
    level=Spinbox(Frame1, from_=1, to=maxlevel, increment=1)
    level.pack(side=LEFT, padx=5)
    bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    bouton.pack(side=RIGHT, padx=5)
    Level.mainloop()



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
    
    #Rafraichissement
    pygame.display.flip()
	
    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        gameAnimations.mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre)
        mainMenuPlayed=True

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_a or event.type == KEYDOWN and event.key == K_q:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0
            elif event.type == KEYDOWN:
                #Lancement du niveau 1
                if event.key == K_SPACE:
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,0
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,exitSpaceGame)
                elif event.key == K_BACKSPACE or event.key == K_RETURN:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,0,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choselevels()
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                    print("exited the boucledejeu")
                    print(choix)
                #elif event.key == K_s:
		#	continuer_accueil = 0
		#	choix = ''
                elif event.key == K_c:
                    continuer_accueil = 0
                    tkinterWindows.main_credits()
                elif event.key == K_h:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="h"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F1:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="m1"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F2:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="m2"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_i:
                    print("K_i")
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="I"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                if event.key == K_m:
                    print("K_m")
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="M"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F3:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,True,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="credits"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)