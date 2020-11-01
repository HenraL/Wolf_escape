# Sprite file link = https://repl.it/@HanraLatalliar/Sprites#Spritelist.py
from tkinter import *
from time import sleep
answer=""
class tk_windows:
    def __init__(twin,mainwinchoice):
        twin.mainwinchoice=mainwinchoice
    # def main_menu(twin):
    #     continue
    def QuestionYN(sentence1,sentence2,answer1,answer2):
        def Yes():
            fenetre.destroy()
            answer="yes"
            return answer
        def No():
            answer="no"
            fenetre.destroy()
            return answer
        fenetre = Tk()
        Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
        Frame1.pack(side=TOP, padx=10, pady=10)
        FrameButt=Frame(fenetre, borderwidth=2, relief=FLAT)
        FrameButt.pack(side=TOP, padx=0, pady=10)

        label = Label(Frame1, text="{sentence1}")
        label.pack()
        label = Label(Frame1, text="{sentence2}")
        label.pack()
        bouton=Button(FrameButt, text="{answer1}", command=Yes)
        bouton.pack(side=RIGHT, padx=5)
        bouton=Button(FrameButt, text="{answer2}", command=No)
        bouton.pack(side=RIGHT, padx=5)
        fenetre.mainloop()
    def watermarkf(s):
        print("\nCreated by Henry Letellier\n ._____. \n |.   .| \n |  |  | \n |\___/| \n |_____| ")
        sleep(s)
    def main_menu():
        def Yes():
            fenetre.destroy()
            answer="yes"
            return answer
        def No():
            answer="no"
            fenetre.destroy()
            return answer
        fenetre = Tk()
        Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
        Frame1.pack(side=TOP, padx=10, pady=10)
        FrameButt=Frame(fenetre, borderwidth=2, relief=FLAT)
        FrameButt.pack(side=TOP, padx=0, pady=10)

        label = Label(Frame1, text="{sentence1}")
        label.pack()
        label = Label(Frame1, text="{sentence2}")
        label.pack()
        bouton=Button(FrameButt, text="{answer1}", command=Yes)
        bouton.pack(side=RIGHT, padx=5)
        bouton=Button(FrameButt, text="{answer2}", command=No)
        bouton.pack(side=RIGHT, padx=5)
        fenetre.mainloop()
import pygame, os, sys, platform
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *

from webbrowser import open_new

given=False
while given==False:
    author=input("(This is for the side info in the level file (knowing who did which))\nHow do you wish to be called? ")
    if author=="" or author==" " or author=="  " or author=="   ":
        given=False
        print("Please enter your name, this is just to put a name on the author of the level")
    else:
        given=True

pygame.init()

Computer_type=platform.system()
CT=str(Computer_type)
# mac: https://youtu.be/j3yH6FfD_Wk
# pc: https://github.com/HenraL/Install_pygame/tree/master/files
# linux: https://www.youtube.com/results?search_query=how+to+install+pip+on+linux

try:
    import requests
except:
    try:
        os.system("pip install requests")
    except:
        try:
            try:
                os.system("py -m pip install pip")
            except:
                os.system("py -m pip install --upgrade pip")
        except:
            print("If this is your first time using this program, please consider running it with admin rights.")
            if CT=='Windows':
                piplink="https://github.com/HenraL/Install_pygame/tree/master/files"
            elif CT=='Linux':
                piplink="https://www.youtube.com/results?search_query=how+to+install+pip+on+linux"
            else:
                piplink="https://youtu.be/j3yH6FfD_Wk"
            tk_windows.QuestionYN("If this is already the case, please consider installing the 'pip' module to enable the program to download and import the 'requests' library.","Do you wish to open the link to the pip installing file? (link: {}) [(y)es/(n)o]".format(piplink),"Yes","No")
            askpip=answer
            if askpip=="y" or askpip=="Y":
                open_new(piplink)
            else:
                print()

class dealsys:
    def __init__(DS,currentd,namespf,filenamebool):
        # global DS
        DS.cd=currentd
        DS.spf=namespf
        DS.fbool=filenamebool
    def pause():
        pause=input("Please press enter to continue...")
    def getCurrent():
        global currentd
        currentd=os.getcwd()
        if platform.system()=="Windows":
           currentd+="\\"
        else:
            currentd+="/"
        return currentd
    def getName(currentd,filename):
        global filenamebool
        if os.path.exists("{}{}".format(currentd,filename))==True:
            filenamebool=True
        else:
            filenamebool=False
        return filenamebool
    def filefetch(url,dest,name):
        myfile = requests.get(url)
        open("{}/{}".format(dest,name), 'wb').write(myfile.content)

# dest="sprite_list"
# url="https://raw.githubusercontent.com/HenraL/Wolf_escape_Sprite/main/file/Common_file/Spritelist.py"
# name="Spritelist.{}".format("py")

dealsys.getCurrent()
dealsys.getName(currentd,"sprite_list")
print(filenamebool)
url="https://raw.githubusercontent.com/HenraL/Wolf_escape_Sprite/main/file/Common_file/Spritelist.py"
name="Spritelist.py"
if filenamebool==True:
    try:
        dealsys.filefetch(url,"sprite_list",name)
        print("The Sprite_list.py file has been successefully updated.")
    except:
      print("We have not succeded in downloading the file {} please visit {} to download it".format(name,url))
      print("Save the page in the folder sprite_list of the program")
    print()
else:
    print("Creating the folder sprite_list")
    try:
        os.makedirs("sprite_list")
        print("The folder sprite_list has successefully been created")
        try:
            dealsys.filefetch(url,"sprite_list",name)
            print("The Sprite_list.py file has been successefully updated.")
        except:
            print("We have not succeded in downloading the file {} please visit {} to download it".format(name,url))
            print("Save the page in the folder sprite_list of the program")
        print()
    except:
        print("Failed to create the sprite_list folder, please create it manualy in the root of the program.")
contiinue=1
while contiinue==1:
    tk_windows.main_menu()
    tw=tk_windows
    if tw=="s": #(show)
#   tw.get_level()
# elif tw=="c": #(create)
#   tw.get_level_file_name()
#   tw.get_spritelist()
#   tw.display_spritelist_collum_scroll() (or if this blocks prog, tw.display_spritelist_collum_scroll_non_blocker()
#   level_list=[]
#   while still_in_edit==True:
#       game.display_pygame_widow(current)
#       height=20
#       length=23
#       while line_still_in_edditing==True:
#           for sprite_line in range(heigth-1):
#               level_list_icon=[]
#               for sprite_icon in range(length-1):
#                   SpriteSpriteGiven=False
#                   while SpriteSpriteGiven==False:
#                       Sprite=input("Entrez le numéro du sprite que vous souhaitez ajouter sur la ligne n°{sprite_line} à la case n°{sprite_icon}")
#                       for checkSprite in range(len(SpriteList)):
#                           if Spritelist[checkSprite]["ID"]==Sprite:
#                               SpriteListExist=True
#                               break
#                           else:
#                               if checkSprite==len(SpriteList):
#                                   SpriteListExist=False
#                                   print(Le Sprite que vous avez entré n'existe pas, vérifiez sont Identifiant et retentez à nouveau.)
#                       if SpriteListExist==True:
#                           GetBon=input("Le srite {Sprite} du nom de {SpriteId} dont l'image se nome {SpriteImage} vous convient-il? [(o)ui/(n)on]")
#                           if GetBon=="o":
#                               level_list_icon.append("{}".format(str(Sprite)))
#                               temp_level_list[sprite_icon]=level_list_icon
#                               game.display_pygame_window(current)
#                           else:
#                               SpritelistExist=False
#                       else:
#                           print()
#               level_list.append(level_list_icon)
#               temp_level_list=level_list
#               game.display_pygame_window(current)
#   dealsys.write_level(level_list) ((  total_to_write=""
#                                       for line in range(len(list)):
#                                           for icons in range(len(list[line])):
#                                               total_to_write+="{icons}|"
#                                           total_to_write+="\n"
#                                       total_to_write+="\n#Level Created by '{author}' at {DATETIMEDATE,DAY,MONTH,YEAR}\n#This level was created with the leve_creator.\n#The program level_creator.py was coded, thougth and designed by Henry Letellier\n#If you liked this level\n#You can inform its creator by posting on the discord server in the following way:\n#Goto the room #level_feedback\n#write your message\n#Please strucutre your message the following way:\n#name of the level file (or of the title of the window)\n#what you thought about the level\n#(optional): your name."
#                                       f=open(filename,"w")
#                                       f.write(total_to_write)
#                                       f.close()
#                                       ))
# elif tw=="t": (test)
#   tw.disclamer_on_partialy_finished_levels()
#   game.play(current_list)
# elif tw=="m": (modify)
#   tw.show_level_list_and_ask_which_level_to_open_to_edit()
#   dealsys.open_level_to_edit()
#   dealsys.show_level_with_sprite_matrix()
#   tw.ask_line_to_mod()
#   tw.ask_sprite_to_mod_in_line()
#   sprite_chosen=False
#   while sprite_chosen==False:
#       new_sprite_get=input("Enter the number corresonding to the new sprite: ")
#       dealsys.check_list()
#       if check_list==True:
#           level_edit[line][sprite]=new_sprite_get
#           sprite_chosen=True
#       else:
#           print("The Sprite that you chose does not exist.\nPlease enter a new one.\nYou have entered {new_sprite_get}.")
#           sprite_chosen=False
# elif tw=="r": (refresh)
#   try:
#       dealsys.refresh(list)
#       from Spritelist import *
#       print("The Spritelist has been refreshed")
#   except:
#       print("The Spritelist coudln't be refreshed due to an unknown error.\nPlease check your internet connection and try again (or running this program whith admin rights).")
# elif tw=="q": (quit)
#   print("Thank you for using this program.\nSee you next time.\nThis program was created by Henry Letellier.")
#   tw.watermarkf(2)
#   dealsys.pause()
    # for i in range(5):
    #     if i<=5:
    #         print(".")
    #     else:
    #         contiinue=False
    #         break
    contiinue=2
    print(contiinue)