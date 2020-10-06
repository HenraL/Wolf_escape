import pygame
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from time import sleep
#int()
#a=input("Entrez un chiffre pour la fréquence des diapositives (en secondes):")
#a=int(a)
a=0.5
#variables
cote_fenetrex=691
cote_fenetrey=600
#Personnalisation de la fenêtre
titre_fenetre = "Wolf Escape"
image_icone = "img/ingame/wolf_icon.png"
imggiff="img/ingame/wolf_mainmenu.png"
imggif="img/ingame/wolf_mainmenu2.png"
#Listes des images du jeu
#1
image_accueil = "img/ingame/accueil.png"
#2
image_accueil2 ="img/ingame/accueilm.png"
#3
image_accueil3 ="img/ingame/endb.png"
#4
image_accueil4 ="img/ingame/endv.png"
#5
image_accueil5 ="img/ingame/mur.png"
#6
image_accueil6 ="img/ingame/start.png"
#7
image_accueil7 ="img/ingame/wolf_icon.png"
contiinue=1

#def
def anim_main_window():
    sleep(1)
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil2).convert()
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil3).convert()
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil4).convert()
    fenetre.blit(accueil, (30,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil5).convert()
    fenetre.blit(accueil, (60,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil6).convert()
    fenetre.blit(accueil, (90,0))
    pygame.display.flip()
    sleep(a)
    accueil = pygame.image.load(image_accueil7).convert()
    fenetre.blit(accueil, (120,0))
    pygame.display.flip()
    sleep(a)
#déb
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
#while contiinue==1:

anim_main_window()
sleep(10)

