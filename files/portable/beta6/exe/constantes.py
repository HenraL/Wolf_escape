from string import ascii_letters
# from string import digits
# from string import punctuation

from pygame.constants import *

""" Booting up, initialising vars to ensure the required files exist before we start the game."""

folder1=["elementary_levels","002_l2","003_l3","004_l4","005_l5","credits","h","I","M","m1","m2","P"]
folder1_dict={"elementary_levels":{'type': 'dir', 'fileName': 'elementary_levels'},"002_l2":{"type":"file","fileName":"002_l2","fileContent":""},"003_l3":{"type":"file","fileName":"003_l3","fileContent":""},"004_l4":{"type":"file","fileName":"004_l4","fileContent":""},"005_l5":{"type":"file","fileName":"005_l5","fileContent":""},"credits":{"type":"file","fileName":"credits","fileContent":""},"h":{"type":"file","fileName":"h","fileContent":""},"I":{"type":"file","fileName":"I","fileContent":""},"M":{"type":"file","fileName":"M","fileContent":""},"m1":{"type":"file","fileName":"m1","fileContent":""},"m2":{"type":"file","fileName":"m2","fileContent":""},"P":{"type":"file","fileName":"P","fileContent":""}}
folder2_2=["img","background","fonds.png"]
folder2_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'background': {'type': 'dir', 'fileName': 'background'}, 'fonds.png': {'type': 'file', 'fileName': 'fonds.png', 'fileContent': ''}}
folder2_3=["img","Credits","end - Copie.PNG","watermark_background - Copie.png"]
folder2_3_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Credits': {'type': 'dir', 'fileName': 'Credits'}, 'end - Copie.PNG': {'type': 'file', 'fileName': 'end - Copie.PNG', 'fileContent': ''}, 'watermark_background - Copie.png': {'type': 'file', 'fileName': 'watermark_background - Copie.png', 'fileContent': ''}}
folder2_4=["img","end","endv.png"]
folder2_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'end': {'type': 'dir', 'fileName': 'end'}, 'endv.png': {'type': 'file', 'fileName': 'endv.png', 'fileContent': ''}}
folder2_5_1=["img","Follow-me","Behance","behance.svg","behance_b.PNG","behance_w.PNG"]
folder2_5_1_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'Behance': {'type': 'dir', 'fileName': 'Behance'}, 'behance.svg': {'type': 'file', 'fileName': 'behance.svg', 'fileContent': ''}, 'behance_b.PNG': {'type': 'file', 'fileName': 'behance_b.PNG', 'fileContent': ''}, 'behance_w.PNG': {'type': 'file', 'fileName': 'behance_w.PNG', 'fileContent': ''}}
folder2_5_2=["img","Follow-me","codepen","codepen.svg","codepen_b.PNG","codepen_w.PNG","link.txt"]
folder2_5_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'codepen': {'type': 'dir', 'fileName': 'codepen'}, 'codepen.svg': {'type': 'file', 'fileName': 'codepen.svg', 'fileContent': ''}, 'codepen_b.PNG': {'type': 'file', 'fileName': 'codepen_b.PNG', 'fileContent': ''}, 'codepen_w.PNG': {'type': 'file', 'fileName': 'codepen_w.PNG', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_3=["img","Follow-me","dev-to","dev-to.svg","dev-to_B.PNG","dev-to_W.png","link.txt"]
folder2_5_3_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'dev-to': {'type': 'dir', 'fileName': 'dev-to'}, 'dev-to.svg': {'type': 'file', 'fileName': 'dev-to.svg', 'fileContent': ''}, 'dev-to_B.PNG': {'type': 'file', 'fileName': 'dev-to_B.PNG', 'fileContent': ''}, 'dev-to_W.png': {'type': 'file', 'fileName': 'dev-to_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_4=["img","Follow-me","discord","discord.svg","discord_B.PNG","discord_W.png","link.txt"]
folder2_5_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'discord': {'type': 'dir', 'fileName': 'discord'}, 'discord.svg': {'type': 'file', 'fileName': 'discord.svg', 'fileContent': ''}, 'discord_B.PNG': {'type': 'file', 'fileName': 'discord_B.PNG', 'fileContent': ''}, 'discord_W.png': {'type': 'file', 'fileName': 'discord_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_5=["img","Follow-me","facebook","facebook.svg","facebook_B.PNG","facebook_W.png","link.txt"]
folder2_5_5_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'facebook': {'type': 'dir', 'fileName': 'facebook'}, 'facebook.svg': {'type': 'file', 'fileName': 'facebook.svg', 'fileContent': ''}, 'facebook_B.PNG': {'type': 'file', 'fileName': 'facebook_B.PNG', 'fileContent': ''}, 'facebook_W.png': {'type': 'file', 'fileName': 'facebook_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_6=["img","Follow-me","github","github.svg","github_B.PNG","github_W.png","link.txt"]
folder2_5_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'github': {'type': 'dir', 'fileName': 'github'}, 'github.svg': {'type': 'file', 'fileName': 'github.svg', 'fileContent': ''}, 'github_B.PNG': {'type': 'file', 'fileName': 'github_B.PNG', 'fileContent': ''}, 'github_W.png': {'type': 'file', 'fileName': 'github_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_7=["img","Follow-me","Instagram","instagram.svg","instagram_B.PNG","instagram_W.png","link.txt"]
folder2_5_7_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'Instagram': {'type': 'dir', 'fileName': 'Instagram'}, 'instagram.svg': {'type': 'file', 'fileName': 'instagram.svg', 'fileContent': ''}, 'instagram_B.PNG': {'type': 'file', 'fileName': 'instagram_B.PNG', 'fileContent': ''}, 'instagram_W.png': {'type': 'file', 'fileName': 'instagram_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}}
folder2_5_8=["img","Follow-me","linkedin","lien.txt","linkedin.svg","linkedin_B.PNG","linkedin_W.png"]
folder2_5_8_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'linkedin': {'type': 'dir', 'fileName': 'linkedin'}, 'lien.txt': {'type': 'file', 'fileName': 'lien.txt', 'fileContent': ''}, 'linkedin.svg': {'type': 'file', 'fileName': 'linkedin.svg', 'fileContent': ''}, 'linkedin_B.PNG': {'type': 'file', 'fileName': 'linkedin_B.PNG', 'fileContent': ''}, 'linkedin_W.png': {'type': 'file', 'fileName': 'linkedin_W.png', 'fileContent': ''}}
folder2_5_9=["img","Follow-me","patreon","link.txt","patreon.svg","patreon_B.PNG","patreon_W.png"]
folder2_5_9_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'patreon': {'type': 'dir', 'fileName': 'patreon'}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}, 'patreon.svg': {'type': 'file', 'fileName': 'patreon.svg', 'fileContent': ''}, 'patreon_B.PNG': {'type': 'file', 'fileName': 'patreon_B.PNG', 'fileContent': ''}, 'patreon_W.png': {'type': 'file', 'fileName': 'patreon_W.png', 'fileContent': ''}}
folder2_5_10=["img","Follow-me","pinterest","pinterest.svg","pinterest_B.PNG","pinterest_W.png"]
folder2_5_10_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'pinterest': {'type': 'dir', 'fileName': 'pinterest'}, 'pinterest.svg': {'type': 'file', 'fileName': 'pinterest.svg', 'fileContent': ''}, 'pinterest_B.PNG': {'type': 'file', 'fileName': 'pinterest_B.PNG', 'fileContent': ''}, 'pinterest_W.png': {'type': 'file', 'fileName': 'pinterest_W.png', 'fileContent': ''}}
folder2_5_11=["img","Follow-me","repl.it","favicon.ico","favicon.svg","favicon_W.png","link.txt","repl_it_B.PNG","repl_it_W.PNG"]
folder2_5_11_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'repl.it': {'type': 'dir', 'fileName': 'repl.it'}, 'favicon.ico': {'type': 'file', 'fileName': 'favicon.ico', 'fileContent': ''}, 'favicon.svg': {'type': 'file', 'fileName': 'favicon.svg', 'fileContent': ''}, 'favicon_W.png': {'type': 'file', 'fileName': 'favicon_W.png', 'fileContent': ''}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}, 'repl_it_B.PNG': {'type': 'file', 'fileName': 'repl_it_B.PNG', 'fileContent': ''}, 'repl_it_W.PNG': {'type': 'file', 'fileName': 'repl_it_W.PNG', 'fileContent': ''}}
folder2_5_12=["img","Follow-me","snapchat","snapchat.svg","snapchat_B.PNG","snapchat_W.PNG"]
folder2_5_12_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'snapchat': {'type': 'dir', 'fileName': 'snapchat'}, 'snapchat.svg': {'type': 'file', 'fileName': 'snapchat.svg', 'fileContent': ''}, 'snapchat_B.PNG': {'type': 'file', 'fileName': 'snapchat_B.PNG', 'fileContent': ''}, 'snapchat_W.PNG': {'type': 'file', 'fileName': 'snapchat_W.PNG', 'fileContent': ''}}
folder2_5_13=["img","Follow-me","sound-cloud","soundcloud.png","soundcloud.svg","soundcloud_B.PNG","soundcloud_W.png"]
folder2_5_13_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'sound-cloud': {'type': 'dir', 'fileName': 'sound-cloud'}, 'soundcloud.png': {'type': 'file', 'fileName': 'soundcloud.png', 'fileContent': ''}, 'soundcloud.svg': {'type': 'file', 'fileName': 'soundcloud.svg', 'fileContent': ''}, 'soundcloud_B.PNG': {'type': 'file', 'fileName': 'soundcloud_B.PNG', 'fileContent': ''}, 'soundcloud_W.png': {'type': 'file', 'fileName': 'soundcloud_W.png', 'fileContent': ''}}
folder2_5_14=["img","Follow-me","steam","link.txt","steam.svg","steam_B.PNG","steam_W.png"]
folder2_5_14_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'steam': {'type': 'dir', 'fileName': 'steam'}, 'link.txt': {'type': 'file', 'fileName': 'link.txt', 'fileContent': ''}, 'steam.svg': {'type': 'file', 'fileName': 'steam.svg', 'fileContent': ''}, 'steam_B.PNG': {'type': 'file', 'fileName': 'steam_B.PNG', 'fileContent': ''}, 'steam_W.png': {'type': 'file', 'fileName': 'steam_W.png', 'fileContent': ''}}
folder2_5_15=["img","Follow-me","tumblr","tumblr.svg","tumblr_B.PNG","tumblr_W.PNG"]
folder2_5_15_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'tumblr': {'type': 'dir', 'fileName': 'tumblr'}, 'tumblr.svg': {'type': 'file', 'fileName': 'tumblr.svg', 'fileContent': ''}, 'tumblr_B.PNG': {'type': 'file', 'fileName': 'tumblr_B.PNG', 'fileContent': ''}, 'tumblr_W.PNG': {'type': 'file', 'fileName': 'tumblr_W.PNG', 'fileContent': ''}}
folder2_5_16=["img","Follow-me","yt","link to youtube svg.txt","youtube.svg","youtube_B.PNG","youtube_W.PNG"]
folder2_5_16_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'Follow-me': {'type': 'dir', 'fileName': 'Follow-me'}, 'yt': {'type': 'dir', 'fileName': 'yt'}, 'link to youtube svg.txt': {'type': 'file', 'fileName': 'link to youtube svg.txt', 'fileContent': ''}, 'youtube.svg': {'type': 'file', 'fileName': 'youtube.svg', 'fileContent': ''}, 'youtube_B.PNG': {'type': 'file', 'fileName': 'youtube_B.PNG', 'fileContent': ''}, 'youtube_W.PNG': {'type': 'file', 'fileName': 'youtube_W.PNG', 'fileContent': ''}}
folder2_6=["img","ingame","accueil.png","accueilm.png","endv.png","mur.png","start.png","teller_start.png","wolf_icon.ico","wolf_icon.png","funkyWalls","wall_beige_black.png","wall_beige_white.png","wall_birght_red_black.png","wall_birght_red_white.png","wall_black_white.png","wall_brigth_orange_black.png","wall_brigth_orange_white.png","wall_brigth_pink_black.png","wall_brigth_pink_white.png","wall_chocolat_black.png","wall_chocolat_white.png","wall_darks_red_black.png","wall_darks_red_white.png","wall_dark_blue_black.png","wall_dark_blue_white.png","wall_dark_green_black.png","wall_dark_green_white.png","wall_dark_purple_black.png","wall_dark_purple_white.png","wall_grey_black.png","wall_grey_white.png","wall_light_blue_black.png","wall_light_blue_white.png","wall_light_green_black.png","wall_light_green_white.png","wall_light_grey_black.png","wall_light_grey_white.png","wall_light_purple_black.png","wall_light_purple_white.png","wall_medium_blue_black.png","wall_medium_blue_white.png","wall_orange_black.png","wall_orange_white.png","wall_very_light_blue_black.png","wall_very_light_blue_white.png","wall_yellow_black.png","wall_yellow_white.png","snipsets","bric.png","snipsets.zip","wall_beige.png","wall_birght_red.png","wall_black.png","wall_brigth_orange.png","wall_brigth_pink.png","wall_chocolat.png","wall_darks_red.png","wall_dark_blue.png","wall_dark_green.png","wall_dark_purple.png","wall_grey.png","wall_light_blue.png","wall_light_green.png","wall_light_grey.png","wall_light_purple.png","wall_medium_blue.png","wall_orange.png","wall_very_light_blue.png","wall_wire_frame.png","wall_wire_frame_white.png","wall_wire_frame_white_red_bricks.png","wall_yellow.png","wall_white.png"]#
folder2_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'ingame': {'type': 'dir', 'fileName': 'ingame'}, 'accueil.png': {'type': 'file', 'fileName': 'accueil.png', 'fileContent': ''}, 'accueilm.png': {'type': 'file', 'fileName': 'accueilm.png', 'fileContent': ''}, 'endv.png': {'type': 'file', 'fileName': 'endv.png', 'fileContent': ''}, 'mur.png': {'type': 'file', 'fileName': 'mur.png', 'fileContent': ''}, 'start.png': {'type': 'file', 'fileName': 'start.png', 'fileContent': ''}, "teller_start.png":{"type":"file","fileName":"teller_start.png","fileContent":""}, 'wolf_icon.ico': {'type': 'file', 'fileName': 'wolf_icon.ico', 'fileContent': ''}, 'wolf_icon.png': {'type': 'file', 'fileName': 'wolf_icon.png', 'fileContent': ''}, 'funkyWalls': {'type': 'dir', 'fileName': 'funkyWalls'}, 'wall_beige_black.png': {'type': 'file', 'fileName': 'wall_beige_black.png', 'fileContent': ''}, 'wall_beige_white.png': {'type': 'file', 'fileName': 'wall_beige_white.png', 'fileContent': ''}, 'wall_birght_red_black.png': {'type': 'file', 'fileName': 'wall_birght_red_black.png', 'fileContent': ''}, 'wall_birght_red_white.png': {'type': 'file', 'fileName': 'wall_birght_red_white.png', 'fileContent': ''}, 'wall_black_white.png': {'type': 'file', 'fileName': 'wall_black_white.png', 'fileContent': ''}, 'wall_brigth_orange_black.png': {'type': 'file', 'fileName': 'wall_brigth_orange_black.png', 'fileContent': ''}, 'wall_brigth_orange_white.png': {'type': 'file', 'fileName': 'wall_brigth_orange_white.png', 'fileContent': ''}, 'wall_brigth_pink_black.png': {'type': 'file', 'fileName': 'wall_brigth_pink_black.png', 'fileContent': ''}, 'wall_brigth_pink_white.png': {'type': 'file', 'fileName': 'wall_brigth_pink_white.png', 'fileContent': ''}, 'wall_chocolat_black.png': {'type': 'file', 'fileName': 'wall_chocolat_black.png', 'fileContent': ''}, 'wall_chocolat_white.png': {'type': 'file', 'fileName': 'wall_chocolat_white.png', 'fileContent': ''}, 'wall_darks_red_black.png': {'type': 'file', 'fileName': 'wall_darks_red_black.png', 'fileContent': ''}, 'wall_darks_red_white.png': {'type': 'file', 'fileName': 'wall_darks_red_white.png', 'fileContent': ''}, 'wall_dark_blue_black.png': {'type': 'file', 'fileName': 'wall_dark_blue_black.png', 'fileContent': ''}, 'wall_dark_blue_white.png': {'type': 'file', 'fileName': 'wall_dark_blue_white.png', 'fileContent': ''}, 'wall_dark_green_black.png': {'type': 'file', 'fileName': 'wall_dark_green_black.png', 'fileContent': ''}, 'wall_dark_green_white.png': {'type': 'file', 'fileName': 'wall_dark_green_white.png', 'fileContent': ''}, 'wall_dark_purple_black.png': {'type': 'file', 'fileName': 'wall_dark_purple_black.png', 'fileContent': ''}, 'wall_dark_purple_white.png': {'type': 'file', 'fileName': 'wall_dark_purple_white.png', 'fileContent': ''}, 'wall_grey_black.png': {'type': 'file', 'fileName': 'wall_grey_black.png', 'fileContent': ''}, 'wall_grey_white.png': {'type': 'file', 'fileName': 'wall_grey_white.png', 'fileContent': ''}, 'wall_light_blue_black.png': {'type': 'file', 'fileName': 'wall_light_blue_black.png', 'fileContent': ''}, 'wall_light_blue_white.png': {'type': 'file', 'fileName': 'wall_light_blue_white.png', 'fileContent': ''}, 'wall_light_green_black.png': {'type': 'file', 'fileName': 'wall_light_green_black.png', 'fileContent': ''}, 'wall_light_green_white.png': {'type': 'file', 'fileName': 'wall_light_green_white.png', 'fileContent': ''}, 'wall_light_grey_black.png': {'type': 'file', 'fileName': 'wall_light_grey_black.png', 'fileContent': ''}, 'wall_light_grey_white.png': {'type': 'file', 'fileName': 'wall_light_grey_white.png', 'fileContent': ''}, 'wall_light_purple_black.png': {'type': 'file', 'fileName': 'wall_light_purple_black.png', 'fileContent': ''}, 'wall_light_purple_white.png': {'type': 'file', 'fileName': 'wall_light_purple_white.png', 'fileContent': ''}, 'wall_medium_blue_black.png': {'type': 'file', 'fileName': 'wall_medium_blue_black.png', 'fileContent': ''}, 'wall_medium_blue_white.png': {'type': 'file', 'fileName': 'wall_medium_blue_white.png', 'fileContent': ''}, 'wall_orange_black.png': {'type': 'file', 'fileName': 'wall_orange_black.png', 'fileContent': ''}, 'wall_orange_white.png': {'type': 'file', 'fileName': 'wall_orange_white.png', 'fileContent': ''}, 'wall_very_light_blue_black.png': {'type': 'file', 'fileName': 'wall_very_light_blue_black.png', 'fileContent': ''}, 'wall_very_light_blue_white.png': {'type': 'file', 'fileName': 'wall_very_light_blue_white.png', 'fileContent': ''}, 'wall_yellow_black.png': {'type': 'file', 'fileName': 'wall_yellow_black.png', 'fileContent': ''}, 'wall_yellow_white.png': {'type': 'file', 'fileName': 'wall_yellow_white.png', 'fileContent': ''}, 'snipsets': {'type': 'dir', 'fileName': 'snipsets'}, 'bric.png': {'type': 'file', 'fileName': 'bric.png', 'fileContent': ''}, 'snipsets.zip': {'type': 'file', 'fileName': 'snipsets.zip', 'fileContent': ''}, 'wall_beige.png': {'type': 'file', 'fileName': 'wall_beige.png', 'fileContent': ''}, 'wall_birght_red.png': {'type': 'file', 'fileName': 'wall_birght_red.png', 'fileContent': ''}, 'wall_black.png': {'type': 'file', 'fileName': 'wall_black.png', 'fileContent': ''}, 'wall_brigth_orange.png': {'type': 'file', 'fileName': 'wall_brigth_orange.png', 'fileContent': ''}, 'wall_brigth_pink.png': {'type': 'file', 'fileName': 'wall_brigth_pink.png', 'fileContent': ''}, 'wall_chocolat.png': {'type': 'file', 'fileName': 'wall_chocolat.png', 'fileContent': ''}, 'wall_darks_red.png': {'type': 'file', 'fileName': 'wall_darks_red.png', 'fileContent': ''}, 'wall_dark_blue.png': {'type': 'file', 'fileName': 'wall_dark_blue.png', 'fileContent': ''}, 'wall_dark_green.png': {'type': 'file', 'fileName': 'wall_dark_green.png', 'fileContent': ''}, 'wall_dark_purple.png': {'type': 'file', 'fileName': 'wall_dark_purple.png', 'fileContent': ''}, 'wall_grey.png': {'type': 'file', 'fileName': 'wall_grey.png', 'fileContent': ''}, 'wall_light_blue.png': {'type': 'file', 'fileName': 'wall_light_blue.png', 'fileContent': ''}, 'wall_light_green.png': {'type': 'file', 'fileName': 'wall_light_green.png', 'fileContent': ''}, 'wall_light_grey.png': {'type': 'file', 'fileName': 'wall_light_grey.png', 'fileContent': ''}, 'wall_light_purple.png': {'type': 'file', 'fileName': 'wall_light_purple.png', 'fileContent': ''}, 'wall_medium_blue.png': {'type': 'file', 'fileName': 'wall_medium_blue.png', 'fileContent': ''}, 'wall_orange.png': {'type': 'file', 'fileName': 'wall_orange.png', 'fileContent': ''}, 'wall_very_light_blue.png': {'type': 'file', 'fileName': 'wall_very_light_blue.png', 'fileContent': ''}, 'wall_wire_frame.png': {'type': 'file', 'fileName': 'wall_wire_frame.png', 'fileContent': ''}, 'wall_wire_frame_white.png': {'type': 'file', 'fileName': 'wall_wire_frame_white.png', 'fileContent': ''}, 'wall_wire_frame_white_red_bricks.png': {'type': 'file', 'fileName': 'wall_wire_frame_white_red_bricks.png', 'fileContent': ''}, 'wall_yellow.png': {'type': 'file', 'fileName': 'wall_yellow.png', 'fileContent': ''}, 'wall_white.png': {'type': 'file', 'fileName': 'wall_white.png', 'fileContent': ''}}#
folder2_7_1=["img","launch_load","menu_anim","accueil.png","accueil_static_2.png"]
folder2_7_1_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'launch_load': {'type': 'dir', 'fileName': 'launch_load'}, 'menu_anim': {'type': 'dir', 'fileName': 'menu_anim'}, 'accueil.png': {'type': 'file', 'fileName': 'accueil.png', 'fileContent': ''}, 'accueil_static_2.png': {'type': 'file', 'fileName': 'accueil_static_2.png', 'fileContent': ''}}
folder2_7_2=["img","launch_load","start_load","stages_stage_1.png","stages_stage_10.png","stages_stage_11.png","stages_stage_12.png","stages_stage_13.png","stages_stage_14.png","stages_stage_15.png","stages_stage_2.png","stages_stage_3.png","stages_stage_4.png","stages_stage_5.png","stages_stage_6.png","stages_stage_7.png","stages_stage_8.png","stages_stage_9.png","stages_stage_black.png"]
folder2_7_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'launch_load': {'type': 'dir', 'fileName': 'launch_load'}, 'start_load': {'type': 'dir', 'fileName': 'start_load'}, 'stages_stage_1.png': {'type': 'file', 'fileName': 'stages_stage_1.png', 'fileContent': ''}, 'stages_stage_10.png': {'type': 'file', 'fileName': 'stages_stage_10.png', 'fileContent': ''}, 'stages_stage_11.png': {'type': 'file', 'fileName': 'stages_stage_11.png', 'fileContent': ''}, 'stages_stage_12.png': {'type': 'file', 'fileName': 'stages_stage_12.png', 'fileContent': ''}, 'stages_stage_13.png': {'type': 'file', 'fileName': 'stages_stage_13.png', 'fileContent': ''}, 'stages_stage_14.png': {'type': 'file', 'fileName': 'stages_stage_14.png', 'fileContent': ''}, 'stages_stage_15.png': {'type': 'file', 'fileName': 'stages_stage_15.png', 'fileContent': ''}, 'stages_stage_2.png': {'type': 'file', 'fileName': 'stages_stage_2.png', 'fileContent': ''}, 'stages_stage_3.png': {'type': 'file', 'fileName': 'stages_stage_3.png', 'fileContent': ''}, 'stages_stage_4.png': {'type': 'file', 'fileName': 'stages_stage_4.png', 'fileContent': ''}, 'stages_stage_5.png': {'type': 'file', 'fileName': 'stages_stage_5.png', 'fileContent': ''}, 'stages_stage_6.png': {'type': 'file', 'fileName': 'stages_stage_6.png', 'fileContent': ''}, 'stages_stage_7.png': {'type': 'file', 'fileName': 'stages_stage_7.png', 'fileContent': ''}, 'stages_stage_8.png': {'type': 'file', 'fileName': 'stages_stage_8.png', 'fileContent': ''}, 'stages_stage_9.png': {'type': 'file', 'fileName': 'stages_stage_9.png', 'fileContent': ''}, 'stages_stage_black.png': {'type': 'file', 'fileName': 'stages_stage_black.png', 'fileContent': ''}}
folder2_8_1=["img","sprite","famille","famille_loup_You_have_won.png","Mere et petits.png","understanding.PNG","w_fam.png"]
folder2_8_1_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'sprite': {'type': 'dir', 'fileName': 'sprite'}, 'famille': {'type': 'dir', 'fileName': 'famille'}, 'famille_loup_You_have_won.png': {'type': 'file', 'fileName': 'famille_loup_You_have_won.png', 'fileContent': ''}, 'Mere et petits.png': {'type': 'file', 'fileName': 'Mere et petits.png', 'fileContent': ''}, 'understanding.PNG': {'type': 'file', 'fileName': 'understanding.PNG', 'fileContent': ''}, 'w_fam.png': {'type': 'file', 'fileName': 'w_fam.png', 'fileContent': ''}}
folder2_8_2=["img","sprite","gardien","Gardien_bas.png","Gardien_Droite.png","Gardien_Gauche.png","Gardien_haut.png"]
folder2_8_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'sprite': {'type': 'dir', 'fileName': 'sprite'}, 'gardien': {'type': 'dir', 'fileName': 'gardien'}, 'Gardien_bas.png': {'type': 'file', 'fileName': 'Gardien_bas.png', 'fileContent': ''}, 'Gardien_Droite.png': {'type': 'file', 'fileName': 'Gardien_Droite.png', 'fileContent': ''}, 'Gardien_Gauche.png': {'type': 'file', 'fileName': 'Gardien_Gauche.png', 'fileContent': ''}, 'Gardien_haut.png': {'type': 'file', 'fileName': 'Gardien_haut.png', 'fileContent': ''}}
folder2_8_3=["img","sprite","w","w_down.png","w_left.png","w_rigth.png","w_up.png"]
folder2_8_3_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'sprite': {'type': 'dir', 'fileName': 'sprite'}, 'w': {'type': 'dir', 'fileName': 'w'}, 'w_down.png': {'type': 'file', 'fileName': 'w_down.png', 'fileContent': ''}, 'w_left.png': {'type': 'file', 'fileName': 'w_left.png', 'fileContent': ''}, 'w_rigth.png': {'type': 'file', 'fileName': 'w_rigth.png', 'fileContent': ''}, 'w_up.png': {'type': 'file', 'fileName': 'w_up.png', 'fileContent': ''}}
folder2_9_1_1=["img","tut_image","alphabet","accents",";.PNG","à.PNG","â.PNG","Â_cap.PNG","ã.PNG","Ã_cap.PNG","ä.PNG","Ä_cap.PNG","ç.PNG","è.PNG","é.PNG","ê.PNG","Ê_cap.png","ë.PNG","Ë_cap.png","î.PNG","Î_cap.PNG","ï.PNG","Ï_cap.PNG","ñ.PNG","Ñ_cap.PNG","ô.PNG","Ô_cap.PNG","õ.PNG","Õ_cap.PNG","ö.PNG","Ö_cap.PNG","ù.PNG","û.PNG","Û_cap.PNG","ü.PNG","Ü_cap.PNG","ÿ.PNG"]
folder2_9_1_1_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'accents': {'type': 'dir', 'fileName': 'accents'}, ';.PNG': {'type': 'file', 'fileName': ';.PNG', 'fileContent': ''}, 'à.PNG': {'type': 'file', 'fileName': 'à.PNG', 'fileContent': ''}, 'â.PNG': {'type': 'file', 'fileName': 'â.PNG', 'fileContent': ''}, 'Â_cap.PNG': {'type': 'file', 'fileName': 'Â_cap.PNG', 'fileContent': ''}, 'ã.PNG': {'type': 'file', 'fileName': 'ã.PNG', 'fileContent': ''}, 'Ã_cap.PNG': {'type': 'file', 'fileName': 'Ã_cap.PNG', 'fileContent': ''}, 'ä.PNG': {'type': 'file', 'fileName': 'ä.PNG', 'fileContent': ''}, 'Ä_cap.PNG': {'type': 'file', 'fileName': 'Ä_cap.PNG', 'fileContent': ''}, 'ç.PNG': {'type': 'file', 'fileName': 'ç.PNG', 'fileContent': ''}, 'è.PNG': {'type': 'file', 'fileName': 'è.PNG', 'fileContent': ''}, 'é.PNG': {'type': 'file', 'fileName': 'é.PNG', 'fileContent': ''}, 'ê.PNG': {'type': 'file', 'fileName': 'ê.PNG', 'fileContent': ''}, 'Ê_cap.png': {'type': 'file', 'fileName': 'Ê_cap.png', 'fileContent': ''}, 'ë.PNG': {'type': 'file', 'fileName': 'ë.PNG', 'fileContent': ''}, 'Ë_cap.png': {'type': 'file', 'fileName': 'Ë_cap.png', 'fileContent': ''}, 'î.PNG': {'type': 'file', 'fileName': 'î.PNG', 'fileContent': ''}, 'Î_cap.PNG': {'type': 'file', 'fileName': 'Î_cap.PNG', 'fileContent': ''}, 'ï.PNG': {'type': 'file', 'fileName': 'ï.PNG', 'fileContent': ''}, 'Ï_cap.PNG': {'type': 'file', 'fileName': 'Ï_cap.PNG', 'fileContent': ''}, 'ñ.PNG': {'type': 'file', 'fileName': 'ñ.PNG', 'fileContent': ''}, 'Ñ_cap.PNG': {'type': 'file', 'fileName': 'Ñ_cap.PNG', 'fileContent': ''}, 'ô.PNG': {'type': 'file', 'fileName': 'ô.PNG', 'fileContent': ''}, 'Ô_cap.PNG': {'type': 'file', 'fileName': 'Ô_cap.PNG', 'fileContent': ''}, 'õ.PNG': {'type': 'file', 'fileName': 'õ.PNG', 'fileContent': ''}, 'Õ_cap.PNG': {'type': 'file', 'fileName': 'Õ_cap.PNG', 'fileContent': ''}, 'ö.PNG': {'type': 'file', 'fileName': 'ö.PNG', 'fileContent': ''}, 'Ö_cap.PNG': {'type': 'file', 'fileName': 'Ö_cap.PNG', 'fileContent': ''}, 'ù.PNG': {'type': 'file', 'fileName': 'ù.PNG', 'fileContent': ''}, 'û.PNG': {'type': 'file', 'fileName': 'û.PNG', 'fileContent': ''}, 'Û_cap.PNG': {'type': 'file', 'fileName': 'Û_cap.PNG', 'fileContent': ''}, 'ü.PNG': {'type': 'file', 'fileName': 'ü.PNG', 'fileContent': ''}, 'Ü_cap.PNG': {'type': 'file', 'fileName': 'Ü_cap.PNG', 'fileContent': ''}, 'ÿ.PNG': {'type': 'file', 'fileName': 'ÿ.PNG', 'fileContent': ''}}
folder2_9_1_2=["img","tut_image","alphabet","minuscule","ami.PNG","bmi.PNG","cmi.PNG","dmi.PNG","emi.PNG","fmi.PNG","gmi.PNG","hmi.PNG","imi.PNG","jmi.PNG","kmi.PNG","lmi.PNG","mmi.png","nmi.PNG","omi.PNG","pmi.PNG","qmi.PNG","rmi.PNG","smi.PNG","tmi.PNG","umi.PNG","vmi.png","wmi.PNG","xmi.PNG","ymi.PNG","zmi.PNG"]
folder2_9_1_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'minuscule': {'type': 'dir', 'fileName': 'minuscule'}, 'ami.PNG': {'type': 'file', 'fileName': 'ami.PNG', 'fileContent': ''}, 'bmi.PNG': {'type': 'file', 'fileName': 'bmi.PNG', 'fileContent': ''}, 'cmi.PNG': {'type': 'file', 'fileName': 'cmi.PNG', 'fileContent': ''}, 'dmi.PNG': {'type': 'file', 'fileName': 'dmi.PNG', 'fileContent': ''}, 'emi.PNG': {'type': 'file', 'fileName': 'emi.PNG', 'fileContent': ''}, 'fmi.PNG': {'type': 'file', 'fileName': 'fmi.PNG', 'fileContent': ''}, 'gmi.PNG': {'type': 'file', 'fileName': 'gmi.PNG', 'fileContent': ''}, 'hmi.PNG': {'type': 'file', 'fileName': 'hmi.PNG', 'fileContent': ''}, 'imi.PNG': {'type': 'file', 'fileName': 'imi.PNG', 'fileContent': ''}, 'jmi.PNG': {'type': 'file', 'fileName': 'jmi.PNG', 'fileContent': ''}, 'kmi.PNG': {'type': 'file', 'fileName': 'kmi.PNG', 'fileContent': ''}, 'lmi.PNG': {'type': 'file', 'fileName': 'lmi.PNG', 'fileContent': ''}, 'mmi.png': {'type': 'file', 'fileName': 'mmi.png', 'fileContent': ''}, 'nmi.PNG': {'type': 'file', 'fileName': 'nmi.PNG', 'fileContent': ''}, 'omi.PNG': {'type': 'file', 'fileName': 'omi.PNG', 'fileContent': ''}, 'pmi.PNG': {'type': 'file', 'fileName': 'pmi.PNG', 'fileContent': ''}, 'qmi.PNG': {'type': 'file', 'fileName': 'qmi.PNG', 'fileContent': ''}, 'rmi.PNG': {'type': 'file', 'fileName': 'rmi.PNG', 'fileContent': ''}, 'smi.PNG': {'type': 'file', 'fileName': 'smi.PNG', 'fileContent': ''}, 'tmi.PNG': {'type': 'file', 'fileName': 'tmi.PNG', 'fileContent': ''}, 'umi.PNG': {'type': 'file', 'fileName': 'umi.PNG', 'fileContent': ''}, 'vmi.png': {'type': 'file', 'fileName': 'vmi.png', 'fileContent': ''}, 'wmi.PNG': {'type': 'file', 'fileName': 'wmi.PNG', 'fileContent': ''}, 'xmi.PNG': {'type': 'file', 'fileName': 'xmi.PNG', 'fileContent': ''}, 'ymi.PNG': {'type': 'file', 'fileName': 'ymi.PNG', 'fileContent': ''}, 'zmi.PNG': {'type': 'file', 'fileName': 'zmi.PNG', 'fileContent': ''}}
folder2_9_1_3=["img","tut_image","alphabet","majuscule","3.PNG","7.PNG","ama.PNG","bma.PNG","cma.PNG","dma.PNG","ema.PNG","fma.PNG","gma.PNG","hma.PNG","ima.PNG","jma.PNG","kma.PNG","lma.PNG","mma.PNG","nma.PNG","oma.PNG","pma.PNG","qma.PNG","rma.PNG","sma.PNG","tma.PNG","uma.PNG","vma.PNG","wma.PNG","xma.PNG","yma.PNG","zma.PNG"]
folder2_9_1_3_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'majuscule': {'type': 'dir', 'fileName': 'majuscule'}, '3.PNG': {'type': 'file', 'fileName': '3.PNG', 'fileContent': ''}, '7.PNG': {'type': 'file', 'fileName': '7.PNG', 'fileContent': ''}, 'ama.PNG': {'type': 'file', 'fileName': 'ama.PNG', 'fileContent': ''}, 'bma.PNG': {'type': 'file', 'fileName': 'bma.PNG', 'fileContent': ''}, 'cma.PNG': {'type': 'file', 'fileName': 'cma.PNG', 'fileContent': ''}, 'dma.PNG': {'type': 'file', 'fileName': 'dma.PNG', 'fileContent': ''}, 'ema.PNG': {'type': 'file', 'fileName': 'ema.PNG', 'fileContent': ''}, 'fma.PNG': {'type': 'file', 'fileName': 'fma.PNG', 'fileContent': ''}, 'gma.PNG': {'type': 'file', 'fileName': 'gma.PNG', 'fileContent': ''}, 'hma.PNG': {'type': 'file', 'fileName': 'hma.PNG', 'fileContent': ''}, 'ima.PNG': {'type': 'file', 'fileName': 'ima.PNG', 'fileContent': ''}, 'jma.PNG': {'type': 'file', 'fileName': 'jma.PNG', 'fileContent': ''}, 'kma.PNG': {'type': 'file', 'fileName': 'kma.PNG', 'fileContent': ''}, 'lma.PNG': {'type': 'file', 'fileName': 'lma.PNG', 'fileContent': ''}, 'mma.PNG': {'type': 'file', 'fileName': 'mma.PNG', 'fileContent': ''}, 'nma.PNG': {'type': 'file', 'fileName': 'nma.PNG', 'fileContent': ''}, 'oma.PNG': {'type': 'file', 'fileName': 'oma.PNG', 'fileContent': ''}, 'pma.PNG': {'type': 'file', 'fileName': 'pma.PNG', 'fileContent': ''}, 'qma.PNG': {'type': 'file', 'fileName': 'qma.PNG', 'fileContent': ''}, 'rma.PNG': {'type': 'file', 'fileName': 'rma.PNG', 'fileContent': ''}, 'sma.PNG': {'type': 'file', 'fileName': 'sma.PNG', 'fileContent': ''}, 'tma.PNG': {'type': 'file', 'fileName': 'tma.PNG', 'fileContent': ''}, 'uma.PNG': {'type': 'file', 'fileName': 'uma.PNG', 'fileContent': ''}, 'vma.PNG': {'type': 'file', 'fileName': 'vma.PNG', 'fileContent': ''}, 'wma.PNG': {'type': 'file', 'fileName': 'wma.PNG', 'fileContent': ''}, 'xma.PNG': {'type': 'file', 'fileName': 'xma.PNG', 'fileContent': ''}, 'yma.PNG': {'type': 'file', 'fileName': 'yma.PNG', 'fileContent': ''}, 'zma.PNG': {'type': 'file', 'fileName': 'zma.PNG', 'fileContent': ''}}
folder2_9_1_4=["img","tut_image","alphabet","punctuation","and.PNG","at.PNG","border.png","bracketclosed.PNG","bracketopen.PNG","colum.PNG","dot.PNG","endboard.PNG","exclamation.PNG","paragraph.PNG","paragraph_fermé.PNG","paragraph_ouvert.PNG","questionmark.PNG","[.PNG","].PNG"]
folder2_9_1_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'punctuation': {'type': 'dir', 'fileName': 'punctuation'}, 'and.PNG': {'type': 'file', 'fileName': 'and.PNG', 'fileContent': ''}, 'at.PNG': {'type': 'file', 'fileName': 'at.PNG', 'fileContent': ''}, 'border.png': {'type': 'file', 'fileName': 'border.png', 'fileContent': ''}, 'bracketclosed.PNG': {'type': 'file', 'fileName': 'bracketclosed.PNG', 'fileContent': ''}, 'bracketopen.PNG': {'type': 'file', 'fileName': 'bracketopen.PNG', 'fileContent': ''}, 'colum.PNG': {'type': 'file', 'fileName': 'colum.PNG', 'fileContent': ''}, 'dot.PNG': {'type': 'file', 'fileName': 'dot.PNG', 'fileContent': ''}, 'endboard.PNG': {'type': 'file', 'fileName': 'endboard.PNG', 'fileContent': ''}, 'exclamation.PNG': {'type': 'file', 'fileName': 'exclamation.PNG', 'fileContent': ''}, 'paragraph.PNG': {'type': 'file', 'fileName': 'paragraph.PNG', 'fileContent': ''}, 'paragraph_fermé.PNG': {'type': 'file', 'fileName': 'paragraph_fermé.PNG', 'fileContent': ''}, 'paragraph_ouvert.PNG': {'type': 'file', 'fileName': 'paragraph_ouvert.PNG', 'fileContent': ''}, 'questionmark.PNG': {'type': 'file', 'fileName': 'questionmark.PNG', 'fileContent': ''}, '[.PNG': {'type': 'file', 'fileName': '[.PNG', 'fileContent': ''}, '].PNG': {'type': 'file', 'fileName': '].PNG', 'fileContent': ''}}
folder2_9_1_5=["img","tut_image","alphabet","temperature","celsius.PNG","fahraneit.PNG"]
folder2_9_1_5_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'temperature': {'type': 'dir', 'fileName': 'temperature'}, 'celsius.PNG': {'type': 'file', 'fileName': 'celsius.PNG', 'fileContent': ''}, 'fahraneit.PNG': {'type': 'file', 'fileName': 'fahraneit.PNG', 'fileContent': ''}}
folder2_9_2=["img","tut_image","arrow","adown.png","aleft.png","aright.png","aup.png"]
folder2_9_2_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'arrow': {'type': 'dir', 'fileName': 'arrow'}, 'adown.png': {'type': 'file', 'fileName': 'adown.png', 'fileContent': ''}, 'aleft.png': {'type': 'file', 'fileName': 'aleft.png', 'fileContent': ''}, 'aright.png': {'type': 'file', 'fileName': 'aright.png', 'fileContent': ''}, 'aup.png': {'type': 'file', 'fileName': 'aup.png', 'fileContent': ''}}
folder2_9_3=["img","tut_image","currency","dollard.PNG","euro.PNG","pound.PNG","wan.PNG","yen.PNG"]
folder2_9_3_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'currency': {'type': 'dir', 'fileName': 'currency'}, 'dollard.PNG': {'type': 'file', 'fileName': 'dollard.PNG', 'fileContent': ''}, 'euro.PNG': {'type': 'file', 'fileName': 'euro.PNG', 'fileContent': ''}, 'pound.PNG': {'type': 'file', 'fileName': 'pound.PNG', 'fileContent': ''}, 'wan.PNG': {'type': 'file', 'fileName': 'wan.PNG', 'fileContent': ''}, 'yen.PNG': {'type': 'file', 'fileName': 'yen.PNG', 'fileContent': ''}}
folder2_9_4=["img","tut_image","heart","heartbig.png","heartsmall.png"]
folder2_9_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'heart': {'type': 'dir', 'fileName': 'heart'}, 'heartbig.png': {'type': 'file', 'fileName': 'heartbig.png', 'fileContent': ''}, 'heartsmall.png': {'type': 'file', 'fileName': 'heartsmall.png', 'fileContent': ''}}
folder2_9_5=["img","tut_image","math","%.PNG","+.PNG","-.PNG","=.PNG","diviser.PNG","lessthan.PNG","morethan.PNG","times.PNG"]
folder2_9_5_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'math': {'type': 'dir', 'fileName': 'math'}, '%.PNG': {'type': 'file', 'fileName': '%.PNG', 'fileContent': ''}, '+.PNG': {'type': 'file', 'fileName': '+.PNG', 'fileContent': ''}, '-.PNG': {'type': 'file', 'fileName': '-.PNG', 'fileContent': ''}, '=.PNG': {'type': 'file', 'fileName': '=.PNG', 'fileContent': ''}, 'diviser.PNG': {'type': 'file', 'fileName': 'diviser.PNG', 'fileContent': ''}, 'lessthan.PNG': {'type': 'file', 'fileName': 'lessthan.PNG', 'fileContent': ''}, 'morethan.PNG': {'type': 'file', 'fileName': 'morethan.PNG', 'fileContent': ''}, 'times.PNG': {'type': 'file', 'fileName': 'times.PNG', 'fileContent': ''}}
folder2_9_6=["img","tut_image","numbers","0.PNG","1.PNG","2.PNG","3.PNG","4.PNG","5.PNG","6.PNG","7.PNG","8.PNG","9.PNG"]
folder2_9_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'numbers': {'type': 'dir', 'fileName': 'numbers'}, '0.PNG': {'type': 'file', 'fileName': '0.PNG', 'fileContent': ''}, '1.PNG': {'type': 'file', 'fileName': '1.PNG', 'fileContent': ''}, '2.PNG': {'type': 'file', 'fileName': '2.PNG', 'fileContent': ''}, '3.PNG': {'type': 'file', 'fileName': '3.PNG', 'fileContent': ''}, '4.PNG': {'type': 'file', 'fileName': '4.PNG', 'fileContent': ''}, '5.PNG': {'type': 'file', 'fileName': '5.PNG', 'fileContent': ''}, '6.PNG': {'type': 'file', 'fileName': '6.PNG', 'fileContent': ''}, '7.PNG': {'type': 'file', 'fileName': '7.PNG', 'fileContent': ''}, '8.PNG': {'type': 'file', 'fileName': '8.PNG', 'fileContent': ''}, '9.PNG': {'type': 'file', 'fileName': '9.PNG', 'fileContent': ''}}
folder3=["levels","001_l1","002_l2","003_l3","004_l4","005_l5","006_l6","007_l7","008_l8"]
folder3_dict={'levels': {'type': 'dir', 'fileName': 'levels'}, '001_l1': {'type': 'file', 'fileName': '001_l1', 'fileContent': ''}, '002_l2': {'type': 'file', 'fileName': '002_l2', 'fileContent': ''}, '003_l3': {'type': 'file', 'fileName': '003_l3', 'fileContent': ''}, '004_l4': {'type': 'file', 'fileName': '004_l4', 'fileContent': ''}, '005_l5': {'type': 'file', 'fileName': '005_l5', 'fileContent': ''}, '006_l6': {'type': 'file', 'fileName': '006_l6', 'fileContent': ''}, '007_l7': {'type': 'file', 'fileName': '007_l7', 'fileContent': ''}, '008_l8': {'type': 'file', 'fileName': '008_l8', 'fileContent': ''}}

main_for_rec=[folder1,folder2_2,folder2_3,folder2_4,folder2_5_1,folder2_5_2,folder2_5_3,folder2_5_4,folder2_5_5,folder2_5_6,folder2_5_7,folder2_5_8,folder2_5_9,folder2_5_10,folder2_5_11,folder2_5_12,folder2_5_13,folder2_5_14,folder2_5_15,folder2_5_16,folder2_6,folder2_7_1,folder2_7_2,folder2_8_1,folder2_8_2,folder2_8_3,folder2_9_1_1,folder2_9_1_2,folder2_9_1_3,folder2_9_1_4,folder2_9_1_5,folder2_9_2,folder2_9_3,folder2_9_4,folder2_9_5,folder2_9_6,folder3]
main_for_rec_dict=[folder1_dict,folder2_2_dict,folder2_3_dict,folder2_4_dict,folder2_5_1_dict,folder2_5_2_dict,folder2_5_3_dict,folder2_5_4_dict,folder2_5_5_dict,folder2_5_6_dict,folder2_5_7_dict,folder2_5_8_dict,folder2_5_9_dict,folder2_5_10_dict,folder2_5_11_dict,folder2_5_12_dict,folder2_5_13_dict,folder2_5_14_dict,folder2_5_15_dict,folder2_5_16_dict,folder2_6_dict,folder2_7_1_dict,folder2_7_2_dict,folder2_8_1_dict,folder2_8_2_dict,folder2_8_3_dict,folder2_9_1_1_dict,folder2_9_1_2_dict,folder2_9_1_3_dict,folder2_9_1_4_dict,folder2_9_1_5_dict,folder2_9_2_dict,folder2_9_3_dict,folder2_9_4_dict,folder2_9_5_dict,folder2_9_6_dict,folder3_dict]


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
