from string import ascii_letters
# from string import digits
# from string import punctuation
import requests
from pygame.constants import *

""" Booting up, initialising vars to ensure the required files exist before we start the game."""
r=open(requests.get("https://hanralatalliardwork.github.io/wolf_escape_home/files/requirements/List.txt").content,"r").read()
class unTreat:
    def __init__(self):
        self.BigList="\\n\\n"
        self.childList="\\n"
        self.subChildren="\n"
    def Layers(self,element):
        """decompose the string into the first layer of lists"""
        temp=element.split(self.BigList)
        temp2=[]
        for i in range(len(temp)):
            print(temp[i])
            temp2.append(temp[i].split(self.childList))
        print(temp2)
        listMain=[]
        for i in range(len(temp2)):
            for b in range(len(temp2[i])):
                temp3=temp2[i][b].split(self.subChildren)
                listMain.append(temp3)
        print("\n\n\\n\\n\\n\n\n")
        print(listMain)
        toPop=[]
        for i in range(len(listMain)):
            #toPop.append(i)
            temp1=[]
            for b in range(len(listMain[i])):
                #temp1.append(b)
                temp2=[]
                #print("in b")
                if listMain[i][b]=="":
                    temp2.append(b)
                temp1.append(temp2)
            toPop.append(temp1)
        print(toPop)
        #for i in range(len(toPop)):
        #    print(f"toPop[{i}]={toPop[i]}")
        #    for b in range(len(toPop[i])):
        #        print(f"toPop[{i}][{b}]={toPop[i][b]}")
        #        for c in range(len(toPop[i][b])):
        #            print(f"toPop[{i}][{b}][{c}]={toPop[i][b][c]}")
        #            print(f"[{i}][{b}][{c}]={listMain.pop(toPop[i][b][c])}")
                #print(f"toPop[{i}][{b}]={toPop[i][b]}")
        return listMain#,toPop
UI=unTreat()
m=UI.Layers(r)

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
img_micro="img/tut_image/alphabet/punctuation/µ.PNG"
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
ponctuation=[img_square_bracket_open,img_square_bracket_closed,img_micro,img_and,img_at,img_border,img_cureved_bracket_closed,img_cureved_bracket_open,colum,img_full_stop,img_end_cell,img_exclamation_mark,img_percentage,img_open_quote,img_close_quote,img_question_mark,semicolon]
ponctuationDone=[""]*len(ponctuation)
ponctuation_count=["[","]","Âµ","&","@","20",")","(",":",".","Â¤","!","Â§","21","22","?",";"]


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
