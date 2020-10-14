#here is where the enemy data, (how to place the ennemy, info, where, ...)
#for each level, it will be imported in the main and class files
import pygame
from constantes import *
NiVeAu=[['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '²'],
        ['^', '^', ' ', ' ', ' ', '^', '^', '^', '^', '^', '^', '^', ' ', '^', '^', '^', '^', '^', ' ', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', ' ', '^', '^', '^', '^', '^', ' ', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^'],
        ['^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^', '^']]

class Perso:
    def __init__(self, droite, gauche, haut, bas, niveau):
        #print ("Je suis dans la classe perso.init")
        self.droite=pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        #print("J'ai initialisé les images pour le sprite")
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #print("J'ai placé le sprite")
        #Direction par défaut
        self.direction = self.droite
        #print("Je l'ai orienté vers la droite")
        #Niveau dans lequel le personnage se trouve
        self.niveau = niveau
        #print("self.niveau = niveau")
    def deplacer(self, direction):
        print("Je suis dans la def deplacer (self, direction")
        if direction=='droite':
            if self.case_x<(nombre_sprite_cote -1):
                print("droite")
                if self.niveau.structure[self.case_y][self.case_x+1]!='^':
                    self.case_x+=1
                    self.x=self.case_x*taille_sprite
            self.direction=self.droite
        if direction=='gauche':
            if self.case_x>0:
                print("gauche")
                if self.niveau.structure[self.case_y][self.case_x-1]!='^':
                    self.case_x-=1
                    self.x=self.case_x*taille_sprite
            self.direction=self.gauche
        if direction=='haut':
            if self.case_y>0:
                print("haut")
                if self.niveau.structure[self.case_y-1][self.case_x]!='^':
                    self.case_y-=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.haut
        if direction=='bas':
            if self.case_y<(nombre_sprite_cote-1):
                print("bas")
                if self.niveau.structure[self.case_y+1][self.case_x]!='^':
                    self.case_y+=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.bas
class Niveau:
    def __init__(self,NiVeAu):
        self.structure=0
        self.structure=NiVeAu
    def afficher(self, fenetre):
        #print("Je suis dans afficher (self, fenetre)")
        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()
        arrivee_fam=pygame.image.load(image_arrivee_fam).convert_alpha()
        #On parcourt la liste du niveau
        num_ligne = 0
        #print("J'ai chargé les variables-images")
        for ligne in self.structure:
            #print("Je suis dans for line in self.structure",end="")
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #print("Je suis dans for sprite in ligne")
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                #print("J'ai innitialisé les x et y des images")
                if sprite == '^':		   #m = Mur
                    fenetre.blit(mur, (x,y))
                elif sprite == '#':		   #d = Départ
                    fenetre.blit(depart, (x,y))
                elif sprite == '²':		   #a = Arrivée 3ϵα♦
                    fenetre.blit(arrivee, (x,y))
                num_case += 1
            num_ligne += 1


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
continuer=1
while continuer:
    
    #Rafraichissement
    pygame.display.flip()
	
    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        
        Niveau.afficher()
