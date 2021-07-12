import pygame, os, sys,requests
from string import ascii_letters,punctuation
from pygame.locals import *
from pygame.mixer import *
from pygame.display import *
from pygame.constants import *
from tkinter import *
from time import sleep
from webbrowser import open_new
#------------------------- Constanstes.py file -------------------------------

""" Booting up, initialising vars to ensure the required files exist before we start the game."""
contentOflist=requests.get("https://hanralatalliardwork.github.io/wolf_escape_home/files/requirements/list.py")
if contentOflist.status_code==200:
    open("liste.py","wb").write(contentOflist.content)
import liste as theLists
main_for_rec=theLists.main_for_rec
main_for_rec_dict=theLists.main_for_rec_dict

"""Constantes du jeu de Labyrinthe Wolf escape"""

#ingame booleen variables
CREDIT=False
# exitSpaceGame=False

#Paramètres de la fenêtre
# nombre_sprite_cote = 15
nombre_sprite_cote = 100
taille_sprite = 30
# cote_fenetrex = 455
# cote_fenetrey = 450
cote_fenetrex=691
cote_fenetrey=600

#Personnalisation de la fenêtre
titre_fenetre = "Wolf Escape"
image_icone = "img/ingame/wolf_icon.png"
image_icone_bmp = "img/ingame/wolf_icon.ico"
image_main1="img/launch_load/menu_anim/accueil.png"
image_main2="img/launch_load/menu_anim/accueil_static_2.png"

#annimation du jeux
##Annimation du menu démarer
mainMenuPlayed=True#False#True#False#True #False #True #False #True #False#True
frameMainMenuWait=0.5
image_accueil1="img/launch_load/start_load/stages_stage_1.png"
image_accueil2="img/launch_load/start_load/stages_stage_2.png"
image_accueil3="img/launch_load/start_load/stages_stage_3.png"
image_accueil4="img/launch_load/start_load/stages_stage_4.png"
image_accueil5="img/launch_load/start_load/stages_stage_5.png"
image_accueil6="img/launch_load/start_load/stages_stage_6.png"
image_accueil7="img/launch_load/start_load/stages_stage_7.png"
image_accueil8="img/launch_load/start_load/stages_stage_8.png"
image_accueil9="img/launch_load/start_load/stages_stage_9.png"
image_accueil10="img/launch_load/start_load/stages_stage_10.png"
image_accueil11="img/launch_load/start_load/stages_stage_11.png"
image_accueil12="img/launch_load/start_load/stages_stage_12.png"
image_accueil13="img/launch_load/start_load/stages_stage_13.png"
image_accueil14="img/launch_load/start_load/stages_stage_14.png"
image_accueil15="img/launch_load/start_load/stages_stage_15.png"

load_images=[image_accueil1,image_accueil2,image_accueil3,image_accueil4,image_accueil5,image_accueil6,image_accueil7,image_accueil8,image_accueil9,image_accueil10,image_accueil11,image_accueil12,image_accueil13,image_accueil14,image_accueil15,image_main1,image_main2]


#Listes des images du jeu
image_accueil = "img/ingame/accueil.png"

#creation du gardien
img_mean_up="img/sprite/gardien/Gardien_haut.png"
img_mean_down="img/sprite/gardien/Gardien_bas.png"
img_mean_left="img/sprite/gardien/Gardien_Gauche.png"
img_mean_right="img/sprite/gardien/Gardien_Droite.png"
mean=[img_mean_up,img_mean_down,img_mean_left,img_mean_right]
meandone=[""]*len(mean)
mean_count=[""]*len(mean)
for i in range(len(mean)):mean_count[i]="{}".format(i+128)


#fond
image_fond="img/background/fonds.png"
image_fond_credits="img/Credits/end - Copie.PNG"

#départ
image_depart="img/ingame/start.png"
image_depart_du_loup="img/ingame/teller_start.png"
image_arrivee="img/end/endv.png"
image_arrivee_fam="img/sprite/famille/w_fam.png"
# mur
image_mur = "img/ingame/mur.png"
# path="img/ingame/funkyWalls"
WBB="img/ingame/funkyWalls/wall_beige_black.png"
WBW="img/ingame/funkyWalls/wall_beige_white.png"
WBRB="img/ingame/funkyWalls/wall_birght_red_black.png"
WBRW="img/ingame/funkyWalls/wall_birght_red_white.png"
WBW="img/ingame/funkyWalls/wall_black_white.png"
WBOB="img/ingame/funkyWalls/wall_brigth_orange_black.png"
WBOW="img/ingame/funkyWalls/wall_brigth_orange_white.png"
WBPB="img/ingame/funkyWalls/wall_brigth_pink_black.png"
WBPW="img/ingame/funkyWalls/wall_brigth_pink_white.png"
WCB="img/ingame/funkyWalls/wall_chocolat_black.png"
WCW="img/ingame/funkyWalls/wall_chocolat_white.png"
WDRB="img/ingame/funkyWalls/wall_darks_red_black.png"
WDRW="img/ingame/funkyWalls/wall_darks_red_white.png"
WDBB="img/ingame/funkyWalls/wall_dark_blue_black.png"
WDBW="img/ingame/funkyWalls/wall_dark_blue_white.png"
WDGB="img/ingame/funkyWalls/wall_dark_green_black.png"
WDGW="img/ingame/funkyWalls/wall_dark_green_white.png"
WDPB="img/ingame/funkyWalls/wall_dark_purple_black.png"
WDPW="img/ingame/funkyWalls/wall_dark_purple_white.png"
WGB="img/ingame/funkyWalls/wall_grey_black.png"
WGW="img/ingame/funkyWalls/wall_grey_white.png"
WLBB="img/ingame/funkyWalls/wall_light_blue_black.png"
WLBW="img/ingame/funkyWalls/wall_light_blue_white.png"
WLGB="img/ingame/funkyWalls/wall_light_green_black.png"
WLGW="img/ingame/funkyWalls/wall_light_green_white.png"
WLGB="img/ingame/funkyWalls/wall_light_grey_black.png"
WLGW="img/ingame/funkyWalls/wall_light_grey_white.png"
WLPB="img/ingame/funkyWalls/wall_light_purple_black.png"
WLPW="img/ingame/funkyWalls/wall_light_purple_white.png"
WMBB="img/ingame/funkyWalls/wall_medium_blue_black.png"
WMBW="img/ingame/funkyWalls/wall_medium_blue_white.png"
WOB="img/ingame/funkyWalls/wall_orange_black.png"
WOW="img/ingame/funkyWalls/wall_orange_white.png"
WVLBB="img/ingame/funkyWalls/wall_very_light_blue_black.png"
WVLBW="img/ingame/funkyWalls/wall_very_light_blue_white.png"
WW="img/ingame/funkyWalls/wall_white.png"
WYB="img/ingame/funkyWalls/wall_yellow_black.png"
WYW="img/ingame/funkyWalls/wall_yellow_white.png"

FunkyWalls=[image_mur,WBB,WBW,WBRB,WBRW,WBW,WBOB,WBOW,WBPB,WBPW,WCB,WCW,WDRB,WDRW,WDBB,WDBW,WDGB,WDGW,WDPB,WDPW,WGB,WGW,WLBB,WLBW,WLGB,WLGW,WLGB,WLGW,WLPB,WLPW,WMBB,WMBW,WOB,WOW,WVLBB,WVLBW,WW,WYB,WYW]
FunkyWalsDone=[""]*len(FunkyWalls)
walls=["^"]*len(FunkyWalls)
for i in range(len(FunkyWalls)):
      if i!=0:
        walls[i]=str(i+23)
# walls=['^','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74']


#Création du perso
ld="img/sprite/w/w_rigth.png"
lg="img/sprite/w/w_left.png"
lh="img/sprite/w/w_up.png"
lb="img/sprite/w/w_down.png"



#Crédits
image_credits_fond="img/Credits/end.png"
#Crédits_image_gané
image_credits_gagne="img/sprite/famille/famille_loup_You_have_won.png"
#Crédits_image_w_Irina
image_credits_w_Irina="img/sprite/famille/Mere et petits.png"

#numéros
image_zero="img/tut_image/numbers/0.png"
image_one="img/tut_image/numbers/1.png"
image_two="img/tut_image/numbers/2.png"
image_three="img/tut_image/numbers/3.png"
image_four="img/tut_image/numbers/4.png"
image_five="img/tut_image/numbers/5.png"
image_six="img/tut_image/numbers/6.png"
image_seven="img/tut_image/numbers/7.png"
image_eight="img/tut_image/numbers/8.png"
image_nine="img/tut_image/numbers/9.png"
namedigit=[image_zero,image_one,image_two,image_three,image_four,image_five,image_six,image_seven,image_eight,image_nine]
didgits=[""]*len(namedigit)
didgit_count=[""]*len(namedigit)
for i in range(len(didgits)):didgit_count[i]="{}".format(i)
# didgits=list(range(len(namedigit)))

#monaie
image_dollar="img/tut_image/currency/dollard.png"
image_pound="img/tut_image/currency/pound.png"
image_euro="img/tut_image/currency/euro.png"
image_yen="img/tut_image/currency/yen.png"
image_whan="img/tut_image/currency/wan.png"
currency=[image_dollar,image_pound,image_euro,image_yen,image_whan]
currencydone=[""]*len(currency)
currency_count=[""]*len(currency)
for i in range(len(currency)):currency_count[i]="1{}".format(i+1)

# ponctuation
img_square_bracket_open="img/tut_image/alphabet/punctuation/[.PNG"
img_square_bracket_closed="img/tut_image/alphabet/punctuation/].PNG"
# img_micro="img/tut_image/alphabet/punctuation/µ.PNG"
img_and="img/tut_image/alphabet/punctuation/and.PNG"
img_at="img/tut_image/alphabet/punctuation/at.PNG"
img_border="img/tut_image/alphabet/punctuation/border.png"
img_cureved_bracket_closed="img/tut_image/alphabet/punctuation/bracketclosed.PNG"
img_cureved_bracket_open="img/tut_image/alphabet/punctuation/bracketopen.PNG"
colum="img/tut_image/alphabet/punctuation/colum.PNG"
img_full_stop="img/tut_image/alphabet/punctuation/dot.PNG"
img_end_cell="img/tut_image/alphabet/punctuation/endboard.PNG"
img_exclamation_mark="img/tut_image/alphabet/punctuation/exclamation.PNG"
img_percentage="img/tut_image/alphabet/punctuation/paragraph.PNG"
img_open_quote="img/tut_image/alphabet/punctuation/paragraph_ouvert.PNG"
img_close_quote="img/tut_image/alphabet/punctuation/paragraph_fermé.PNG"
img_question_mark="img/tut_image/alphabet/punctuation/questionmark.PNG"
semicolon="img/tut_image/alphabet/accents/;.PNG"
ponctuation=[
    img_square_bracket_open,img_square_bracket_closed,
    # img_micro,
    img_and,img_at,img_border,img_cureved_bracket_closed,img_cureved_bracket_open,colum,img_full_stop,img_end_cell,img_exclamation_mark,img_percentage,img_open_quote,img_close_quote,img_question_mark,semicolon]
ponctuationDone=[""]*len(ponctuation)
ponctuation_count=[
    "[","]",
    # "Âµ",
    "&","@","20",")","(",":",".","Â¤","!","Â§","21","22","?",";"]


#création des flèches de direction pour le tuto
img_aright="img/tut_image/arrow/aright.PNG"
img_aleft="img/tut_image/arrow/aleft.PNG"
img_aup="img/tut_image/arrow/aup.PNG"
img_adown="img/tut_image/arrow/adown.PNG"
arrows=[img_aright,img_aleft,img_aup,img_adown]
arrowsprocessed=[""]*len(arrows)
arrows_count=[""]*len(arrows)
for i in range(len(arrows)):arrows_count[i]="1{}".format(i+6)


#Températures
img_Celsius="img/tut_image/alphabet/temperature/celsius.PNG"
img_fahraneit="img/tut_image/alphabet/temperature/fahraneit.PNG"
Temperature=[img_Celsius,img_fahraneit]
TemperatureDone=[""]*len(Temperature)
Temperature_count=[""]*len(Temperature)
for i in range(len(Temperature)):Temperature_count[i]="{}".format(i+126)


#Accents
a_accent="img/tut_image/alphabet/accents/à.PNG"
a_flex_low="img/tut_image/alphabet/accents/â.PNG"
a_flex_cap="img/tut_image/alphabet/accents/Â_cap.PNG"
a_wave_low="img/tut_image/alphabet/accents/ã.PNG"
a_wave_cap="img/tut_image/alphabet/accents/Ã_cap.PNG"
a_diaeresis_low="img/tut_image/alphabet/accents/ä.PNG"
a_diaeresis_cap="img/tut_image/alphabet/accents/Ä_cap.PNG"
c_five="img/tut_image/alphabet/accents/ç.PNG"
e_accent_é="img/tut_image/alphabet/accents/è.PNG"
e_accent_ê="img/tut_image/alphabet/accents/ê.PNG"
e_accent_Ê="img/tut_image/alphabet/accents/Ê_cap.png"
e_accent_è="img/tut_image/alphabet/accents/é.PNG"
e_diaeresis_low="img/tut_image/alphabet/accents/ë.PNG"
e_diaeresis_cap="img/tut_image/alphabet/accents/Ë_cap.png"
i_flex_low="img/tut_image/alphabet/accents/î.PNG"
i_flex_cap="img/tut_image/alphabet/accents/Î_cap.PNG"
i_diaeresis_low="img/tut_image/alphabet/accents/ï.PNG"
i_diaeresis_cap="img/tut_image/alphabet/accents/Ï_cap.PNG"
n_wave_low="img/tut_image/alphabet/accents/ñ.PNG"
n_wave_cap="img/tut_image/alphabet/accents/Ñ_cap.PNG"
o_flex_low="img/tut_image/alphabet/accents/ô.PNG"
o_flex_cap="img/tut_image/alphabet/accents/Ô_cap.PNG"
o_wave_low="img/tut_image/alphabet/accents/õ.PNG"
o_wave_cap="img/tut_image/alphabet/accents/Õ_cap.PNG"
o_diaeresis_low="img/tut_image/alphabet/accents/ö.PNG"
o_diaeresis_cap="img/tut_image/alphabet/accents/Ö_cap.PNG"
u_accent_ù="img/tut_image/alphabet/accents/ù.PNG"
u_flex_low="img/tut_image/alphabet/accents/û.PNG"
u_flex_cap="img/tut_image/alphabet/accents/Û_cap.PNG"
u_diaeresis_low="img/tut_image/alphabet/accents/ü.PNG"
u_diaeresis_cap="img/tut_image/alphabet/accents/Ü_cap.PNG"
y_diaeresis="img/tut_image/alphabet/accents/ÿ.PNG"


Accents=[a_accent,a_flex_low,a_flex_cap,a_wave_low,a_wave_cap,a_diaeresis_low,a_diaeresis_cap,c_five,e_accent_é,e_accent_ê,e_accent_Ê,e_accent_è,e_diaeresis_low,e_diaeresis_cap,i_flex_low,i_flex_cap,i_diaeresis_low,i_diaeresis_cap,n_wave_low,n_wave_cap,o_flex_low,o_flex_cap,o_wave_low,o_wave_cap,o_diaeresis_low,o_diaeresis_cap,u_accent_ù,u_flex_low,u_flex_cap,u_diaeresis_low,u_diaeresis_cap,y_diaeresis]
Accentsdone=[""]*len(Accents)
Accents_count=[""]*len(Accents)
for i in range(len(Accents)):Accents_count[i]=str(i+62)

#mathématiques
path="img/tut_image/math"
img_percent="img/tut_image/math/%.png"
img_minus="img/tut_image/math/-.png"
img_plus="img/tut_image/math/+.png"
img_equal="img/tut_image/math/=.png"
img_divide="img/tut_image/math/diviser.png"
img_less_than="img/tut_image/math/lessthan.png"
img_more_than="img/tut_image/math/morethan.png"
img_times="img/tut_image/math/times.png"
Maths=[img_percent,img_minus,img_plus,img_equal,img_divide,img_less_than,img_more_than,img_times]
Mathsdone=[""]*len(Maths)
Maths_count=["%","-","+","=","/","<",">","*"]


#lettres
lowerletterletter=[]
upperletterletter=[]

letters = dict()
for letter in ascii_letters:
    if letter.islower():
        letters[letter] = f"img/tut_image/alphabet/minuscule/{letter}mi.png"
        lowerletterletter.append(letter)
    else:
        letters[letter] = f"img/tut_image/alphabet/majuscule/{letter.lower()}ma.png"
        upperletterletter.append(letter)
lowerletter=[""]*len(lowerletterletter)
upperletter=[""]*len(upperletterletter)
Lowerletter_count=lowerletterletter
Upperletter_count=upperletterletter

#follow_me
img_behance_black="img/Follow-me/Behance/behance_b.PNG"
img_codepen_black="img/Follow-me/codepen/codepen_b.PNG"
img_dev_to_black="img/Follow-me/dev-to/dev-to_B.PNG"
img_discord_black="img/Follow-me/discord/discord_B.PNG"
img_facebook_black="img/Follow-me/facebook/facebook_B.PNG"
img_github_black="img/Follow-me/github/github_B.PNG"
img_instagram_black="img/Follow-me/Instagram/instagram_B.PNG"
img_linkedin_black="img/Follow-me/linkedin/linkedin_B.PNG"
img_patreon_black="img/Follow-me/patreon/patreon_B.PNG"
img_pinterest_black="img/Follow-me/pinterest/pinterest_B.PNG"
img_repl_it_black="img/Follow-me/repl.it/repl_it_B.PNG"
img_snapchat_black="img/Follow-me/snapchat/snapchat_B.PNG"
img_sound_cloud_black="img/Follow-me/sound-cloud/soundcloud_B.PNG"
img_steam_black="img/Follow-me/steam/steam_B.PNG"
img_tumblr_black="img/Follow-me/tumblr/tumblr_B.PNG"
img_yt_black="img/Follow-me/yt/youtube_B.PNG"
img_behance_white="img/Follow-me/Behance/behance_w.PNG"
img_codepen_white="img/Follow-me/codepen/codepen_w.PNG"
img_dev_to_white="img/Follow-me/dev-to/dev-to_W.PNG"
img_discord_white="img/Follow-me/discord/discord_W.PNG"
img_facebook_white="img/Follow-me/facebook/facebook_W.PNG"
img_github_white="img/Follow-me/github/github_W.PNG"
img_instagram_white="img/Follow-me/Instagram/instagram_W.PNG"
img_linkedin_white="img/Follow-me/linkedin/linkedin_W.PNG"
img_patreon_white="img/Follow-me/patreon/patreon_W.PNG"
img_pinterest_white="img/Follow-me/pinterest/pinterest_W.PNG"
img_repl_it_white="img/Follow-me/repl.it/repl_it_W.PNG"
img_snapchat_white="img/Follow-me/snapchat/snapchat_W.PNG"
img_sound_cloud_white="img/Follow-me/sound-cloud/soundcloud_W.PNG"
img_steam_white="img/Follow-me/steam/steam_W.PNG"
img_tumblr_white="img/Follow-me/tumblr/tumblr_W.PNG"
img_yt_white="img/Follow-me/yt/youtube_W.PNG"

Follow_me=[img_behance_black,img_codepen_black,img_dev_to_black,img_discord_black,img_facebook_black,img_github_black,img_instagram_black,img_linkedin_black,img_patreon_black,img_pinterest_black,img_repl_it_black,img_snapchat_black,img_sound_cloud_black,img_steam_black,img_tumblr_black,img_yt_black,img_behance_white,img_codepen_white,img_dev_to_white,img_discord_white,img_facebook_white,img_github_white,img_instagram_white,img_linkedin_white,img_patreon_white,img_pinterest_white,img_repl_it_white,img_snapchat_white,img_sound_cloud_white,img_steam_white,img_tumblr_white,img_yt_white]
Follow_medone=[""]*len(Follow_me)
Follow_me_count=[""]*len(Follow_me)
for i in range(len(Follow_me)):Follow_me_count[i]=str(i+94)



#Autre
#coeur
heart_small="img/tut_image/heart/heartsmall.png"
heart_big="img/tut_image/heart/heartbig.png"

paragraph="img/tut_image/alphabet/punctuation/paragraph.PNG"
open_parageraph="img/tut_image/alphabet/punctuation/paragraph_ouvert.PNG"
closed_paragraph="img/tut_image/alphabet/punctuation/paragraph_fermé.PNG"


Autre=[paragraph,open_parageraph,closed_paragraph,heart_small,heart_big]
Autredone=[""]*len(Autre)
Autre_count=[""]*len(Autre)
for i in range(len(Autre)):Autre_count[i]=str(i+132)

#-------------------------------------- Classes.py file -----------------------------------------


class root:
    def __init__(self,main,main_dict,links):
        #-------------------- Abort program --------------------
        self.abort_program=False
        #-------------------- Other vars --------------------
        self.mainLoop=True
        self.main=main
        self.main_dict=main_dict
        self.links=links
        self.home="https://hanralatalliardwork.github.io/wolf_escape_home/"
        self.file_location="files/requirements"
        self.ggg=0
        self.list_dict=[]
        self.error_ticket_title=""
        self.error_ticket_content=""
                        
        #------------------ Tkinter ------------------
        self.universalBackground="white"
        self.maxDots=35
        #---------------------------------ICON------------------------------------
        self.icon=""
        self.displayIcon=False
        #---------------------------------DISPLAY---------------------------------
        self.window_size_x=424
        self.window_size_y=200
        self.window_geometry=f"{self.window_size_x}x{self.window_size_y}"
        #---------------------------------TEXT------------------------------------
        self.cursor="none"
        self.person="gumby"
        self.text_cells_width=51
        self.text_cells_height=22
        self.window_cell_size_x=self.window_size_x
        self.window_cell_size_y=self.window_size_y+250
        self.window_geometry_cell=f"{self.window_cell_size_x}x{self.window_cell_size_y}"
        self.cursor="X_cursor"
        self.watermark=f"{chr(169)} Created by Henry Letellier"
        #------------------------------ S ------------------------------
        self.extension=".we"
        self.All_the_levels=["_____Visible Levels_____"]
        self.All_the_levels_index={"_____Visible Levels_____":"None","_____Hidden Levels______":"None"}
        self.visible=os.listdir("levels")
        self.hidden=os.listdir("elementary_levels")
        self.keys_for_hidden={'002_l2':"", '003_l3':"", '004_l4':"", '005_l5':"", 'credits':"F3", 'h':"h", 'I':"i", 'M':"m", 'm1':"F1", 'm2':"F2", 'P':"p"}
        self.path="img/the_levels/"
        self.finalImageForCanvasS=f"{self.path}fonds.png"
        self.photoS=""
class boot(root):
    class get:
        def dots(word="",maxDots=10):
            word=len(word)
            maxDots=maxDots-word
            result=""
            for i in range(maxDots):result+="."
            return result
        class online:
            def tempFile(url):
                road=requests.get(url)
                print(f"road.status_code={road.status_code}")
                if road.status_code!="404":
                    road=road.content
                    try:
                        e=open(road,"rb").read()
                        # print("rb")
                        return e
                    except:
                        try:
                            e=open(road,"r").read()
                            # print("r")
                            return e
                        except:
                            try:
                                e=road.decode()
                                # print("decode")
                                return e
                            except:
                                return road
                else:
                    print(f"\n\n\n\nStatus for {url} is {road.status_code}.")
                    sleep(10)
                    return road.status_code
        def make_links(lst_from):
            path=""
            lst_to=[]
            # print(RI.ggg)
            # print(f"\n\nlst_from={lst_from}")
            open("list_lengths.txt","a").write(f"lst_to='{lst_to}',before for\n")
            for i in lst_from:
                if lst_from[i]["type"].lower()=="file" or lst_from[i]["type"].lower()=="<file>":
                    lst_to.append(f"{path}/{i}")
                    open("list_lengths.txt","a").write(f"|__lst_to='{lst_to}',in if type=file,path='{path}',lst_from[i]\"type\"]='{lst_from[i]['type']}',lst_from[i]\"fileName\"]='{lst_from[i]['fileName']}'\n")
                elif lst_from[i]["type"].lower()=='dir' or lst_from[i]["type"].lower()=='<dir>':
                    path+=f"/{i}"
                    lst_to.append("")
                    open("list_lengths.txt","a").write(f"|__lst_to='{lst_to}',in if type=dir,path={path},lst_from[i]\"type\"]='{lst_from[i]['type']}',lst_from[i]\"fileName\"]='{lst_from[i]['fileName']}'\n")
                else:
                    Error=f"Error, type {lst_from[i]} unknown. must be <dir> or dir for a folder or <file> or file for a file."
                    open("list_lengths.txt","a").write(f"|__Error='{Error}',path={path},lst_from[i]\"type\"]='{lst_from[i]['type']}',lst_from[i]\"fileName\"]='{lst_from[i]['fileName']}'\n")
                    return Error
            # print(lst_to)
            # RI.ggg+=1

            return lst_to
        def content(self,list1,list2,links,home,LabelInfo,progress,ProgressBar,window,ProgressWindow):
            list1_length=the_percentage_progression=ProgressIndex=prev=0
            maxDots=50
            for i in range(len(list1)):
                list1_length+=len(list1[i])
            The_error_color="red"
            The_success_color="lightGreen"
            zeta={}
            zs=f"len(list1)={len(list1)},len(list2)={len(list2)}"
            print(zs)
            f=open("list_lengths.txt","a").write(f"{zs}\n")
            for i in range(len(list1)):
                peth="."
                z=f"len(list1[{i}])={len(list1[i])},len(list2[{i}])={len(list2[i])}"
                print(z)
                f=open("list_lengths.txt","a").write(f"|__{z}\n")
                f=open("list_lengths.txt","a").write(f"|\t|__len(links[{i}])='{len(links[i])}'\n")
                f=open("list_lengths.txt","a").write(f"|\t|__list1[{i}]={list1[i]}\n")
                tr=[]
                for alpha in list2[i]:
                    tr.append(alpha)
                f=open("list_lengths.txt","a").write(f"|\t|__list2[{i}]={tr}\n")
                f=open("list_lengths.txt","a").write(f"|\t|__links[{i}]='{links[i]}'\n")
                
                # pause=input("press enter to continue...")
                for b in range(len(list1[i])):
                    error_suggested_message=""
                    if list2[i][list1[i][b]]['type'].lower()=="dir" or list2[i][list1[i][b]]['type'].lower()=="<dir>":
                        list2[i][list1[i][b]]['typeBeautified']="folder"
                    else:
                        list2[i][list1[i][b]]['typeBeautified']="file"
                    the_current_percentage=int(101*(the_percentage_progression/list1_length)*100/100)
                    from_folder=False
                    zeta=boot.TKinter.window.updateProgress(
                        self,
                        LabelInfo=LabelInfo,
                        LabelInfoContent=f"Checking if {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]} exists",
                        progress=progress,
                        element=list1[i][b],
                        percentage=the_current_percentage,
                        progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                        success=True,
                        prev=prev,
                        To=ProgressBar,
                        FileIndex=ProgressIndex,
                        ifSuccess="CHEKING",
                        ifSuccessColor=The_success_color,
                        progressInfo=ProgressWindow,
                        error_files=zeta,
                        ifNotSuccess="DOES NOT EXIST",
                        ifNotSuccessColor=The_error_color,
                        window=window,
                        maxDots=maxDots,
                        update_bar=False
                    )
                    print(f"i={i},b={b}")
                    za=f"i={i},b={b},len(list1[{i}][{b}])={len(list1[i][b])}={list1[i][b]},len(list2[{i}][{list1[i][b]}])={len(list2[i][list1[i][b]])}={list2[i][list1[i][b]]}"
                    # print(za)
                    f=open("list_lengths.txt","a").write(f"|\t|__{za}\n")
                    f=open("list_lengths.txt","a").write(f"|\t|\t|__type='{list2[i][list1[i][b]]['type']}'\n")
                    f=open("list_lengths.txt","a").write(f"|\t|\t|__filename='{list2[i][list1[i][b]]['fileName']}'\n")
                    # sleep(1)
                    # print(f"list2[i][list1[i][b]]={list2[i][list1[i][b]]}={list1[i][b]}")
                    if list2[i][list1[i][b]]["type"].lower()=='file' or list2[i][list1[i][b]]["type"].lower()=='<file>':
                        # print(f"list2[i][list1[i][b]][\"type\"]={list2[i][list1[i][b]]['type']}")
                        # print(f"link=\"{home}{links[i][b]}\"")
                        try:
                            a=open(f"{peth}/{list1[i][b]}","r").read()
                            c=len(a)
                            print(f"c={c}")
                            wasSuccessFull=True
                        except:
                            c=0
                        if os.path.exists(f"{peth}/{list1[i][b]}")==False and c==0:
                            # try:
                            # print(f"trying with link=\"{home}{links[i][b]}\"")
                            f=open("list_lengths.txt","a").write(f"|\t|\t|__len(list1[{i}][{b}])='{len(list1[i][b])}',list1[{i}][{b}]='{list1[i][b]}'\n")
                            f=open("list_lengths.txt","a").write(f"|\t|\t|__len(list2[{i}][{list1[i][b]}])='{len(list2[i][list1[i][b]])}',list2[{i}][list1[{i}][{b}]]='{list2[i][list1[i][b]]}'\n")
                            f=open("list_lengths.txt","a").write(f"|\t|\t|__len(links[{i}])='{len(links[i])}'\n")
                            f=open("list_lengths.txt","a").write(f"|\t|\t|__links[{i}]={links[i]}\n")
                            zeta=boot.TKinter.window.updateProgress(
                                self,
                                LabelInfo=LabelInfo,
                                LabelInfoContent=f"Fetching {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]}.",
                                progress=progress,
                                element=list1[i][b],
                                percentage=the_current_percentage,
                                progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                                success=True,
                                prev=prev,
                                To=ProgressBar,
                                FileIndex=ProgressIndex,
                                ifSuccess="Fetching",
                                ifSuccessColor=The_success_color,
                                progressInfo=ProgressWindow,
                                error_files=zeta,
                                ifNotSuccess="DOES NOT EXIST",
                                ifNotSuccessColor=The_error_color,
                                window=window,
                                maxDots=maxDots,
                                update_bar=False
                            )
                            list2[i][list1[i][b]]["fileContent"]=boot.get.online.tempFile(f"{home}{links[i][b]}")
                            print(f"type(fileContent)={type(list2[i][list1[i][b]]['fileContent'])}")
                            # list2[i][list1[i][b]]['fileContent']=404
                            if list2[i][list1[i][b]]['fileContent']==404:
                                print("404")
                                # sleep(10)
                                LabelInfoContent=f"Failed to fetch {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]}. (404)"
                                wasSuccessFull=False
                                message_type="Not found"
                                error_suggested_message=f"\nInternet connaction innactive or file does not exist on the server \n'{home}{links[i][b]}'\nPlease check that you are connected to the internet so that the program can fetch its required files.\nIf problem persists and you are connected to the internet, please open a support ticket (if not already opened by another user).\nThe title of the support ticket must be: file <filename> missing."
                                ifSuccess=ifNotSuccess="COULD NOT FETCH"
                                update_bar=True
                            else:
                                zeta=boot.TKinter.window.updateProgress(
                                    self,
                                    LabelInfo=LabelInfo,
                                    LabelInfoContent=f"Fetched {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]}.",
                                    progress=progress,
                                    element=list1[i][b],
                                    percentage=the_current_percentage,
                                    progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                                    success=True,
                                    prev=prev,
                                    To=ProgressBar,
                                    FileIndex=ProgressIndex,
                                    ifSuccess="FETCHED",
                                    ifSuccessColor=The_success_color,
                                    progressInfo=ProgressWindow,
                                    error_files=zeta,
                                    ifNotSuccess="COULD NOT FETCH",
                                    ifNotSuccessColor=The_error_color,
                                    window=window,
                                    maxDots=maxDots,
                                    update_bar=False,
                                    error_suggested_message=f"Failed to create '{list1[i][b]}' wich is a {list2[i][list1[i][b]]['typeBeautified']}.\nTry running this program with admin rights.\nThe reason of this error was probably because the access was 'denied' \nor that you do not have enough space on your disk."
                                )
                                if type(b'0')==type(list2[i][list1[i][b]]["fileContent"]):
                                    print("in try")
                                    f=open(f"{peth}/{list2[i][list1[i][b]]['fileName']}","wb")
                                    print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} opened")
                                    f.write(list2[i][list1[i][b]]["fileContent"])
                                    # print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} written to")
                                    print("opened as wb")
                                    list2[i][list1[i][b]]["opening_method"]="wb"
                                    list2[i][list1[i][b]]["exists"]="No"
                                elif type('0')==type(list2[i][list1[i][b]]["fileContent"]):
                                    f=open(f"{peth}/{list2[i][list1[i][b]]['fileName']}","w")
                                    print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} opened")
                                    f.write(list2[i][list1[i][b]]["fileContent"])
                                    # print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} written to")
                                    print("opened as w")
                                    list2[i][list1[i][b]]["opening_method"]="w"
                                    list2[i][list1[i][b]]["exists"]="No"
                                else:
                                    ticketTitle=f"File {list2[i][list1[i][b]]['fileName']} Could not be created"
                                    ticketBody=f"The file {list2[i][list1[i][b]]['fileName']} with the path {peth} could not be created in the user directory.\nThis problem can occur when:\n- The program is not allowed to write to the disk\n- the disk is full\n- the type is unsupported. (read on [please])\n\n (bellow is some user usefull info, and the ticket body)\n\nInfo for the user to do before opening a ticket:\n- Try running the program with administrator rights\n- Try manually downloading the required file\n- Download the executable (mac, windows or linux) to fix it\n\nIf the problem still persits open a ticket in the discord server with the content above and following body:\n____________Begin body_____________\nfile_type={type(list2[i][list1[i][b]]['fileContent'])},\nfile_length={len(list2[i][list1[i][b]]['fileContent'])},\npath={peth},\nfilename={list2[i][list1[i][b]]['fileName']}\n_____________End body______________\n"
                                    continue_error_window=True
                                    while continue_error_window==True:
                                        continue_error_window=boot.TKinter.window.error_abortion(self,window,ticketTitle,ticketBody)
                                        if self.abort_program==True:
                                            return 'Program aborted'
                                sleep(5)
                                f.close()
                                print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} closed")
                                wasSuccessFull=True
                                message_type="created"
                                LabelInfoContent=f"The {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]} was created."
                                ifSuccess="CREATED"
                                ifNotSuccess="FAILED TO CREATE"
                                update_bar=False
                                # print(list2[i][list1[i][b]])
                            zeta=boot.TKinter.window.updateProgress(
                                self,
                                LabelInfo=LabelInfo,
                                LabelInfoContent=LabelInfoContent,
                                progress=progress,
                                element=list1[i][b],
                                percentage=the_current_percentage,
                                progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                                success=wasSuccessFull,
                                prev=prev,
                                To=ProgressBar,
                                FileIndex=ProgressIndex,
                                ifSuccess=ifSuccess,
                                ifSuccessColor=The_success_color,
                                progressInfo=ProgressWindow,
                                error_files=zeta,
                                ifNotSuccess=ifNotSuccess,
                                ifNotSuccessColor=The_error_color,
                                window=window,
                                maxDots=maxDots,
                                update_bar=update_bar,
                                error_suggested_message=error_suggested_message
                            )
                            if list2[i][list1[i][b]]['fileContent']==404:
                                ticketTitle=f"File {list2[i][list1[i][b]]['fileName']} does not exist on server"
                                ticketBody=f"Internet connaction innactive or file does not exist on the server \n'{home}{links[i][b]}'\n_______________________________\nTo the user:\n_______________________________\nPlease check that you are connected to the internet so that the program can fetch its required files.\nIf the problem persists and you are connected to the internet, please open a support ticket (if not already opened by another user).\nWith the following body (ticket tile is above):\n_______________________________\nSupport ticket body\n_______________________________\n\n_____________Begin body_____________\nThe file {list2[i][list1[i][b]]['fileName']} with the path {peth} does not exist in the server.\n_____________End body______________\n"
                                continue_error_window=True
                                while continue_error_window==True:
                                    continue_error_window=boot.TKinter.window.error_abortion(self,window,ticketTitle,ticketBody)
                                    if self.abort_program==True:
                                        return 'Program aborted'
                                # return list1[i][b],zeta
                        else:
                            print(f"file {list1[i][b]} already exists in {peth}.")
                            list2[i][list1[i][b]]["opening_method"]=None
                            list2[i][list1[i][b]]["exists"]="Yes"
                            wasSuccessFull=True
                            message_type="exists"
                    elif list2[i][list1[i][b]]["type"].lower()=="dir" or list2[i][list1[i][b]]["type"].lower()=="<dir>":
                        peth+=f"/{list2[i][list1[i][b]]['fileName']}"
                        if os.path.exists(peth)==False:
                            try:
                                # print(teta)
                                os.mkdir(peth)
                                print(f"{peth}........[CREATED]")
                                message_type="CREATED"
                                from_folder=True
                                wasSuccessFull=True
                            except:
                                message_type="Failed To Create"
                                from_folder=True
                                wasSuccessFull=False
                                zeta=boot.TKinter.window.updateProgress(
                                    self,
                                    LabelInfo=LabelInfo,
                                    LabelInfoContent=f"Error: {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]} does not exists",
                                    progress=progress,
                                    element=list1[i][b],
                                    percentage=the_current_percentage+1,
                                    progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                                    success=wasSuccessFull,
                                    prev=prev,
                                    To=ProgressBar,
                                    FileIndex=ProgressIndex,
                                    ifSuccess="CREATED",
                                    ifSuccessColor=The_success_color,
                                    progressInfo=ProgressWindow,
                                    error_files=zeta,
                                    ifNotSuccess="FAILED TO CREATE",
                                    ifNotSuccessColor=The_error_color,
                                    window=window,
                                    maxDots=maxDots,
                                    update_bar=True,
                                    error_suggested_message=f"Failed to create '{list1[i][b]}' wich is a {list2[i][list1[i][b]]['typeBeautified']}.\nTry running this program with admin rights.\nThe reason of this error was probably because the access was 'denied' \nor that you do not have enough space on your disk."
                                )
                                ticketTitleText=f"What do you wish to do?"
                                ticketBodyText=f"(The below options are not buttons\nplease scroll down to see the options)\n- Abort and run the program with admin rights\n-Create the folder yourself in {peth} then restart the program\n- Download the files at (*) and place them manually at the source of the program\n* {self.home}{self.file_location}\nIf the problem has not been solved, please open a support ticket in the server."
                                continue_error_window=True
                                while continue_error_window==True:
                                    continue_error_window=boot.TKinter.window.error_abortion(self,TT=window,ticketTitleText=ticketTitleText,ticketBodyText=ticketBodyText)
                                    if self.abort_program==True:
                                        return 'Program aborted'
                                # return zeta
                        else:
                            wasSuccessFull=True
                            from_folder=False
                            message_type="exists"
                        
                    else:
                        a=f"{list2[i][list1[i][b]]} = [UNKNOWN TYPE]\npath={peth}"
                        print(f"a={a}")
                        wasSuccessFull=False
                        zeta=boot.TKinter.window.updateProgress(
                            self,
                            LabelInfo=LabelInfo,
                            LabelInfoContent=f"Error: {list2[i][list1[i][b]]['type']} {list1[i][b]} does not exists",
                            progress=progress,
                            element=list1[i][b],
                            percentage=the_current_percentage+1,
                            progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                            success=wasSuccessFull,
                            prev=prev,
                            To=ProgressBar,
                            FileIndex=ProgressIndex,
                            ifSuccess="EXISTS",
                            ifSuccessColor=The_success_color,
                            progressInfo=ProgressWindow,
                            error_files=zeta,
                            ifNotSuccess="DOES NOT EXIST",
                            ifNotSuccessColor=The_error_color,
                            window=window,
                            maxDots=maxDots,
                            update_bar=True,
                            error_suggested_message=f"Unknown type.\nElement: {list1[i][b]} has {list2[i][list1[i][b]]['type']} as type.\nType can only be: dir or <dir> for a folder.\nfile or <file> for a file."
                        )
                        ticketTitle="Unknown type."
                        ticketBody=f"_____________Begin body_____________\nElement: {list1[i][b]} has {list2[i][list1[i][b]]['type']} as type.\n_____________End body______________\n"
                        continue_error_window=True
                        while continue_error_window==True:
                            continue_error_window=boot.TKinter.window.error_abortion(self,window,ticketTitle,ticketBody)
                            if self.abort_program==True:
                                return 'Program aborted'
                        return a,zeta
                    zeta=boot.TKinter.window.updateProgress(
                        self,
                        LabelInfo=LabelInfo,
                        LabelInfoContent=f"The {list2[i][list1[i][b]]['typeBeautified']} {list1[i][b]} {message_type}",
                        progress=progress,
                        element=list1[i][b],
                        percentage=the_current_percentage,
                        progressText=f"Checked {ProgressIndex}/{list1_length-1} files - {the_current_percentage}%",
                        success=wasSuccessFull,
                        prev=prev,
                        To=ProgressBar,
                        FileIndex=ProgressIndex,
                        ifSuccess="EXISTS",
                        ifSuccessColor=The_success_color,
                        progressInfo=ProgressWindow,
                        error_files=zeta,
                        ifNotSuccess="DOES NOT EXIST",
                        ifNotSuccessColor=The_error_color,
                        window=window,
                        maxDots=maxDots,
                        update_bar=True,
                        error_suggested_message=error_suggested_message
                    )
                    if from_folder==True:sleep(0.5)#1)
                    print(f"the_percentage_progression={the_percentage_progression},prev={prev},ProgressIndex={ProgressIndex}")
                    the_percentage_progression+=1
                    prev=the_current_percentage
                    ProgressIndex+=1
                    print(f"path={peth}")
                    f=open("list_lengths.txt","a").write(f"|\t|\t|__[ROUND b END]'\n")
                f=open("list_lengths.txt","a").write(f"|\t|__[ROUND i END]'\n")
            f=open("list_lengths.txt","a").write(f"[END OF ROUNDS]'\n")
            f=open("list_lengths.txt","a").write(f".\n")
            # print(f"list2='{list2}'=list2")
            for i in list2[0]:
                self.list_dict.append(list2[0][i])
            return zeta
    class TKinter(root):
        class window:
            def error_abortion(self,TT,ticketTitleText,ticketBodyText):
                def Abort_program():
                    TT.destroy()
                    TTT.destroy()
                    self.abort_program=True
                    return False
                def continue_anyway():
                    TTT.destroy()
                    return False
                window_size_y=self.window_size_y+30
                window_size_x=self.window_size_x+170
                TTT=Tk()
                TTT.geometry(f"{window_size_x}x{window_size_y}")
                TTT.minsize(window_size_x,window_size_y)
                TTT.title("Open Report Log")
                TTT['bg']=self.universalBackground
                TitleLabel=Label(TTT,text="The program has stopped due to an error.\nA report_log has been created\nI recommend opening a support ticket in\n the discord server with the following title...\n",bg=self.universalBackground,anchor="center")
                TitleLabel.pack(side=TOP,fill=X)
                ticket=Frame(TTT,bg=self.universalBackground,borderwidth=1,relief=FLAT)
                ticket.pack(side=TOP,fill=X)
                ticketTitle=Text(ticket,stat="normal",fg="black",bg="white",wrap="none",cursor="xterm",height=1,width=100,relief=FLAT,insertbackground="black")
                ticketTitle.pack(side=TOP)
                ticketTitle.insert(0.0,f"{ticketTitleText}") #
                bodyLabel=Label(ticket,text="... and the following body.",bg=self.universalBackground,anchor="center")
                bodyLabel.pack(side=TOP,fill=X)
                ticketBody=Text(ticket,stat="normal",fg="black",bg="white",wrap="word",cursor="xterm",height=4,width=100,relief=FLAT,insertbackground="black")
                ticketBody.pack(side=TOP) #
                ticketBody.insert(0.0,f"{ticketBodyText}")
                FrameButton=Frame(TTT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
                FrameButton.pack(side=TOP,fill=X)
                Abort=Button(FrameButton,text="Abort (recommended)",command=Abort_program,bg=self.universalBackground)
                Abort.pack(side=LEFT)
                ContinueAnyway=Button(FrameButton,text="Continue anyway\n(the program might lag or stop unexpectedly)",command=continue_anyway,bg=self.universalBackground)
                ContinueAnyway.pack(side=RIGHT)
                TTT.mainloop()
            def updateProgress(self,LabelInfo,LabelInfoContent,progress,element,percentage,progressText,success,prev,To,FileIndex,ifSuccess,ifSuccessColor,progressInfo,error_files,ifNotSuccess,ifNotSuccessColor,window,maxDots=35,update_bar=True,error_suggested_message="Try running program with admin rights."):
                def update_Status_bar(string,inc,windows,colorF):
                    #print(string)
                    windows.insert(float(inc),string,"taged")
                    windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorF}")
                def update_Status_log(string,inc,windows,colorF):
                    #print(string)
                    colorB="black"
                    windows.insert(float(inc),string,"taged")
                    windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorB}")
                def cleanText(windows):
                    windows.delete("1.0","end")
                a=boot.get.dots(word=element,maxDots=maxDots)
                # print(f"element={element}")
                # print(f"current_width_progress={percentage}")
                LabelInfo.config(text=f"{LabelInfoContent}")
                progress.config(text=f"{progressText}")
                inc=0.0
                # print(f"prev={prev},percentage={percentage}")
                if success==True:
                    if prev<percentage and update_bar==True:
                        update_Status_bar(string=f".",inc=inc,windows=To,colorF=ifSuccessColor)
                    update_Status_log(string=f"\n{FileIndex} {element}{a}[{ifSuccess}]",inc=inc,windows=progressInfo,colorF=ifSuccessColor)
                else:
                    # print(f"element={element},error_files={error_files},ifNotSuccess={ifNotSuccess},FileIndex={FileIndex}")
                    # FileIndex#element
                    error_files[FileIndex]=f"[{ifNotSuccess}]"
                    LabelInfo.config(text=f"Failed for {element}")
                    if prev<percentage and update_bar==True:
                        update_Status_bar(string=f".",inc=inc,windows=To,colorF=ifNotSuccessColor)
                    update_Status_log(string=f"\n{i} {element}{a}[{ifNotSuccess}]",inc=inc,windows=progressInfo,colorF=ifNotSuccessColor)
                    update_Status_log(string=error_suggested_message,inc=inc,windows=progressInfo,colorF=ifNotSuccessColor)
                window.title(f"Checking and downloading - {percentage}%")
                window.update()
                return error_files
            def update_Status(string,inc,windows):
                print(string)
                windows.insert(float(inc),string)
            def FetchingFiles(self):
                print("Checking files...")
                TT=Tk()
                window_size_x,window_size_y=820,300
                window_geometry=f"{window_size_x}x{window_size_y}"
                TT.geometry(window_geometry)
                TT.minsize(window_size_x,window_size_y)
                TT.title("Checking and downloading")
                TT['bg']=self.universalBackground
                TitleLabel=Label(TT,text="Checking if required files are present. (This may take a few minutes if it is the first time you start the program)",bg=self.universalBackground,anchor="w")
                TitleLabel.pack(side=TOP,fill=X)
                CurrentFile=Label(TT,text="Checking if file   exists",bg=self.universalBackground,anchor="w")
                CurrentFile.pack(side=TOP,fill=X)
                Progress=Label(TT,text="",bg=self.universalBackground,anchor="w")
                Progress.pack(side=TOP,fill=X)
                ProgressBar=Text(TT,state="normal",
                                    insertbackground="lightGreen",#"white",
                                    fg="lightGreen",#"black",#"white",
                                    exportselection=0,
                                    width=100,height=1,
                                    padx=5,pady=5,relief=FLAT,
                                    bg="white",#"blue",
                                    cursor="watch",wrap="none",tabs="1c"#,
            
            #padx=0,pady=0,
                                    )#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressBar.pack()
                ProgressWindow=Text(TT,state="normal",
                                    insertbackground="lightGreen",#"white",
                                    fg="lightGreen",#"black",#"white",
                                    bg="black",
                                    exportselection=0,
                                    width=100,height=10,
                                    padx=5,pady=5,relief=FLAT,
                                    cursor="watch",wrap="none",tabs="1c"#,
            
            #padx=0,pady=0,
                                    )#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressWindow.pack()
                boot.get.content(self,list1=self.main,list2=self.main_dict,links=self.links,home=f"{self.home}{self.file_location}",LabelInfo=CurrentFile,progress=Progress,ProgressBar=ProgressBar,window=TT,ProgressWindow=ProgressWindow)
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Great!",command=TT.destroy,bg=self.universalBackground)
                DownloadButton.pack(side=TOP,fill=X)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()

    def initialise_links(e):
        links=[]
        for i in range(len(e)):
            links.append(boot.get.make_links(e[i]))

        return links
class Niveau:
    def __init__(self, fichier):
        self.fichier=fichier
        self.structure=0
    def generer(self):
        f=open(self.fichier, "r")
        file=f.read()
        f.close()
        GameLine=[]
        CreatingGameSprite=""
        GameSprite=[]
        for line in file:
            if line!="|" and line!="\n":
                CreatingGameSprite+=line
            elif line=="|" and line!="\n":
                #print("CreatingGameSprite=",CreatingGameSprite)
                #print("GameSprite=",GameSprite)
                GameSprite.append(CreatingGameSprite)
                CreatingGameSprite=""
            elif line=="\n":
                GameLine.append(GameSprite)
                GameSprite=[]
        self.structure=GameLine
        print("self.structure=",self.structure)
        print("GameSprite=",GameSprite)

    def afficher(self, fenetre):
        #print("Je suis dans afficher (self, fenetre)")
        #murs
        for i in range(len(FunkyWalls)):FunkyWalsDone[i]=pygame.image.load(FunkyWalls[i]).convert_alpha()
        #depart
        depart = pygame.image.load(image_depart).convert()
        depart_positionnement=pygame.image.load(image_depart_du_loup).convert()
        # arrivee
        arrivee = pygame.image.load(image_arrivee).convert_alpha()
        arrivee_fam=pygame.image.load(image_arrivee_fam).convert_alpha()
        # alphabet
        for i in range(len(lowerletter)):lowerletter[i]=pygame.image.load(letters[lowerletterletter[i]]).convert_alpha()#i
        for i in range(len(upperletter)):upperletter[i]=pygame.image.load(letters[upperletterletter[i]]).convert_alpha()
        #arrows
        for i in range(len(arrows)):arrowsprocessed[i]=pygame.image.load(arrows[i]).convert_alpha()
        #credits
        #credits_fond=pygame.image.load(image_credits_fond).convert()
        credits_gagne=pygame.image.load(image_credits_gagne).convert()
        credits_w_Irina=pygame.image.load(image_credits_w_Irina).convert()
        #credits_w_Henry=pygame.image.load(image_credits_w_Henry).convert()
        #credits_l_Irina=pygame.image.load(image_credits_l_Irina).convert()
        #credits_l_Henry=pygame.image.load(image_credits_l_Henry).convert()
        #mean
        for i in range(len(mean)):meandone[i]=pygame.image.load(mean[i]).convert_alpha()
        #number
        for i in range(len(namedigit)):didgits[i]=pygame.image.load(namedigit[i]).convert_alpha()
        #currency
        for i in range(len(currency)):currencydone[i]=pygame.image.load(currency[i]).convert_alpha()
        # Accents
        for i in range(len(Accents)):Accentsdone[i]=pygame.image.load(Accents[i]).convert_alpha()
        # punctuation
        for i in range(len(ponctuation)):ponctuationDone[i]=pygame.image.load(ponctuation[i]).convert_alpha()
        #Températures
        for i in range(len(Temperature)):TemperatureDone[i]=pygame.image.load(Temperature[i]).convert_alpha()
        #Maths
        for i in range(len(Maths)):Mathsdone[i]=pygame.image.load(Maths[i]).convert_alpha()
        #Follow-me
        for i in range(len(Follow_me)):Follow_medone[i]=pygame.image.load(Follow_me[i]).convert_alpha()
        # Autre
        for i in range(len(Autre)):Autredone[i]=pygame.image.load(Autre[i]).convert_alpha()

        #On parcourt la liste du niveau
        num_ligne = 0
        #print("J'ai chargé les variables-images")
        for ligne in self.structure:
            #print("Je suis dans for line in self.structure",end="")
            #On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                #print("Je suis dans for sprite in ligne")
                #On calcule la position réelle en pixels
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                #print("J'ai innitialisé les x et y des images")
                # funky walls
                # for i in range(38):if i!=0:walls[i]=str(i+36)
                # for i in range (len(walls)):if sprite == walls[i]:fenetre.blit(FunkyWalsDone[i],(x,y))
                # if sprite == '^':		   #m = Mur
                    # fenetre.blit(FunkyWalsDone[0], (x,y))
                # d=sprite in walls
                # print(d)
                if sprite in walls:
                    for i in range(len(walls)):
                        if sprite != walls[i]:
                            continue
                        else:
                            fenetre.blit(FunkyWalsDone[i],(x,y))
                            break
                elif sprite == '#':		   #d = Départ
                    fenetre.blit(depart, (x,y))
                elif sprite=="ts":
                    fenetre.blit(depart_positionnement,(x,y))
                    dk.x=x
                    dk.y=y
                    print(f"dk.x={dk.x},x={x},dk.y={dk.y},y={y}")
                elif sprite == '10':		   #a = Arrivée 3ϵα♦²
                    fenetre.blit(arrivee, (x,y))
                elif sprite == '_':		   #a = Arrivée_enfant 4дβ
                    fenetre.blit(arrivee_fam, (x,y))
                #nombres
                elif sprite in didgit_count:
                    for i in range(len(didgit_count)):
                        if sprite != didgit_count[i]:
                            continue
                        else:
                            fenetre.blit(didgits[i],(x,y))
                            break
                #monnaie
                elif sprite in currency_count:
                    for i in range(len(currency_count)):
                        if sprite != currency_count[i]:
                            continue
                        else:
                            fenetre.blit(currencydone[i],(x,y))
                            break
                #ponctuation
                elif sprite in ponctuation_count:
                    for i in range(len(ponctuation_count)):
                        if sprite != ponctuation_count[i]:
                            continue
                        else:
                            fenetre.blit(ponctuationDone[i],(x,y))
                            break
                # flèches
                elif sprite in arrows_count:
                    for i in range(len(arrows_count)):
                        if sprite != arrows_count[i]:
                            continue
                        else:
                            fenetre.blit(arrowsprocessed[i],(x,y))
                            break

                #Températures
                elif sprite in Temperature_count:
                    for i in range(len(Temperature_count)):
                        if sprite != Temperature_count[i]:
                            continue
                        else:
                            fenetre.blit(TemperatureDone[i],(x,y))
                            break
                #Accents
                elif sprite in Accents_count:
                    for i in range(len(Accents_count)):
                        if sprite != Accents_count[i]:
                            continue
                        else:
                            fenetre.blit(Accentsdone[i],(x,y))
                            break
                
                #mathématiques
                elif sprite in Maths_count:
                    for i in range(len(Maths_count)):
                        if sprite != Maths_count[i]:
                            continue
                        else:
                            fenetre.blit(Mathsdone[i],(x,y))
                            break
                
                #Alphabet Minuscule
                elif sprite in Lowerletter_count:
                    for i in range(len(Lowerletter_count)):
                        if sprite != Lowerletter_count[i]:
                            continue
                        else:
                            fenetre.blit(lowerletter[i],(x,y))
                            break
                #Alphabet Majuscule
                elif sprite in Upperletter_count:
                    for i in range(len(Upperletter_count)):
                        if sprite != Upperletter_count[i]:
                            continue
                        else:
                            fenetre.blit(upperletter[i],(x,y))
                            break
                
                #Follow-me
                elif sprite in Follow_me_count:
                    for i in range(len(Follow_me_count)):
                        if sprite != Follow_me_count[i]:
                            continue
                        else:
                            fenetre.blit(Follow_medone[i],(x,y))
                            break
                
                # Autre
                elif sprite in Autre_count:
                    for i in range(len(Autre_count)):
                        if sprite != Autre_count[i]:
                            continue
                        else:
                            fenetre.blit(Autredone[i],(x,y))
                            break
                #mean
                elif sprite in mean_count:
                    for i in range(len(mean_count)):
                        if sprite != mean_count[i]:
                            continue
                        else:
                            fenetre.blit(meandone[i],(x,y))
                            break
                num_case += 1
            num_ligne += 1
            #print("Je viens d'incrémenter num_case et num_ligne")

class Perso:
    def __init__(self, droite, gauche, haut, bas, niveau):
        #print ("Je suis dans la classe perso.init")
        self.droite=pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        #print("J'ai initialisé les images pour le sprite")
        #Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        #print("J'ai placé le sprite")
        #Direction par défaut
        self.direction = self.droite
        #print("Je l'ai orienté vers la droite")
        #Niveau dans lequel le personnage se trouve
        self.niveau = niveau
        #print("self.niveau = niveau")

    def deplacer(self, direction):
        print("Je suis dans la def deplacer (self, direction")
        if direction=='droite':
            if self.case_x<(nombre_sprite_cote -1):
                if self.niveau.structure[self.case_y][self.case_x+1] not in walls:
                    self.case_x+=1
                    self.x=self.case_x*taille_sprite
            self.direction=self.droite
        if direction=='gauche':
            if self.case_x>0:
                if self.niveau.structure[self.case_y][self.case_x-1] not in walls:
                    self.case_x-=1
                    self.x=self.case_x*taille_sprite
            self.direction=self.gauche
        if direction=='haut':
            if self.case_y>0:
                if self.niveau.structure[self.case_y-1][self.case_x] not in walls:
                    self.case_y-=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.haut

        if direction=='bas':
            if self.case_y<(nombre_sprite_cote-1):
                if self.niveau.structure[self.case_y+1][self.case_x] not in walls:
                    self.case_y+=1
                    self.y=self.case_y*taille_sprite
            self.direction=self.bas

class trackProgress:
    def refreshlevels(PATH):
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

class tkinterWindows(root):
    def choselevels():
        def LEVEL():
            Levelnumber = int(level.get())
            Cevel.destroy()
            print(Levelnumber)
            trackProgress.refreshlevels("levels")#levelfiles
            maxlevel=len(levelfiles)
            # global choix
            choix=levelfiles[Levelnumber-1]
            print("choix= ",choix)
            print("Levelnumber= ",Levelnumber)
            #MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix)#niveau,
            return choix,maxlevel,Levelnumber
        trackProgress.refreshlevels("levels")#levelfiles
        maxlevel=len(levelfiles)
        Cevel = Tk()
        Frame1 = Frame(Cevel, borderwidth=2, relief=FLAT)
        Frame1.pack(side=LEFT, padx=10, pady=10)
        label = Label(Frame1, text="Choose you're level:")
        label.pack()
        level=Spinbox(Frame1, from_=-1, to=maxlevel, increment=1)
        level.pack(side=LEFT, padx=5)
        bouton=Button(Frame1, text="Jouer!", command=LEVEL)
        bouton.pack(side=RIGHT, padx=5)
        Cevel.mainloop()
        # return choix, Choix, maxlevel, CREDIT
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
        fenetre.iconbitmap(image_icone_bmp)
        fenetre.title("restorer?")
        Frame1 = Frame(fenetre, borderwidth=2, relief=FLAT)
        Frame1.pack(side=TOP, padx=10, pady=10)
        FrameButt=Frame(fenetre, borderwidth=2, relief=FLAT)
        FrameButt.pack(side=TOP, padx=0, pady=10)

        label = Label(Frame1, text="Une sauvegarde a été trouvée.")
        label.pack()
        label = Label(Frame1, text="Voulez-vous continuer la partie déjà entamée?")
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
        root.iconbitmap(image_icone_bmp)
        root.title("Credits")
        root.geometry("900x630")
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
        Henry=Label(Frame1TOP3, text="starter code From Open ClassRooms, TP Dk", bg=bgColor)
        Henry.pack(anchor=CENTER,side=TOP)#,fill=X
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
        Feedback=Label(Frame1TOP4, text="Feedback:", bg=bgColor)
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
    def initialiseS(self):
        def removeExtention(element,extension):
                if extension in element:
                        f=element.split(extension)
                        return f[0]
                else:
                        return element
        for i in range(len(self.visible)):
                self.visible[i]=removeExtention(self.visible[i],self.extension)
                self.All_the_levels.append(self.visible[i])
                e=i
                self.All_the_levels_index[self.visible[i]]=e+1
        self.All_the_levels.append("_____Hidden Levels______")
        for i in range(len(self.hidden)):
                if self.hidden[i] not in ['002_l2', '003_l3', '004_l4', '005_l5']:
                        self.hidden[i]=removeExtention(self.hidden[i],self.extension)
                        self.All_the_levels.append(self.hidden[i])
                        self.All_the_levels_index[self.hidden[i]]=self.keys_for_hidden[self.hidden[i]]
        print(f"All_the_levels_index={self.All_the_levels_index}")
    def S(self):
        print(f"self.All_the_levels={self.All_the_levels}\nself.All_the_levels_index={self.All_the_levels_index}\nself.visible={self.visible}\nself.hidden={self.hidden}\nself.path={self.path}\nself.finalImageForCanvasS={self.finalImageForCanvasS}\nself.keys_for_hidden={self.keys_for_hidden}")
        def test(*args):
            index = listbox.curselection()
            # if len(index)==0:
            #     index=1
            # else:
            #         index=index[0]
            index=index[0]
            print(f"name={self.All_the_levels[index]}, access={self.All_the_levels_index[self.All_the_levels[index]]}")
            DescriptionLabel.config(text=f"name='{self.All_the_levels[index]}', access='{self.All_the_levels_index[self.All_the_levels[index]]}'")
            if self.All_the_levels[index] in ["_____Visible Levels_____","_____Hidden Levels______"]:
                self.finalImageForCanvasS="img/background/fonds.png"
            else:
                self.finalImageForCanvasS=f"{self.path}{self.All_the_levels[index]}.png"
            self.photoS=PhotoImage(file=self.finalImageForCanvasS)
            ViewingBox.config(image=self.photoS)
            ViewingBox.image=self.photoS
            print(f"index={index}")#,type(index)={type(index)}")
            TT.update()
            DescriptionLabel.update()
            listbox.update()
        size_x=515
        size_y=350
        TT = Tk()
        TT.geometry(f"{size_x}x{size_y}")
        TT.minsize(size_x,size_y)
        TT["bg"]=self.universalBackground
        TT.title("The Levels")
        FrameTOP=Frame(TT,bg=self.universalBackground, relief=FLAT)
        FrameTOP.pack(side=TOP,fill=X)
        FrameLeft=Frame(FrameTOP,bg=self.universalBackground, relief=FLAT)
        FrameLeft.pack(side=LEFT,fill=Y)
        FrameRight=Frame(FrameTOP,bg=self.universalBackground, relief=FLAT)
        FrameRight.pack(side=RIGHT,padx=6)
        listbox = Listbox(FrameLeft)
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(FrameLeft)
        scrollbar.pack(side = RIGHT, fill = BOTH)

        for i in range(len(self.All_the_levels)):
            listbox.insert(END, self.All_the_levels[i])
        listbox.bind('<Double-Button>', test)
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        DescriptionLabel=Label(FrameRight,fg="black",bg=self.universalBackground,borderwidth=0,relief=GROOVE,text="...",anchor="center")
        DescriptionLabel.pack(side=TOP, fill=X)
        self.photoS = PhotoImage(file=self.finalImageForCanvasS)
        ViewingBox=Label(FrameRight,image=self.photoS)
        ViewingBox.pack(side=TOP,fill=X)
        #TT.update()
        #DescriptionLabel.update()
        #listbox.update()
        FrameBottom=Frame(TT,bg=self.universalBackground,relief=FLAT)
        FrameBottom.pack(side=TOP,fill=X)
        CloseButton=Button(FrameBottom,text="Close",bg=self.universalBackground,fg="black",command=TT.destroy)
        CloseButton.pack(side=LEFT)
        WatermarkLabel=Label(FrameBottom,bg=self.universalBackground,text=self.watermark,fg="black")
        WatermarkLabel.pack(side=RIGHT,fill=X)
        TT.bind("<Return>", test)
        TT.mainloop()



class gameAnimations:
    def mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre):
        if mainMenuPlayed==False:
            #Titre
            pygame.display.set_caption(titre_fenetre)
            for i in range(len(load_images)):
                accueil = pygame.image.load(load_images[i]).convert()
                fenetre.blit(accueil, (0,0))
                pygame.display.flip()
                sleep(0.5)
            mainMenuPlayed=True
            gameAnimations.mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre)
        else:
            accueil = pygame.image.load(image_main1).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(0.5)
            accueil = pygame.image.load(image_main2).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(0.5)
            #Titre
            pygame.display.set_caption(titre_fenetre)
        # return acceuil

class MainLoopGame:
    def boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien,maxlevel,hidden,exitSpaceGame): #
        if exitSpaceGame!=True:
            print("Je suis dans la boucle boucledejeu")
            #BOUCLE DE JEU
            while continuer_jeu:
                print("Je suis dans la while continuer jeux")
                #Limitation de vitesse de la boucle
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                    print("Je suis dans for event in pygame.event.get()")
                    #Si l'utilisateur quitte, on met la variable qui continue le jeu
                    #ET la variable générale à 0 pour fermer la fenêtre
                    if event.type == QUIT:
                        # maxlevel=
                        print("Je suis dans event.type==QUIT")
                        continuer_jeu = 0
                        continuer = 0
                        exitSpaceGame=True
                        # LEVEL=maxlevels
                        if hidden==1:
                            trackProgress.refreshlevels("elementary_levels")
                        else:
                            trackProgress.refreshlevels("levels")
                        LEVEL=len(levelfiles)
                        return LEVEL,exitSpaceGame
                    elif event.type == KEYDOWN:
                        print("Je suis dans event.type == KEYDOWN")
                        #Si l'utilisateur presse Echap ici, on revient seulement au menu
                        if event.key == K_ESCAPE:
                            print("Je suis dans event.key==K_ESCAPE")
                            continuer_jeu = 0
                            exitSpaceGame=True
                            return exitSpaceGame
                        #Touches de déplacement de Wolf
                        elif event.key == K_RIGHT or event.key==K_d:
                            print("Je suis dans event.key==K_RIGHT")
                            dk.deplacer('droite')
                        elif event.key == K_LEFT or event.key==K_a or event.key == K_q:
                            print("Je suis dans event.key==K_LEFT")
                            dk.deplacer('gauche')
                        elif event.key == K_UP or event.key == K_z or event.key==K_w:
                            print("Je suis dans event.key==K_UP")
                            dk.deplacer('haut')
                        elif event.key == K_DOWN or event.key==K_s:
                            print("Je suis dans event.key==K_DOWN")
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
                # print("J'ai fait un fenetre.blit(fond, (0,0))")
                # print("Je tente un niveau.afficher(fenetre)")
                niveau.afficher(fenetre)
                # print("J'ai fait niveau.afficher(fenetre)")
                fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
                # print("J'ai fait fenetre.blit(dk.direction, (dk.x, dk.y))")
                pygame.display.flip()
                # print("J'ai fait pygame.display.flip()")
                #Victoire -> Retour à l'accueil
                if niveau.structure[dk.case_y][dk.case_x] == '10' or niveau.structure[dk.case_y][dk.case_x] == '_':continuer_jeu = 0 #or niveau.structure[dk.case_y][dk.case_x] == '0':
                #return continuer_jeu, continuer
    def check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix,hidden): #niveau,
        if choix != 0 and Choix!=0:
            # print("Je suis dans la check boucle")
            # pygame.display.set_caption("{}{}".format(titre_fenetre,choix))
            # checkcredit()
            #Chargement du fond
            global fond
            if CREDIT==True:
                fond = pygame.image.load(image_fond_credits).convert()
                # return fond
            else:
                fond=pygame.image.load(image_fond).convert()
            # if CREDIT==False:fond=pygame.image.load(image_fond).convert()
            # else:fond=pygame.image.load(image_fond_credits).convert() 
            if hidden==1:
                choix="elementary_levels/{}".format(choix)
            else:
                choix="levels/{}".format(choix)
                # return choix, fond
            #Génération d'un niveau à partir d'un fichier
            global niveau
            print("choix={}".format(choix))
            niveau = Niveau(choix)
            print("Je rentre dans la boucle generer")
            niveau.generer()
            print("La boucle Niveau.generer a fonctionnée")
            niveau.afficher(fenetre)
            print("La boucle affiche fenêtre a fonctionnée")
            #Création du loup
            global dk
            dk = Perso("img/sprite/w/w_rigth.png", "img/sprite/w/w_left.png", "img/sprite/w/w_up.png", "img/sprite/w/w_down.png", niveau)
            #Creating the ennemi (The gardian)
            global gardien
            gardien=Perso("img/sprite/gardien/Gardien_Droite.png", "img/sprite/gardien/Gardien_Gauche.png", "img/sprite/gardien/Gardien_haut.png", "img/sprite/gardien/Gardien_bas.png", niveau)
            # MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau,dk,gardien)
        return dk, gardien, fond, choix, niveau, fenetre
    def play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,exitSpaceGame):
        # global exitSpaceGame
        exitSpaceGame=False#True
        print("Je suis dans la play boucle")
        #continuer_accueil = 0
        if hidden==0:trackProgress.refreshlevels("levels")#levelfiles
        else:trackProgress.refreshlevels("elementary_levels")
        global maxlevels, LEVEL
        maxlevel=len(levelfiles)
        LEVEL=0
        # print(levelfiles)
        while LEVEL<len(levelfiles):
            print("ExitSpaceGame={}".format(exitSpaceGame))
            # for LEVEL in range(len(levelfiles)):
            # print(levelfiles)
            print("level={}".format(LEVEL))
            #global continuer_jeu
            if exitSpaceGame==False:
                continuer_jeu = 1
            else:continuer_jeu=0
            #global choix
            if exitSpaceGame==False:
                if Choix!=0:
                    choix=levelfiles[LEVEL]
                    pygame.display.set_caption("{} {}".format(titre_fenetre,LEVEL))
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    if hidden==1:trackProgress.refreshlevels("elementary_levels")
                    else:trackProgress.refreshlevels("levels")
                    LEVEL=len(levelfiles)
                    continuer_jeu = 0
                    # LEVEL=maxlevel
                    continuer = 0
                    continuer_accueil=1
                    #Variable de choix du niveau
                    # choix = levelfiles[len(levelfiles-1)]
                    choix=0
                    Choix=0
                    exitSpaceGame=True
                    # LEVEL=len(levelfiles)
                    # print(bababa)
                    sys.exit(0)
                    break
                else:
                    print (choix)
                    #choix = 'l{}'.format(i+1)
                    MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix,hidden)#niveau
                    MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien,maxlevel,hidden,exitSpaceGame)
                    #print("tour = {}\ncontinuer_jeu = {}\nchoix={}\ncontinuer={}\nniveau={}".format(i,continuer_jeu,choix,continuer,niveau))
                    LEVEL+=1
            else:
                exitSpaceGame=True
                LEVEL+=1
        if exitSpaceGame==False:
            CREDIT=True
            hidden=1
            choix="credits"
            MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix,hidden)
            MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien,maxlevel,hidden,exitSpaceGame)
        else:exitSpaceGame=True
        return Choix, continuer_accueil, exitSpaceGame
    def Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix):
        # event=pygame.event.get()
        exitSpaceGame=False
        print("Je suis dans la play boucle")
        #continuer_accueil = 0
        if hidden==0:trackProgress.refreshlevels("levels")#levelfiles
        else:trackProgress.refreshlevels("elementary_levels")
        if CREDIT==False:fond=pygame.image.load(image_fond).convert()
        else:fond=pygame.image.load(image_fond_credits).convert()
        global maxlevels, LEVEL
        maxlevel=len(levelfiles)
        #LEVEL=0
        # print(levelfiles)
        #while LEVEL<len(levelfiles):
        # for LEVEL in range(len(levelfiles)):
        LEVEL=choix
        print(levelfiles)
        print("level={}".format(LEVEL))
        #global continuer_jeu
        continuer_jeu = 1
        #global choix
        if Choix!=0:pygame.display.set_caption("{} {}".format(titre_fenetre,LEVEL))
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_q:
            continuer_jeu = 0
            LEVEL=maxlevel
            continuer = 0
            continuer_accueil=1
            #Variable de choix du niveau
            # choix = levelfiles[len(levelfiles-1)]
            choix=0
            Choix=0
            exitSpaceGame=True
            #LEVEL=len(levelfiles)
            #sys.exit(0)
            #break
        else:
            print ("Specificlevels.choix = ",choix)
            #choix = 'l{}'.format(i+1)
            MainLoopGame.check(image_fond,image_fond_credits,fenetre,choix,CREDIT,Choix,hidden)#niveau
            MainLoopGame.boucledejeu(event,continuer_jeu,continuer,fond,fenetre,niveau, dk,gardien,maxlevel,hidden,exitSpaceGame)
            #print("tour = {}\ncontinuer_jeu = {}\nchoix={}\ncontinuer={}\nniveau={}".format(i,continuer_jeu,choix,continuer,niveau))
            #LEVEL+=1
        return Choix, continuer_accueil

#---------------------------------- Wolf escape.pyw file ---------------------------------------------

levels=4
CREDIT=False
exitSpaceGame=False
#levelfiles=[]
"""
Jeu Wolf escape Labyrinthe
Jeu dans lequel on doit déplacer un loup jusqu'à la viande à travers un labyrinthe.
Script Python
Fichiers : trop pour les lister ici
"""
links=boot.initialise_links(main_for_rec_dict)
RI=root(main=main_for_rec,main_dict=main_for_rec_dict,links=links) #initialising root
for i in RI.links:
    print(i)
boot.TKinter.window.FetchingFiles(RI)


def choselevels():
    def LEVEL():
        global choix
        choix=levelfiles[int(level.get())-1]
        Level.destroy()
        print("Wolf escape.py.choselevels.LEVEL.choix= ",choix)
        #return choix
    trackProgress.refreshlevels("levels")#levelfiles
    maxlevel=len(levelfiles)
    Level = Tk()
    Frame1 = Frame(Level, borderwidth=2, relief=FLAT)
    Frame1.pack(side=LEFT, padx=10, pady=10)
    label = Label(Frame1, text="Choose your level:")
    label.pack()
    level=Spinbox(Frame1, from_=1, to=maxlevel, increment=1)
    level.pack(side=LEFT, padx=5)
    bouton=Button(Frame1, text="Jouer!", command=LEVEL)
    bouton.pack(side=RIGHT, padx=5)
    Level.mainloop()



pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetrex, cote_fenetrey))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)
#rendre le déplacement fluide
pygame.key.set_repeat(400, 30)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
    
    #Rafraichissement
    pygame.display.flip()
	
    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
        gameAnimations.mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre)
        mainMenuPlayed=True

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or event.type == KEYDOWN and event.key == K_a or event.type == KEYDOWN and event.key == K_q:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0
            elif event.type == KEYDOWN:
                #Lancement du niveau 1
                if event.key == K_SPACE:
                    continuer_accueil,LEVEL,Choix,hidden=0,0,1,0
                    MainLoopGame.play(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,exitSpaceGame)
                elif event.key == K_BACKSPACE or event.key == K_RETURN:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,0,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choselevels()
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                    print("exited the boucledejeu")
                    print(choix)
                elif event.key == K_s:
                    continuer_accueil = 0
                    tkinterWindows.initialiseS(RI)
                    tkinterWindows.S(RI)
                elif event.key == K_c:
                    continuer_accueil = 0
                    tkinterWindows.main_credits()
                elif event.key == K_h:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="h"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F1:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="m1"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F2:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="m2"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_i:
                    print("K_i")
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="I"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_m:
                    print("K_m")
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="M"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_p:
                    print("K_p")
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,False,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="P"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
                elif event.key == K_F3:
                    continuer_accueil, hidden,levelfiles,Choix,CREDIT,fond=0,1,os.listdir("levels"),1,True,pygame.image.load(image_fond).convert()
                    maxlevel=len(levelfiles)
                    choix="credits"
                    MainLoopGame.Specificlevel(event,continuer_accueil,image_fond,continuer_jeu,continuer,fenetre,levels,Choix,hidden,CREDIT,choix)
