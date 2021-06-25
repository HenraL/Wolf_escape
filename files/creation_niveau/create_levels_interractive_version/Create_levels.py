__version__="0.0"
__Author__="Henry Letellier"
__SoftwareName__="Create_levels"
try:
    from tkinter import *
    from tkinter.filedialog import *
except:
    from Tkinter import *
    from Tkinter.filedialog import *



import os,shutil,requests
from time import sleep
from webbrowser import open_new_tab,open_new
import_error=False
# try:
#     # import tkhtmlview
#     from tkhtmlview import HTMLLabel
# except ImportError:
#     # from Tkhtmlview import *
#     from Tkhtmlview import HTMLLabel
# except:
#     try:
#         os.system("py -m pip install tkhtmlview")
#         # from tkhtmlview import *
#         from tkhtmlview import HTMLLabel
#     except:
#         try:
#             os.system("py -m pip install Tkhtmlview")
#             # from Tkhtmlview import *
#             from Tkhtmlview import HTMLLabel
#         except:
#             TTT=Tk()
#             TTT.title("Error")
#             TTT["bg"]="white"
#             TitleLabel=Label(TTT,text="Error:")
#             TitleLabel.pack(side=TOP)
#             ErrorLabel=Label(TTT,text="Failed to download tkhtmlview\nPlease try running this program with Admin rights.\nIf the problem isstill present, please open a support ticket with the following title:\n tkhtmlview import failure")
#             ErrorLabel.pack(side=TOP)
#             ButtonRetry=Button(TTT,text="Let's try again",command=TTT.destroy)
#             ButtonRetry.pack(side=TOP)
#             TTT.mainloop()
            # import_er;ror=True
f=open("list_lengths.txt","w").write("")
class root:
    def __init__(self,main,main_dict,links,version,Author,SoftwareName):
        #-------------------- Abort program --------------------
        self.abort_program=False
        self.loginValidated=False
        self.version=version
        self.Author=Author
        self.SoftwareName=SoftwareName
        #-------------------- Other vars --------------------
        self.mainLoop=True
        self.main=main
        self.main_dict=main_dict
        self.links=links
        self.home="https://hanralatalliardwork.github.io/wolf_escape_home/"
        self.file_location="files/requirements"
        self.LevelCreators='files/level_creators/'
        self.ggg=0
        self.list_dict=[]
        self.error_ticket_title=""
        self.error_ticket_content=""
        #------------------ Info about the user ------------------  
        self.username=""
        self.userDiscordTagAndID=""
        self.userOtherSocialMedia=""
        self.DiscordCodeID=""
        # self.
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
        self.fontFamilly="Times"
        self.fontSizeAE=20
        #--------------------------------- The program's vars ---------------------------------
        self.mainMenuPadX=5
        #--------------------------------- Level creation ---------------------------------
        self.path="UserLevels"
        self.grid_entry_background="black"
        self.grid_entry_foreground=self.universalBackground
        self.grid_insert_entry_background=self.grid_entry_foreground
        self.Entry_relief=FLAT
        self.mid_line_padx=0
        self.mid_line_pady=0.5
        self.entry_padx=0.5
        self.entry_pady=0
        #-------------------------------- Descriptions --------------------------------
        self.Index_y=6
        self.Index_x=6
        self.h=40
        self.w=40
        self.image_width=50
        self.image_height=50
        self.AvailableFilePage=f"{self.home}{self.LevelCreators}available_decorations/"
    def readFile(path):
        f=open(path,"r")
        e=f.read()
        f.close()
        return e

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
            RI.ggg+=1

            return lst_to
        def content(list1,list2,links,home,LabelInfo,progress,ProgressBar,window,ProgressWindow):
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
                        RI,
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
                                RI,
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
                                    RI,
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
                                        continue_error_window=boot.TKinter.window.error_abortion(RI,window,ticketTitle,ticketBody)
                                        if RI.abort_program==True:
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
                                RI,
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
                                    continue_error_window=boot.TKinter.window.error_abortion(RI,window,ticketTitle,ticketBody)
                                    if RI.abort_program==True:
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
                                    RI,
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
                                ticketBodyText=f"(The below options are not buttons\nplease scroll down to see the options)\n- Abort and run the program with admin rights\n-Create the folder yourself in {peth} then restart the program\n- Download the files at (*) and place them manually at the source of the program\n* {RI.home}{RI.file_location}\nIf the problem has not been solved, please open a support ticket in the server."
                                continue_error_window=True
                                while continue_error_window==True:
                                    continue_error_window=boot.TKinter.window.error_abortion(RI,TT=window,ticketTitleText=ticketTitleText,ticketBodyText=ticketBodyText)
                                    if RI.abort_program==True:
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
                            RI,
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
                            continue_error_window=boot.TKinter.window.error_abortion(RI,window,ticketTitle,ticketBody)
                            if RI.abort_program==True:
                                return 'Program aborted'
                        return a,zeta
                    zeta=boot.TKinter.window.updateProgress(
                        RI,
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
                RI.list_dict.append(list2[0][i])
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
                boot.get.content(list1=RI.main,list2=RI.main_dict,links=RI.links,home=f"{RI.home}{RI.file_location}",LabelInfo=CurrentFile,progress=Progress,ProgressBar=ProgressBar,window=TT,ProgressWindow=ProgressWindow)
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Great!",command=TT.destroy,bg=self.universalBackground)
                DownloadButton.pack(side=TOP,fill=X)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()

    def initialise():
        folder1=["levels"]
        folder1_dict={'levels': {'type': 'dir', 'fileName': 'levels'}}
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
        folder2_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'ingame': {'type': 'dir', 'fileName': 'ingame'}, 'accueil.png': {'type': 'file', 'fileName': 'accueil.png', 'fileContent': ''}, 'accueilm.png': {'type': 'file', 'fileName': 'accueilm.png', 'fileContent': ''}, 'endv.png': {'type': 'file', 'fileName': 'endv.png', 'fileContent': ''}, 'mur.png': {'type': 'file', 'fileName': 'mur.png', 'fileContent': ''}, 'start.png': {'type': 'file', 'fileName': 'start.png', 'fileContent': ''}, "teller_start.png":{"type":"file","fileName":"teller_start.png","fileContent":""},'wolf_icon.ico': {'type': 'file', 'fileName': 'wolf_icon.ico', 'fileContent': ''}, 'wolf_icon.png': {'type': 'file', 'fileName': 'wolf_icon.png', 'fileContent': ''}, 'funkyWalls': {'type': 'dir', 'fileName': 'funkyWalls'}, 'wall_beige_black.png': {'type': 'file', 'fileName': 'wall_beige_black.png', 'fileContent': ''}, 'wall_beige_white.png': {'type': 'file', 'fileName': 'wall_beige_white.png', 'fileContent': ''}, 'wall_birght_red_black.png': {'type': 'file', 'fileName': 'wall_birght_red_black.png', 'fileContent': ''}, 'wall_birght_red_white.png': {'type': 'file', 'fileName': 'wall_birght_red_white.png', 'fileContent': ''}, 'wall_black_white.png': {'type': 'file', 'fileName': 'wall_black_white.png', 'fileContent': ''}, 'wall_brigth_orange_black.png': {'type': 'file', 'fileName': 'wall_brigth_orange_black.png', 'fileContent': ''}, 'wall_brigth_orange_white.png': {'type': 'file', 'fileName': 'wall_brigth_orange_white.png', 'fileContent': ''}, 'wall_brigth_pink_black.png': {'type': 'file', 'fileName': 'wall_brigth_pink_black.png', 'fileContent': ''}, 'wall_brigth_pink_white.png': {'type': 'file', 'fileName': 'wall_brigth_pink_white.png', 'fileContent': ''}, 'wall_chocolat_black.png': {'type': 'file', 'fileName': 'wall_chocolat_black.png', 'fileContent': ''}, 'wall_chocolat_white.png': {'type': 'file', 'fileName': 'wall_chocolat_white.png', 'fileContent': ''}, 'wall_darks_red_black.png': {'type': 'file', 'fileName': 'wall_darks_red_black.png', 'fileContent': ''}, 'wall_darks_red_white.png': {'type': 'file', 'fileName': 'wall_darks_red_white.png', 'fileContent': ''}, 'wall_dark_blue_black.png': {'type': 'file', 'fileName': 'wall_dark_blue_black.png', 'fileContent': ''}, 'wall_dark_blue_white.png': {'type': 'file', 'fileName': 'wall_dark_blue_white.png', 'fileContent': ''}, 'wall_dark_green_black.png': {'type': 'file', 'fileName': 'wall_dark_green_black.png', 'fileContent': ''}, 'wall_dark_green_white.png': {'type': 'file', 'fileName': 'wall_dark_green_white.png', 'fileContent': ''}, 'wall_dark_purple_black.png': {'type': 'file', 'fileName': 'wall_dark_purple_black.png', 'fileContent': ''}, 'wall_dark_purple_white.png': {'type': 'file', 'fileName': 'wall_dark_purple_white.png', 'fileContent': ''}, 'wall_grey_black.png': {'type': 'file', 'fileName': 'wall_grey_black.png', 'fileContent': ''}, 'wall_grey_white.png': {'type': 'file', 'fileName': 'wall_grey_white.png', 'fileContent': ''}, 'wall_light_blue_black.png': {'type': 'file', 'fileName': 'wall_light_blue_black.png', 'fileContent': ''}, 'wall_light_blue_white.png': {'type': 'file', 'fileName': 'wall_light_blue_white.png', 'fileContent': ''}, 'wall_light_green_black.png': {'type': 'file', 'fileName': 'wall_light_green_black.png', 'fileContent': ''}, 'wall_light_green_white.png': {'type': 'file', 'fileName': 'wall_light_green_white.png', 'fileContent': ''}, 'wall_light_grey_black.png': {'type': 'file', 'fileName': 'wall_light_grey_black.png', 'fileContent': ''}, 'wall_light_grey_white.png': {'type': 'file', 'fileName': 'wall_light_grey_white.png', 'fileContent': ''}, 'wall_light_purple_black.png': {'type': 'file', 'fileName': 'wall_light_purple_black.png', 'fileContent': ''}, 'wall_light_purple_white.png': {'type': 'file', 'fileName': 'wall_light_purple_white.png', 'fileContent': ''}, 'wall_medium_blue_black.png': {'type': 'file', 'fileName': 'wall_medium_blue_black.png', 'fileContent': ''}, 'wall_medium_blue_white.png': {'type': 'file', 'fileName': 'wall_medium_blue_white.png', 'fileContent': ''}, 'wall_orange_black.png': {'type': 'file', 'fileName': 'wall_orange_black.png', 'fileContent': ''}, 'wall_orange_white.png': {'type': 'file', 'fileName': 'wall_orange_white.png', 'fileContent': ''}, 'wall_very_light_blue_black.png': {'type': 'file', 'fileName': 'wall_very_light_blue_black.png', 'fileContent': ''}, 'wall_very_light_blue_white.png': {'type': 'file', 'fileName': 'wall_very_light_blue_white.png', 'fileContent': ''}, 'wall_yellow_black.png': {'type': 'file', 'fileName': 'wall_yellow_black.png', 'fileContent': ''}, 'wall_yellow_white.png': {'type': 'file', 'fileName': 'wall_yellow_white.png', 'fileContent': ''}, 'snipsets': {'type': 'dir', 'fileName': 'snipsets'}, 'bric.png': {'type': 'file', 'fileName': 'bric.png', 'fileContent': ''}, 'snipsets.zip': {'type': 'file', 'fileName': 'snipsets.zip', 'fileContent': ''}, 'wall_beige.png': {'type': 'file', 'fileName': 'wall_beige.png', 'fileContent': ''}, 'wall_birght_red.png': {'type': 'file', 'fileName': 'wall_birght_red.png', 'fileContent': ''}, 'wall_black.png': {'type': 'file', 'fileName': 'wall_black.png', 'fileContent': ''}, 'wall_brigth_orange.png': {'type': 'file', 'fileName': 'wall_brigth_orange.png', 'fileContent': ''}, 'wall_brigth_pink.png': {'type': 'file', 'fileName': 'wall_brigth_pink.png', 'fileContent': ''}, 'wall_chocolat.png': {'type': 'file', 'fileName': 'wall_chocolat.png', 'fileContent': ''}, 'wall_darks_red.png': {'type': 'file', 'fileName': 'wall_darks_red.png', 'fileContent': ''}, 'wall_dark_blue.png': {'type': 'file', 'fileName': 'wall_dark_blue.png', 'fileContent': ''}, 'wall_dark_green.png': {'type': 'file', 'fileName': 'wall_dark_green.png', 'fileContent': ''}, 'wall_dark_purple.png': {'type': 'file', 'fileName': 'wall_dark_purple.png', 'fileContent': ''}, 'wall_grey.png': {'type': 'file', 'fileName': 'wall_grey.png', 'fileContent': ''}, 'wall_light_blue.png': {'type': 'file', 'fileName': 'wall_light_blue.png', 'fileContent': ''}, 'wall_light_green.png': {'type': 'file', 'fileName': 'wall_light_green.png', 'fileContent': ''}, 'wall_light_grey.png': {'type': 'file', 'fileName': 'wall_light_grey.png', 'fileContent': ''}, 'wall_light_purple.png': {'type': 'file', 'fileName': 'wall_light_purple.png', 'fileContent': ''}, 'wall_medium_blue.png': {'type': 'file', 'fileName': 'wall_medium_blue.png', 'fileContent': ''}, 'wall_orange.png': {'type': 'file', 'fileName': 'wall_orange.png', 'fileContent': ''}, 'wall_very_light_blue.png': {'type': 'file', 'fileName': 'wall_very_light_blue.png', 'fileContent': ''}, 'wall_wire_frame.png': {'type': 'file', 'fileName': 'wall_wire_frame.png', 'fileContent': ''}, 'wall_wire_frame_white.png': {'type': 'file', 'fileName': 'wall_wire_frame_white.png', 'fileContent': ''}, 'wall_wire_frame_white_red_bricks.png': {'type': 'file', 'fileName': 'wall_wire_frame_white_red_bricks.png', 'fileContent': ''}, 'wall_yellow.png': {'type': 'file', 'fileName': 'wall_yellow.png', 'fileContent': ''}, 'wall_white.png': {'type': 'file', 'fileName': 'wall_white.png', 'fileContent': ''}}#
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
        folder4=["UserLevels"]
        folder4_dict={"UserLevels":{"type":"dir","fileName":"UserLevels"}}
        main_for_rec=[folder1,folder2_2,folder2_3,folder2_4,folder2_5_1,folder2_5_2,folder2_5_3,folder2_5_4,folder2_5_5,folder2_5_6,folder2_5_7,folder2_5_8,folder2_5_9,folder2_5_10,folder2_5_11,folder2_5_12,folder2_5_13,folder2_5_14,folder2_5_15,folder2_5_16,folder2_6,folder2_7_1,folder2_7_2,folder2_8_1,folder2_8_2,folder2_8_3,folder2_9_1_1,folder2_9_1_2,folder2_9_1_3,folder2_9_1_4,folder2_9_1_5,folder2_9_2,folder2_9_3,folder2_9_4,folder2_9_5,folder2_9_6,folder3,folder4]
        main_for_rec_dict=[folder1_dict,folder2_2_dict,folder2_3_dict,folder2_4_dict,folder2_5_1_dict,folder2_5_2_dict,folder2_5_3_dict,folder2_5_4_dict,folder2_5_5_dict,folder2_5_6_dict,folder2_5_7_dict,folder2_5_8_dict,folder2_5_9_dict,folder2_5_10_dict,folder2_5_11_dict,folder2_5_12_dict,folder2_5_13_dict,folder2_5_14_dict,folder2_5_15_dict,folder2_5_16_dict,folder2_6_dict,folder2_7_1_dict,folder2_7_2_dict,folder2_8_1_dict,folder2_8_2_dict,folder2_8_3_dict,folder2_9_1_1_dict,folder2_9_1_2_dict,folder2_9_1_3_dict,folder2_9_1_4_dict,folder2_9_1_5_dict,folder2_9_2_dict,folder2_9_3_dict,folder2_9_4_dict,folder2_9_5_dict,folder2_9_6_dict,folder3_dict,folder4_dict]
        return main_for_rec,main_for_rec_dict
    def initialise_links(e):
        links=[]
        for i in range(len(e[1])):
            links.append(boot.get.make_links(e[1][i]))

        return links

class read(root):
    def levels(self):
        print("")

class display(root):
    def AvailableEnds(self):
        window_size_x=self.window_size_x
        window_size_y=self.window_size_y
        window_geometry=f"{window_size_x}x{window_size_y}" 
        image_description_padding_x=5
        TTT=Tk()
        TTT.geometry(window_geometry)
        TTT.minsize(window_size_x,window_size_y)
        TTT.title("Available Ends")
        TTT['bg']=self.universalBackground
        titleLabel=Label(TTT,text=f"Here are the available ends and their ID (what you put in the box for the image).")
        titleLabel.pack(side=TOP)
        FrameContainer=Frame(TTT,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameContainer.pack(side=TOP,fill=X)
        FrameLeft=Frame(FrameContainer,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameLeft.pack(side=LEFT)
        FrameRight=Frame(FrameContainer,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameRight.pack(side=LEFT)
        Start = PhotoImage(file="img/ingame/start.png",width=self.image_width,height=self.image_height)
        canvasStart = Canvas(FrameLeft,width=self.w, height=self.h,bg="white")
        # Cells.add(canvasEndv)
        canvasStart.create_image(self.Index_y, self.Index_x, anchor=NW, image=Start)
        canvasStart.pack()
        endv = PhotoImage(file="img/end/endv.png",width=self.image_width,height=self.image_height)
        canvasEndv = Canvas(FrameLeft,width=self.w, height=self.h,bg="white")
        # Cells.add(canvasEndv)
        canvasEndv.create_image(self.Index_y, self.Index_x, anchor=NW, image=endv)
        canvasEndv.pack()
        endFam=PhotoImage(file="img/sprite/famille/w_fam.png",width=self.image_width,height=self.image_height)
        canvasEndFam = Canvas(FrameLeft,width=self.w, height=self.h,bg="white")
        # Cells.add(canvasEndFam)
        canvasEndFam.create_image(self.Index_y, self.Index_x, anchor=NW, image=endFam)
        canvasEndFam.pack()
        e=Label(FrameRight,text="#",bg=self.universalBackground,borderwidth=1,font=(self.fontFamilly,self.fontSizeAE))
        e.pack(pady=image_description_padding_x)
        e=Label(FrameRight,text="10",bg=self.universalBackground,borderwidth=1,font=(self.fontFamilly,self.fontSizeAE))
        e.pack(pady=image_description_padding_x)
        e=Label(FrameRight,text="_",bg=self.universalBackground,borderwidth=1,font=(self.fontFamilly,self.fontSizeAE))
        e.pack(pady=image_description_padding_x)
        # Cells.pack()
        CloseButton=Button(TTT,text="Close",command=TTT.destroy)
        CloseButton.pack(side=TOP)
        TTT.mainloop()
    def AvailableDecoration(self):
        open_new(self.AvailableFilePage)
    #     window_size_x=self.window_size_x
    #     window_size_y=self.window_size_y
    #     window_geometry=f"{window_size_x}x{window_size_y}" 
    #     image_description_padding_x=5
    #     TTT=Tk()
    #     TTT.geometry(window_geometry)
    #     TTT.minsize(window_size_x,window_size_y)
    #     TTT.title("Available Decoration")
    #     TTT['bg']=self.universalBackground
    #     titleLabel=Label(TTT,text=f"Here are the available Decorations and their ID (what you put in the box for the image).")
    #     titleLabel.pack(side=TOP)
    #     FrameContainer=Frame(TTT,bg=self.universalBackground,borderwidth=0,relief=FLAT)
    #     FrameContainer.pack(side=TOP,fill=X)
        # CurrentAvailableSprites=boot.get.online.tempFile(self.AvailableFilePage)
    #     my_label = HTMLLabel(FrameContainer, html=CurrentAvailableSprites)

    #     # Adjust label
    #     my_label.pack(pady=20, padx=20)
    #     CloseButton=Button(TTT,text="Close",command=TTT.destroy)
    #     CloseButton.pack(side=TOP)
    #     TTT.mainloop()
    def preview(self,content,title):
        print(f"title={title},content=\n{content}")
    def ShowErrorMessage(self,message,buttonText="Let me correct my error!"):
        TTT=Tk()
        TTT.title("Error")
        TTT["bg"]=self.universalBackground
        TitleLabel=Label(TTT,text="Error:")
        TitleLabel.pack(side=TOP)
        ErrorLabel=Label(TTT,text=message)
        ErrorLabel.pack(side=TOP)
        ButtonRetry=Button(TTT,text=buttonText,command=TTT.destroy)
        ButtonRetry.pack(side=TOP)
        TTT.mainloop()
    def ShowSuccessMessage(self,message,ButtonText="Great!"):
        TTT=Tk()
        TTT.title("Success")
        TTT["bg"]=self.universalBackground
        TitleLabel=Label(TTT,text="Success")
        TitleLabel.pack(side=TOP)
        ErrorLabel=Label(TTT,text=message)
        ErrorLabel.pack(side=TOP)
        ButtonRetry=Button(TTT,text=ButtonText,command=TTT.destroy)
        ButtonRetry.pack(side=TOP)
        TTT.mainloop()
    def getInfo(self):
        self.loginValidated=False
        def loadFromFile():
            foundFile=False
            while foundFile==False:
                filepath = askopenfilename(title="Open the file containing the required info",filetypes=[('Wolf Escape files','.we'),('all files','.*')])
                Content=root.readFile(filepath)
                if len(Content)==0:
                    display.ShowErrorMessage(self,"The selected file is empty or does not contain the required information.")
                else:
                    foundFile=True
                    try:
                        Info={}
                        word=""
                        o=0
                        required=["username","userDiscordTagAndID","DiscordCodeID","userOtherSocialMedia"]
                        for i in Content:
                            if i=="\n":
                                Info[required[o]]=word
                                o+=1
                                word=""
                            else:
                                word+=f"{i}"
                        usernameVar = StringVar()
                        usernameVar.set(Info['username'])
                        usernameEntry.config(textvariable=usernameVar)
                        r=Info["userDiscordTagAndID"].split("#")
                        userDiscordTagVar = StringVar()
                        userDiscordTagVar.set(r[0])
                        userDiscordTagEntry.config(text=userDiscordTagVar)
                        userDiscordIDVar = StringVar()
                        userDiscordIDVar.set(r[1])
                        userDiscordIDEntry.config(text=userDiscordIDVar)
                        userOtherSocialMediaVar = StringVar()
                        userOtherSocialMediaVar.set(Info["userOtherSocialMedia"])
                        userOtherSocialMediaEntry.config(text=userOtherSocialMediaVar)
                        userDiscordCodeIDVar = StringVar()
                        userDiscordCodeIDVar.set(Info["DiscordCodeID"])
                        userDiscordCodeIDEntry.config(text=userDiscordCodeIDVar)
                        TTT=Tk()
                        TTT.title("Success")
                        TTT["bg"]=self.universalBackground
                        TitleLabel=Label(TTT,text="Success:")
                        TitleLabel.pack(side=TOP)
                        ErrorLabel=Label(TTT,text="The required information has successfully been loaded from the file.\nPlease click the 'Continue' button on the bottom of the form to submit it.")
                        ErrorLabel.pack(side=TOP)
                        ButtonRetry=Button(TTT,text="Great!",command=TTT.destroy)
                        ButtonRetry.pack(side=TOP)
                        TTT.mainloop()
                    except:
                        display.ShowErrorMessage(self,"Could not find the required information in the provided file\nPlease try again or enter the required information manually.")
        def LoadFromInput(*args):
            error=False
            username=usernameEntry.get()
            userDiscordTag=userDiscordTagEntry.get()
            userDiscordID=userDiscordIDEntry.get()
            try:
                int(userDiscordID)
            except:
                error=True
                display.ShowErrorMessage(self,f"Your discord ID must only contain numbers\nYou have entered: {userDiscordID}")
            userDiscordTagAndID=f"{userDiscordTag}#{userDiscordID}"
            userOtherSocialMedia=userOtherSocialMediaEntry.get()
            DiscordCodeID=userDiscordCodeIDEntry.get()
            if len(username)==0:
                error=True
                display.ShowErrorMessage(self,"The username field must contain the name of the user.")
            elif len(userDiscordTag)==0 or len(userDiscordID)<4 or len(userDiscordID)>4 or len(DiscordCodeID)!=18:
                error=True
                if len(userDiscordTag)==0:
                    display.ShowErrorMessage(self,"You must enter your discord tag")
                elif len(userDiscordID)<4 or len(userDiscordID)>4:
                    display.ShowErrorMessage(self,"The discord ID must contain the four numbers that are after the '#' sign")
                elif len(DiscordCodeID)!=18:
                    display.ShowErrorMessage(self,f"There is a digit missing or to many,\n you have {len(DiscordCodeID)} but should only have 18 characters in you discord codeID.")
                else:
                    error=True
            elif len(userDiscordTagAndID)<6 or ("#" not in userDiscordTagAndID):
                error=True
                display.ShowErrorMessage(self,message="The discord field must contain the name of the user and the id, ex: myDiscordName#0000.")
            else:
                pass
            if error==False:
                self.username=username
                self.userDiscordTagAndID=userDiscordTagAndID
                self.DiscordCodeID=DiscordCodeID
                self.userOtherSocialMedia=userOtherSocialMedia
                TT.destroy()
                self.loginValidated=True
        TT=Tk()
        TT["bg"]=self.universalBackground
        TT.title("A bit about you")
        TitleLabel=Label(TT,text="A bit about you",bg=self.universalBackground)
        TitleLabel.pack(side=TOP)
        ButtonLoadFile=Button(TT,text="Load info from a file.",command=loadFromFile)
        ButtonLoadFile.pack(side=TOP,fill=X)
        StarInfoLabel=Label(TT,text="Fields that have a '*' are fields that must be filled.",bg=self.universalBackground)
        StarInfoLabel.pack(side=TOP)
        FrameUserName=Frame(TT,bg=self.universalBackground,relief=GROOVE)
        FrameUserName.pack(side=TOP)
        NameLabel=Label(FrameUserName,text="UserName * :",bg=self.universalBackground,anchor="w")
        NameLabel.pack(side=LEFT)
        usernameEntry=Entry(FrameUserName,text="",bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background)
        usernameEntry.pack(side=LEFT)
        FrameDicordId=Frame(TT,bg=self.universalBackground,relief=GROOVE)
        FrameDicordId.pack(side=TOP)
        subFrame=Frame(FrameDicordId,bg=self.universalBackground,relief=GROOVE)
        subFrame.pack(side=TOP)
        DicordLabel=Label(subFrame,text="Discord * :",bg=self.universalBackground,anchor="w")
        DicordLabel.pack(side=LEFT)
        DicordTagLabel=Label(FrameDicordId,text="Tag (before the #) * :",bg=self.universalBackground)
        DicordTagLabel.pack(side=LEFT)
        userDiscordTagEntry=Entry(FrameDicordId,text="",bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background)
        userDiscordTagEntry.pack(side=LEFT)
        DicordIdLabel=Label(FrameDicordId,text="ID (after the #) * :",bg=self.universalBackground)
        DicordIdLabel.pack(side=LEFT)
        userDiscordIDEntry=Entry(FrameDicordId,text="",bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background)
        userDiscordIDEntry.pack(side=LEFT)
        FrameUserOtherSocialMedia=Frame(TT,bg=self.universalBackground,relief=GROOVE)
        FrameUserOtherSocialMedia.pack(side=TOP)
        OtherSocialMediaLabel=Label(FrameUserOtherSocialMedia,text="Other social media :",bg=self.universalBackground,anchor="w")
        OtherSocialMediaLabel.pack(side=LEFT)
        userOtherSocialMediaEntry=Entry(FrameUserOtherSocialMedia,text="",bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background)
        userOtherSocialMediaEntry.pack(side=LEFT)
        FrameUserDiscordCodeID=Frame(TT,bg=self.universalBackground,relief=GROOVE)
        FrameUserDiscordCodeID.pack(side=TOP)
        DiscordCodeIDLabel=Label(FrameUserDiscordCodeID,text="Your Discord Code ID (it was given to you when you obtained a copy of the program) * :",bg=self.universalBackground,anchor="w")
        DiscordCodeIDLabel.pack(side=LEFT)
        userDiscordCodeIDEntry=Entry(FrameUserDiscordCodeID,text="",bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background)
        userDiscordCodeIDEntry.pack(side=LEFT)
        ButtonConfirm=Button(TT,text="Continue",command=LoadFromInput)
        ButtonConfirm.pack(side=TOP,fill=X)
        TT.mainloop()
    def mainMenu(self):
        def createLevel():
            TT.destroy()
            display.CreateALevel(self)
        def editLevel():
            TT.destroy()
            display.EditALevel(self)
        def viewLevel():
            TT.destroy()
            display.ViewALevel(self)
        def quit():
            TT.destroy()
            self.mainLoop=False
            self.abort_program=True
        TT=Tk()
        if self.displayIcon==True:
            TT.iconbitmap(self.icon)
        window_size_x=self.window_size_x
        window_size_y=self.window_size_y-110
        window_geometry=f"{window_size_x}x{window_size_y}"
        TT.geometry(window_geometry)
        TT.minsize(window_size_x,window_size_y)
        TT.title("Main Menu")
        TT['bg']=self.universalBackground
        TitleLabel=Label(TT,text="Create a Level for Wolf Escape",bg=self.universalBackground,anchor="center")
        TitleLabel.pack(side=TOP,fill=X)
        FrameMainButton=PanedWindow(TT, orient=HORIZONTAL,bg=self.universalBackground)
        FrameMainButton.pack(side=TOP,expand=Y,fill=X, pady=0, padx=0)
        Top=PanedWindow(FrameMainButton, orient=VERTICAL,bg=self.universalBackground)
        Top.pack(side=LEFT,expand=Y,fill=X, pady=2, padx=2)
        Bottom = PanedWindow(FrameMainButton, orient=VERTICAL,bg=self.universalBackground)
        Bottom.pack(side=LEFT,expand=Y,fill=X, pady=2, padx=2)
        Top.add(Button(Top,text="Create a Level",command=createLevel,bg=self.universalBackground))
        Bottom.add(Button(Bottom,text="Edit a level",command=editLevel,bg=self.universalBackground))

        Top.add(Button(Top,text="View a level",command=viewLevel,bg=self.universalBackground))
        Bottom.add(Button(Bottom,text="Quit",command=quit,bg=self.universalBackground))
        Top.pack()
        Bottom.pack()

        TT.mainloop()
    def CreateALevel(self):
        print("create a level")
        def Save(*args):
            content_of_grid=Get(*args)
            title=content_of_grid[0]
            content_of_grid=content_of_grid[1]
            print("writing")
            f=open(f"{self.path}/{title}.we","w")
            f.write(content_of_grid)
            f.close()
            print("Prompt")
            window_size_y=self.window_size_y-150
            window_geometry=f"{self.window_size_x}x{window_size_y}"
            TTT=Tk()
            TTT.geometry(window_geometry)
            TTT.minsize(self.window_size_x,window_size_y)
            TTT.title("File saved")
            TTT['bg']=self.universalBackground
            titleLabel=Label(TTT,text=f"File {title} was saved successfully.")
            titleLabel.pack(side=TOP)
            CloseButton=Button(TTT,text="Great",command=TTT.destroy)
            CloseButton.pack(side=TOP)
            TTT.mainloop()
        def Help():
            print("help")
            open_new_tab(f"{self.home}{self.LevelCreators}help/create_a_level")
        def preview(*args):
            print("preview")
            content=Get(*args)
            display.preview(self,content=content[1],title=content[0])
        def Get(*args):
            GridList=[
                [self.L1_R1, self.L1_R2, self.L1_R3, self.L1_R4, self.L1_R5, self.L1_R6, self.L1_R7, self.L1_R8, self.L1_R9, self.L1_R10, self.L1_R11, self.L1_R12, self.L1_R13, self.L1_R14, self.L1_R15, self.L1_R16, self.L1_R17, self.L1_R18, self.L1_R19, self.L1_R20, self.L1_R21, self.L1_R22, self.L1_R23,"^"],
                [self.L2_R1, self.L2_R2, self.L2_R3, self.L2_R4, self.L2_R5, self.L2_R6, self.L2_R7, self.L2_R8, self.L2_R9, self.L2_R10, self.L2_R11, self.L2_R12, self.L2_R13, self.L2_R14, self.L2_R15, self.L2_R16, self.L2_R17, self.L2_R18, self.L2_R19, self.L2_R20, self.L2_R21, self.L2_R22, self.L2_R23,"^"],
                [self.L3_R1, self.L3_R2, self.L3_R3, self.L3_R4, self.L3_R5, self.L3_R6, self.L3_R7, self.L3_R8, self.L3_R9, self.L3_R10, self.L3_R11, self.L3_R12, self.L3_R13, self.L3_R14, self.L3_R15, self.L3_R16, self.L3_R17, self.L3_R18, self.L3_R19, self.L3_R20, self.L3_R21, self.L3_R22, self.L3_R23,"^"],
                [self.L4_R1, self.L4_R2, self.L4_R3, self.L4_R4, self.L4_R5, self.L4_R6, self.L4_R7, self.L4_R8, self.L4_R9, self.L4_R10, self.L4_R11, self.L4_R12, self.L4_R13, self.L4_R14, self.L4_R15, self.L4_R16, self.L4_R17, self.L4_R18, self.L4_R19, self.L4_R20, self.L4_R21, self.L4_R22, self.L4_R23,"^"],
                [self.L5_R1, self.L5_R2, self.L5_R3, self.L5_R4, self.L5_R5, self.L5_R6, self.L5_R7, self.L5_R8, self.L5_R9, self.L5_R10, self.L5_R11, self.L5_R12, self.L5_R13, self.L5_R14, self.L5_R15, self.L5_R16, self.L5_R17, self.L5_R18, self.L5_R19, self.L5_R20, self.L5_R21, self.L5_R22, self.L5_R23,"^"],
                [self.L6_R1, self.L6_R2, self.L6_R3, self.L6_R4, self.L6_R5, self.L6_R6, self.L6_R7, self.L6_R8, self.L6_R9, self.L6_R10, self.L6_R11, self.L6_R12, self.L6_R13, self.L6_R14, self.L6_R15, self.L6_R16, self.L6_R17, self.L6_R18, self.L6_R19, self.L6_R20, self.L6_R21, self.L6_R22, self.L6_R23,"^"],
                [self.L7_R1, self.L7_R2, self.L7_R3, self.L7_R4, self.L7_R5, self.L7_R6, self.L7_R7, self.L7_R8, self.L7_R9, self.L7_R10, self.L7_R11, self.L7_R12, self.L7_R13, self.L7_R14, self.L7_R15, self.L7_R16, self.L7_R17, self.L7_R18, self.L7_R19, self.L7_R20, self.L7_R21, self.L7_R22, self.L7_R23,"^"],
                [self.L8_R1, self.L8_R2, self.L8_R3, self.L8_R4, self.L8_R5, self.L8_R6, self.L8_R7, self.L8_R8, self.L8_R9, self.L8_R10, self.L8_R11, self.L8_R12, self.L8_R13, self.L8_R14, self.L8_R15, self.L8_R16, self.L8_R17, self.L8_R18, self.L8_R19, self.L8_R20, self.L8_R21, self.L8_R22, self.L8_R23,"^"],
                [self.L9_R1, self.L9_R2, self.L9_R3, self.L9_R4, self.L9_R5, self.L9_R6, self.L9_R7, self.L9_R8, self.L9_R9, self.L9_R10, self.L9_R11, self.L9_R12, self.L9_R13, self.L9_R14, self.L9_R15, self.L9_R16, self.L9_R17, self.L9_R18, self.L9_R19, self.L9_R20, self.L9_R21, self.L9_R22, self.L9_R23,"^"],
                [self.L10_R1, self.L10_R2,self.L10_R3, self.L10_R4, self.L10_R5, self.L10_R6, self.L10_R7, self.L10_R8, self.L10_R9, self.L10_R10, self.L10_R11, self.L10_R12, self.L10_R13, self.L10_R14, self.L10_R15, self.L10_R16, self.L10_R17, self.L10_R18, self.L10_R19, self.L10_R20, self.L10_R21, self.L10_R22, self.L10_R23,"^"],
                [self.L11_R1, self.L11_R2, self.L11_R3, self.L11_R4, self.L11_R5, self.L11_R6, self.L11_R7, self.L11_R8, self.L11_R9, self.L11_R10, self.L11_R11, self.L11_R12, self.L11_R13, self.L11_R14, self.L11_R15, self.L11_R16, self.L11_R17,self.L11_R18, self.L11_R19, self.L11_R20, self.L11_R21, self.L11_R22, self.L11_R23,"^"],
                [self.L12_R1, self.L12_R2, self.L12_R3, self.L12_R4, self.L12_R5, self.L12_R6, self.L12_R7, self.L12_R8, self.L12_R9, self.L12_R10, self.L12_R11, self.L12_R12, self.L12_R13, self.L12_R14, self.L12_R15, self.L12_R16, self.L12_R17, self.L12_R18, self.L12_R19, self.L12_R20, self.L12_R21, self.L12_R22, self.L12_R23,"^"],
                [self.L13_R1, self.L13_R2, self.L13_R3, self.L13_R4, self.L13_R5, self.L13_R6, self.L13_R7, self.L13_R8, self.L13_R9, self.L13_R10, self.L13_R11, self.L13_R12, self.L13_R13, self.L13_R14, self.L13_R15, self.L13_R16, self.L13_R17, self.L13_R18, self.L13_R19, self.L13_R20, self.L13_R21, self.L13_R22, self.L13_R23,"^"],
                [self.L14_R1, self.L14_R2, self.L14_R3, self.L14_R4, self.L14_R5, self.L14_R6, self.L14_R7, self.L14_R8, self.L14_R9, self.L14_R10, self.L14_R11, self.L14_R12, self.L14_R13, self.L14_R14, self.L14_R15, self.L14_R16, self.L14_R17, self.L14_R18, self.L14_R19, self.L14_R20, self.L14_R21, self.L14_R22, self.L14_R23,"^"],
                [self.L15_R1, self.L15_R2, self.L15_R3, self.L15_R4, self.L15_R5, self.L15_R6, self.L15_R7, self.L15_R8, self.L15_R9, self.L15_R10, self.L15_R11, self.L15_R12, self.L15_R13, self.L15_R14, self.L15_R15, self.L15_R16, self.L15_R17, self.L15_R18, self.L15_R19, self.L15_R20, self.L15_R21, self.L15_R22, self.L15_R23,"^"],
                [self.L16_R1, self.L16_R2, self.L16_R3,self.L16_R4, self.L16_R5, self.L16_R6, self.L16_R7, self.L16_R8, self.L16_R9, self.L16_R10, self.L16_R11, self.L16_R12, self.L16_R13, self.L16_R14, self.L16_R15, self.L16_R16, self.L16_R17, self.L16_R18, self.L16_R19, self.L16_R20, self.L16_R21, self.L16_R22, self.L16_R23,"^"],
                [self.L17_R1, self.L17_R2, self.L17_R3, self.L17_R4, self.L17_R5, self.L17_R6, self.L17_R7, self.L17_R8, self.L17_R9, self.L17_R10, self.L17_R11, self.L17_R12, self.L17_R13, self.L17_R14, self.L17_R15, self.L17_R16, self.L17_R17, self.L17_R18, self.L17_R19, self.L17_R20, self.L17_R21, self.L17_R22, self.L17_R23,"^"],
                [self.L18_R1, self.L18_R2, self.L18_R3, self.L18_R4, self.L18_R5, self.L18_R6, self.L18_R7, self.L18_R8, self.L18_R9, self.L18_R10, self.L18_R11, self.L18_R12, self.L18_R13, self.L18_R14, self.L18_R15, self.L18_R16, self.L18_R17, self.L18_R18, self.L18_R19, self.L18_R20, self.L18_R21, self.L18_R22, self.L18_R23,"^"],
                [self.L19_R1, self.L19_R2, self.L19_R3, self.L19_R4, self.L19_R5, self.L19_R6, self.L19_R7, self.L19_R8, self.L19_R9, self.L19_R10, self.L19_R11, self.L19_R12, self.L19_R13, self.L19_R14, self.L19_R15, self.L19_R16, self.L19_R17, self.L19_R18, self.L19_R19, self.L19_R20, self.L19_R21, self.L19_R22, self.L19_R23,"^"],
                [self.L20_R1, self.L20_R2, self.L20_R3, self.L20_R4, self.L20_R5, self.L20_R6, self.L20_R7, self.L20_R8, self.L20_R9, self.L20_R10, self.L20_R11, self.L20_R12, self.L20_R13, self.L20_R14, self.L20_R15, self.L20_R16, self.L20_R17, self.L20_R18, self.L20_R19, self.L20_R20, self.L20_R21, self.L20_R22, self.L20_R23,"^"],
                ["^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",    "^"]
            ]
            print("save")
            print("title")
            title=TitleOfLevelLabel.get()
            print(title)
            # if os.path.exists(f"{RI.path}/{title}")==True:
            #     TTT=Tk()
            print("Grid")
            content_of_grid=""
            # print("self.L20_R23")
            # print(self.L20_R23.get())
            for i in range(len(GridList)):
                for b in range(len(GridList[i])):
                    print(f"i={i},b={b}")
                    if type(GridList[i][b])==type("e"):
                        content_of_grid+=f"{GridList[i][b]}|"
                    else:
                        g=GridList[i][b].get()
                        if len(g)==0:
                            content_of_grid+=f" |"
                        else:
                            content_of_grid+=f"{g}|"
                content_of_grid+="\n"
            content_of_grid+=f"\nLevel created with the software 'Create_levels', dedicated to creating levels for wolf escape.\nThis software was written by {self.watermark}."
            content_of_grid+=f"\nThe person who created this level:\nusername={self.username}\nuserDiscordTagAndID={self.userDiscordTagAndID}\nDiscordCodeID={self.DiscordCodeID}\nuserOtherSocialMedia={self.userOtherSocialMedia}\n"
            # print(content_of_grid)
            return title,content_of_grid
        def Discard(*args):
            title=TitleOfLevelLabel.get()
            print(f'Discarding {title}.we')
            if os.path.exists(f"{self.path}/{title}.we")==True:
                os.remove(f"{self.path}/{title}.we")
            elif os.path.exists(f"{self.path}/{title}")==True:
                os.remove(f"{self.path}/{title}") 
            else:
                pass
            TT.destroy()
            print(f"{title} discarded")
            success=f"The file {title} was successfully discarded."
            display.ShowSuccessMessage(self,message=success,ButtonText="Great")
            display.CreateALevel(self)
        def BackToMain():
            TT.destroy()
            display.mainMenu(self)
        def AvailableEnds():
            print("AvailableEnds")
            display.AvailableEnds(self)
        def AvailableDecoration():
            print("AvialableDecoration")
            display.AvailableDecoration(self)
        #20+1(hidden)x23+1(hidden)
        #hxL
        TT=Tk()
        if self.displayIcon==True:
            TT.iconbitmap(self.icon)
        window_size_x=self.window_size_x+310
        window_size_y=self.window_size_y+305
        window_geometry=f"{window_size_x}x{window_size_y}"
        TT.geometry(window_geometry)
        TT.minsize(window_size_x,window_size_y)
        TT.title("Create A Level")
        TT['bg']=self.universalBackground
        TitleLabel=Label(TT,text="Create a level.",bg=self.universalBackground,anchor="center")
        TitleLabel.pack(side=TOP,fill=X)
        FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
        FrameButton.pack(side=TOP,fill=X,padx=5)
        HelpButton=Button(FrameButton,text="?",bg=self.universalBackground,relief=GROOVE,command=Help)
        HelpButton.pack(side=RIGHT)
        FrameTitle=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
        FrameTitle.pack(side=TOP,fill=X,padx=5)
        LevelTitleLabel=Label(FrameTitle,text="Title of the level:",bg=self.universalBackground,anchor="center")
        LevelTitleLabel.pack(side=LEFT,fill=X)
        TitleOfLevelLabel=Entry(FrameTitle,bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=95)
        TitleOfLevelLabel.pack(side=LEFT)
        FrameButton2=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
        FrameButton2.pack(side=TOP,fill=X,padx=5)
        PreviewButton=Button(FrameButton,text="Preview",bg=self.universalBackground,relief=GROOVE,command=preview)
        PreviewButton.pack(side=LEFT)
        SaveButton=Button(FrameButton,text="Save",bg=self.universalBackground,relief=GROOVE,command=Save)
        SaveButton.pack(side=LEFT)
        DiscardButton=Button(FrameButton,text="Discard",bg=self.universalBackground,relief=GROOVE,command=Discard)
        DiscardButton.pack(side=LEFT)
        BackToMainButton=Button(FrameButton,text="Main Menu",bg=self.universalBackground,relief=GROOVE,command=BackToMain)
        BackToMainButton.pack(side=LEFT)
        EndSetButton=Button(FrameButton,text="Available Ends and start",bg=self.universalBackground,relief=GROOVE,command=AvailableEnds)
        EndSetButton.pack(side=LEFT)
        DecorationButton=Button(FrameButton,text="Available Decoration",bg=self.universalBackground,relief=GROOVE,command=AvailableDecoration)
        DecorationButton.pack(side=LEFT)
        FrameGrid=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
        FrameGrid.pack(side=TOP,fill=X,padx=20,pady=2)
        
        # for height in range(20):
        #     for length in range(23):

        FrameL1=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL1.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL2=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL2.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL3=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL3.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL4=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL4.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL5=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL5.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL6=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL6.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL7=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL7.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL8=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL8.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL9=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL9.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL10=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL10.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL11=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL11.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL12=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL12.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL13=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL13.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL14=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL14.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL15=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL15.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL16=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL16.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL17=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL17.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL18=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL18.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL19=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL19.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)
        FrameL20=Frame(FrameGrid,bg=self.universalBackground,borderwidth=0,relief=FLAT)
        FrameL20.pack(side=TOP,fill=X,padx=self.mid_line_padx,pady=self.mid_line_pady)

        self.L1_R1=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R2=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R3=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R4=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R5=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R6=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R7=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R8=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R9=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R10=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R11=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R12=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R13=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R14=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R15=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R16=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R17=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R18=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R19=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R20=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R21=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R22=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L1_R23=Entry(FrameL1, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L1_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L2_R1=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R2=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R3=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R4=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R5=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R6=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R7=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R8=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R9=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R10=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R11=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R12=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R13=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R14=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R15=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R16=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R17=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R18=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R19=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R20=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R21=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R22=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L2_R23=Entry(FrameL2, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L2_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L3_R1=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R2=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R3=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R4=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R5=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R6=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R7=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R8=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R9=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R10=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R11=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R12=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R13=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R14=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R15=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R16=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R17=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R18=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R19=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R20=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R21=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R22=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L3_R23=Entry(FrameL3, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L3_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L4_R1=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R2=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R3=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R4=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R5=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R6=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R7=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R8=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R9=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R10=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R11=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R12=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R13=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R14=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R15=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R16=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R17=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R18=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R19=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R20=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R21=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R22=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L4_R23=Entry(FrameL4, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L4_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L5_R1=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R2=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R3=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R4=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R5=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R6=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R7=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R8=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R9=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R10=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R11=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R12=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R13=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R14=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R15=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R16=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R17=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R18=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R19=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R20=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R21=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R22=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L5_R23=Entry(FrameL5, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L5_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L6_R1=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R2=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R3=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R4=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R5=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R6=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R7=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R8=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R9=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R10=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R11=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R12=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R13=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R14=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R15=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R16=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R17=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R18=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R19=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R20=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R21=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R22=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L6_R23=Entry(FrameL6, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L6_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L7_R1=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R2=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R3=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R4=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R5=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R6=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R7=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R8=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R9=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R10=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R11=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R12=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R13=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R14=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R15=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R16=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R17=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R18=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R19=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R20=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R21=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R22=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L7_R23=Entry(FrameL7, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L7_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L8_R1=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R2=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R3=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R4=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R5=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R6=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R7=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R8=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R9=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R10=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R11=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R12=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R13=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R14=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R15=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R16=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R17=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R18=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R19=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R20=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R21=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R22=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L8_R23=Entry(FrameL8, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L8_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L9_R1=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R2=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R3=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R4=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R5=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R6=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R7=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R8=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R9=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R10=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R11=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R12=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R13=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R14=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R15=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R16=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R17=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R18=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R19=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R20=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R21=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R22=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L9_R23=Entry(FrameL9, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L9_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L10_R1=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R2=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R3=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R4=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R5=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R6=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R7=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R8=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R9=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R10=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R11=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R12=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R13=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R14=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R15=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R16=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R17=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R18=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R19=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R20=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R21=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R22=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L10_R23=Entry(FrameL10, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L10_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L11_R1=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R2=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R3=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R4=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R5=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R6=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R7=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R8=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R9=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R10=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R11=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R12=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R13=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R14=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R15=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R16=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R17=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R18=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R19=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R20=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R21=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R22=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L11_R23=Entry(FrameL11, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L11_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L12_R1=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R2=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R3=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R4=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R5=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R6=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R7=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R8=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R9=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R10=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R11=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R12=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R13=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R14=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R15=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R16=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R17=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R18=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R19=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R20=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R21=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R22=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L12_R23=Entry(FrameL12, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L12_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L13_R1=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R2=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R3=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R4=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R5=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R6=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R7=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R8=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R9=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R10=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R11=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R12=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R13=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R14=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R15=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R16=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R17=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R18=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R19=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R20=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R21=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R22=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L13_R23=Entry(FrameL13, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L13_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L14_R1=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R2=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R3=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R4=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R5=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R6=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R7=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R8=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R9=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R10=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R11=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R12=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R13=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R14=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R15=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R16=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R17=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R18=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R19=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R20=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R21=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R22=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L14_R23=Entry(FrameL14, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L14_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L15_R1=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R2=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R3=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R4=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R5=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R6=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R7=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R8=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R9=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R10=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R11=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R12=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R13=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R14=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R15=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R16=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R17=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R18=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R19=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R20=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R21=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R22=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L15_R23=Entry(FrameL15, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L15_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L16_R1=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R2=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R3=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R4=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R5=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R6=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R7=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R8=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R9=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R10=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R11=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R12=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R13=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R14=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R15=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R16=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R17=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R18=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R19=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R20=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R21=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R22=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L16_R23=Entry(FrameL16, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L16_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L17_R1=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R2=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R3=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R4=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R5=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R6=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R7=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R8=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R9=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R10=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R11=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R12=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R13=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R14=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R15=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R16=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R17=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R18=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R19=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R20=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R21=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R22=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L17_R23=Entry(FrameL17, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L17_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L18_R1=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R2=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R3=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R4=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R5=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R6=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R7=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R8=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R9=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R10=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R11=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R12=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R13=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R14=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R15=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R16=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R17=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R18=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R19=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R20=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R21=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R22=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L18_R23=Entry(FrameL18, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L18_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L19_R1=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R2=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R3=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R4=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R5=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R6=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R7=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R8=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R9=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R10=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R11=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R12=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R13=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R14=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R15=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R16=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R17=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R18=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R19=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R20=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R21=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R22=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L19_R23=Entry(FrameL19, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L19_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)

        self.L20_R1=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R1.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R2=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R2.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R3=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R3.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R4=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R4.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R5=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R5.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R6=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R6.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R7=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R7.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R8=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R8.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R9=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R9.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R10=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R10.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R11=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R11.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R12=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R12.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R13=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R13.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R14=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R14.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R15=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R15.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R16=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R16.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R17=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R17.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R18=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R18.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R19=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R19.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R20=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R20.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R21=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R21.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R22=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R22.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        self.L20_R23=Entry(FrameL20, bg=self.grid_entry_background,fg=self.grid_entry_foreground,insertbackground=self.grid_insert_entry_background, width=4,relief=self.Entry_relief)
        self.L20_R23.pack(side=LEFT,padx=self.entry_padx,pady=self.entry_pady)
        # self.GridList=[
        #     [L1_R1, L1_R2, L1_R3, L1_R4, L1_R5, L1_R6, L1_R7, L1_R8, L1_R9, L1_R10, L1_R11, L1_R12, L1_R13, L1_R14, L1_R15, L1_R16, L1_R17, L1_R18, L1_R19, L1_R20, L1_R21, L1_R22, L1_R23,"^"],
        #     [L2_R1, L2_R2, L2_R3, L2_R4, L2_R5, L2_R6, L2_R7, L2_R8, L2_R9, L2_R10, L2_R11, L2_R12, L2_R13, L2_R14, L2_R15, L2_R16, L2_R17, L2_R18, L2_R19, L2_R20, L2_R21, L2_R22, L2_R23,"^"],
        #     [L3_R1, L3_R2, L3_R3, L3_R4, L3_R5, L3_R6, L3_R7, L3_R8, L3_R9, L3_R10, L3_R11, L3_R12, L3_R13, L3_R14, L3_R15, L3_R16, L3_R17, L3_R18, L3_R19, L3_R20, L3_R21, L3_R22, L3_R23,"^"],
        #     [L4_R1, L4_R2, L4_R3, L4_R4, L4_R5, L4_R6, L4_R7, L4_R8, L4_R9, L4_R10, L4_R11, L4_R12, L4_R13, L4_R14, L4_R15, L4_R16, L4_R17, L4_R18, L4_R19, L4_R20, L4_R21, L4_R22, L4_R23,"^"],
        #     [L5_R1, L5_R2, L5_R3, L5_R4, L5_R5, L5_R6, L5_R7, L5_R8, L5_R9, L5_R10, L5_R11, L5_R12, L5_R13, L5_R14, L5_R15, L5_R16, L5_R17, L5_R18, L5_R19, L5_R20, L5_R21, L5_R22, L5_R23,"^"],
        #     [L6_R1, L6_R2, L6_R3, L6_R4, L6_R5, L6_R6, L6_R7, L6_R8, L6_R9, L6_R10, L6_R11, L6_R12, L6_R13, L6_R14, L6_R15, L6_R16, L6_R17, L6_R18, L6_R19, L6_R20, L6_R21, L6_R22, L6_R23,"^"],
        #     [L7_R1, L7_R2, L7_R3, L7_R4, L7_R5, L7_R6, L7_R7, L7_R8, L7_R9, L7_R10, L7_R11, L7_R12, L7_R13, L7_R14, L7_R15, L7_R16, L7_R17, L7_R18, L7_R19, L7_R20, L7_R21, L7_R22, L7_R23,"^"],
        #     [L8_R1, L8_R2, L8_R3, L8_R4, L8_R5, L8_R6, L8_R7, L8_R8, L8_R9, L8_R10, L8_R11, L8_R12, L8_R13, L8_R14, L8_R15, L8_R16, L8_R17, L8_R18, L8_R19, L8_R20, L8_R21, L8_R22, L8_R23,"^"],
        #     [L9_R1, L9_R2, L9_R3, L9_R4, L9_R5, L9_R6, L9_R7, L9_R8, L9_R9, L9_R10, L9_R11, L9_R12, L9_R13, L9_R14, L9_R15, L9_R16, L9_R17, L9_R18, L9_R19, L9_R20, L9_R21, L9_R22, L9_R23,"^"],
        #     [L10_R1, L10_R2,L10_R3, L10_R4, L10_R5, L10_R6, L10_R7, L10_R8, L10_R9, L10_R10, L10_R11, L10_R12, L10_R13, L10_R14, L10_R15, L10_R16, L10_R17, L10_R18, L10_R19, L10_R20, L10_R21, L10_R22, L10_R23,"^"],
        #     [L11_R1, L11_R2, L11_R3, L11_R4, L11_R5, L11_R6, L11_R7, L11_R8, L11_R9, L11_R10, L11_R11, L11_R12, L11_R13, L11_R14, L11_R15, L11_R16, L11_R17,L11_R18, L11_R19, L11_R20, L11_R21, L11_R22, L11_R23,"^"],
        #     [L12_R1, L12_R2, L12_R3, L12_R4, L12_R5, L12_R6, L12_R7, L12_R8, L12_R9, L12_R10, L12_R11, L12_R12, L12_R13, L12_R14, L12_R15, L12_R16, L12_R17, L12_R18, L12_R19, L12_R20, L12_R21, L12_R22, L12_R23,"^"],
        #     [L13_R1, L13_R2, L13_R3, L13_R4, L13_R5, L13_R6, L13_R7, L13_R8, L13_R9, L13_R10, L13_R11, L13_R12, L13_R13, L13_R14, L13_R15, L13_R16, L13_R17, L13_R18, L13_R19, L13_R20, L13_R21, L13_R22, L13_R23,"^"],
        #     [L14_R1, L14_R2, L14_R3, L14_R4, L14_R5, L14_R6, L14_R7, L14_R8, L14_R9, L14_R10, L14_R11, L14_R12, L14_R13, L14_R14, L14_R15, L14_R16, L14_R17, L14_R18, L14_R19, L14_R20, L14_R21, L14_R22, L14_R23,"^"],
        #     [L15_R1, L15_R2, L15_R3, L15_R4, L15_R5, L15_R6, L15_R7, L15_R8, L15_R9, L15_R10, L15_R11, L15_R12, L15_R13, L15_R14, L15_R15, L15_R16, L15_R17, L15_R18, L15_R19, L15_R20, L15_R21, L15_R22, L15_R23,"^"],
        #     [L16_R1, L16_R2, L16_R3,L16_R4, L16_R5, L16_R6, L16_R7, L16_R8, L16_R9, L16_R10, L16_R11, L16_R12, L16_R13, L16_R14, L16_R15, L16_R16, L16_R17, L16_R18, L16_R19, L16_R20, L16_R21, L16_R22, L16_R23,"^"],
        #     [L17_R1, L17_R2, L17_R3, L17_R4, L17_R5, L17_R6, L17_R7, L17_R8, L17_R9, L17_R10, L17_R11, L17_R12, L17_R13, L17_R14, L17_R15, L17_R16, L17_R17, L17_R18, L17_R19, L17_R20, L17_R21, L17_R22, L17_R23,"^"],
        #     [L18_R1, L18_R2, L18_R3, L18_R4, L18_R5, L18_R6, L18_R7, L18_R8, L18_R9, L18_R10, L18_R11, L18_R12, L18_R13, L18_R14, L18_R15, L18_R16, L18_R17, L18_R18, L18_R19, L18_R20, L18_R21, L18_R22, L18_R23,"^"],
        #     [L19_R1, L19_R2, L19_R3, L19_R4, L19_R5, L19_R6, L19_R7, L19_R8, L19_R9, L19_R10, L19_R11, L19_R12, L19_R13, L19_R14, L19_R15, L19_R16, L19_R17, L19_R18, L19_R19, L19_R20, L19_R21, L19_R22, L19_R23,"^"],
        #     [L20_R1, L20_R2, L20_R3, L20_R4, L20_R5, L20_R6, L20_R7, L20_R8, L20_R9, L20_R10, L20_R11, L20_R12, L20_R13, L20_R14, L20_R15, L20_R16, L20_R17, L20_R18, L20_R19, L20_R20, L20_R21, L20_R22, L20_R23,"^"],
        #     ["^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",    "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",     "^",    "^"]
        #     ]
        
    def EditALevel(self):
        print("edit a level")
    def ViewALevel(self):
        print("View level")
    
    # def CreateALevel(self):
    #     def Generate(*args):
    #         e=Title.get()

e=boot.initialise()
RI=boot(main=e[0],main_dict=e[1],links=[],version=__version__,Author=__Author__,SoftwareName=__SoftwareName__)
RI.links=boot.initialise_links(e)
# for i in RI.links:
#     print(i)
# pause=input("Press enter to continue...")
# boot.TKinter.window.FetchingFiles(RI)
if import_error==True:
    RI.abort_program=True
RI.abort_program=True
display.AvailableDecoration(RI)
while RI.abort_program==False:
    if RI.abort_program==False and RI.loginValidated==False:
        display.getInfo(RI)
    if RI.abort_program==False and RI.loginValidated==True:
        display.mainMenu(RI)