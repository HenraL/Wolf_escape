#!/usr/bin/python3
# -*- coding: Utf-8 -*

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

from classes import *
from constantes import *

def choselevels():
    def LEVEL():
        Levelnumber = int(level.get())
        Cevel.destroy()
        print(Levelnumber)
        global choix
        choix='l{}'.format(Levelnumber)
        return choix
    Cevel = Tk()
    Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
    Frame1.pack(side=LEFT, padx=10, pady=10)

    label = Label(Frame1, text="Hello World")
    label.pack()
    level=Spinbox(Frame1, from_=1, to=10, increment=1)
    level.pack(side=LEFT, padx=5)
    bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    bouton.pack(side=RIGHT, padx=5)
    Cevel.mainloop()
    # return choix

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
					continuer_accueil = 0
					for i in range(2):
    						choix = 'm{}'.format(i+1)
				elif event.key == K_BACKSPACE or event.key == K_RETURN:
					continuer_accueil = 0
					# Cevel = Tk()
					# Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
					# Frame1.pack(side=LEFT, padx=10, pady=10)

					# label = Label(Frame1, text="Hello World")
					# label.pack()
					# level=Spinbox(Frame1, from_=0, to=10, increment=1)
					# level.pack(side=LEFT, padx=5)
					# bouton=Button(Frame1, text="Jouer!", command=LEVEL)
					# bouton.pack(side=RIGHT, padx=5)
					# Cevel.mainloop()
					choselevels()
					# choix=
					print(choix)
				elif event.key == K_s:
					continuer_accueil = 0
					choix = 'n4'
				if event.key == K_F1:continuer_accueil,choix = 0,'m1'
				#Lancement du niveau 2
				elif event.key == K_F2:continuer_accueil,choix =0,'m2'
	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		dk = Perso("img/sprite/w/w_rigth.png", "img/sprite/w/w_left.png", "img/sprite/w/w_up.png", "img/sprite/w/w_down.png", niveau)
        # dk=Perso(ld, lg, lh, lb, niveau)
		
		

				
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
		if niveau.structure[dk.case_y][dk.case_x] == '3':
			continuer_jeu = 0
