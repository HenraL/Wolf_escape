from tkinter import image_names
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
        
        def correlate_E_ID(element=CO.walls,ID=CO.FunkyWalls,IDDone=CO.FunkyWalsDone,Description1="walls",Description2="FW",Description3="FWD"):
            """Correlate Elements and IDs"""
            print("\n#######################################################################\n")
            print(f"len({str(Description1)})={len(element)}, len({str(Description2)})={len(ID)}, len({str(Description3)})={len(IDDone)}\n")
            if len(element)==len(ID) and len(element)==len(IDDone):
                for i in range(len(element)):
                    print(f"{Description1}={element[i]}, {Description2}={ID[i]}, {Description3}={IDDone[i]}")
            print("\n#######################################################################\n")
            return The_Debug.Vars.MakeDict(element,ID,IDDone,Description1,Description2,Description3)
        def MakeDict(element=CO.walls,ID=CO.FunkyWalls,IDDone=CO.FunkyWalsDone,Description1="walls",Description2="FW",Description3="FWD"):
            temp={}
            if len(element)==len(ID) and len(element)==len(IDDone):
                for i in range(len(element)):
                    a=element[i].split("/")
                    temp[a[len(a)-1]]=ID[i]
            print(temp)
            return temp

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
    elif fullInitialisation==2:
        CO.theLists.main_for_rec
        CO.theLists.main_for_rec_dict
        CO.main_for_rec
        CO.main_for_rec_dict
        CO.CREDIT
        # CO.exitSpaceGame
        CO.nombre_sprite_cote
        CO.taille_sprite
        CO.cote_fenetrex
        CO.cote_fenetrey
        CO.titre_fenetre
        CO.image_icone
        CO.image_icone_bmp
        CO.image_main1
        CO.image_main2
        CO.mainMenuPlayed
        CO.frameMainMenuWait
        CO.image_accueil1
        CO.image_accueil2
        CO.image_accueil3
        CO.image_accueil4
        CO.image_accueil5
        CO.image_accueil6
        CO.image_accueil7
        CO.image_accueil8
        CO.image_accueil9
        CO.image_accueil10
        CO.image_accueil11
        CO.image_accueil12
        CO.image_accueil13
        CO.image_accueil14
        CO.image_accueil15
        CO.load_images
        CO.image_accueil
        CO.img_mean_up
        CO.img_mean_down
        CO.img_mean_left
        CO.img_mean_right
        CO.mean
        CO.meandone
        CO.mean_count
        CO.image_fond
        CO.image_fond_credits
        CO.image_depart
        CO.image_depart_du_loup
        CO.image_arrivee
        CO.image_arrivee_fam
        CO.image_mur
        CO.WBB
        CO.WBW
        CO.WBRB
        CO.WBRW
        CO.WBW
        CO.WBOB
        CO.WBOW
        CO.WBPB
        CO.WBPW
        CO.WCB
        CO.WCW
        CO.WDRB
        CO.WDRW
        CO.WDBB
        CO.WDBW
        CO.WDGB
        CO.WDGW
        CO.WDPB
        CO.WDPW
        CO.WGB
        CO.WGW
        CO.WLBB
        CO.WLBW
        CO.WLGB
        CO.WLGW
        CO.WLGB
        CO.WLGW
        CO.WLPB
        CO.WLPW
        CO.WMBB
        CO.WMBW
        CO.WOB
        CO.WOW
        CO.WVLBB
        CO.WVLBW
        CO.WW
        CO.WYB
        CO.WYW
        CO.FunkyWalls
        CO.FunkyWalsDone
        CO.walls
        CO.ld
        CO.lg
        CO.lh
        CO.lb
        CO.image_credits_fond
        CO.image_credits_gagne
        CO.image_credits_w_Irina
        CO.image_zero
        CO.image_one
        CO.image_two
        CO.image_three
        CO.image_four
        CO.image_five
        CO.image_six
        CO.image_seven
        CO.image_eight
        CO.image_nine
        CO.namedigit
        CO.didgits
        CO.didgit_count
        CO.image_dollar
        CO.image_pound
        CO.image_euro
        CO.image_yen
        CO.image_whan
        CO.currency
        CO.currencydone
        CO.currency_count
        
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

    else:
        BigList=[]
        BigList.append(The_Debug.Vars.correlate_E_ID(element=[CO.image_arrivee,CO.image_arrivee_fam],ID=["10","_"],IDDone=["",""],Description1="[CO.image_arrivee,CO.image_arrivee_fam]",Description2='["10","_"]',Description3='["",""]')) # Ends 
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.Follow_me,ID=CO.Follow_me_count,IDDone=CO.Follow_medone,Description1="CO.Follow_me",Description2="CO.Follow_me_count",Description3="CO.Follow_medone")) # Social
        BigList.append(The_Debug.Vars.correlate_E_ID(element=[CO.image_depart,CO.image_depart_du_loup],ID=["#","ts"],IDDone=["",""],Description1="[CO.image_depart,CO.image_depart_du_loup]",Description2='["#","ts"]',Description3='["",""]')) # Start
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.FunkyWalls,ID=CO.walls,IDDone=CO.FunkyWalsDone,Description1="FW",Description2="walls",Description3="FWD")) #Walls 
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # Backgrounds
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # GameIcon
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # Wolf
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # Guard
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.upperletterletter,ID=CO.Upperletter_count,IDDone=CO.upperletter,Description1="CO.upperletterletter",Description2="CO.Upperletter_count",Description3="CO.upperletter")) # Caps
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.lowerletterletter,ID=CO.Lowerletter_count,IDDone=CO.lowerletter,Description1="CO.lowerletterletter",Description2="CO.Lowerletter_count",Description3="CO.lowerletter")) # Lowercases
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.Accents,ID=CO.Accents_count,IDDone=CO.Accentsdone,Description1="CO.Accents",Description2="CO.Accents_count",Description3="CO.Accentsdone")) # Accents
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.namedigit,ID=CO.didgit_count,IDDone=CO.didgits,Description1="CO.namedigit",Description2="CO.didgit_count",Description3="CO.didgits")) # Digits
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.Temperature,ID=CO.Temperature_count,IDDone=CO.TemperatureDone,Description1="CO.Temperature",Description2="CO.Temperature_count",Description3="CO.TemperatureDone")) # Temperature
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.arrows,ID=CO.arrows_count,IDDone=CO.arrowsprocessed,Description1="CO.arrows",Description2="CO.arrows_count",Description3="CO.arrowsprocessed")) # Arrows
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.currency,ID=CO.currency_count,IDDone=CO.currencydone,Description1="CO.currency",Description2="CO.currency_count",Description3="CO.currencydone")) # Currency
        BigList.append(The_Debug.Vars.correlate_E_ID(element=CO.Autre,ID=CO.Autre_count,IDDone=CO.Autredone,Description1="CO.Autre",Description2="CO.Autre_count",Description3="CO.Autredone")) # Hearts
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # Common symbols
        # The_Debug.Vars.correlate_E_ID(element=CO.,ID=CO.,IDDone=CO.,Description1="",Description2="",Description3="") # Maths  

OneOrAll(fullInitialisation)
# OneOrAll(1)
OneOrAll(fullInitialisation)
The_Debug.overwrite_line(file=FI.DebugO_F,line=0,content="0")