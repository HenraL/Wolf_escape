# import Spritelist as spritelist
from Spritelist import *
from webbrowser import open_new
alert=[
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' '], 
    [' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', '\\', ' '], 
    [' ', ' ', ' ', ' ', ' ', '/', ' ', '|', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', '|', ' ', ' ', '\\', ' '], 
    [' ', ' ', ' ', ' ', '/', ' ', ' ', '|', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', '|', ' ', ' ', ' ', '\\', ' '], 
    [' ', ' ', ' ', '/', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '\\', ' '], 
    [' ', ' ', '/', ' ', ' ', ' ', ' ', '_', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ' ', ' ', ' ', ' ', '_', ' ', ' ', ' ', ' ', ' ', '\\', ' '], 
    [' ', '/', ' ', ' ', ' ', ' ', '|', '_', '|', ' ', ' ', ' ', ' ', ' ', '\\', ' ', ' ', '!', 'L', "'", 'a', 'c', 't', 'i', 'o', 'n', ' ', 'à', ' ', 'l', 'a', 'q', 'u', 'e', 'l', 'l', 'e', ' ', 'v', 'o', 'u', 's', ' ', 'v', 'o', 'u', 's', ' ', 'a', 'p', 'p', 'r', 'é', 't', 'e', 'z', ' ', 'e', 's', 't', ' ', 'i', 'r', 'r', 'é', 'v', 'e', 'r', 's', 'i', 'b', 'l', 'e', ' ', ' ', '/', ' ', ' ', ' ', ' ', '|', '_', '|', ' ', ' ', ' ', ' ', ' ', '\\', ' '], 
    ['/', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', ' ', 'ê', 't', 'e', 's', '-', 'v', 'o', 'u', 's', ' ', 's', 'û', 'r', 'e', ' ', 'd', 'e', ' ', 'v', 'o', 'u', 'l', 'o', 'i', 'r', ' ', 's', 'u', 'p', 'p', 'r', 'i', 'm', 'e', 'r', ' ', 'c', 'e', ' ', 's', 'p', 'r', 'i', 't', 'e', '?', '!', ' ', ' ', ' ', ' ', ' ', '/', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '\\', ' '], 
    []]
face=[
    [' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], 
    [' ', ' ', '/', ' ', '_', '_', ' ', ' ', ' ', '_', '_', ' ', ' ', '\\'], 
    [' ', '/', ' ', '|', '_', '_', '|', ' ', '|', '_', '_', '|', ' ', ' ', '\\'], 
    ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'], 
    [' ', '\\', ' ', '\\', '_', '_', '_', '_', '_', '_', '_', '_', '/', ' ', '/'], 
    [' ', ' ', '\\', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '/'], 
    []]
facesad=[
    [' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], 
    [' ', ' ', '/', ' ', '_', '_', ' ', ' ', ' ', '_', '_', ' ', ' ', '\\'], 
    [' ', '/', ' ', '|', '_', '_', '|', ' ', '|', '_', '_', '|', ' ', ' ', '\\'], 
    ['|', ' ', ' ', ' ', '_', '_', '_', '_', '_', '_', '_', '_', ' ', ' ', ' ', '|'], 
    [' ', '\\', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ' ', '/'], 
    [' ', ' ', '\\', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '/'], 
    []]
rounded=False
class edditing:
    def __init__(self,spritelist):
        self.list=spritelist
    def images(image):
        for i in range(len(image)):
            for j in range(len(image[i])):
                print(image[i][j],end="")
            print()
    def WRITE(content):
        f=open("Spritelist.py",'w')
        f.write("{}\n#Créé par Henry Letellier".format(content))
        f.close()
    def show(list,ask):
        if ask==True:
            show=input("\nVoulez-vous afficher la liste actuelle des sprite? [(o)ui/(n)on]")
        else:
            show="o"
        if show=="o" or show=="O" or show=="0":
            IDSPACE,NAMESPACE,SPRITEIMAGENAMESPACE="","",""
            print("._____________________________________.")
            print("|             Sprite                  |")
            print("|_____________________________________|")
            print("|ID:        |Name:       |ImageName:  |")
            for TABLE in range(len(list)):
                ID=len(list[TABLE]["SpriteId"])
                for e in range(11-ID):
                    IDSPACE+=" "
                NAME=len(list[TABLE]["SpriteName"])
                for e in range(12-NAME):
                    NAMESPACE+=" "
                SPRITEIMAGENAME=len(list[TABLE]["SpriteImageName"])
                for e in range(12-SPRITEIMAGENAME):
                    SPRITEIMAGENAMESPACE+=" "
                print("|{}{}|{}{}|{}{}|".format(list[TABLE]["SpriteId"],IDSPACE,list[TABLE]["SpriteName"],NAMESPACE,list[TABLE]["SpriteImageName"],SPRITEIMAGENAMESPACE))
                IDSPACE,NAMESPACE,SPRITEIMAGENAMESPACE="","",""
            print("|___________|____________|____________|")
        else:
            print()
            #print("______Retour au menu précedent_________")
    def search(list,type,item):
        if type==1:
            type="SpriteId"
        elif type==2:
            type="SpriteImageName"
        else:
            type="SpriteName"
        for i in range(len(list)):
            if list[i][type]==item:
                print("\nLe Sprite que vous cherchez est le numéro {}, il se nome '{}' et est représenté par l'image '{}'.".format(list[i]["SpriteId"],list[i]["SpriteName"],list[i]["SpriteImageName"]))
                edditing.show(list,True)
                break
            else:
                if i==len(list)-1:
                    print("\nLe Sprite que vous cherchiez n'as pas été trouvé")
                    edditing.show(spritelist,False)
    def appendlist(list):
        edditing.show(list,True)
        GetSpriteId=int(spritelist[len(spritelist)-1]["SpriteId"])+1
        GetSpriteName=input("\nEntrez le nom de votre sprite:")
        GetSpriteImageName=input("\nEntrez le nom de l'image qui représente votre sprite (n'oubliez pas de préciser l'extension):")
        testListAdd={"SpriteId":"{}".format(GetSpriteId),"SpriteName":"{}".format(GetSpriteName),"SpriteImageName":"{}".format(GetSpriteImageName)}
        testListAddSpriteName="{}".format(testListAdd["SpriteName"])
        testListAddSpriteImageName="{}".format(testListAdd["SpriteImageName"])
        for i in range(len(list)):
            testListInc={"SpriteId":"{}".format(list[i]["SpriteId"]),"SpriteName":"{}".format(list[i]["SpriteName"]),"SpriteImageName":"{}".format(list[i]["SpriteImageName"])}
            testListIncSpriteName="{}".format(testListInc["SpriteName"])
            testListIncSpriteImageName="{}".format(testListInc["SpriteImageName"])
            if testListAddSpriteName==testListIncSpriteName:
                print("\nLe nom de sprite que vous avez choisi existe déjà. Veuillez en choisir un autre")
                break
            elif testListAddSpriteImageName==testListIncSpriteImageName:
                print("\nL'image pour le sprite que vous avez entré existe déjà, il apparitient au sprite {}".format(testListIncSpriteImageName))
                break
            else:
                if i==len(list)-1:
                    spritelist.append({"SpriteId":"{}".format(GetSpriteId),"SpriteImageName":"{}".format(GetSpriteImageName),"SpriteName":"{}".format(GetSpriteName)})
                    print("\nLe Sprite {} a été ajouté avec succès.".format(testListAdd["SpriteName"]))
                    edditing.WRITE("spritelist={}".format(spritelist))
                    edditing.show(list,True)
                    return spritelist
                else:
                    continue
    def replace(list,idd):
        edditing.show(list,True)
        for i in range(len(list)):
            if list[i]["SpriteId"]==idd:
                getModifyElementcont=True
                while getModifyElementcont==True:
                    print("\nIndexe du sprite: {} (1) Nom: '{}' (2) Nom de l'image: '{}'.".format(list[i]["SpriteId"],list[i]["SpriteName"],list[i]["SpriteImageName"]))
                    getModifyElement=input("\nQue voulez-vous changer? [(1) le nom, (2) le nom de l'image]:")
                    try:
                        getModifyElementcont=False
                        getModifyElement=int(getModifyElement)
                        if getModifyElement==1:
                            spriteNameCorrect=False
                            while spriteNameCorrect==False:
                                NewElement=input("\nEntrez le nouveau nom que vous souhaitez affecter au sprite:")
                                for azteck in range(len(list)):
                                    if list[azteck]["SpriteName"]==NewElement:
                                        print("\nMerci de choisir un nouveau nom car celui-ci appartient déjà au sprite numéro {}".format(list[azteck]["SpriteId"]))
                                        break
                                    else:
                                        if azteck==len(list)-1:
                                            print("\nCe nom est disponible et a été affecté au sprite que vous désiriez modifier.")
                                            list[i]["SpriteName"]=NewElement
                                            print("\nIndexe du sprite: {} Nom: '{}' Nom de l'image: '{}'.".format(list[i]["SpriteId"],list[i]["SpriteName"],list[i]["SpriteImageName"]))
                                            edditing.show(list,True)
                                            spriteNameCorrect=True
                                            edditing.WRITE("spritelist={}".format(list))
                                            return list
                                        else:
                                            continue
                            
                        elif getModifyElement==2:
                            spriteNameImageCorrect=False
                            while spriteNameImageCorrect==False:
                                NewElement=input("\nEntrez le nouveau nom que vous souhaitez affecter à l'image du sprite:")
                                for azteck in range(len(list)):
                                    if list[azteck]["SpriteImageName"]==NewElement:
                                        print("\nMerci de choisir un nouveau nom d'image car celui-ci appartient déjà au sprite numéro {}".format(list[azteck]["SpriteId"]))
                                        break
                                    else:
                                        if azteck==len(list)-1:
                                            print("\nCe nom est disponible et a été affecté au nom de l'image du sprite que vous désiriez modifier.")
                                            list[i]["SpriteImageName"]=NewElement
                                            print("\nIndexe du sprite: {} Nom: '{}' Nom de l'image: '{}'.".format(list[i]["SpriteId"],list[i]["SpriteName"],list[i]["SpriteImageName"]))
                                            edditing.show(list,True)
                                            spriteNameImageCorrect=True
                                            edditing.WRITE("spritelist={}".format(list))
                                            return list
                                        else:
                                            continue
                    except:
                        print("\nMerci de ne rentrer que 1 (pour le nom) ou 2 (pour le nom de l'image).\nVous avez entré {}".format(getModifyElement))
                        getModifyElementcont==True
                        # continue
                break
            else:
                if i==len(list)-1:
                    print("\nLe Sprite que vous cherchiez n'as pas été trouvé")
                    edditing.show(list,False)
    def remove(spritelist):
        edditing.show(spritelist,True)
        GetSpriteListID=input("Entrez l'ID du sprite à supprimer:")
        if GetSpriteListID.isnumeric()==True:
            for i in range(len(spritelist)):
                if spritelist[i]["SpriteId"]==str(GetSpriteListID):
                    print("Le sprite que vous allez supprimer est : ID: {} Nom: {} Nom de L'image: {}".format(spritelist[i]["SpriteId"],spritelist[i]["SpriteName"],spritelist[i]["SpriteImageName"]))
                    edditing.images(alert)
                    confirme=input("Confirmez-vous vouloir supprimer ce sprite à jamais? [(o)ui/(n)on]")
                    if confirme=="o" or confirme=="O":
                        spritelist.pop(i)
                        edditing.images(face)
                        print("Le sprite a été supprimé avec succès.")
                        edditing.WRITE("spritelist={}".format(spritelist))
                        edditing.show(spritelist,True)
                    else:
                        print("Suppression annulée, le sprite n'a pas été détruit.")
                        edditing.images(face)
                        edditing.show(spritelist,True)
                else:
                    if i==len(spritelist)-1:
                        edditing.images(facesad)
                        print("\nLe Sprite que vous cherchiez n'as pas été trouvé")
                        edditing.show(spritelist,True)
        else:
            print("\nMerci de ne rentrer qu'un nombre allant de 0 à {}".format(spritelist[len(spritelist)-1]["SpriteId"]))
                            


# spritelist=[{"SpriteId":"1","SpriteImageName":"didgit_one.png","SpriteName":"one"}]
# print(spritelist)
contiinue=True
while contiinue:
    if rounded==False:
        print("\nBienvenue sur le programme de répertoriation des sprites du jeux:")
        rounded=True
    main_menu_choice=input("\nMerci de ne pas mettre de \" \" de part et d'autre de vos réponses.\nSi vous le faites, le programme ne vous donneras aucune réponse ou une erreur.\n(s) afficher la liste actuelle des sprite, (f) Trouver les informations sur un sprite, (a) Ajouter un nouveau personnage à la liste, (c) Modifier un atribut d'un des sprite de la liste, (r) Supprimer un sprite (q) Quitter:\n")
    if main_menu_choice=="s" or main_menu_choice=="S":
        edditing.show(spritelist,False)
    elif main_menu_choice=="f" or main_menu_choice=="F":
        mainGetType=True
        while mainGetType==True:
            edditing.show(spritelist,True)
            GetType=input("\nEntrez le mode de recherche souhaité: [(1)[\"SpriteId\"],(2)[\"SpriteName\"],(3)[\"SpriteImageName\"]]")
            try :
                GetType=int(GetType)
                if GetType==1:
                    mainGetType=False
                    type=GetType
                    getItem=True
                    while getItem==True:
                        Item=input("\nEntrez le numéro correspondant au sprite recherché: (de 0 à {})".format(spritelist[len(spritelist)-1]["SpriteId"]))
                        try:
                            item=int(Item)
                            item=str(item)
                            getItem=False
                        except:
                            print("\nMerci de ne rentrer qu'un nombre allant de 0 à {}".format(spritelist[len(spritelist)-1]["SpriteId"]))
                            continue
                elif GetType==2:
                    mainGetType=False
                    type=3
                    item=input("\nEntrez le nom correspondant au sprite recherché:")
                elif GetType==3:
                    mainGetType=False
                    type=2
                    item=input("\nEntrez le nom de l'image correspondant au sprite recherché:")
            except:
                print("\nMerci de ne rentrer que 1 2 ou 3.\n Vous avez entré {}".format(GetType))
                continue
        edditing.search(spritelist,type,item)
    elif main_menu_choice=="a" or main_menu_choice=="A":
        edditing.appendlist(spritelist)
    elif main_menu_choice=="c" or main_menu_choice=="C":
        edditing.show(spritelist,False)
        getItem=True
        while getItem==True:
            ID=input("\nEntrez le numéro correspondant au sprite recherché: (de 0 à {})".format(spritelist[len(spritelist)-1]["SpriteId"]))
            try:
                item=int(ID)
                idd=str(item)
                getItem=False
            except:
                print("\nMerci de ne rentrer qu'un nombre allant de 0 à {}".format(spritelist[len(spritelist)-1]["SpriteId"]))
                continue
        edditing.replace(spritelist,idd)
    
    elif main_menu_choice=="r" or main_menu_choice=="R":
        edditing.remove(spritelist)
    elif main_menu_choice=="q" or main_menu_choice=="Q":
            print("\nAu revoir.\n\n    /\ \n   /__\ \n  /____\ \n /______\ \n|.      .| \n|        | \n|\______/| \n|________| \n\nCréé par Henry Letellier")
            contiinue=False
    else:
        print("\nMerci de vous assurer de n'avoir entré que: s ou S (pour afficher la liste actuelle des sprite), f ou F (pour trouver les informations sur un sprite), a ou A (pour ajouter un nouveau personnage à la liste), C ou C (pour modifier un atribut d'un des sprite de la liste), r ou R (pour supprimer un sprite), q ou Q (pour quitter).\n Vous avez entré {}".format(main_menu_choice))

# spritelist.remove

#        /\                                                                        /\
#       /  \                                                                      /  \
#      / |  \                                                                    / |  \
#     /  |   \                                                                  /  |   \
#    /   |    \                                                                /   |    \
#   /    _     \                                                              /    _     \
#  /    |_|     \  !L'action à laquelle vous vous apprêtez est irréversible  /    |_|     \
# /______________\      êtes-vous sûre de vouloir supprimer ce sprite?!     /______________\

#    __________
#   / __   __  \
#  / |__| |__|  \
# |              |
#  \ \________/ /
#   \__________/

#    __________
#   / __   __  \
#  / |__| |__|  \
# |   ________   |
#  \ /        \ /
#   \__________/