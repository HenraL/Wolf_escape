import pygame, os, sys
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from tkinter import *
from webbrowser import *

from classes import *
from constantes import *
levels=4
CREDIT=False
#levelfiles=[]
"""
Jeu Wolf escape Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

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
    gameAnimations.mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,image_accueil,image_accueil2,image_accueil3,image_accueil4,image_accueil5,image_accueil6,image_accueil7)
    mainMenuPlayed=True

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
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,0
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT)
                elif event.key == K_BACKSPACE or event.key == K_RETURN:
                    continuer_accueil = 0
                    tkinterWindows.choselevels()
                    hidden=0
                    MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix)#niveau,
                    MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)#
                    print(choix)
                #elif event.key == K_s:
		#	continuer_accueil = 0
		#	choix = ''
                elif event.key == K_c:
                    continuer_accueil = 0
                    tkinterWindows.main_credits()
                elif event.key == K_h:
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,0
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT)
                elif event.key == K_F1:
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,1
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT)
                elif event.key == K_F2:
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,1
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT)
