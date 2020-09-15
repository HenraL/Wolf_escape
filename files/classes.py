"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=pygame.image.load(a).convert_alpha(),pygame.image.load(b).convert_alpha(),pygame.image.load(c).convert_alpha(),pygame.image.load(d).convert_alpha(),pygame.image.load(e).convert_alpha(),pygame.image.load(f).convert_alpha(),pygame.image.load(g).convert_alpha(),pygame.image.load(h).convert_alpha(),pygame.image.load(i).convert_alpha(),pygame.image.load(j).convert_alpha(),pygame.image.load(j).convert_alpha(),pygame.image.load(k).convert_alpha(),pygame.image.load(l).convert_alpha(),pygame.image.load(m).convert_alpha(),pygame.image.load(n).convert_alpha(),pygame.image.load(o).convert_alpha(),pygame.image.load(p).convert_alpha(),pygame.image.load(q).convert_alpha(),pygame.image.load(r).convert_alpha(),pygame.image.load(s).convert_alpha(),pygame.image.load(t).convert_alpha(),pygame.image.load(u).convert_alpha(),pygame.image.load(v).convert_alpha(),pygame.image.load(w).convert_alpha(),pygame.image.load(x).convert_alpha(),pygame.image.load(y).convert_alpha(),pygame.image.load(z).convert_alpha()

		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == '1':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == '2':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == '3':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				# elif sprite == 'a':		   
				# 	fenetre.blit(a, (x,y))
				# elif sprite == 'b':		   
				# 	fenetre.blit(b, (x,y))
				# elif sprite == 'c':		   
				# 	fenetre.blit(c, (x,y))
				# elif sprite == 'd':		   
				# 	fenetre.blit(d, (x,y))
				# elif sprite == 'e':		   
				# 	fenetre.blit(e, (x,y))
				# elif sprite == 'f':		   
				# 	fenetre.blit(f, (x,y))
				# elif sprite == 'g':		   
				# 	fenetre.blit(g, (x,y))
				# elif sprite == 'h':		   
				# 	fenetre.blit(h, (x,y))
				# elif sprite == 'i':		   
				# 	fenetre.blit(i, (x,y))
				# elif sprite == 'j':		   
				# 	fenetre.blit(j, (x,y))
				# elif sprite == 'k':		   
				# 	fenetre.blit(k, (x,y))
				# elif sprite == 'l':		   
				# 	fenetre.blit(l, (x,y))
				# elif sprite == 'n':		   
				# 	fenetre.blit(n, (x,y))
				# elif sprite == 'o':		   
				# 	fenetre.blit(o, (x,y))
				# elif sprite == 'p':		   
				# 	fenetre.blit(p, (x,y))
				# elif sprite == 'q':		   
				# 	fenetre.blit(q, (x,y))
				# elif sprite == 'r':		   
				# 	fenetre.blit(r, (x,y))
				# elif sprite == 's':		   
				# 	fenetre.blit(s, (x,y))
				# elif sprite == 't':		   
				# 	fenetre.blit(t, (x,y))
				# elif sprite == 'u':		   
				# 	fenetre.blit(u, (x,y))
				# elif sprite == 'v':		   
				# 	fenetre.blit(v, (x,y))
				# elif sprite == 'w':		   
				# 	fenetre.blit(w, (x,y))
				# elif sprite == 'x':		   
				# 	fenetre.blit(x, (x,y))
				# elif sprite == 'y':		   
				# 	fenetre.blit(y, (x,y))
				# elif sprite == 'z':		   
				# 	fenetre.blit(z, (x,y))
				# elif sprite == 'A':	
				# 	fenetre.blit(A, (x,y))
				# elif sprite == 'B':	
				# 	fenetre.blit(B, (x,y))
				# elif sprite == 'C':	
				# 	fenetre.blit(C, (x,y))
				# elif sprite == 'D':	
				# 	fenetre.blit(D, (x,y))
				# elif sprite == 'E':	
				# 	fenetre.blit(E, (x,y))
				# elif sprite == 'F':	
				# 	fenetre.blit(F, (x,y))
				# elif sprite == 'G':	
				# 	fenetre.blit(G, (x,y))
				# elif sprite == 'H':	
				# 	fenetre.blit(H, (x,y))
				# elif sprite == 'I':	
				# 	fenetre.blit(I, (x,y))
				# elif sprite == 'J':	
				# 	fenetre.blit(J, (x,y))
				# elif sprite == 'K':	
				# 	fenetre.blit(K, (x,y))
				# elif sprite == 'L':	
				# 	fenetre.blit(L, (x,y))
				# elif sprite == 'M':	
				# 	fenetre.blit(M, (x,y))
				# elif sprite == 'N':	
				# 	fenetre.blit(N, (x,y))
				# elif sprite == 'O':	
				# 	fenetre.blit(O, (x,y))
				# elif sprite == 'P':	
				# 	fenetre.blit(P, (x,y))
				# elif sprite == 'Q':	
				# 	fenetre.blit(Q, (x,y))
				# elif sprite == 'R':	
				# 	fenetre.blit(R, (x,y))
				# elif sprite == 'S':	
				# 	fenetre.blit(S, (x,y))
				# elif sprite == 'T':	
				# 	fenetre.blit(T, (x,y))
				# elif sprite == 'U':	
				# 	fenetre.blit(U, (x,y))
				# elif sprite == 'V':	
				# 	fenetre.blit(V, (x,y))
				# elif sprite == 'W':		   
				# 	fenetre.blit(W, (x,y))
				# elif sprite == 'X':		  
				# 	fenetre.blit(X, (x,y))
				# elif sprite == 'Y':		   
				# 	fenetre.blit(Y, (x,y))
				# elif sprite == 'Z':		   
				# 	fenetre.blit(Z, (x,y))
				# elif sprite == '4':		   
				# 	fenetre.blit(aright, (x,y))
				# elif sprite == '5':		  
				# 	fenetre.blit(aleft, (x,y))
				# elif sprite == '6':		   
				# 	fenetre.blit(aup, (x,y))
				# elif sprite == '7':		   
				# 	fenetre.blit(adown, (x,y))
				
				
				num_case += 1
			num_ligne += 1
			
			
			
			
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
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
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != '1':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != '1':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != '1':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != '1':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
