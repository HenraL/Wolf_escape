"""#| | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | |"""

import pygame, os, platform, requests
message=["Ok","Fail","Done","Created","Exists"]
dots="........................................"
def dire(file):
    global levelfiles
    levelfiles=os.listdir("{}".format(file))
    return levelfiles

class dealsys:
    def __init__(self,currentd,namespf,filenamebool):
        # global DS
        self.cd=currentd
        self.spf=namespf
        self.fbool=filenamebool
        # DS.slash=slash
    def pause():
        pause=input("Please press enter to continue...")
    def getName(currentd,filename):
        global filenamebool
        if os.path.exists("{}{}".format(currentd,filename))==True:
            filenamebool=True
        else:
            filenamebool=False
        return filenamebool
    def filefetch(url,spec,dest,name):
        myfile = requests.get(url)
        if spec==True:
            open("{}/{}".format(dest,name), 'wb').write(myfile.content)
        else:
            open("{}".format(name), 'wb').write(myfile.content)
    def create(folder,location):
        print("Creating folder {}".format(folder))
        try:
            os.makedirs("{}".format(folder))
            print("The folder {} has successefully been created".format(folder))
        except:
            print("Failed to create the folder {}, please create it manualy in {} of the program.".format(folder,location))
            dealsys.pause()

folder="created_levels"
dealsys.getName("",folder)
if filenamebool==False:
    dealsys.create(folder,"root")
else:
    print("{}{}[{}]".format(folder,dots,message[0]))

level=[""]*21
for i in range(len(level)-2):
    lines=[" |"]*23
    level[i]=lines
# print(level)
# for i in range(len(level)-1):
#     for j in range(len(level[i])-1):
#         print(level[i][j],end="")
#     print()
given=False
forbidden=[".","/","*","|","<",">","?",":","\\","\""]
while given==False:
    name_of_level=input("This is going to be the name of the file\nPlease do not use any  sybols such as \".\", \"/\",\"\\\",\"*\",\"|\",\"<\",\">\",\"?\",\":\", \"\"\"\nTo do a space, you can use \" \" or \"_\"\nEnter the name of the level you are going to create :")
    if name_of_level=="" or name_of_level==" " or name_of_level=="  " or name_of_level=="   ":
        given=False
        print("Please enter the name of the level, this is necessary to be able to proceed to the creation of the level.\nYou have entered: {}".format(name_of_level))
    elif name_of_level in forbidden:
        print("Please enter the name of the level without using any forbidden symbols, this is necessary to be able to proceed to the creation of the level.\nYou have entered: {}".format(name_of_level))
    else:
        print("The name of the file is: {}".format(name_of_level))
        content=False
        Change=input("Do you whish to change the name : [(y)es/(n)o]")
        if 
        given=True
given=False
while given==False:
    name_of_person=input("(This is for the side info in the level file (knowing who did which))\nHow do you wish to be called? ")
    if name_of_person=="" or name_of_person==" " or name_of_person=="  " or name_of_person=="   ":
        given=False
        print("Please enter your name, this is just to put a name on the author of the level")
    else:
        given=True