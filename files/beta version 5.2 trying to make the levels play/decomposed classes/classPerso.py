from pygame import *
from classImporter import *
class Perso:
    def __init__(self, droite, gauche, haut, bas, niveau):
        self.droite=pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #Direction par défaut
        self.direction = self.droite
        #Niveau dans lequel le personnage se trouve
        self.niveau = niveau

    def deplacer(self, direction):
        if direction=='droite':
            if self.case_x<(nombre_sprite_cote -1):
                if self.niveau.structure[self.case_y][self.case_x+1]!='^':
                    self.case_x+=1
                    self.x=self.case_x*taille_sprite
            self.direction=self.droite
        if direction=='gauche':
            if self.case_x>0:
                if self.niveau.structure[self.case_y][self.case_x-1]!='^':
                    self.case_x-1
                    self.x=self.case_x*taille_sprite
            self.direction=self.gauche
        if direction=='bas':
            if self.case_y>0:
                if self.niveau.structure[self.case_y-1][self.case_x]!='^':
                    self.case_y-=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.haut

        if direction=='bas':
            if self.case_y<(nombre_sprite_cote-1):
                if self.niveau.structure[self.case_y+1][self.case_x]!='^':
                    self.case_y+=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.bas
