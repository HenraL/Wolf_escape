from pygame import *
from classImporter import *
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
            # MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)
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
