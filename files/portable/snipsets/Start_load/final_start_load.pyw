import pygame
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from time import sleep
#int()
#a=input("Entrez un chiffre pour la fréquence des diapositives (en secondes):")
#a=int(a)
a=0.5
#a=1
#variables
cote_fenetrex=691
cote_fenetrey=600
#Personnalisation de la fenêtre
titre_fenetre = "Wolf Escape"
image_icone = "img/ingame/wolf_icon.png"
#Listes des images du jeu
image_accueil1="img/launch_load/start_load/stages_stage_1.png"
image_accueil2="img/launch_load/start_load/stages_stage_2.png"
image_accueil3="img/launch_load/start_load/stages_stage_3.png"
image_accueil4="img/launch_load/start_load/stages_stage_4.png"
image_accueil5="img/launch_load/start_load/stages_stage_5.png"
image_accueil6="img/launch_load/start_load/stages_stage_6.png"
image_accueil7="img/launch_load/start_load/stages_stage_7.png"
image_accueil8="img/launch_load/start_load/stages_stage_8.png"
image_accueil9="img/launch_load/start_load/stages_stage_9.png"
image_accueil10="img/launch_load/start_load/stages_stage_10.png"
image_accueil11="img/launch_load/start_load/stages_stage_11.png"
image_accueil12="img/launch_load/start_load/stages_stage_12.png"
image_accueil13="img/launch_load/start_load/stages_stage_13.png"
image_accueil14="img/launch_load/start_load/stages_stage_14.png"
image_accueil15="img/launch_load/start_load/stages_stage_15.png"
image_main1="img/launch_load/menu_anim/accueil.png"
image_main2="img/launch_load/menu_anim/accueil_static_2.png"
image_black="img/launch_load/start_load/stages_stage_black.png"
contiinue=1

load_images=[image_accueil1,image_accueil2,image_accueil3,image_accueil4,image_accueil5,image_accueil6,image_accueil7,image_accueil8,image_accueil9,image_accueil10,image_accueil11,image_accueil12,image_accueil13,image_accueil14,image_accueil15,image_main1,image_main2]

#def
def standby(image_main1,image_main2):
    for i in range(50):
        accueil = pygame.image.load(image_main1).convert()#_alpha
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
        sleep(a)
        accueil = pygame.image.load(image_main2).convert()#_alpha
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
        sleep(a)
def anim_main_window(load_images):
    sleep(1)
    for i in range(len(load_images)):
        accueil = pygame.image.load(load_images[i]).convert()#_alpha
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
        sleep(a)
    standby(image_main1,image_main2)

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

anim_main_window(load_images)
#sleep(10)

