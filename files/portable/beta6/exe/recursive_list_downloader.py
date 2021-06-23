import requests, os
from time import sleep
#:{"type":"file","fileName":"","fileContent":""}
# lst=["","","",""]
# def makeDict(lst):
#  for i in range(len(lst)):
#   print("\""+lst[i]+"\":{\"type\":\"file\",\"fileName\":\""+lst[i]+"\",\"fileContent\":boot.get.online.tempFile(url=\"http://www.a.fr\")},",end="")
class root:
    def __init__(self,main,main_dict,links):
        self.main=main
        self.main_dict=main_dict
        self.links=links
        self.home="https://hanralatalliardwork.github.io/wolf_escape_home/"
        self.file_location="files/requirements"
        self.ggg=0
        self.list_dict=[]
        
class boot(root):
    class get:
        class online:
            def tempFile(url):
                road=requests.get(url)
                if road.status_code!="404":
                    road=road.content
                    try:
                        e=open(road,"rb").read()
                        print("rb")
                        return e
                    except:
                        try:
                            e=open(road,"r").read()
                            print("r")
                            return e
                        except:
                            try:
                                e=road.decode()
                                print("decode")
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
            print(RI.ggg)
            # print(f"\n\nlst_from={lst_from}")
            for i in lst_from:
                try:
                    if lst_from[i]["type"].lower()=="file" or lst_from[i]["type"].lower()=="<file>":
                        lst_to.append(f"{path}/{i}")
                except:
                    try:
                        if lst_from[i].lower()=='dir' or lst_from[i].lower()=='<dir>':
                            path+=f"/{i}"
                            lst_to.append("")
                    except:
                        return f"Error, type {lst_from[i]} unknown. must be <dir> or dir for a folder or <file> or file for a file."
            # print(lst_to)
            RI.ggg+=1
            return lst_to
        def content(list1,list2,links,home):
            # peth="."
            for i in range(len(list1)):
                peth,peth_link=".",""
                for b in range(len(list1[i])):
                    print(f"list2[i][list1[i][b]]={list2[i][list1[i][b]]}={list1[i][b]}")
                    try:
                        print(f"list2[i][list1[i][b]][\"type\"]={list2[i][list1[i][b]]['type']}")
                        print(f"link=\"{home}{links[i][b]}\"")
                        if list2[i][list1[i][b]]["type"].lower()=='file' or list2[i][list1[i][b]]["type"].lower()=='<file>':
                            try:
                                a=open(f"{peth}/{list1[i][b]}","r").read()
                                c=len(a)
                                print(f"c={c}")
                            except:
                                c=0
                            if os.path.exists(f"{peth}/{list1[i][b]}")==False and c==0:
                                # try:
                                print(f"trying with link=\"{home}{links[i][b]}\"")
                                list2[i][list1[i][b]]["fileContent"]=boot.get.online.tempFile(f"{home}{links[i][b]}")
                                if list2[i][list1[i][b]]["fileContent"]==404:print(f"status={list2[i][list1[i][b]]['fileContent']}")
                                # except:
                                #     print(f"failed so trying with link=\"{home}{RI.file_location}{links[i][b]}\"")
                                #     list2[i][list1[i][b]]["fileContent"]=boot.get.online.tempFile(f"{home}{RI.file_location}{links[i][b]}")
                                #     if list2[i][list1[i][b]]["fileContent"]==404:print(f"status={list2[i][list1[i][b]]['fileContent']}")
                                # print(f"\n\n\nfilecontent=\n{list2[i][list1[i][b]]['fileContent']}\n\n\n")
                                if list2[i][list1[i][b]]['fileContent']==404:
                                    print(f"\n\n\nfilecontent=\n{list2[i][list1[i][b]]['fileContent']}\n\n\n")
                                    sleep(10)
                                try:
                                    f=open(f"{peth}/{list2[i][list1[i][b]]['fileName']}","wb")
                                    print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} opened")
                                    f.write(list2[i][list1[i][b]]["fileContent"])
                                    # print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} written to")
                                    print("opened as wb")
                                    list2[i][list1[i][b]]["opening_method"]="wb"
                                    list2[i][list1[i][b]]["exists"]="No"
                                except:
                                    f=open(f"{peth}/{list2[i][list1[i][b]]['fileName']}","w")
                                    print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} opened")
                                    f.write(list2[i][list1[i][b]]["fileContent"])
                                    # print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} written to")
                                    print("opened as w")
                                    list2[i][list1[i][b]]["opening_method"]="w"
                                    list2[i][list1[i][b]]["exists"]="No"
                                sleep(5)
                                f.close()
                                print(f"file {peth}/{list2[i][list1[i][b]]['fileName']} closed")
                                print(list2[i][list1[i][b]])
                            else:
                                print(f"file {list1[i][b]} already exists in {peth}.")
                                list2[i][list1[i][b]]["opening_method"]=None
                                list2[i][list1[i][b]]["exists"]="Yes"
                    except:
                        try:
                            if list2[i][list1[i][b]].lower()=="dir" or list2[i][list1[i][b]].lower()=="<dir>":
                                peth+=f"/{list1[i][b]}"
                                if os.path.exists(peth)==False:
                                    os.mkdir(peth)
                                    print(f"{peth}........[CREATED]")
                        except:
                            return f"{list2[i][list1[i][b]]} = [UNKNOWN TYPE]\npath={peth}"
                    print(f"path={peth}")
            for i in list2:
                RI.list_dict.append(list2[i])
            return RI.list_dict
folder1=["elementary_levels","002_l2","003_l3","004_l4","005_l5","credits","h","I","M","m1","m2","P"]
folder1_dict={"elementary_levels":"dir",
              "002_l2":{"type":"file","fileName":"002_l2","fileContent":""},
              "003_l3":{"type":"file","fileName":"003_l3","fileContent":""},
              "004_l4":{"type":"file","fileName":"004_l4","fileContent":""},
              "005_l5":{"type":"file","fileName":"005_l5","fileContent":""},
              "credits":{"type":"file","fileName":"credits","fileContent":""},
              "h":{"type":"file","fileName":"h","fileContent":""},
              "I":{"type":"file","fileName":"I","fileContent":""},
              "M":{"type":"file","fileName":"M","fileContent":""},
              "m1":{"type":"file","fileName":"m1","fileContent":""},
              "m2":{"type":"file","fileName":"m2","fileContent":""},
              "P":{"type":"file","fileName":"P","fileContent":""}}

#folder2_1=["img","advertising images",]
folder2_2=["img","background","fonds.png"]
folder2_2_dict={"img":"dir","background":"dir","fonds.png":{"type":"file","fileName":"fonds.png","fileContent":""}}
folder2_3=["img","Credits","end - Copie.PNG","watermark_background - Copie.png"]
folder2_3_dict={"img":"dir","Credits":"dir","end - Copie.PNG":{"type":"file","fileName":"end - Copie.PNG","fileContent":""},"watermark_background - Copie.png":{"type":"file","fileName":"watermark_background - Copie.png","fileContent":""}}
folder2_4=["img","end","endv.png"]
folder2_4_dict={"img":"dir","end":"dir","endv.png":{"type":"file","fileName":"endv.png","fileContent":""}}
# folder2_5=["img","Follow-me"]
# folder2_5_dir={"img":"dir","Follow-me":"dir"}
folder2_5_1=["img","Follow-me","Behance","behance.svg","behance_b.PNG","behance_w.PNG"]
folder2_5_1_dict={"img":"dir","Follow-me":"dir","Behance":"dir","behance.svg":{"type":"file","fileName":"behance.svg","fileContent":""},"behance_b.PNG":{"type":"file","fileName":"behance_b.PNG","fileContent":""},"behance_w.PNG":{"type":"file","fileName":"behance_w.PNG","fileContent":""}}
folder2_5_2=["img","Follow-me","codepen","codepen.svg","codepen_b.PNG","codepen_w.PNG","link.txt"]
folder2_5_2_dict={"img":"dir","Follow-me":"dir","codepen":"dir","codepen.svg":{"type":"file","fileName":"codepen.svg","fileContent":""},"codepen_b.PNG":{"type":"file","fileName":"codepen_b.PNG","fileContent":""},"codepen_w.PNG":{"type":"file","fileName":"codepen_w.PNG","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_3=["img","Follow-me","dev-to","dev-to.svg","dev-to_B.PNG","dev-to_W.png","link.txt"]
folder2_5_3_dict={"img":"dir","Follow-me":"dir","dev-to":"dir","dev-to.svg":{"type":"file","fileName":"dev-to.svg","fileContent":""},"dev-to_B.PNG":{"type":"file","fileName":"dev-to_B.PNG","fileContent":""},"dev-to_W.png":{"type":"file","fileName":"dev-to_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_4=["img","Follow-me","discord","discord.svg","discord_B.PNG","discord_W.png","link.txt"]
folder2_5_4_dict={"img":"dir","Follow-me":"dir","discord":"dir","discord.svg":{"type":"file","fileName":"discord.svg","fileContent":""},"discord_B.PNG":{"type":"file","fileName":"discord_B.PNG","fileContent":""},"discord_W.png":{"type":"file","fileName":"discord_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_5=["img","Follow-me","facebook","facebook.svg","facebook_B.PNG","facebook_W.png","link.txt"]
folder2_5_5_dict={"img":"dir","Follow-me":"dir","facebook":"dir","facebook.svg":{"type":"file","fileName":"facebook.svg","fileContent":""},"facebook_B.PNG":{"type":"file","fileName":"facebook_B.PNG","fileContent":""},"facebook_W.png":{"type":"file","fileName":"facebook_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_6=["img","Follow-me","github","github.svg","github_B.PNG","github_W.png","link.txt"]
folder2_5_6_dict={"img":"dir","Follow-me":"dir","github":"dir","github.svg":{"type":"file","fileName":"github.svg","fileContent":""},"github_B.PNG":{"type":"file","fileName":"github_B.PNG","fileContent":""},"github_W.png":{"type":"file","fileName":"github_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_7=["img","Follow-me","Instagram","instagram.svg","instagram_B.PNG","instagram_W.png","link.txt"]
folder2_5_7_dict={"img":"dir","Follow-me":"dir","Instagram":"dir","instagram.svg":{"type":"file","fileName":"instagram.svg","fileContent":""},"instagram_B.PNG":{"type":"file","fileName":"instagram_B.PNG","fileContent":""},"instagram_W.png":{"type":"file","fileName":"instagram_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""}}
folder2_5_8=["img","Follow-me","linkedin","lien.txt","linkedin.svg","linkedin_B.PNG","linkedin_W.png"]
folder2_5_8_dict={"img":"dir","Follow-me":"dir","linkedin":"dir","lien.txt":{"type":"file","fileName":"lien.txt","fileContent":""},"linkedin.svg":{"type":"file","fileName":"linkedin.svg","fileContent":""},"linkedin_B.PNG":{"type":"file","fileName":"linkedin_B.PNG","fileContent":""},"linkedin_W.png":{"type":"file","fileName":"linkedin_W.png","fileContent":""}}
folder2_5_9=["img","Follow-me","patreon","link.txt","patreon.svg","patreon_B.PNG","patreon_W.png"]
folder2_5_9_dict={"img":"dir","Follow-me":"dir","patreon":"dir","link.txt":{"type":"file","fileName":"link.txt","fileContent":""},"patreon.svg":{"type":"file","fileName":"patreon.svg","fileContent":""},"patreon_B.PNG":{"type":"file","fileName":"patreon_B.PNG","fileContent":""},"patreon_W.png":{"type":"file","fileName":"patreon_W.png","fileContent":""}}
folder2_5_10=["img","Follow-me","pinterest","pinterest.svg","pinterest_B.PNG","pinterest_W.png"]
folder2_5_10_dict={"img":"dir","Follow-me":"dir","pinterest":"dir","pinterest.svg":{"type":"file","fileName":"pinterest.svg","fileContent":""},"pinterest_B.PNG":{"type":"file","fileName":"pinterest_B.PNG","fileContent":""},"pinterest_W.png":{"type":"file","fileName":"pinterest_W.png","fileContent":""}}
folder2_5_11=["img","Follow-me","repl.it","favicon.ico","favicon.svg","favicon_W.png","link.txt","repl_it_B.PNG","repl_it_W.PNG"]
folder2_5_11_dict={"img":"dir","Follow-me":"dir","repl.it":"dir","favicon.ico":{"type":"file","fileName":"favicon.ico","fileContent":""},"favicon.svg":{"type":"file","fileName":"favicon.svg","fileContent":""},"favicon_W.png":{"type":"file","fileName":"favicon_W.png","fileContent":""},"link.txt":{"type":"file","fileName":"link.txt","fileContent":""},"repl_it_B.PNG":{"type":"file","fileName":"repl_it_B.PNG","fileContent":""},"repl_it_W.PNG":{"type":"file","fileName":"repl_it_W.PNG","fileContent":""},}
folder2_5_12=["img","Follow-me","snapchat","snapchat.svg","snapchat_B.PNG","snapchat_W.PNG"]
folder2_5_12_dict={"img":"dir","Follow-me":"dir","snapchat":"dir","snapchat.svg":{"type":"file","fileName":"snapchat.svg","fileContent":""},"snapchat_B.PNG":{"type":"file","fileName":"snapchat_B.PNG","fileContent":""},"snapchat_W.PNG":{"type":"file","fileName":"snapchat_W.PNG","fileContent":""}}
folder2_5_13=["img","Follow-me","sound-cloud","soundcloud.png","soundcloud.svg","soundcloud_B.PNG","soundcloud_W.png"]
folder2_5_13_dict={"img":"dir","Follow-me":"dir","sound-cloud":"dir","soundcloud.png":{"type":"file","fileName":"soundcloud.png","fileContent":""},"soundcloud.svg":{"type":"file","fileName":"soundcloud.svg","fileContent":""},"soundcloud_B.PNG":{"type":"file","fileName":"soundcloud_B.PNG","fileContent":""},"soundcloud_W.png":{"type":"file","fileName":"soundcloud_W.png","fileContent":""}}
folder2_5_14=["img","Follow-me","steam","link.txt","steam.svg","steam_B.PNG","steam_W.png"]
folder2_5_14_dict={"img":"dir","Follow-me":"dir","steam":"dir","link.txt":{"type":"file","fileName":"link.txt","fileContent":""},"steam.svg":{"type":"file","fileName":"steam.svg","fileContent":""},"steam_B.PNG":{"type":"file","fileName":"steam_B.PNG","fileContent":""},"steam_W.png":{"type":"file","fileName":"steam_W.png","fileContent":""}}
folder2_5_15=["img","Follow-me","tumblr","tumblr.svg","tumblr_B.PNG","tumblr_W.PNG"]
folder2_5_15_dict={"img":"dir","Follow-me":"dir","tumblr":"dir","tumblr.svg":{"type":"file","fileName":"tumblr.svg","fileContent":""},"tumblr_B.PNG":{"type":"file","fileName":"tumblr_B.PNG","fileContent":""},"tumblr_W.PNG":{"type":"file","fileName":"tumblr_W.PNG","fileContent":""}}
folder2_5_16=["img","Follow-me","yt","link to youtube svg.txt","youtube.svg","youtube_B.PNG","youtube_W.PNG"]
folder2_5_16_dict={"img":"dir","Follow-me":"dir","yt":"dir","link to youtube svg.txt":{"type":"file","fileName":"link to youtube svg.txt","fileContent":""},"youtube.svg":{"type":"file","fileName":"youtube.svg","fileContent":""},"youtube_B.PNG":{"type":"file","fileName":"youtube_B.PNG","fileContent":""},"youtube_W.PNG":{"type":"file","fileName":"youtube_W.PNG","fileContent":""}}
folder2_6=["img","ingame","accueil.png","accueilm.png","endv.png","mur.png","start.png","wolf_icon.ico","wolf_icon.png","funkyWalls","wall_beige_black.png","wall_beige_white.png","wall_birght_red_black.png","wall_birght_red_white.png","wall_black_white.png","wall_brigth_orange_black.png","wall_brigth_orange_white.png","wall_brigth_pink_black.png","wall_brigth_pink_white.png","wall_chocolat_black.png","wall_chocolat_white.png","wall_darks_red_black.png","wall_darks_red_white.png","wall_dark_blue_black.png","wall_dark_blue_white.png","wall_dark_green_black.png","wall_dark_green_white.png","wall_dark_purple_black.png","wall_dark_purple_white.png","wall_grey_black.png","wall_grey_white.png","wall_light_blue_black.png","wall_light_blue_white.png","wall_light_green_black.png","wall_light_green_white.png","wall_light_grey_black.png","wall_light_grey_white.png","wall_light_purple_black.png","wall_light_purple_white.png","wall_medium_blue_black.png","wall_medium_blue_white.png","wall_orange_black.png","wall_orange_white.png","wall_very_light_blue_black.png","wall_very_light_blue_white.png","wall_white.png","wall_yellow_black.png","wall_yellow_white.png","snipsets","bric.png","snipsets.zip","wall_beige.png","wall_birght_red.png","wall_black.png","wall_brigth_orange.png","wall_brigth_pink.png","wall_chocolat.png","wall_darks_red.png","wall_dark_blue.png","wall_dark_green.png","wall_dark_purple.png","wall_grey.png","wall_light_blue.png","wall_light_green.png","wall_light_grey.png","wall_light_purple.png","wall_medium_blue.png","wall_orange.png","wall_very_light_blue.png","wall_white.png","wall_wire_frame.png","wall_wire_frame_white.png","wall_wire_frame_white_red_bricks.png","wall_yellow.png"]
folder2_6_dict={"img":"dir","ingame":"dir","accueil.png":{"type":"file","fileName":"accueil.png","fileContent":""},"accueilm.png":{"type":"file","fileName":"accueilm.png","fileContent":""},"endv.png":{"type":"file","fileName":"endv.png","fileContent":""},"mur.png":{"type":"file","fileName":"mur.png","fileContent":""},"start.png":{"type":"file","fileName":"start.png","fileContent":""},"wolf_icon.ico":{"type":"file","fileName":"wolf_icon.ico","fileContent":""},"wolf_icon.png":{"type":"file","fileName":"wolf_icon.png","fileContent":""},"funkyWalls":"dir","wall_beige_black.png":{"type":"file","fileName":"wall_beige_black.png","fileContent":""},"wall_beige_white.png":{"type":"file","fileName":"wall_beige_white.png","fileContent":""},"wall_birght_red_black.png":{"type":"file","fileName":"wall_birght_red_black.png","fileContent":""},"wall_birght_red_white.png":{"type":"file","fileName":"wall_birght_red_white.png","fileContent":""},"wall_black_white.png":{"type":"file","fileName":"wall_black_white.png","fileContent":""},"wall_brigth_orange_black.png":{"type":"file","fileName":"wall_brigth_orange_black.png","fileContent":""},"wall_brigth_orange_white.png":{"type":"file","fileName":"wall_brigth_orange_white.png","fileContent":""},"wall_brigth_pink_black.png":{"type":"file","fileName":"wall_brigth_pink_black.png","fileContent":""},"wall_brigth_pink_white.png":{"type":"file","fileName":"wall_brigth_pink_white.png","fileContent":""},"wall_chocolat_black.png":{"type":"file","fileName":"wall_chocolat_black.png","fileContent":""},"wall_chocolat_white.png":{"type":"file","fileName":"wall_chocolat_white.png","fileContent":""},"wall_darks_red_black.png":{"type":"file","fileName":"wall_darks_red_black.png","fileContent":""},"wall_darks_red_white.png":{"type":"file","fileName":"wall_darks_red_white.png","fileContent":""},"wall_dark_blue_black.png":{"type":"file","fileName":"wall_dark_blue_black.png","fileContent":""},"wall_dark_blue_white.png":{"type":"file","fileName":"wall_dark_blue_white.png","fileContent":""},"wall_dark_green_black.png":{"type":"file","fileName":"wall_dark_green_black.png","fileContent":""},"wall_dark_green_white.png":{"type":"file","fileName":"wall_dark_green_white.png","fileContent":""},"wall_dark_purple_black.png":{"type":"file","fileName":"wall_dark_purple_black.png","fileContent":""},"wall_dark_purple_white.png":{"type":"file","fileName":"wall_dark_purple_white.png","fileContent":""},"wall_grey_black.png":{"type":"file","fileName":"wall_grey_black.png","fileContent":""},"wall_grey_white.png":{"type":"file","fileName":"wall_grey_white.png","fileContent":""},"wall_light_blue_black.png":{"type":"file","fileName":"wall_light_blue_black.png","fileContent":""},"wall_light_blue_white.png":{"type":"file","fileName":"wall_light_blue_white.png","fileContent":""},"wall_light_green_black.png":{"type":"file","fileName":"wall_light_green_black.png","fileContent":""},"wall_light_green_white.png":{"type":"file","fileName":"wall_light_green_white.png","fileContent":""},"wall_light_grey_black.png":{"type":"file","fileName":"wall_light_grey_black.png","fileContent":""},"wall_light_grey_white.png":{"type":"file","fileName":"wall_light_grey_white.png","fileContent":""},"wall_light_purple_black.png":{"type":"file","fileName":"wall_light_purple_black.png","fileContent":""},"wall_light_purple_white.png":{"type":"file","fileName":"wall_light_purple_white.png","fileContent":""},"wall_medium_blue_black.png":{"type":"file","fileName":"wall_medium_blue_black.png","fileContent":""},"wall_medium_blue_white.png":{"type":"file","fileName":"wall_medium_blue_white.png","fileContent":""},"wall_orange_black.png":{"type":"file","fileName":"wall_orange_black.png","fileContent":""},"wall_orange_white.png":{"type":"file","fileName":"wall_orange_white.png","fileContent":""},"wall_very_light_blue_black.png":{"type":"file","fileName":"wall_very_light_blue_black.png","fileContent":""},"wall_very_light_blue_white.png":{"type":"file","fileName":"wall_very_light_blue_white.png","fileContent":""},"wall_white.png":{"type":"file","fileName":"wall_white.png","fileContent":""},"wall_yellow_black.png":{"type":"file","fileName":"wall_yellow_black.png","fileContent":""},"wall_yellow_white.png":{"type":"file","fileName":"wall_yellow_white.png","fileContent":""},"snipsets":"dir","bric.png":{"type":"file","fileName":"bric.png","fileContent":""},"snipsets.zip":{"type":"file","fileName":"snipsets.zip","fileContent":""},"wall_beige.png":{"type":"file","fileName":"wall_beige.png","fileContent":""},"wall_birght_red.png":{"type":"file","fileName":"wall_birght_red.png","fileContent":""},"wall_black.png":{"type":"file","fileName":"wall_black.png","fileContent":""},"wall_brigth_orange.png":{"type":"file","fileName":"wall_brigth_orange.png","fileContent":""},"wall_brigth_pink.png":{"type":"file","fileName":"wall_brigth_pink.png","fileContent":""},"wall_chocolat.png":{"type":"file","fileName":"wall_chocolat.png","fileContent":""},"wall_darks_red.png":{"type":"file","fileName":"wall_darks_red.png","fileContent":""},"wall_dark_blue.png":{"type":"file","fileName":"wall_dark_blue.png","fileContent":""},"wall_dark_green.png":{"type":"file","fileName":"wall_dark_green.png","fileContent":""},"wall_dark_purple.png":{"type":"file","fileName":"wall_dark_purple.png","fileContent":""},"wall_grey.png":{"type":"file","fileName":"wall_grey.png","fileContent":""},"wall_light_blue.png":{"type":"file","fileName":"wall_light_blue.png","fileContent":""},"wall_light_green.png":{"type":"file","fileName":"wall_light_green.png","fileContent":""},"wall_light_grey.png":{"type":"file","fileName":"wall_light_grey.png","fileContent":""},"wall_light_purple.png":{"type":"file","fileName":"wall_light_purple.png","fileContent":""},"wall_medium_blue.png":{"type":"file","fileName":"wall_medium_blue.png","fileContent":""},"wall_orange.png":{"type":"file","fileName":"wall_orange.png","fileContent":""},"wall_very_light_blue.png":{"type":"file","fileName":"wall_very_light_blue.png","fileContent":""},"wall_white.png":{"type":"file","fileName":"wall_white.png","fileContent":""},"wall_wire_frame.png":{"type":"file","fileName":"wall_wire_frame.png","fileContent":""},"wall_wire_frame_white.png":{"type":"file","fileName":"wall_wire_frame_white.png","fileContent":""},"wall_wire_frame_white_red_bricks.png":{"type":"file","fileName":"wall_wire_frame_white_red_bricks.png","fileContent":""},"wall_yellow.png":{"type":"file","fileName":"wall_yellow.png","fileContent":""}}
folder2_7_1=["img","launch_load","menu_anim","acceuil.png","accueil_static_2.png"]
folder2_7_1_dict={"img":"dir","launch_load":"dir","menu_anim":"dir","accueil.png":{"type":"file","fileName":"accueil.png","fileContent":""},"accueil_static_2.png":{"type":"file","fileName":"accueil_static_2.png","fileContent":""}}
folder2_7_2=["img","launch_load","start_load","stages_stage_1.png","stages_stage_10.png","stages_stage_11.png","stages_stage_12.png","stages_stage_13.png","stages_stage_14.png","stages_stage_15.png","stages_stage_2.png","stages_stage_3.png","stages_stage_4.png","stages_stage_5.png","stages_stage_6.png","stages_stage_7.png","stages_stage_8.png","stages_stage_9.png","stages_stage_black.png"]
folder2_7_2_dict={"img":"dir","launch_load":"dir","start_load":"dir","stages_stage_1.png":{"type":"file","fileName":"stages_stage_1.png","fileContent":""},"stages_stage_10.png":{"type":"file","fileName":"stages_stage_10.png","fileContent":""},"stages_stage_11.png":{"type":"file","fileName":"stages_stage_11.png","fileContent":""},"stages_stage_12.png":{"type":"file","fileName":"stages_stage_12.png","fileContent":""},"stages_stage_13.png":{"type":"file","fileName":"stages_stage_13.png","fileContent":""},"stages_stage_14.png":{"type":"file","fileName":"stages_stage_14.png","fileContent":""},"stages_stage_15.png":{"type":"file","fileName":"stages_stage_15.png","fileContent":""},"stages_stage_2.png":{"type":"file","fileName":"stages_stage_2.png","fileContent":""},"stages_stage_3.png":{"type":"file","fileName":"stages_stage_3.png","fileContent":""},"stages_stage_4.png":{"type":"file","fileName":"stages_stage_4.png","fileContent":""},"stages_stage_5.png":{"type":"file","fileName":"stages_stage_5.png","fileContent":""},"stages_stage_6.png":{"type":"file","fileName":"stages_stage_6.png","fileContent":""},"stages_stage_7.png":{"type":"file","fileName":"stages_stage_7.png","fileContent":""},"stages_stage_8.png":{"type":"file","fileName":"stages_stage_8.png","fileContent":""},"stages_stage_9.png":{"type":"file","fileName":"stages_stage_9.png","fileContent":""},"stages_stage_black.png":{"type":"file","fileName":"stages_stage_black.png","fileContent":""}}
folder2_8_1=["img","sprite","famille","famille_loup_You_have_won.png","Mere et petits.png","understanding.PNG","w_fam.png"]
folder2_8_1_dict={"img":"dir","sprite":"dir","famille":"dir","famille_loup_You_have_won.png":{"type":"file","fileName":"famille_loup_You_have_won.png","fileContent":""},"Mere et petits.png":{"type":"file","fileName":"Mere et petits.png","fileContent":""},"understanding.PNG":{"type":"file","fileName":"understanding.PNG","fileContent":""},"w_fam.png":{"type":"file","fileName":"w_fam.png","fileContent":""}}
folder2_8_2=["img","sprite","gardien","Gardien_bas.png","Gardien_Droite.png","Gardien_Gauche.png","Gardien_haut.png"]
folder2_8_2_dict={"img":"dir","sprite":"dir","gardien":"dir","Gardien_bas.png":{"type":"file","fileName":"Gardien_bas.png","fileContent":""},"Gardien_Droite.png":{"type":"file","fileName":"Gardien_Droite.png","fileContent":""},"Gardien_Gauche.png":{"type":"file","fileName":"Gardien_Gauche.png","fileContent":""},"Gardien_haut.png":{"type":"file","fileName":"Gardien_haut.png","fileContent":""}}
folder2_8_3=["img","sprite","w","w_down.png","w_left.png","w_rigth.png","w_up.png"]
folder2_8_3_dict={"img":"dir","sprite":"dir","w":"dir","w_down.png":{"type":"file","fileName":"w_down.png","fileContent":""},"w_left.png":{"type":"file","fileName":"w_left.png","fileContent":""},"w_rigth.png":{"type":"file","fileName":"w_rigth.png","fileContent":""},"w_up.png":{"type":"file","fileName":"w_up.png","fileContent":""}}
folder2_9_1_1=["img","tut_image","alphabet","accents",";.PNG","à.PNG","â.PNG","Â_cap.PNG","ã.PNG","Ã_cap.PNG","ä.PNG","Ä_cap.PNG","ç.PNG","è.PNG","é.PNG","ê.PNG","Ê_cap.png","ë.PNG","Ë_cap.png","î.PNG","Î_cap.PNG","ï.PNG","Ï_cap.PNG","ñ.PNG","Ñ_cap.PNG","ô.PNG","Ô_cap.PNG","õ.PNG","Õ_cap.PNG","ö.PNG","Ö_cap.PNG","ù.PNG","û.PNG","Û_cap.PNG","ü.PNG","Ü_cap.PNG","ÿ.PNG"]
folder2_9_1_1_dict={"img":"dir","tut_image":"dir","alphabet":"dir","accents":"dir",";.PNG":{"type":"file","fileName":";.PNG","fileContent":""},"à.PNG":{"type":"file","fileName":"à.PNG","fileContent":""},"â.PNG":{"type":"file","fileName":"â.PNG","fileContent":""},"Â_cap.PNG":{"type":"file","fileName":"Â_cap.PNG","fileContent":""},"ã.PNG":{"type":"file","fileName":"ã.PNG","fileContent":""},"Ã_cap.PNG":{"type":"file","fileName":"Ã_cap.PNG","fileContent":""},"ä.PNG":{"type":"file","fileName":"ä.PNG","fileContent":""},"Ä_cap.PNG":{"type":"file","fileName":"Ä_cap.PNG","fileContent":""},"ç.PNG":{"type":"file","fileName":"ç.PNG","fileContent":""},"è.PNG":{"type":"file","fileName":"è.PNG","fileContent":""},"é.PNG":{"type":"file","fileName":"é.PNG","fileContent":""},"ê.PNG":{"type":"file","fileName":"ê.PNG","fileContent":""},"Ê_cap.png":{"type":"file","fileName":"Ê_cap.png","fileContent":""},"ë.PNG":{"type":"file","fileName":"ë.PNG","fileContent":""},"Ë_cap.png":{"type":"file","fileName":"Ë_cap.png","fileContent":""},"î.PNG":{"type":"file","fileName":"î.PNG","fileContent":""},"Î_cap.PNG":{"type":"file","fileName":"Î_cap.PNG","fileContent":""},"ï.PNG":{"type":"file","fileName":"ï.PNG","fileContent":""},"Ï_cap.PNG":{"type":"file","fileName":"Ï_cap.PNG","fileContent":""},"ñ.PNG":{"type":"file","fileName":"ñ.PNG","fileContent":""},"Ñ_cap.PNG":{"type":"file","fileName":"Ñ_cap.PNG","fileContent":""},"ô.PNG":{"type":"file","fileName":"ô.PNG","fileContent":""},"Ô_cap.PNG":{"type":"file","fileName":"Ô_cap.PNG","fileContent":""},"õ.PNG":{"type":"file","fileName":"õ.PNG","fileContent":""},"Õ_cap.PNG":{"type":"file","fileName":"Õ_cap.PNG","fileContent":""},"ö.PNG":{"type":"file","fileName":"ö.PNG","fileContent":""},"Ö_cap.PNG":{"type":"file","fileName":"Ö_cap.PNG","fileContent":""},"ù.PNG":{"type":"file","fileName":"ù.PNG","fileContent":""},"û.PNG":{"type":"file","fileName":"û.PNG","fileContent":""},"Û_cap.PNG":{"type":"file","fileName":"Û_cap.PNG","fileContent":""},"ü.PNG":{"type":"file","fileName":"ü.PNG","fileContent":""},"Ü_cap.PNG":{"type":"file","fileName":"Ü_cap.PNG","fileContent":""},"ÿ.PNG":{"type":"file","fileName":"ÿ.PNG","fileContent":""}}
folder2_9_1_2=["img","tut_image","alphabet","minuscule","ami.PNG","bmi.PNG","cmi.PNG","dmi.PNG","emi.PNG","fmi.PNG","gmi.PNG","hmi.PNG","imi.PNG","jmi.PNG","kmi.PNG","lmi.PNG","mmi.png","nmi.PNG","omi.PNG","pmi.PNG","qmi.PNG","rmi.PNG","smi.PNG","tmi.PNG","umi.PNG","vmi.png","wmi.PNG","xmi.PNG","ymi.PNG","zmi.PNG"]
folder2_9_1_2_dict={"img":"dir","tut_image":"dir","alphabet":"dir","minuscule":"dir","ami.PNG":{"type":"file","fileName":"ami.PNG","fileContent":""},"bmi.PNG":{"type":"file","fileName":"bmi.PNG","fileContent":""},"cmi.PNG":{"type":"file","fileName":"cmi.PNG","fileContent":""},"dmi.PNG":{"type":"file","fileName":"dmi.PNG","fileContent":""},"emi.PNG":{"type":"file","fileName":"emi.PNG","fileContent":""},"fmi.PNG":{"type":"file","fileName":"fmi.PNG","fileContent":""},"gmi.PNG":{"type":"file","fileName":"gmi.PNG","fileContent":""},"hmi.PNG":{"type":"file","fileName":"hmi.PNG","fileContent":""},"imi.PNG":{"type":"file","fileName":"imi.PNG","fileContent":""},"jmi.PNG":{"type":"file","fileName":"jmi.PNG","fileContent":""},"kmi.PNG":{"type":"file","fileName":"kmi.PNG","fileContent":""},"lmi.PNG":{"type":"file","fileName":"lmi.PNG","fileContent":""},"mmi.png":{"type":"file","fileName":"mmi.png","fileContent":""},"nmi.PNG":{"type":"file","fileName":"nmi.PNG","fileContent":""},"omi.PNG":{"type":"file","fileName":"omi.PNG","fileContent":""},"pmi.PNG":{"type":"file","fileName":"pmi.PNG","fileContent":""},"qmi.PNG":{"type":"file","fileName":"qmi.PNG","fileContent":""},"rmi.PNG":{"type":"file","fileName":"rmi.PNG","fileContent":""},"smi.PNG":{"type":"file","fileName":"smi.PNG","fileContent":""},"tmi.PNG":{"type":"file","fileName":"tmi.PNG","fileContent":""},"umi.PNG":{"type":"file","fileName":"umi.PNG","fileContent":""},"vmi.png":{"type":"file","fileName":"vmi.png","fileContent":""},"wmi.PNG":{"type":"file","fileName":"wmi.PNG","fileContent":""},"xmi.PNG":{"type":"file","fileName":"xmi.PNG","fileContent":""},"ymi.PNG":{"type":"file","fileName":"ymi.PNG","fileContent":""},"zmi.PNG":{"type":"file","fileName":"zmi.PNG","fileContent":""}}
folder2_9_1_3=["img","tut_image","alphabet","majuscule","3.PNG","7.PNG","ama.PNG","bma.PNG","cma.PNG","dma.PNG","ema.PNG","fma.PNG","gma.PNG","hma.PNG","ima.PNG","jma.PNG","kma.PNG","lma.PNG","mma.PNG","nma.PNG","oma.PNG","pma.PNG","qma.PNG","rma.PNG","sma.PNG","tma.PNG","uma.PNG","vma.PNG","wma.PNG","xma.PNG","yma.PNG","zma.PNG"]
folder2_9_1_3_dict={"img":"dir","tut_image":"dir","alphabet":"dir","majuscule":"dir","3.PNG":{"type":"file","fileName":"3.PNG","fileContent":""},"7.PNG":{"type":"file","fileName":"7.PNG","fileContent":""},"ama.PNG":{"type":"file","fileName":"ama.PNG","fileContent":""},"bma.PNG":{"type":"file","fileName":"bma.PNG","fileContent":""},"cma.PNG":{"type":"file","fileName":"cma.PNG","fileContent":""},"dma.PNG":{"type":"file","fileName":"dma.PNG","fileContent":""},"ema.PNG":{"type":"file","fileName":"ema.PNG","fileContent":""},"fma.PNG":{"type":"file","fileName":"fma.PNG","fileContent":""},"gma.PNG":{"type":"file","fileName":"gma.PNG","fileContent":""},"hma.PNG":{"type":"file","fileName":"hma.PNG","fileContent":""},"ima.PNG":{"type":"file","fileName":"ima.PNG","fileContent":""},"jma.PNG":{"type":"file","fileName":"jma.PNG","fileContent":""},"kma.PNG":{"type":"file","fileName":"kma.PNG","fileContent":""},"lma.PNG":{"type":"file","fileName":"lma.PNG","fileContent":""},"mma.PNG":{"type":"file","fileName":"mma.PNG","fileContent":""},"nma.PNG":{"type":"file","fileName":"nma.PNG","fileContent":""},"oma.PNG":{"type":"file","fileName":"oma.PNG","fileContent":""},"pma.PNG":{"type":"file","fileName":"pma.PNG","fileContent":""},"qma.PNG":{"type":"file","fileName":"qma.PNG","fileContent":""},"rma.PNG":{"type":"file","fileName":"rma.PNG","fileContent":""},"sma.PNG":{"type":"file","fileName":"sma.PNG","fileContent":""},"tma.PNG":{"type":"file","fileName":"tma.PNG","fileContent":""},"uma.PNG":{"type":"file","fileName":"uma.PNG","fileContent":""},"vma.PNG":{"type":"file","fileName":"vma.PNG","fileContent":""},"wma.PNG":{"type":"file","fileName":"wma.PNG","fileContent":""},"xma.PNG":{"type":"file","fileName":"xma.PNG","fileContent":""},"yma.PNG":{"type":"file","fileName":"yma.PNG","fileContent":""},"zma.PNG":{"type":"file","fileName":"zma.PNG","fileContent":""}}
folder2_9_1_4=["img","tut_image","alphabet","punctuation","and.PNG","at.PNG","border.png","bracketclosed.PNG","bracketopen.PNG","colum.PNG","dot.PNG","endboard.PNG","exclamation.PNG","paragraph.PNG","paragraph_fermé.PNG","paragraph_ouvert.PNG","questionmark.PNG","[.PNG","].PNG","æ.PNG"]
folder2_9_1_4_dict={"img":"dir","tut_image":"dir","alphabet":"dir","punctuation":"dir","and.PNG":{"type":"file","fileName":"and.PNG","fileContent":""},"at.PNG":{"type":"file","fileName":"at.PNG","fileContent":""},"border.png":{"type":"file","fileName":"border.png","fileContent":""},"bracketclosed.PNG":{"type":"file","fileName":"bracketclosed.PNG","fileContent":""},"bracketopen.PNG":{"type":"file","fileName":"bracketopen.PNG","fileContent":""},"colum.PNG":{"type":"file","fileName":"colum.PNG","fileContent":""},"dot.PNG":{"type":"file","fileName":"dot.PNG","fileContent":""},"endboard.PNG":{"type":"file","fileName":"endboard.PNG","fileContent":""},"exclamation.PNG":{"type":"file","fileName":"exclamation.PNG","fileContent":""},"paragraph.PNG":{"type":"file","fileName":"paragraph.PNG","fileContent":""},"paragraph_fermé.PNG":{"type":"file","fileName":"paragraph_fermé.PNG","fileContent":""},"paragraph_ouvert.PNG":{"type":"file","fileName":"paragraph_ouvert.PNG","fileContent":""},"questionmark.PNG":{"type":"file","fileName":"questionmark.PNG","fileContent":""},"[.PNG":{"type":"file","fileName":"[.PNG","fileContent":""},"].PNG":{"type":"file","fileName":"].PNG","fileContent":""},"æ.PNG":{"type":"file","fileName":"æ.PNG","fileContent":""}}
folder2_9_1_5=["img","tut_image","alphabet","temperature","celsius.PNG","fahraneit.PNG"]
folder2_9_1_5_dict={"img":"dir","tut_image":"dir","alphabet":"dir","temperature":"dir","celsius.PNG":{"type":"file","fileName":"celsius.PNG","fileContent":""},"fahraneit.PNG":{"type":"file","fileName":"fahraneit.PNG","fileContent":""}}
folder2_9_2=["img","tut_image","arrow","adown.png","aleft.png","aright.png","aup.png"]
folder2_9_2_dict={"img":"dir","tut_image":"dir","arrow":"dir","adown.png":{"type":"file","fileName":"adown.png","fileContent":""},"aleft.png":{"type":"file","fileName":"aleft.png","fileContent":""},"aright.png":{"type":"file","fileName":"aright.png","fileContent":""},"aup.png":{"type":"file","fileName":"aup.png","fileContent":""}}
folder2_9_3=["img","tut_image","currency","dollard.PNG","euro.PNG","pound.PNG","wan.PNG","yen.PNG"]
folder2_9_3_dict={"img":"dir","tut_image":"dir","currency":"dir","dollard.PNG":{"type":"file","fileName":"dollard.PNG","fileContent":""},"euro.PNG":{"type":"file","fileName":"euro.PNG","fileContent":""},"pound.PNG":{"type":"file","fileName":"pound.PNG","fileContent":""},"wan.PNG":{"type":"file","fileName":"wan.PNG","fileContent":""},"yen.PNG":{"type":"file","fileName":"yen.PNG","fileContent":""}}
folder2_9_4=["img","tut_image","heart","heartbig.png","heartsmall.png"]
folder2_9_4_dict={"img":"dir","tut_image":"dir","heart":"dir","heartbig.png":{"type":"file","fileName":"heartbig.png","fileContent":""},"heartsmall.png":{"type":"file","fileName":"heartsmall.png","fileContent":""}}
folder2_9_5=["img","tut_image","math","%.PNG","+.PNG","-.PNG","=.PNG","diviser.PNG","lessthan.PNG","morethan.PNG","times.PNG"]
folder2_9_5_dict={"img":"dir","tut_image":"dir","math":"dir","%.PNG":{"type":"file","fileName":"%.PNG","fileContent":""},"+.PNG":{"type":"file","fileName":"+.PNG","fileContent":""},"-.PNG":{"type":"file","fileName":"-.PNG","fileContent":""},"=.PNG":{"type":"file","fileName":"=.PNG","fileContent":""},"diviser.PNG":{"type":"file","fileName":"diviser.PNG","fileContent":""},"lessthan.PNG":{"type":"file","fileName":"lessthan.PNG","fileContent":""},"morethan.PNG":{"type":"file","fileName":"morethan.PNG","fileContent":""},"times.PNG":{"type":"file","fileName":"times.PNG","fileContent":""}}
folder2_9_6=["img","tut_image","numbers","0.PNG","1.PNG","2.PNG","3.PNG","4.PNG","5.PNG","6.PNG","7.PNG","8.PNG","9.PNG"]
folder2_9_6_dict={"img":"dir","tut_image":"dir","numbers":"dir","0.PNG":{"type":"file","fileName":"0.PNG","fileContent":""},"1.PNG":{"type":"file","fileName":"1.PNG","fileContent":""},"2.PNG":{"type":"file","fileName":"2.PNG","fileContent":""},"3.PNG":{"type":"file","fileName":"3.PNG","fileContent":""},"4.PNG":{"type":"file","fileName":"4.PNG","fileContent":""},"5.PNG":{"type":"file","fileName":"5.PNG","fileContent":""},"6.PNG":{"type":"file","fileName":"6.PNG","fileContent":""},"7.PNG":{"type":"file","fileName":"7.PNG","fileContent":""},"8.PNG":{"type":"file","fileName":"8.PNG","fileContent":""},"9.PNG":{"type":"file","fileName":"9.PNG","fileContent":""}}
folder3=["levels","001_l1","002_l2","003_l3","004_l4","005_l5","006_l6","007_l7","008_l8"]
folder3_dict={"levels":"dir","001_l1":{"type":"file","fileName":"001_l1","fileContent":""},"002_l2":{"type":"file","fileName":"002_l2","fileContent":""},"003_l3":{"type":"file","fileName":"003_l3","fileContent":""},"004_l4":{"type":"file","fileName":"004_l4","fileContent":""},"005_l5":{"type":"file","fileName":"005_l5","fileContent":""},"006_l6":{"type":"file","fileName":"006_l6","fileContent":""},"007_l7":{"type":"file","fileName":"007_l7","fileContent":""},"008_l8":{"type":"file","fileName":"008_l8","fileContent":""}}
print("initialising links")


main_for_rec=[folder1,folder2_2,folder2_3,folder2_4,folder2_5_1,folder2_5_2,folder2_5_3,folder2_5_4,folder2_5_5,folder2_5_6,folder2_5_7,folder2_5_8,folder2_5_9,folder2_5_10,folder2_5_11,folder2_5_12,folder2_5_13,folder2_5_14,folder2_5_15,folder2_5_16,folder2_6,folder2_7_1,folder2_7_2,folder2_8_1,folder2_8_2,folder2_8_3,folder2_9_1_1,folder2_9_1_2,folder2_9_1_3,folder2_9_1_4,folder2_9_1_5,folder2_9_2,folder2_9_3,folder2_9_4,folder2_9_5,folder2_9_6,folder3]
main_for_rec_dict=[folder1_dict,folder2_2_dict,folder2_3_dict,folder2_4_dict,folder2_5_1_dict,folder2_5_2_dict,folder2_5_3_dict,folder2_5_4_dict,folder2_5_5_dict,folder2_5_6_dict,folder2_5_7_dict,folder2_5_8_dict,folder2_5_9_dict,folder2_5_10_dict,folder2_5_11_dict,folder2_5_12_dict,folder2_5_13_dict,folder2_5_14_dict,folder2_5_15_dict,folder2_5_16_dict,folder2_6_dict,folder2_7_1_dict,folder2_7_2_dict,folder2_8_1_dict,folder2_8_2_dict,folder2_8_3_dict,folder2_9_1_1_dict,folder2_9_1_2_dict,folder2_9_1_3_dict,folder2_9_1_4_dict,folder2_9_1_5_dict,folder2_9_2_dict,folder2_9_3_dict,folder2_9_4_dict,folder2_9_5_dict,folder2_9_6_dict,folder3_dict]

RI=boot(main=main_for_rec,main_dict=main_for_rec_dict,links=[])
RI.folder1=folder1
RI.folder1_dict=folder1_dict
print(folder1)
print(folder1_dict)
links1=boot.get.make_links(folder1_dict)
# print(f"\n##############################################\nlinks1={links1}\n##############################################\n")
links2_2=boot.get.make_links(folder2_2_dict)
links2_3=boot.get.make_links(folder2_3_dict)
links2_4=boot.get.make_links(folder2_4_dict)
links2_5_1=boot.get.make_links(folder2_5_1_dict)
links2_5_2=boot.get.make_links(folder2_5_2_dict)
links2_5_3=boot.get.make_links(folder2_5_3_dict)
links2_5_4=boot.get.make_links(folder2_5_4_dict)
links2_5_5=boot.get.make_links(folder2_5_5_dict)
links2_5_6=boot.get.make_links(folder2_5_6_dict)
links2_5_7=boot.get.make_links(folder2_5_7_dict)
links2_5_8=boot.get.make_links(folder2_5_8_dict)
links2_5_9=boot.get.make_links(folder2_5_9_dict)
links2_5_10=boot.get.make_links(folder2_5_10_dict)
links2_5_11=boot.get.make_links(folder2_5_11_dict)
links2_5_12=boot.get.make_links(folder2_5_12_dict)
links2_5_13=boot.get.make_links(folder2_5_13_dict)
links2_5_14=boot.get.make_links(folder2_5_14_dict)
links2_5_15=boot.get.make_links(folder2_5_15_dict)
links2_5_16=boot.get.make_links(folder2_5_16_dict)
links2_6=boot.get.make_links(folder2_6_dict)
links2_7_1=boot.get.make_links(folder2_7_1_dict)
links2_7_2=boot.get.make_links(folder2_7_2_dict)
links2_8_1=boot.get.make_links(folder2_8_1_dict)
links2_8_2=boot.get.make_links(folder2_8_2_dict)
links2_8_3=boot.get.make_links(folder2_8_3_dict)
links2_9_1_1=boot.get.make_links(folder2_9_1_1_dict)
links2_9_1_2=boot.get.make_links(folder2_9_1_2_dict)
links2_9_1_3=boot.get.make_links(folder2_9_1_3_dict)
links2_9_1_4=boot.get.make_links(folder2_9_1_4_dict)
links2_9_1_5=boot.get.make_links(folder2_9_1_5_dict)
links2_9_2=boot.get.make_links(folder2_9_2_dict)
links2_9_3=boot.get.make_links(folder2_9_3_dict)
links2_9_4=boot.get.make_links(folder2_9_4_dict)
links2_9_5=boot.get.make_links(folder2_9_5_dict)
links2_9_6=boot.get.make_links(folder2_9_6_dict)
links3=boot.get.make_links(folder3_dict)
print(f"links3={links3}\nfolder3_dict={folder3_dict}\nfolder3={folder3}")
print("links initialised")
main_links=[links1,links2_2,links2_3,links2_4,links2_5_1,links2_5_2,links2_5_3,links2_5_4,links2_5_5,links2_5_6,links2_5_7,links2_5_8,links2_5_9,links2_5_10,links2_5_11,links2_5_12,links2_5_13,links2_5_14,links2_5_15,links2_5_16,links2_6,links2_7_1,links2_7_2,links2_8_1,links2_8_2,links2_8_3,links2_9_1_1,links2_9_1_2,links2_9_1_3,links2_9_1_4,links2_9_1_5,links2_9_2,links2_9_3,links2_9_4,links2_9_5,links2_9_6,links3]
RI.links=main_links
print("Getting content")
print(boot.get.content(list1=RI.main,list2=RI.main_dict,links=RI.links,home=f"{RI.home}{RI.file_location}"))
i,b=0,2
print(f"list2[{i}][list1[{i}][{b}]]={RI.main_dict[i][RI.main[i][b]]}")
print("writing info")
# f=open("downloaded_results.txt","w")
# f.write(f"{main_for_rec}")
# f.write("\n")
# f.write(f"{main_for_rec_dict}")
# f.write("\n")
# f.write(f"{main_links}")
# f.write("\nCreated by Henry Letellier")
# f.close()
print("[DONE]")
pause=input("Press enter to continue...")
print(f"RI.list_dict={RI.list_dict}")
pause=input("Press enter to continue...")