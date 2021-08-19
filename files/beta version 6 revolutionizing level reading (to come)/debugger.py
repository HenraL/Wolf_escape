import pygame
def overwrite_line(file="Start_debug.txt",line=0,content=1):
    """Overwriting the line determining if the program can or not start"""
    f=open(file,"r")
    e=f.read().split("\n")
    f.close()
    e[line]=content
    r=""
    for i in e:
        r+=i
    f=open(file,"w")
    f.write(r)
    f.close()
overwrite_line(file="Start_debug.txt",line=0,content="1")
import classes as CA
import constantes as CO
import wolf_escape as WE
class root:
    def __init__(self,CA,CO,WE):
        self.continuer=1
        self.continuer_jeu = 1
        self.continuer_accueil = 1
        self.choix=0
        self.CA=CA
        self.CO=CO
        self.WE=WE
        self.CREDIT=False
        self.image_fond_credits=CO.image_fond_credits
        self.image_fond=CO.image_fond

class The_Debug(root):
    def __init__(self):
        self.a=""

    class Run:
        def __init__(self,CO):
            self.fenetre=""
            self.cote_fenetrex=CO.cote_fenetrex
            self.cote_fenetrey=CO.cote_fenetrey
            self.image_icone=CO.image_icone
            self.titre_fenetre=CO.titre_fenetre
            self.choix="levels/002_l2_2.we"
            self.Choix=""
            self.hidden=0
            self.wolf_right="img/sprite/w/w_rigth.png"
            self.wolf_left="img/sprite/w/w_left.png"
            self.wolf_up="img/sprite/w/w_up.png"
            self.wolf_down="img/sprite/w/w_down.png"
        
        def pygame_window(self):
            WE.pygame.init()
            #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
            self.fenetre = WE.pygame.display.set_mode((self.cote_fenetrex, self.cote_fenetrey))
            #Icone
            self.icone = WE.pygame.image.load(self.image_icone)
            WE.pygame.display.set_icon(self.icone)
            #Titre
            WE.pygame.display.set_caption(self.titre_fenetre)
            #rendre le déplacement fluide
            WE.pygame.key.set_repeat(400, 30)
            #Rafraichissement
            WE.pygame.display.flip()
        def pygame_launch_game(self):
            continuer_jeu = ri.continuer_jeu
            continuer_accueil = ri.continuer_accueil
            
            # CA.MainLoopGame.check(ri.image_fond,ri.image_fond_credits,self.fenetre,self.choix,ri.CREDIT,self.Choix,self.hidden)#niveau
            fond=pygame.image.load(CO.image_fond).convert()
            niveau=CA.Niveau(self.choix)
            niveau.generer()
            niveau.afficher(self.fenetre)
            wolf=CA.Perso(self.wolf_right,self.wolf_left,self.wolf_up,self.wolf_down,niveau)


    class File:
        def __init__(self):
            self.a=""
            self.DebugO_F="Start_debug.txt"
            
        def Read(file):
            f=open(file,"r")
            e=f.read()
            f.close()
            return e
        def Write(file,content):
            f=open(file,"w")
            f.write(f"{content}")
            f.close()
        def Add(file,content):
            f=open(file,"a")
            f.write(str(content))
            f.close()

    def e():
        print("debug initialised")
    def overwrite_line(file="",line=0,content=1):
        """Overwriting the line determining if the program can or not start"""
        if file=="":
            file=The_Debug.File.DebugO_F
        e=The_Debug.File.Read(file)
        e=e.split("\n")
        e[line]=content
        r=""
        for i in e:
            r+=i
        The_Debug.File.Write(file,r)
    

    class Vars:
        def __init__(self):
            self.a=""
        
        def correlate_W_ID():
            """Correlate Walls and IDs"""
            walls=CO.walls
            FW=CO.FunkyWalls
            FWD=CO.FunkyWalsDone
            print(f"len(walls)={len(walls)}, len(FW)={len(FW)}, len(FWD)={len(FWD)}")
            if len(walls)==len(FW) and len(walls)==len(FWD):
                for i in range(len(walls)):
                    print(f"walls={walls[i]}, FW={FW[i]}, FWD={FWD[i]}")
            

ri=root(CA,CO,WE)
TDI=The_Debug()
FI=TDI.File()
VI=TDI.Vars()
RI=TDI.Run(CO)
fullInitialisation=0
The_Debug.e()
def OneOrAll(fullInitialisation=1):
    if fullInitialisation==1:
        The_Debug.Run.pygame_window(RI)
        The_Debug.Run.pygame_launch_game(RI)


    else:
        The_Debug.Vars.correlate_W_ID()
OneOrAll(fullInitialisation)
OneOrAll(1)
OneOrAll(fullInitialisation)
The_Debug.overwrite_line(file=FI.DebugO_F,line=0,content="0")