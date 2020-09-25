"""Classes du jeu de Labyrinthe Wolf Escape"""

#Уеишщксдзцбьяаожгтнвмчюйъэфхпрл¿¡°•|¥₩ ∞±=≠~×÷!<>≤≥≈≡∂√∩%°∆←↑→↓↔+-¬αβγδεϵθϑμπρστφω*∙

from _typeshed import WriteableBuffer
import pygame
import os
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier #"levels/{}".format(fichier)
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
		arrivee_fam=pygame.image.load(image_arrivee_fam).convert_alpha()
		a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=pygame.image.load(leta).convert_alpha(),pygame.image.load(letb).convert_alpha(),pygame.image.load(letc).convert_alpha(),pygame.image.load(letd).convert_alpha(),pygame.image.load(lete).convert_alpha(),pygame.image.load(letf).convert_alpha(),pygame.image.load(letg).convert_alpha(),pygame.image.load(leth).convert_alpha(),pygame.image.load(leti).convert_alpha(),pygame.image.load(letj).convert_alpha(),pygame.image.load(letk).convert_alpha(),pygame.image.load(letl).convert_alpha(),pygame.image.load(letm).convert_alpha(),pygame.image.load(letn).convert_alpha(),pygame.image.load(leto).convert_alpha(),pygame.image.load(letp).convert_alpha(),pygame.image.load(letq).convert_alpha(),pygame.image.load(letr).convert_alpha(),pygame.image.load(lets).convert_alpha(),pygame.image.load(lett).convert_alpha(),pygame.image.load(letu).convert_alpha(),pygame.image.load(letv).convert_alpha(),pygame.image.load(letw).convert_alpha(),pygame.image.load(letx).convert_alpha(),pygame.image.load(lety).convert_alpha(),pygame.image.load(letz).convert_alpha()
		A=pygame.image.load(letA).convert_alpha()
		B=pygame.image.load(letB).convert_alpha()
		C=pygame.image.load(letC).convert_alpha()
		D=pygame.image.load(letD).convert_alpha()
		E=pygame.image.load(letE).convert_alpha()
		F=pygame.image.load(letF).convert_alpha()
		G=pygame.image.load(letG).convert_alpha()
		H=pygame.image.load(letH).convert_alpha()
		I=pygame.image.load(letI).convert_alpha()
		J=pygame.image.load(letJ).convert_alpha()
		K=pygame.image.load(letK).convert_alpha()
		L=pygame.image.load(letL).convert_alpha()
		M=pygame.image.load(letM).convert_alpha()
		N=pygame.image.load(letN).convert_alpha()
		O=pygame.image.load(letO).convert_alpha()
		P=pygame.image.load(letP).convert_alpha()
		Q=pygame.image.load(letQ).convert_alpha()
		R=pygame.image.load(letR).convert_alpha()
		S=pygame.image.load(letS).convert_alpha()
		T=pygame.image.load(letT).convert_alpha()
		U=pygame.image.load(letU).convert_alpha()
		V=pygame.image.load(letV).convert_alpha()
		W=pygame.image.load(letW).convert_alpha()
		X=pygame.image.load(letX).convert_alpha()
		Y=pygame.image.load(letY).convert_alpha()
		Z=pygame.image.load(letZ).convert_alpha()
		#credits
		#credits_fond=pygame.image.load(image_credits_fond).convert()
		credits_gagne=pygame.image.load(image_credits_gagne).convert()
		credits_w_Irina=pygame.image.load(image_credits_w_Irina).convert()
		credits_w_Henry=pygame.image.load(image_credits_w_Henry).convert()
		credits_l_Irina=pygame.image.load(image_credits_l_Irina).convert()
		credits_l_Henry=pygame.image.load(image_credits_l_Henry).convert()
		#mean
		mean_up=pygame.image.load(img_mean_up).convert()
		mean_down=pygame.image.load(img_mean_down).convert()
		mean_left=pygame.image.load(img_mean_left).convert()
		mean_right=pygame.image.load(img_mean_right).convert()
		#number
		zero=pygame.image.load(image_zero).convert_alpha()
		one=pygame.image.load(image_one).convert_alpha()
		two=pygame.image.load(image_two).convert_alpha()
		three=pygame.image.load(image_three).convert_alpha()
		four=pygame.image.load(image_four).convert_alpha()
		five=pygame.image.load(image_five).convert_alpha()
		six=pygame.image.load(image_six).convert_alpha()
		seven=pygame.image.load(image_seven).convert_alpha()
		eight=pygame.image.load(image_eight).convert_alpha()
		nine=pygame.image.load(image_nine).convert_alpha()
		#currency
		dollar=pygame.image.load(image_dollar).convert_alpha()
		pound=pygame.image.load(image_pound).convert_alpha()
		euro=pygame.image.load(image_euro).convert_alpha()
		yen=pygame.image.load(image_yen).convert_alpha()
		whan=pygame.image.load(image_whan).convert_alpha()
        #arrows
        #aright=pygame.image.load(img_aright).convert_alpha()


		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == '^':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == '#':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == '²':		   #a = Arrivée 3ϵα♦
					fenetre.blit(arrivee, (x,y))
				elif sprite == '_':		   #a = Arrivée_enfant 4дβ
					fenetre.blit(arrivee_fam, (x,y))
				elif sprite == '0':		   
				  	fenetre.blit(zero, (x,y))
				elif sprite == '1':		   
				  	fenetre.blit(one, (x,y))              
				elif sprite == '2':		   
				  	fenetre.blit(two, (x,y))              
				elif sprite == '3':		   
				  	fenetre.blit(three, (x,y))              
				elif sprite == '4':		   
				  	fenetre.blit(four, (x,y))              
				elif sprite == '5':		   
				  	fenetre.blit(five, (x,y))              
				elif sprite == '6':		   
				  	fenetre.blit(six, (x,y))              
				elif sprite == '7':		   
				  	fenetre.blit(seven, (x,y))              
				elif sprite == '8':		   
				  	fenetre.blit(eight, (x,y))              
				elif sprite == '9':		   
				  	fenetre.blit(nine, (x,y))
				elif sprite == 'γ':		   
				 	fenetre.blit(aright, (x,y))
				elif sprite == 'δ':		  
				 	fenetre.blit(aleft, (x,y))
				elif sprite == 'ε':		   
				 	fenetre.blit(aup, (x,y))
				elif sprite == 'Ω':		   
				 	fenetre.blit(adown, (x,y))              
				elif sprite == '':		   
				 	fenetre.blit(mean_up, (x,y))              
				elif sprite == '':		   
				 	fenetre.blit(mean_down, (x,y))              
				elif sprite == '':		   
				 	fenetre.blit(mean_left, (x,y))              
				elif sprite == '':		   
				 	fenetre.blit(mean_right, (x,y))
				elif sprite == '$':		   
				  	fenetre.blit(dollar, (x,y))             
				elif sprite == '£':		   
				  	fenetre.blit(pound, (x,y))             
				elif sprite == '€':		   
				  	fenetre.blit(euro, (x,y))             
				elif sprite == '¥':		   
				  	fenetre.blit(yen, (x,y))             
				elif sprite == '₩':		   
				 	fenetre.blit(whan, (x,y))  
				#elif sprite == '':		   
				#  	fenetre.blit(credits_w_Irina, (x,y))             
				#elif sprite == '':		   
				#  	fenetre.blit(credits_w_Henry, (x,y))             
				#elif sprite == '':		   
				#  	fenetre.blit(credits_l_Irina, (x,y))             
				#elif sprite == '':		   
				#  	fenetre.blit(credits_l_Henry, (x,y))             
				#elif sprite == '':		   
				#  	fenetre.blit(credits_gagne, (x,y))            
				#elif sprite == 'Ψ':		   
				# 	fenetre.blit(adown, (x,y))              
				#elif sprite == 'Ω':		   
				# 	fenetre.blit(adown, (x,y)) 
				# elif sprite == 'η,ζ,':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'θ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ϑ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ι':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'κ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'λ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'μ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ν':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ξ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ο':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ο':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'π':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ϖ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ρ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ϱ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'σ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ς':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'τ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'υ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'φ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ϕ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'χ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ψ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'ω':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Γ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Δ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Θ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Λ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Ξ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Ο':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Π':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Ρ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Σ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Τ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Υ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Φ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Χ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Ψ':		   
				#  	fenetre.blit(adown, (x,y))              
				# elif sprite == 'Ω':		   
				#  	fenetre.blit(adown, (x,y))              
				
				elif sprite == 'a':		   
					fenetre.blit(a, (x,y))
				elif sprite == 'b':		   
					fenetre.blit(b, (x,y))
				elif sprite == 'c':		   
					fenetre.blit(c, (x,y))
				elif sprite == 'd':		   
					fenetre.blit(d, (x,y))
				elif sprite == 'e':		   
					fenetre.blit(e, (x,y))
				elif sprite == 'f':		   
					fenetre.blit(f, (x,y))
				elif sprite == 'g':		   
					fenetre.blit(g, (x,y))
				elif sprite == 'h':		   
					fenetre.blit(h, (x,y))
				elif sprite == 'i':		   
					fenetre.blit(i, (x,y))
				elif sprite == 'j':		   
					fenetre.blit(j, (x,y))
				elif sprite == 'k':		   
					fenetre.blit(k, (x,y))
				elif sprite == 'l':		   
					fenetre.blit(l, (x,y))
				elif sprite == 'n':		   
					fenetre.blit(n, (x,y))
				elif sprite == 'o':		   
					fenetre.blit(o, (x,y))
				elif sprite == 'p':		   
					fenetre.blit(p, (x,y))
				elif sprite == 'q':		   
					fenetre.blit(q, (x,y))
				elif sprite == 'r':		   
					fenetre.blit(r, (x,y))
				elif sprite == 's':		   
					fenetre.blit(s, (x,y))
				elif sprite == 't':		   
					fenetre.blit(t, (x,y))
				elif sprite == 'u':		   
					fenetre.blit(u, (x,y))
				elif sprite == 'v':		   
					fenetre.blit(v, (x,y))
				elif sprite == 'w':		   
					fenetre.blit(w, (x,y))
				elif sprite == 'x':		   
					fenetre.blit(x, (x,y))
				elif sprite == 'y':		   
					fenetre.blit(y, (x,y))
				elif sprite == 'z':		   
					fenetre.blit(z, (x,y))
				elif sprite == 'A':	
					fenetre.blit(A, (x,y))
				elif sprite == 'B':	
					fenetre.blit(B, (x,y))
				elif sprite == 'C':	
					fenetre.blit(C, (x,y))
				elif sprite == 'D':	
					fenetre.blit(D, (x,y))
				elif sprite == 'E':	
					fenetre.blit(E, (x,y))
				elif sprite == 'F':	
					fenetre.blit(F, (x,y))
				elif sprite == 'G':	
					fenetre.blit(G, (x,y))
				elif sprite == 'H':	
					fenetre.blit(H, (x,y))
				elif sprite == 'I':	
					fenetre.blit(I, (x,y))
				elif sprite == 'J':	
					fenetre.blit(J, (x,y))
				elif sprite == 'K':	
					fenetre.blit(K, (x,y))
				elif sprite == 'L':	
					fenetre.blit(L, (x,y))
				elif sprite == 'M':	
					fenetre.blit(M, (x,y))
				elif sprite == 'N':	
					fenetre.blit(N, (x,y))
				elif sprite == 'O':	
					fenetre.blit(O, (x,y))
				elif sprite == 'P':	
					fenetre.blit(P, (x,y))
				elif sprite == 'Q':	
					fenetre.blit(Q, (x,y))
				elif sprite == 'R':	
					fenetre.blit(R, (x,y))
				elif sprite == 'S':	
					fenetre.blit(S, (x,y))
				elif sprite == 'T':	
					fenetre.blit(T, (x,y))
				elif sprite == 'U':	
					fenetre.blit(U, (x,y))
				elif sprite == 'V':	
					fenetre.blit(V, (x,y))
				elif sprite == 'W':		   
					fenetre.blit(W, (x,y))
				elif sprite == 'X':		  
					fenetre.blit(X, (x,y))
				elif sprite == 'Y':		   
					fenetre.blit(Y, (x,y))
				elif sprite == 'Z':		   
					fenetre.blit(Z, (x,y))
				elif sprite == ':':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '[':		   
					fenetre.blit(Z, (x,y))
				elif sprite == ']':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'µ':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '&':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '@':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'border':		   
					fenetre.blit(Z, (x,y))
				elif sprite == ')':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '(':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '°C':		   
					fenetre.blit(Z, (x,y))
				elif sprite == ':':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '.':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '¤':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '!':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '°F':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '>':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '<':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '§':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'closedparagraph':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'openparagraph':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '%':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '?':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '*':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '-':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '+':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '=':		   
					fenetre.blit(Z, (x,y))
				elif sprite == '/':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'à':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'ç':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'é':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'è':		   
					fenetre.blit(Z, (x,y))
				elif sprite == 'ù':		   
					fenetre.blit(Z, (x,y))
				
				
				
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
				if self.niveau.structure[self.case_y][self.case_x+1] != '^':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != '^':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != '^':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != '^':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas

class trackProgress:
    def WriteProgressToFile(progress):
        f=open("Progress","w")
        f.write(progress)
        f.close()
        return progress
    def GetProgress(IngameProgress):
        if os.path.exists("Progress")==True:
            f=open("Progress","r")
            FileProgress=f.read()
            f.close()
            if len(FileProgress)==0:
                trackProgress.WriteProgressToFile("0")
                IngameProgress=FileProgress=0
                return IngameProgress, FileProgress
            else:
                List=[]
                List.append(FileProgress)
                for i in List:
                    if i.isnumeric()==True:
                        FileProgress=int(i)
                        trackProgress.WriteProgressToFile(FileProgress)
                        return IngameProgress, FileProgress
                    else:
                        trackProgress.WriteProgressToFile("0")
                        IngameProgress=FileProgress=0
                        return IngameProgress, FileProgress
        else:
            trackProgress.WriteProgressToFile("0")
    def AskRestoreProgress(ProgressFile):print("tkwindows, question, if yes, choix=ProgressFile if no, choix=0, ProgressFile=0")

class movingEnemies: 
    def ToCome():
        print("annimated mooving enemies")