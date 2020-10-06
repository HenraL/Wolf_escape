import pygame
#from constantes import *
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from tkinter import*
# from classImporter import *
from time import sleep
import os
import webbrowser
class Niveau:
    def __init__(self, fichier):
        self.fichier=choix
        self.structure=0
    # def generer(self, choix):
    #     print("je suis dans la boucle niveau.generer")
    #     with open(choix, "r") as file:#self.fichier
    #         print("J'ai réussis à lire le fichier")
    #         structure_niveau=[]
    #         for line in file:
    #             ligne_niveau=[]
    #             for sprite in line:
    #                 if sprite !='\n':
    #                     ligne_niveau.append(sprite)
    #             structure_niveau.append(ligne_niveau)
    #         self.structure=structure_niveau
    def generer(self):
        f=open("levels/003_l3.txt", "r")#self.fichier
        file=f.read()
        f.close()
        structure_niveau=[]
        for line in file:
            ligne_niveau=[]
            for sprite in line:
                if sprite !='\n':
                    ligne_niveau.append(sprite)
            structure_niveau.append(ligne_niveau)
        self.structure=structure_niveau

    def afficher(self):
        num_case = 0
        for sprite in ligne:
            #On calcule la position réelle en pixels
            x = num_case * taille_sprite
            y = num_ligne * taille_sprite
            if sprite == '^':
                print("wall")
            elif sprite == '#':
                print("start")
            elif sprite == '²':
                print("finish")
            num_case += 1
        num_ligne += 1

choix="levels/003_l3.txt"

Niveau.generer(choix)
Niveau.afficher(self)
