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
exitSpaceGame=False

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
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_q:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0
            elif event.type == KEYDOWN:
                #Lancement du niveau 1
                if event.key == K_BACKSPACE or event.key == K_RETURN:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,0,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choselevels()
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                    print("exited the boucledejeu")
                    print(choix)
                elif event.key == K_c:
                    continuer_accueil = 0
                    tkinterWindows.main_credits()
                elif event.key == K_h:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="h"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
