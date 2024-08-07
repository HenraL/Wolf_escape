import sys
import os
def charge_labyrinthe(nom) :
"""
Charge le labyrinthe depuis le fichier nom.txt
nom : nom du fichier contenant le labyrinthe(sans l’extension .txt)
Valeur de retour :
Tuple contenant les données du labyrinthe
"""
fic = open(nom + ".txt", "r")
data = fic.readlines()
fic.close()
for i in range(len(data)) :
    data[i] = data[i].strip()
    return tuple(data)
def barre_score(n_level) :
    """
    Barre de score affichant les données du jeu
    n_level : niveau courant
    Pas de valeur de retour
    """
    print("Level : {:3d}".format(n_level))
def affiche_labyrinthe(lab, perso, pos_perso):
    """
    Affichage d’un labyrinthe
    lab : Variable contenant le labyrinthe
    perso : caractère représentant le personnage
    pos_perso : liste contenant la position du personnage
    [ligne, colonne]
    Pas de valeur de retour
    """
    n_ligne = 0
    for ligne in lab:
        if n_ligne == pos_perso[1]:
            print(ligne[0:pos_perso[0]] + perso + ligne[pos_perso[0]+1:]) #slicing
        else :
            print(ligne)
        n_ligne += 1
def efface_ecran() :
    """
    Efface l’écran de la console
    """
    if sys.platform.startswith("win") :
        # Si système Windows
        os.system("cls")
    else :
        # Si système Linux ou OS X
        os.system("clear")
def verification_deplacement(lab, pos_col, pos_ligne):
    """
    Indique si le déplacement du personnage est autorisé ou pas.
    lab : Labyrinthe
    pos_ligne : position du personnage sur les lignes
    pos_col : position du personnage sur les colonnes
    Valeurs de retour :
    None : déplacement interdit
    [col, ligne] : déplacement autorisé
    sur la case indiquée par la liste
    """
    # Calcul de la taille du labyrinthe
    n_cols = len(lab[0])
    n_lignes = len(lab)
    # Teste si le déplacement conduit le personnage en dehors de l’aire
    # de jeu
    if pos_ligne < 0 or pos_col < 0 or pos_ligne > (n_lignes -1) or \
        pos_col > (n_cols -1) :
        return None
    elif lab[pos_ligne][pos_col] == "O" :
        # Une position hors labyrinthe indique la victoire
        return[-1, -1]
    elif lab[pos_ligne][pos_col] != " " :
        return None
    else :
        return [pos_col, pos_ligne]
def choix_joueur(lab, pos_perso):
    """
    Demande au joueur de saisir son déplacement
    et vérifie s’il est possible.
    Si ce n’est pas le cas affiche un message,
    sinon modifie la position du perso dans la liste pos_perso
    lab : Labyrinthe
    pos_perso : liste contenant la position du personnage
    [colonne, ligne]
    Pas de valeur de retour
    """
    choix = input("Votre déplacement (Haut/Bas/Droite/Gauche/Quitter) ? ")
    if choix == "H" or choix == "Haut" :
        dep = verification_deplacement(lab, pos_perso[0], pos_perso[1] -1)
    elif choix == "B" or choix == "Bas" :
        dep = verification_deplacement(lab, pos_perso[0], pos_perso[1] +1)
    elif choix == "G" or choix == "Gauche" :
        dep = verification_deplacement(lab, pos_perso[0] -1, pos_perso[1])
    elif choix == "D" or choix == "Droite" :
        dep = verification_deplacement(lab, pos_perso[0] +1, pos_perso[1])
    elif choix == "Q" or choix == "Quitter" :
        os._exit(1)
    if dep == None :
        print("Déplacement impossible")
        input("Appuyez sur <Return> pour continuer")
    else :
        pos_perso[0] = dep[0]
        pos_perso[1] = dep[1]
def jeu(level, n_level, perso, pos_perso):
"""
Boucle principale du jeu. Affiche le labyrinthe dans ses différents
états après les déplacements du joueur.
level : Labyrinthe
n_level : numéro du niveau courant
perso : caractère représentant le personnage
pos_perso : liste contenant la position du personnage
[colonne, ligne]
"""
while True :
efface_ecran()
affiche_labyrinthe(level, perso, pos_perso)
barre_score(n_level)
choix_joueur(level, pos_perso)
if pos_perso == [-1, -1] :
print("Vous avez passé le niveau !")
input("Appuyez sur <Return> pour continuer")
break
