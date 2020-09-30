"""Classes du jeu de Labyrinthe Wolf Escape"""

#Уеишщксдзцбьяаожгтнвмчюйъэфхпрл¿¡°•|¥₩ ∞±=≠~×÷!<>≤≥≈≡∂√∩%°∆←↑→↓↔+-¬αβγδεϵθϑμπρστφω*∙

# from _typeshed import WriteableBuffer
from tkinter.constants import GROOVE
import pygame
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
import os
from constantes import *
from time import sleep
from tkinter import *
from webbrowser import *

#Définition pour le système
#Pour pygame
#Définitions pour le système
#Pour pygame
# event=pygame.event.get()

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier #"levels/{}".format(fichier)
		self.structure = 0
	
	
	def generer(self):
                """Méthode permettant de générer le niveau en fonction du fichier.
                On crée une liste générale, contenant une liste par ligne à afficher"""
                print(self.fichier)
                #On ouvre le fichier
                with open(self.fichier, "r") as fichier:
                    print("we are in the with open self loop")
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
    def refreshlevels(PATH):#levelfiles
        global levelfiles
        levelfiles=os.listdir("{}".format(PATH))
        return levelfiles
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
                        if FileProgress!=0:
                            tkinterWindows.retorelevel(FileProgress)
                        
                        trackProgress.WriteProgressToFile(FileProgress)
                        return IngameProgress, FileProgress
                    else:
                        trackProgress.WriteProgressToFile("0")
                        IngameProgress=FileProgress=0
                        return IngameProgress, FileProgress
        else:
            trackProgress.WriteProgressToFile("0")
    def AskRestoreProgress(FileProgress):print("tkwindows, question, if yes, choix=ProgressFile if no, choix=0, ProgressFile=0")
    

class movingEnemies: 
    def ToCome():
        print("annimated mooving enemies")

class tkinterWindows: #currently global windows
    def choselevels():
        def LEVEL():
            Levelnumber = int(level.get())
            Cevel.destroy()
            print(Levelnumber)
            trackProgress.refreshlevels("levels")#levelfiles
            maxlevel=len(levelfiles)
            global choix
            choix=levelfiles[Levelnumber-1]
            global CREDIT
            CREDIT=False
            return choix
        trackProgress.refreshlevels("levels")#levelfiles
        maxlevel=len(levelfiles)
        Cevel = Tk()
        Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
        Frame1.pack(side=LEFT, padx=10, pady=10)

        label = Label(Frame1, text="Choose you're level:")
        label.pack()
        level=Spinbox(Frame1, from_=1, to=maxlevel, increment=1)
        level.pack(side=LEFT, padx=5)
        bouton=Button(Frame1, text="Jouer!", command=LEVEL)
        bouton.pack(side=RIGHT, padx=5)
        Cevel.mainloop()
    def retorelevel(FileProgress):
        def Yes():
            print("yes")
            choix=FileProgress
            fenetre.destroy()
            return choix, FileProgress
        def No():
            print("No")
            choix=0
            FileProgress=0
            fenetre.destroy()
            return choix, FileProgress
        fenetre = Tk()
        Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
        Frame1.pack(side=TOP, padx=10, pady=10)
        FrameButt=Frame(fenetre, borderwidth=2, relief=FLAT)
        FrameButt.pack(side=TOP, padx=0, pady=10)

        label = Label(Frame1, text="Une sauvegarde a été trouvée.")
        label.pack()
        label = Label(Frame1, text="Voulez-vous contiunuer la partie déjà entamée?")
        label.pack()
        bouton=Button(FrameButt, text="Oui", command=Yes)
        bouton.pack(side=RIGHT, padx=5)
        bouton=Button(FrameButt, text="Non", command=No)
        bouton.pack(side=RIGHT, padx=5)
        fenetre.mainloop()
    def web(url):open_new("{}".format(url))
    def Githubh():tkinterWindows.web("https://bit.ly/2YcQ4ce")
    def Facebookh():tkinterWindows.web("http://bit.ly/2EieENH")
    def Instagramh():tkinterWindows.web("http://bit.ly/2PRGBkG")
    def InstagramI():tkinterWindows.web("https://bit.ly/2EmmERy")
    def discord():tkinterWindows.web("http://bit.ly/wolfesc")
    def Answerasurveyform():tkinterWindows.web("http://bit.ly/wolfescf")
    def tipyee():tkinterWindows.web("https://bit.ly/3cqnOYV")
    def utip():tkinterWindows.web("https://github.com/404")
    def monosis():tkinterWindows.web("https://github.com/")
    def suxene():tkinterWindows.web("https://github.com/Suxene?tab=repositories")
    def totopoo():tkinterWindows.web("https://www.instagram.com/haiko_hana/")
    def gabin():tkinterWindows.web("https://github.com/")
    def defucoa():tkinterWindows.web("https://www.instagram.com/quentin.defu/")
    def marina():tkinterWindows.web("https://www.instagram.com/marinamarraskuu/")#https://www.facebook.com/marina.toussaint.5201
    def marinaF():tkinterWindows.web("https://www.facebook.com/marina.toussaint.5201")
    def caroline():tkinterWindows.web("https://github.com/")


    def main_credits():
        pfonty="Times New Roman"
        pfontw="bold"
        pfonts=9
        F1=FLAT
        bgColor="White"
        root = Tk()
        root['bg']=bgColor
        root.title("tkinter.Text sample")
        root.geometry("900x600")
        Frame1 = Frame(root, borderwidth=2, relief=F1, bg=bgColor)
        Frame1Scroolbar = Frame(Frame1, borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP2=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP =Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP3=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOPMarina=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP4=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP5=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1TOP6=Frame(Frame1Scroolbar,borderwidth=2, relief=F1, bg=bgColor)
        Frame1.pack(side=TOP, padx=10, pady=10, fill=X)
        Frame1Scroolbar.pack(side=TOP, padx=0, pady=0, fill=X)
        Frame1TOP.pack(side=TOP, padx=0, pady=0, fill=X)
        Frame1TOP2.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP3.pack(anchor=CENTER, side=TOP, padx=0, pady=0, fill=X)
        Frame1TOPMarina.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP4.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP5.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Frame1TOP6.pack(anchor=CENTER, side=TOP, padx=0, pady=0)#, fill=X
        Credits=Label(Frame1TOP, text="Credits of Wolf Escape", font=(pfonty,pfonts,pfontw), bg=bgColor)
        Programmed=Label(Frame1TOP, text="Programmed by:", bg=bgColor)
        Henry=Label(Frame1TOP, text="Henry Letellier", bg=bgColor)
        Credits.pack(anchor=CENTER)
        Programmed.pack(anchor=CENTER,side=TOP)#,fill=X
        Henry.pack(anchor=CENTER,side=TOP)#,fill=X
        git=Button(Frame1TOP2, text="Github", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Githubh)
        fac=Button(Frame1TOP2, text="Facebook", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Facebookh)
        insth=Button(Frame1TOP2, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Instagramh)
        git.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        fac.pack(anchor=CENTER,side=LEFT) #,fill=X, border=FLAT
        insth.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        Graphics=Label(Frame1TOP3, text="Graphics by:", bg=bgColor)
        Graphics.pack(anchor=CENTER,side=TOP,fill=X)
        Irina=Label(Frame1TOP3, text="Irina Marchand", bg=bgColor)
        Irina.pack(anchor=CENTER,side=TOP,fill=X)
        insti=Button(Frame1TOP3, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.InstagramI)
        insti.pack(anchor=CENTER,side=TOP)#,fill=X, relief=FLAT
        Marina=Label(Frame1TOP3, text="Marina Toussain", bg=bgColor)
        Marina.pack(anchor=CENTER,side=TOP)#,fill=X
        git=Button(Frame1TOPMarina, text="Instagram", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.marina)
        fac=Button(Frame1TOPMarina, text="Facebook", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.marinaF)
        git.pack(anchor=CENTER,side=LEFT)#,fill=X, border=FLAT
        fac.pack(anchor=CENTER,side=LEFT) #,fill=X, border=FLAT
        Feedback=Label(Frame1TOP3, text="Feedback:", bg=bgColor)
        Feedback.pack(anchor=CENTER, side=TOP)
        TUWYTATG=Label(Frame1TOP4, text="Tell us what you think about the game:", bg=bgColor)
        TUWYTATG.pack(anchor=CENTER, side=TOP)
        TUO=Label(Frame1TOP4, text="Tell us on:", bg=bgColor)
        TUO.pack(anchor=CENTER, side=TOP)
        Discord=Button(Frame1TOP4, text="Discord", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.discord)
        Discord.pack(anchor=CENTER, side=LEFT)#,fill=X
        Form=Button(Frame1TOP4, text="Answer a survey form", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.Answerasurveyform)
        Form.pack(anchor=CENTER, side=LEFT)#,fill=X
        SU=Label(Frame1TOP5, text="Support us:", bg=bgColor)
        SU.pack(anchor=CENTER, side=TOP)
        Tipyee=Button(Frame1TOP5, text="On Tipyee", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.tipyee)
        Tipyee.pack(anchor=CENTER, side=LEFT)#,fill=X
        Utip=Button(Frame1TOP5, text="On Utip", relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.utip)
        Utip.pack(anchor=CENTER, side=LEFT)#,fill=X
        MT=Label(Frame1TOP6, text="Many Thanks To all the beta testers:", bg=bgColor)
        MT.pack(anchor=CENTER, side=TOP)
        Monosis=Button(Frame1TOP6, text="Monosis", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.monosis)
        Monosis.pack(anchor=CENTER, side=TOP)#,fill=X
        Suxene=Button(Frame1TOP6, text="Suxene", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.suxene)
        Suxene.pack(anchor=CENTER, side=TOP)#,fill=X
        Totopoo=Button(Frame1TOP6, text="Totopoo", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.totopoo)
        Totopoo.pack(anchor=CENTER, side=TOP)#,fill=X
        Gabin=Button(Frame1TOP6, text="Gabin", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.gabin)
        Gabin.pack(anchor=CENTER, side=TOP)#,fill=X
        Defucoa=Button(Frame1TOP6, text="Defucoa", font=(pfonty, pfonts, pfontw), relief=F1, fg="#AE20FF", bg=bgColor, command=tkinterWindows.defucoa)
        Defucoa.pack(anchor=CENTER, side=TOP)#,fill=X
        Caroline=Button(Frame1TOP6, text="Caroline", font=(pfonty, pfonts, pfontw), relief=F1, fg="blue", bg=bgColor, command=tkinterWindows.caroline)
        Caroline.pack(anchor=CENTER, side=TOP)#,fill=X
        Quit=Button(root, text="Exit", command=root.destroy)
        Quit.pack()
        
        root.mainloop()
    def accueil(continuer_jeu,continuer_accueil):
        #Chargement et affichage de l'écran d'accueil
        accueil = pygame.image.load(image_accueil).convert()
        fenetre.blit(accueil, (0,0))
        #Rafraichissement
        pygame.display.flip()
        #On remet ces variables à 1 à chaque tour de boucle
        #global continuer_jeu,continuer_accueil
        continuer_jeu = 1
        continuer_accueil = 1
        return continuer_jeu,continuer_accueil


class gameAnimations:
    def mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,image_accueil,image_accueil2,image_accueil3,image_accueil4,image_accueil5,image_accueil6,image_accueil7):
        if mainMenuPlayed==False:
            accueil = pygame.image.load(image_accueil).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil2).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil3).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil4).convert()
            fenetre.blit(accueil, (30,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil5).convert()
            fenetre.blit(accueil, (60,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil6).convert()
            fenetre.blit(accueil, (90,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            accueil = pygame.image.load(image_accueil7).convert()
            fenetre.blit(accueil, (120,0))
            pygame.display.flip()
            sleep(frameMainMenuWait)
            mainMenuPlayed=True
            return mainMenuPlayed
        else:
            accueil = pygame.image.load(image_accueil).convert()
            fenetre.blit(accueil, (0,0))
            #Titre
            pygame.display.set_caption(titre_fenetre)
        # return acceuil

class MainLoopGame:
    def boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien): #
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
                    LEVEL=maxlevels
                    return LEVEL
                elif event.type == KEYDOWN:
                    #Si l'utilisateur presse Echap ici, on revient seulement au menu
                    if event.key == K_ESCAPE:
                        continuer_jeu = 0
                        LEVEL=maxlevels
                        return LEVEL
                    #Touches de déplacement de Wolf
                    elif event.key == K_RIGHT:
                        dk.deplacer('droite')
                    elif event.key == K_LEFT:
                        dk.deplacer('gauche')
                    elif event.key == K_UP:
                        dk.deplacer('haut')
                    elif event.key == K_DOWN:
                        dk.deplacer('bas')
                #if level (1 or 2 or ...)
                #if enemy(x,y)==(x,y):
            #enemy up/down
            #elif enemy(x,y)==(x,y):
                    #enemy left/right
                #move=1
            #if enemy up +move ==m(x,y):
                    #move=-1
            #elif enemy down -move==m(x,y):
            #move=1
            #move=1
            #if enemy left +move ==m(x,y):
                    #move=-1
            #elif enemy right -move==m(x,y):
            #move=1
                
            #Affichages aux nouvelles positions
            fenetre.blit(fond, (0,0))
            niveau.afficher(fenetre)
            fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
            pygame.display.flip()
            #Victoire -> Retour à l'accueil
            if niveau.structure[dk.case_y][dk.case_x] == '²' or niveau.structure[dk.case_y][dk.case_x] == '_'or niveau.structure[dk.case_y][dk.case_x] == '0':continuer_jeu = 0
            #return continuer_jeu, continuer
    def check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix): #niveau,
        if choix != 0 and Choix!=0:
            pygame.display.set_caption("{}{}".format(titre_fenetre,choix))
            CHOIX=choix
            # checkcredit()
            #Chargement du fond
            global fond
            if CREDIT==True:#creditindex
                fond = pygame.image.load(image_fond_credits).convert()
                # return fond
            else:
                choix="levels/{}".format(choix)
                fond = pygame.image.load(image_fond).convert()
                # return choix, fond
            #Génération d'un niveau à partir d'un fichier
            # global niveau
            niveau = Niveau(choix)
            niveau.generer()
            niveau.afficher(fenetre)
            #Création du loup
            global dk
            dk = Perso("img/sprite/w/w_rigth.png", "img/sprite/w/w_left.png", "img/sprite/w/w_up.png", "img/sprite/w/w_down.png", niveau)
            #Creating the ennemi (The gardian)
            global gardien
            gardien=Perso("img/sprite/gardien/Gardien_Droite.png", "img/sprite/gardien/Gardien_Gauche.png", "img/sprite/gardien/Gardien_haut.png", "img/sprite/gardien/Gardien_bas.png", niveau)
        return dk, gardien, fond, choix, niveau, fenetre
    def play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT):
        print("we are in the play loop")
        #continuer_accueil = 0
        if hidden==0:   
            trackProgress.refreshlevels("levels")#levelfiles
        else:
            trackProgress.refreshlevels("elementary_levels")
        global maxlevels, LEVEL
        maxlevel=len(levelfiles)
        LEVEL=0
        # print(levelfiles)
        while LEVEL<len(levelfiles):
        # for LEVEL in range(len(levelfiles)):
            print(levelfiles)
            print("level={}".format(LEVEL))
            #global continuer_jeu
            continuer_jeu = 1
            #global choix
            if Choix!=0:
                choix=levelfiles[LEVEL]
                pygame.display.set_caption("{} {}".format(titre_fenetre,choix))
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_q:
                continuer_jeu = 0
                LEVEL=maxlevel
                continuer = 0
                continuer_accueil=1
                #Variable de choix du niveau
                # choix = levelfiles[len(levelfiles-1)]
                choix=0
                Choix=0
                LEVEL=len(levelfiles)
                sys.exit(0)
                break
            else:
                print (choix)
                #choix = 'l{}'.format(i+1)
                MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix)#niveau
                MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)
                #print("tour = {}\ncontinuer_jeu = {}\nchoix={}\ncontinuer={}\nniveau={}".format(i,continuer_jeu,choix,continuer,niveau))
                LEVEL+=1
        CREDIT=True
        choix="elementary_levels/credits"
        MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix)
        MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)
        return Choix, continuer_accueil

#try and master a pygame flip for background animation in the main menu
#for i in (5)
#bg 1
#pygame.flip()
#sleep(1)
#bg 2
#pygame.flip()
#Do this for the load, and do 
#bg 1 title wolf escape
#pygame flip
#sleep (2)
#bg2 title+ HenryLetellier bla bla bla
#pygame flip
#sleep (2)
#bg3 title+ HenryLetellier bla bla bla + Irina Marchand bla bla bla
#pygame flip
#sleep (2)
#bg3 title+ HenryLetellier bla bla bla + Irina Marchand bla bla bla+Marina
#pygame flip
#...
