import os
def clean():
    os.system("cls")
fichier="002_l2"
fichier="002_l2 - Copie"
CreatingGameLine=""
GameLine=[]
CreatingGameSprite=""
GameSprite=[]
def read(choice):
    f=open(choice,"r")
    global file
    file=f.read()
    f.close()
    return file
#with open(fichier, "r") as file:#self.fichier
def process(file):
    #print("fichier=",fichier)
    print("file=",file)
    GameLine=[]
    CreatingGameSprite=""
    GameSprite=[]
    for line in file:
        if line!="|" and line!="\n":
            CreatingGameSprite+=line
            #print("line=",line)
            #print("CreatingGameSprite=",CreatingGameSprite)
        elif line=="|" and line!="\n":
            #print("CreatingGameSprite=",CreatingGameSprite)
            #print("GameSprite=",GameSprite)
            GameSprite.append(CreatingGameSprite)
            CreatingGameSprite=""
        elif line=="\n":
            GameLine.append(GameSprite)
            GameSprite=[]
    structure=GameLine
    print("structure=",structure)
    print("GameSprite=",GameSprite)

read(fichier)
process(file)
