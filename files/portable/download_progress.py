from tkinter import *
import os,shutil,requests
from time import sleep

class root:
    def __init__(self,liste):
        self.a=""
        self.All_the_versions1=liste#[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,10]
        self.All_the_versions=[]
        for b in range(2):
            for i in range(len(self.All_the_versions1)):
                self.All_the_versions.append(self.All_the_versions1[i])
        self.version=11
        self.window_size_x=820
        self.window_size_y=300
        self.window_geometry=f"{self.window_size_x}x{self.window_size_y}"
        self.universalBackground="white"
        self.text_cells_width=100
        self.watermark=".."
class boot(root):
    print("class get")    
    class TKinter(root):
        class window:
            #                  1=self,2=list_to_use,3=ProgressBar,4=TT,  5=CurrentFile,6=Progress,7=ProgressWindow,8=def_to_call
            def updateProgress(self,    list_to_use,  To,           window,LabelInfo,    progress,  progressInfo,    def_to_call):
                def update_Status_bar(string,inc,windows):
                    #print(string)
                    colorF="lightGreen"
                    windows.insert(float(inc),string,"taged")
                    windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorF}")
                def update_Status_log(string,inc,windows):
                    #print(string)
                    colorF="lightGreen"
                    colorB="black"
                    windows.insert(float(inc),string,"taged")
                    windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorB}")
                def cleanText(windows):
                    windows.delete("1.0","end")
                error_files={}
                o=a=prev=0
                max_list_length=len(list_to_use)
                print(f"list_to_use={list_to_use}")
                for i in range(len(list_to_use)):#range(-1):
                    taux=(i/max_list_length)*100
                    current_width_progress=int(101*taux/100)
                    print(f"current_width_progress={current_width_progress}")
                    #sleep(0.5)#1)
                    LabelInfo.config(text=f"Checking if file {list_to_use[i]} exists")
                    progress.config(text=f"Checked {i}/{len(list_to_use)-1} files")
                    inc=0.0
                    if os.path.exists(i)==True:
                        def_to_call()
                        if prev<current_width_progress:
                            update_Status_bar(string=f".",inc=inc,windows=To)
                        update_Status_log(string=f"\n{i} {list_to_use[i]}{a}[EXISTS]",inc=inc,windows=progressInfo)
                    else:
                        def_to_call()
                        error_files[i]="[Not Found]"
                        LabelInfo.config(text=f"Downloading file {list_to_use[i]}")
                        if prev<current_width_progress:
                            update_Status_bar(string=f".",inc=inc,windows=To)
                        update_Status_log(string=f"\n{i} {list_to_use[i]}{a}[Not Found]",inc=inc,windows=progressInfo)
                    window.update()
                    o+=1
                    prev=current_width_progress
                return error_files
            # def updateProgress(self,LabelInfo,progress,element,percentage,ProgressIndex,nb_of_files,success,prev,To,FileIndex,ifSuccess,progressInfo,error_files,ifNotSuccess,window):
            #     def update_Status_bar(string,inc,windows,colorF):
            #         #print(string)
            #         windows.insert(float(inc),string,"taged")
            #         windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorF}")
            #     def update_Status_log(string,inc,windows,colorF):
            #         #print(string)
            #         colorB="black"
            #         windows.insert(float(inc),string,"taged")
            #         windows.tag_config(f"taged",foreground=f"{colorF}",background=f"{colorB}")
            #     def cleanText(windows):
            #         windows.delete("1.0","end")
            #     a=get.numberOfDots
            #     print(f"element={element}")
            #     print(f"current_width_progress={percentage}")
            #     LabelInfo.config(text=f"Checking if file {element} exists")
            #     progress.config(text=f"Checked {ProgressIndex}/{nb_of_files} files")
            #     inc=0.0
            #     if success==True:
            #         if prev<percentage:
            #             update_Status_bar(string=f".",inc=inc,windows=To,colorF="lightGreen")
            #         update_Status_log(string=f"\n{FileIndex} {element}{a}[{ifSuccess}]",inc=inc,windows=progressInfo,colorF="lightGreen")
            #     else:
            #         error_files[FileIndex]=f"[{ifNotSuccess}]"
            #         LabelInfo.config(text=f"Failed for {element}")
            #         if prev<percentage:
            #             update_Status_bar(string=f".",inc=inc,windows=To,colorF="red")
            #         update_Status_log(string=f"\n{i} {element}{a}[{ifNotSuccess}]",inc=inc,windows=progressInfo,colorF="lightRed")
            #     window.update()
            #     return error_files
            def update_Status(string,inc,windows):
                print(string)
                windows.insert(float(inc),string)
            def FetchingFiles(self,def_to_call,list_to_use):
                print("Checking files...")
                TT=Tk()
                TT.geometry(self.window_geometry)
                TT.minsize(self.window_size_x,self.window_size_y)
                TT.title("Checking and downloading")
                TT['bg']=self.universalBackground
                TitleLabel=Label(TT,text="Checking if required files are present.",bg=self.universalBackground,anchor="w")
                TitleLabel.pack(side=TOP,fill=X)
                CurrentFile=Label(TT,text="Checking if file   exists",bg=self.universalBackground,anchor="w")
                CurrentFile.pack(side=TOP,fill=X)
                Progress=Label(TT,text="",bg=self.universalBackground,anchor="w")
                Progress.pack(side=TOP,fill=X)
                ProgressBar=Text(TT,state="normal",
                                    insertbackground="lightGreen",#"white",
                                    fg="lightGreen",#"black",#"white",
                                    exportselection=0,
                                    width=self.text_cells_width,height=1,
                                    padx=5,pady=5,relief=FLAT,
                                    bg="white",
                                    cursor="watch",wrap="none",tabs="1c"#,
            
            #padx=0,pady=0,
                                    )#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressBar.pack()
                ProgressWindow=Text(TT,state="normal",
                                    insertbackground="lightGreen",#"white",
                                    fg="lightGreen",#"black",#"white",
                                    exportselection=0,
                                    width=self.text_cells_width,height=10,
                                    padx=5,pady=5,relief=FLAT,
                                    bg="black",
                                    cursor="watch",wrap="none",tabs="1c"#,
            
            #padx=0,pady=0,
                                    )#,font=(self.FontBoard,self.SizeBoard,self.weightB))
                ProgressWindow.pack()
                boot.TKinter.window.updateProgress(self,list_to_use,ProgressBar,TT,CurrentFile,Progress,ProgressWindow,def_to_call)
                FrameButton=Frame(TT,bg=self.universalBackground,borderwidth=1,relief=FLAT)#"green"
                FrameButton.pack(side=TOP,fill=X)
                DownloadButton=Button(FrameButton,text="Great!",command=TT.destroy,bg=self.universalBackground)
                DownloadButton.pack(side=TOP,fill=X)
                MessageLabel=Label(TT,text=self.watermark,bg=self.universalBackground,anchor="center")
                MessageLabel.pack(side=RIGHT,fill=X)
                TT.mainloop()
class boot2(root):
    """Give the function a list and links and a window will show you the download progress and files downloaded"""
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
            print(lst_to)
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
        folder2_6=["img","ingame","accueil.png","accueilm.png","endv.png","mur.png","start.png","wolf_icon.ico","wolf_icon.png","funkyWalls","wall_beige_black.png","wall_beige_white.png","wall_birght_red_black.png","wall_birght_red_white.png","wall_black_white.png","wall_brigth_orange_black.png","wall_brigth_orange_white.png","wall_brigth_pink_black.png","wall_brigth_pink_white.png","wall_chocolat_black.png","wall_chocolat_white.png","wall_darks_red_black.png","wall_darks_red_white.png","wall_dark_blue_black.png","wall_dark_blue_white.png","wall_dark_green_black.png","wall_dark_green_white.png","wall_dark_purple_black.png","wall_dark_purple_white.png","wall_grey_black.png","wall_grey_white.png","wall_light_blue_black.png","wall_light_blue_white.png","wall_light_green_black.png","wall_light_green_white.png","wall_light_grey_black.png","wall_light_grey_white.png","wall_light_purple_black.png","wall_light_purple_white.png","wall_medium_blue_black.png","wall_medium_blue_white.png","wall_orange_black.png","wall_orange_white.png","wall_very_light_blue_black.png","wall_very_light_blue_white.png","wall_yellow_black.png","wall_yellow_white.png","snipsets","bric.png","snipsets.zip","wall_beige.png","wall_birght_red.png","wall_black.png","wall_brigth_orange.png","wall_brigth_pink.png","wall_chocolat.png","wall_darks_red.png","wall_dark_blue.png","wall_dark_green.png","wall_dark_purple.png","wall_grey.png","wall_light_blue.png","wall_light_green.png","wall_light_grey.png","wall_light_purple.png","wall_medium_blue.png","wall_orange.png","wall_very_light_blue.png","wall_wire_frame.png","wall_wire_frame_white.png","wall_wire_frame_white_red_bricks.png","wall_yellow.png","wall_white.png"]#
        folder2_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'ingame': {'type': 'dir', 'fileName': 'ingame'}, 'accueil.png': {'type': 'file', 'fileName': 'accueil.png', 'fileContent': ''}, 'accueilm.png': {'type': 'file', 'fileName': 'accueilm.png', 'fileContent': ''}, 'endv.png': {'type': 'file', 'fileName': 'endv.png', 'fileContent': ''}, 'mur.png': {'type': 'file', 'fileName': 'mur.png', 'fileContent': ''}, 'start.png': {'type': 'file', 'fileName': 'start.png', 'fileContent': ''}, 'wolf_icon.ico': {'type': 'file', 'fileName': 'wolf_icon.ico', 'fileContent': ''}, 'wolf_icon.png': {'type': 'file', 'fileName': 'wolf_icon.png', 'fileContent': ''}, 'funkyWalls': {'type': 'dir', 'fileName': 'funkyWalls'}, 'wall_beige_black.png': {'type': 'file', 'fileName': 'wall_beige_black.png', 'fileContent': ''}, 'wall_beige_white.png': {'type': 'file', 'fileName': 'wall_beige_white.png', 'fileContent': ''}, 'wall_birght_red_black.png': {'type': 'file', 'fileName': 'wall_birght_red_black.png', 'fileContent': ''}, 'wall_birght_red_white.png': {'type': 'file', 'fileName': 'wall_birght_red_white.png', 'fileContent': ''}, 'wall_black_white.png': {'type': 'file', 'fileName': 'wall_black_white.png', 'fileContent': ''}, 'wall_brigth_orange_black.png': {'type': 'file', 'fileName': 'wall_brigth_orange_black.png', 'fileContent': ''}, 'wall_brigth_orange_white.png': {'type': 'file', 'fileName': 'wall_brigth_orange_white.png', 'fileContent': ''}, 'wall_brigth_pink_black.png': {'type': 'file', 'fileName': 'wall_brigth_pink_black.png', 'fileContent': ''}, 'wall_brigth_pink_white.png': {'type': 'file', 'fileName': 'wall_brigth_pink_white.png', 'fileContent': ''}, 'wall_chocolat_black.png': {'type': 'file', 'fileName': 'wall_chocolat_black.png', 'fileContent': ''}, 'wall_chocolat_white.png': {'type': 'file', 'fileName': 'wall_chocolat_white.png', 'fileContent': ''}, 'wall_darks_red_black.png': {'type': 'file', 'fileName': 'wall_darks_red_black.png', 'fileContent': ''}, 'wall_darks_red_white.png': {'type': 'file', 'fileName': 'wall_darks_red_white.png', 'fileContent': ''}, 'wall_dark_blue_black.png': {'type': 'file', 'fileName': 'wall_dark_blue_black.png', 'fileContent': ''}, 'wall_dark_blue_white.png': {'type': 'file', 'fileName': 'wall_dark_blue_white.png', 'fileContent': ''}, 'wall_dark_green_black.png': {'type': 'file', 'fileName': 'wall_dark_green_black.png', 'fileContent': ''}, 'wall_dark_green_white.png': {'type': 'file', 'fileName': 'wall_dark_green_white.png', 'fileContent': ''}, 'wall_dark_purple_black.png': {'type': 'file', 'fileName': 'wall_dark_purple_black.png', 'fileContent': ''}, 'wall_dark_purple_white.png': {'type': 'file', 'fileName': 'wall_dark_purple_white.png', 'fileContent': ''}, 'wall_grey_black.png': {'type': 'file', 'fileName': 'wall_grey_black.png', 'fileContent': ''}, 'wall_grey_white.png': {'type': 'file', 'fileName': 'wall_grey_white.png', 'fileContent': ''}, 'wall_light_blue_black.png': {'type': 'file', 'fileName': 'wall_light_blue_black.png', 'fileContent': ''}, 'wall_light_blue_white.png': {'type': 'file', 'fileName': 'wall_light_blue_white.png', 'fileContent': ''}, 'wall_light_green_black.png': {'type': 'file', 'fileName': 'wall_light_green_black.png', 'fileContent': ''}, 'wall_light_green_white.png': {'type': 'file', 'fileName': 'wall_light_green_white.png', 'fileContent': ''}, 'wall_light_grey_black.png': {'type': 'file', 'fileName': 'wall_light_grey_black.png', 'fileContent': ''}, 'wall_light_grey_white.png': {'type': 'file', 'fileName': 'wall_light_grey_white.png', 'fileContent': ''}, 'wall_light_purple_black.png': {'type': 'file', 'fileName': 'wall_light_purple_black.png', 'fileContent': ''}, 'wall_light_purple_white.png': {'type': 'file', 'fileName': 'wall_light_purple_white.png', 'fileContent': ''}, 'wall_medium_blue_black.png': {'type': 'file', 'fileName': 'wall_medium_blue_black.png', 'fileContent': ''}, 'wall_medium_blue_white.png': {'type': 'file', 'fileName': 'wall_medium_blue_white.png', 'fileContent': ''}, 'wall_orange_black.png': {'type': 'file', 'fileName': 'wall_orange_black.png', 'fileContent': ''}, 'wall_orange_white.png': {'type': 'file', 'fileName': 'wall_orange_white.png', 'fileContent': ''}, 'wall_very_light_blue_black.png': {'type': 'file', 'fileName': 'wall_very_light_blue_black.png', 'fileContent': ''}, 'wall_very_light_blue_white.png': {'type': 'file', 'fileName': 'wall_very_light_blue_white.png', 'fileContent': ''}, 'wall_yellow_black.png': {'type': 'file', 'fileName': 'wall_yellow_black.png', 'fileContent': ''}, 'wall_yellow_white.png': {'type': 'file', 'fileName': 'wall_yellow_white.png', 'fileContent': ''}, 'snipsets': {'type': 'dir', 'fileName': 'snipsets'}, 'bric.png': {'type': 'file', 'fileName': 'bric.png', 'fileContent': ''}, 'snipsets.zip': {'type': 'file', 'fileName': 'snipsets.zip', 'fileContent': ''}, 'wall_beige.png': {'type': 'file', 'fileName': 'wall_beige.png', 'fileContent': ''}, 'wall_birght_red.png': {'type': 'file', 'fileName': 'wall_birght_red.png', 'fileContent': ''}, 'wall_black.png': {'type': 'file', 'fileName': 'wall_black.png', 'fileContent': ''}, 'wall_brigth_orange.png': {'type': 'file', 'fileName': 'wall_brigth_orange.png', 'fileContent': ''}, 'wall_brigth_pink.png': {'type': 'file', 'fileName': 'wall_brigth_pink.png', 'fileContent': ''}, 'wall_chocolat.png': {'type': 'file', 'fileName': 'wall_chocolat.png', 'fileContent': ''}, 'wall_darks_red.png': {'type': 'file', 'fileName': 'wall_darks_red.png', 'fileContent': ''}, 'wall_dark_blue.png': {'type': 'file', 'fileName': 'wall_dark_blue.png', 'fileContent': ''}, 'wall_dark_green.png': {'type': 'file', 'fileName': 'wall_dark_green.png', 'fileContent': ''}, 'wall_dark_purple.png': {'type': 'file', 'fileName': 'wall_dark_purple.png', 'fileContent': ''}, 'wall_grey.png': {'type': 'file', 'fileName': 'wall_grey.png', 'fileContent': ''}, 'wall_light_blue.png': {'type': 'file', 'fileName': 'wall_light_blue.png', 'fileContent': ''}, 'wall_light_green.png': {'type': 'file', 'fileName': 'wall_light_green.png', 'fileContent': ''}, 'wall_light_grey.png': {'type': 'file', 'fileName': 'wall_light_grey.png', 'fileContent': ''}, 'wall_light_purple.png': {'type': 'file', 'fileName': 'wall_light_purple.png', 'fileContent': ''}, 'wall_medium_blue.png': {'type': 'file', 'fileName': 'wall_medium_blue.png', 'fileContent': ''}, 'wall_orange.png': {'type': 'file', 'fileName': 'wall_orange.png', 'fileContent': ''}, 'wall_very_light_blue.png': {'type': 'file', 'fileName': 'wall_very_light_blue.png', 'fileContent': ''}, 'wall_wire_frame.png': {'type': 'file', 'fileName': 'wall_wire_frame.png', 'fileContent': ''}, 'wall_wire_frame_white.png': {'type': 'file', 'fileName': 'wall_wire_frame_white.png', 'fileContent': ''}, 'wall_wire_frame_white_red_bricks.png': {'type': 'file', 'fileName': 'wall_wire_frame_white_red_bricks.png', 'fileContent': ''}, 'wall_yellow.png': {'type': 'file', 'fileName': 'wall_yellow.png', 'fileContent': ''}, 'wall_white.png': {'type': 'file', 'fileName': 'wall_white.png', 'fileContent': ''}}#
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
        folder2_9_1_4=["img","tut_image","alphabet","punctuation","and.PNG","at.PNG","border.png","bracketclosed.PNG","bracketopen.PNG","colum.PNG","dot.PNG","endboard.PNG","exclamation.PNG","paragraph.PNG","paragraph_fermé.PNG","paragraph_ouvert.PNG","questionmark.PNG","[.PNG","].PNG","æ.PNG"]
        folder2_9_1_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'punctuation': {'type': 'dir', 'fileName': 'punctuation'}, 'and.PNG': {'type': 'file', 'fileName': 'and.PNG', 'fileContent': ''}, 'at.PNG': {'type': 'file', 'fileName': 'at.PNG', 'fileContent': ''}, 'border.png': {'type': 'file', 'fileName': 'border.png', 'fileContent': ''}, 'bracketclosed.PNG': {'type': 'file', 'fileName': 'bracketclosed.PNG', 'fileContent': ''}, 'bracketopen.PNG': {'type': 'file', 'fileName': 'bracketopen.PNG', 'fileContent': ''}, 'colum.PNG': {'type': 'file', 'fileName': 'colum.PNG', 'fileContent': ''}, 'dot.PNG': {'type': 'file', 'fileName': 'dot.PNG', 'fileContent': ''}, 'endboard.PNG': {'type': 'file', 'fileName': 'endboard.PNG', 'fileContent': ''}, 'exclamation.PNG': {'type': 'file', 'fileName': 'exclamation.PNG', 'fileContent': ''}, 'paragraph.PNG': {'type': 'file', 'fileName': 'paragraph.PNG', 'fileContent': ''}, 'paragraph_fermé.PNG': {'type': 'file', 'fileName': 'paragraph_fermé.PNG', 'fileContent': ''}, 'paragraph_ouvert.PNG': {'type': 'file', 'fileName': 'paragraph_ouvert.PNG', 'fileContent': ''}, 'questionmark.PNG': {'type': 'file', 'fileName': 'questionmark.PNG', 'fileContent': ''}, '[.PNG': {'type': 'file', 'fileName': '[.PNG', 'fileContent': ''}, '].PNG': {'type': 'file', 'fileName': '].PNG', 'fileContent': ''}, 'æ.PNG': {'type': 'file', 'fileName': 'æ.PNG', 'fileContent': ''}}
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
        return main_for_rec,main_for_rec_dict
    def initialise_links(e):
        links=[]
        for i in range(len(e[1])):
            links.append(boot.get.make_links(e[1][i]))

        return links
# boot n°1
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
folder2_6=["img","ingame","accueil.png","accueilm.png","endv.png","mur.png","start.png","wolf_icon.ico","wolf_icon.png","funkyWalls","wall_beige_black.png","wall_beige_white.png","wall_birght_red_black.png","wall_birght_red_white.png","wall_black_white.png","wall_brigth_orange_black.png","wall_brigth_orange_white.png","wall_brigth_pink_black.png","wall_brigth_pink_white.png","wall_chocolat_black.png","wall_chocolat_white.png","wall_darks_red_black.png","wall_darks_red_white.png","wall_dark_blue_black.png","wall_dark_blue_white.png","wall_dark_green_black.png","wall_dark_green_white.png","wall_dark_purple_black.png","wall_dark_purple_white.png","wall_grey_black.png","wall_grey_white.png","wall_light_blue_black.png","wall_light_blue_white.png","wall_light_green_black.png","wall_light_green_white.png","wall_light_grey_black.png","wall_light_grey_white.png","wall_light_purple_black.png","wall_light_purple_white.png","wall_medium_blue_black.png","wall_medium_blue_white.png","wall_orange_black.png","wall_orange_white.png","wall_very_light_blue_black.png","wall_very_light_blue_white.png","wall_yellow_black.png","wall_yellow_white.png","snipsets","bric.png","snipsets.zip","wall_beige.png","wall_birght_red.png","wall_black.png","wall_brigth_orange.png","wall_brigth_pink.png","wall_chocolat.png","wall_darks_red.png","wall_dark_blue.png","wall_dark_green.png","wall_dark_purple.png","wall_grey.png","wall_light_blue.png","wall_light_green.png","wall_light_grey.png","wall_light_purple.png","wall_medium_blue.png","wall_orange.png","wall_very_light_blue.png","wall_wire_frame.png","wall_wire_frame_white.png","wall_wire_frame_white_red_bricks.png","wall_yellow.png","wall_white.png"]#
folder2_6_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'ingame': {'type': 'dir', 'fileName': 'ingame'}, 'accueil.png': {'type': 'file', 'fileName': 'accueil.png', 'fileContent': ''}, 'accueilm.png': {'type': 'file', 'fileName': 'accueilm.png', 'fileContent': ''}, 'endv.png': {'type': 'file', 'fileName': 'endv.png', 'fileContent': ''}, 'mur.png': {'type': 'file', 'fileName': 'mur.png', 'fileContent': ''}, 'start.png': {'type': 'file', 'fileName': 'start.png', 'fileContent': ''}, 'wolf_icon.ico': {'type': 'file', 'fileName': 'wolf_icon.ico', 'fileContent': ''}, 'wolf_icon.png': {'type': 'file', 'fileName': 'wolf_icon.png', 'fileContent': ''}, 'funkyWalls': {'type': 'dir', 'fileName': 'funkyWalls'}, 'wall_beige_black.png': {'type': 'file', 'fileName': 'wall_beige_black.png', 'fileContent': ''}, 'wall_beige_white.png': {'type': 'file', 'fileName': 'wall_beige_white.png', 'fileContent': ''}, 'wall_birght_red_black.png': {'type': 'file', 'fileName': 'wall_birght_red_black.png', 'fileContent': ''}, 'wall_birght_red_white.png': {'type': 'file', 'fileName': 'wall_birght_red_white.png', 'fileContent': ''}, 'wall_black_white.png': {'type': 'file', 'fileName': 'wall_black_white.png', 'fileContent': ''}, 'wall_brigth_orange_black.png': {'type': 'file', 'fileName': 'wall_brigth_orange_black.png', 'fileContent': ''}, 'wall_brigth_orange_white.png': {'type': 'file', 'fileName': 'wall_brigth_orange_white.png', 'fileContent': ''}, 'wall_brigth_pink_black.png': {'type': 'file', 'fileName': 'wall_brigth_pink_black.png', 'fileContent': ''}, 'wall_brigth_pink_white.png': {'type': 'file', 'fileName': 'wall_brigth_pink_white.png', 'fileContent': ''}, 'wall_chocolat_black.png': {'type': 'file', 'fileName': 'wall_chocolat_black.png', 'fileContent': ''}, 'wall_chocolat_white.png': {'type': 'file', 'fileName': 'wall_chocolat_white.png', 'fileContent': ''}, 'wall_darks_red_black.png': {'type': 'file', 'fileName': 'wall_darks_red_black.png', 'fileContent': ''}, 'wall_darks_red_white.png': {'type': 'file', 'fileName': 'wall_darks_red_white.png', 'fileContent': ''}, 'wall_dark_blue_black.png': {'type': 'file', 'fileName': 'wall_dark_blue_black.png', 'fileContent': ''}, 'wall_dark_blue_white.png': {'type': 'file', 'fileName': 'wall_dark_blue_white.png', 'fileContent': ''}, 'wall_dark_green_black.png': {'type': 'file', 'fileName': 'wall_dark_green_black.png', 'fileContent': ''}, 'wall_dark_green_white.png': {'type': 'file', 'fileName': 'wall_dark_green_white.png', 'fileContent': ''}, 'wall_dark_purple_black.png': {'type': 'file', 'fileName': 'wall_dark_purple_black.png', 'fileContent': ''}, 'wall_dark_purple_white.png': {'type': 'file', 'fileName': 'wall_dark_purple_white.png', 'fileContent': ''}, 'wall_grey_black.png': {'type': 'file', 'fileName': 'wall_grey_black.png', 'fileContent': ''}, 'wall_grey_white.png': {'type': 'file', 'fileName': 'wall_grey_white.png', 'fileContent': ''}, 'wall_light_blue_black.png': {'type': 'file', 'fileName': 'wall_light_blue_black.png', 'fileContent': ''}, 'wall_light_blue_white.png': {'type': 'file', 'fileName': 'wall_light_blue_white.png', 'fileContent': ''}, 'wall_light_green_black.png': {'type': 'file', 'fileName': 'wall_light_green_black.png', 'fileContent': ''}, 'wall_light_green_white.png': {'type': 'file', 'fileName': 'wall_light_green_white.png', 'fileContent': ''}, 'wall_light_grey_black.png': {'type': 'file', 'fileName': 'wall_light_grey_black.png', 'fileContent': ''}, 'wall_light_grey_white.png': {'type': 'file', 'fileName': 'wall_light_grey_white.png', 'fileContent': ''}, 'wall_light_purple_black.png': {'type': 'file', 'fileName': 'wall_light_purple_black.png', 'fileContent': ''}, 'wall_light_purple_white.png': {'type': 'file', 'fileName': 'wall_light_purple_white.png', 'fileContent': ''}, 'wall_medium_blue_black.png': {'type': 'file', 'fileName': 'wall_medium_blue_black.png', 'fileContent': ''}, 'wall_medium_blue_white.png': {'type': 'file', 'fileName': 'wall_medium_blue_white.png', 'fileContent': ''}, 'wall_orange_black.png': {'type': 'file', 'fileName': 'wall_orange_black.png', 'fileContent': ''}, 'wall_orange_white.png': {'type': 'file', 'fileName': 'wall_orange_white.png', 'fileContent': ''}, 'wall_very_light_blue_black.png': {'type': 'file', 'fileName': 'wall_very_light_blue_black.png', 'fileContent': ''}, 'wall_very_light_blue_white.png': {'type': 'file', 'fileName': 'wall_very_light_blue_white.png', 'fileContent': ''}, 'wall_yellow_black.png': {'type': 'file', 'fileName': 'wall_yellow_black.png', 'fileContent': ''}, 'wall_yellow_white.png': {'type': 'file', 'fileName': 'wall_yellow_white.png', 'fileContent': ''}, 'snipsets': {'type': 'dir', 'fileName': 'snipsets'}, 'bric.png': {'type': 'file', 'fileName': 'bric.png', 'fileContent': ''}, 'snipsets.zip': {'type': 'file', 'fileName': 'snipsets.zip', 'fileContent': ''}, 'wall_beige.png': {'type': 'file', 'fileName': 'wall_beige.png', 'fileContent': ''}, 'wall_birght_red.png': {'type': 'file', 'fileName': 'wall_birght_red.png', 'fileContent': ''}, 'wall_black.png': {'type': 'file', 'fileName': 'wall_black.png', 'fileContent': ''}, 'wall_brigth_orange.png': {'type': 'file', 'fileName': 'wall_brigth_orange.png', 'fileContent': ''}, 'wall_brigth_pink.png': {'type': 'file', 'fileName': 'wall_brigth_pink.png', 'fileContent': ''}, 'wall_chocolat.png': {'type': 'file', 'fileName': 'wall_chocolat.png', 'fileContent': ''}, 'wall_darks_red.png': {'type': 'file', 'fileName': 'wall_darks_red.png', 'fileContent': ''}, 'wall_dark_blue.png': {'type': 'file', 'fileName': 'wall_dark_blue.png', 'fileContent': ''}, 'wall_dark_green.png': {'type': 'file', 'fileName': 'wall_dark_green.png', 'fileContent': ''}, 'wall_dark_purple.png': {'type': 'file', 'fileName': 'wall_dark_purple.png', 'fileContent': ''}, 'wall_grey.png': {'type': 'file', 'fileName': 'wall_grey.png', 'fileContent': ''}, 'wall_light_blue.png': {'type': 'file', 'fileName': 'wall_light_blue.png', 'fileContent': ''}, 'wall_light_green.png': {'type': 'file', 'fileName': 'wall_light_green.png', 'fileContent': ''}, 'wall_light_grey.png': {'type': 'file', 'fileName': 'wall_light_grey.png', 'fileContent': ''}, 'wall_light_purple.png': {'type': 'file', 'fileName': 'wall_light_purple.png', 'fileContent': ''}, 'wall_medium_blue.png': {'type': 'file', 'fileName': 'wall_medium_blue.png', 'fileContent': ''}, 'wall_orange.png': {'type': 'file', 'fileName': 'wall_orange.png', 'fileContent': ''}, 'wall_very_light_blue.png': {'type': 'file', 'fileName': 'wall_very_light_blue.png', 'fileContent': ''}, 'wall_wire_frame.png': {'type': 'file', 'fileName': 'wall_wire_frame.png', 'fileContent': ''}, 'wall_wire_frame_white.png': {'type': 'file', 'fileName': 'wall_wire_frame_white.png', 'fileContent': ''}, 'wall_wire_frame_white_red_bricks.png': {'type': 'file', 'fileName': 'wall_wire_frame_white_red_bricks.png', 'fileContent': ''}, 'wall_yellow.png': {'type': 'file', 'fileName': 'wall_yellow.png', 'fileContent': ''}, 'wall_white.png': {'type': 'file', 'fileName': 'wall_white.png', 'fileContent': ''}}#
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
folder2_9_1_4=["img","tut_image","alphabet","punctuation","and.PNG","at.PNG","border.png","bracketclosed.PNG","bracketopen.PNG","colum.PNG","dot.PNG","endboard.PNG","exclamation.PNG","paragraph.PNG","paragraph_fermé.PNG","paragraph_ouvert.PNG","questionmark.PNG","[.PNG","].PNG","æ.PNG"]
folder2_9_1_4_dict={'img': {'type': 'dir', 'fileName': 'img'}, 'tut_image': {'type': 'dir', 'fileName': 'tut_image'}, 'alphabet': {'type': 'dir', 'fileName': 'alphabet'}, 'punctuation': {'type': 'dir', 'fileName': 'punctuation'}, 'and.PNG': {'type': 'file', 'fileName': 'and.PNG', 'fileContent': ''}, 'at.PNG': {'type': 'file', 'fileName': 'at.PNG', 'fileContent': ''}, 'border.png': {'type': 'file', 'fileName': 'border.png', 'fileContent': ''}, 'bracketclosed.PNG': {'type': 'file', 'fileName': 'bracketclosed.PNG', 'fileContent': ''}, 'bracketopen.PNG': {'type': 'file', 'fileName': 'bracketopen.PNG', 'fileContent': ''}, 'colum.PNG': {'type': 'file', 'fileName': 'colum.PNG', 'fileContent': ''}, 'dot.PNG': {'type': 'file', 'fileName': 'dot.PNG', 'fileContent': ''}, 'endboard.PNG': {'type': 'file', 'fileName': 'endboard.PNG', 'fileContent': ''}, 'exclamation.PNG': {'type': 'file', 'fileName': 'exclamation.PNG', 'fileContent': ''}, 'paragraph.PNG': {'type': 'file', 'fileName': 'paragraph.PNG', 'fileContent': ''}, 'paragraph_fermé.PNG': {'type': 'file', 'fileName': 'paragraph_fermé.PNG', 'fileContent': ''}, 'paragraph_ouvert.PNG': {'type': 'file', 'fileName': 'paragraph_ouvert.PNG', 'fileContent': ''}, 'questionmark.PNG': {'type': 'file', 'fileName': 'questionmark.PNG', 'fileContent': ''}, '[.PNG': {'type': 'file', 'fileName': '[.PNG', 'fileContent': ''}, '].PNG': {'type': 'file', 'fileName': '].PNG', 'fileContent': ''}, 'æ.PNG': {'type': 'file', 'fileName': 'æ.PNG', 'fileContent': ''}}
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
print(f"len(main_for_rec)={len(main_for_rec)}")
boot_with_number_1=False
if boot_with_number_1==True:
    RI=root(main_for_rec)
    def a():
        print("a worked")
    All_the_versions=[]
    for i in range(len(RI.All_the_versions1)):
        print(f"i={i}")
        for b in range(len(RI.All_the_versions1[i])):
            All_the_versions.append(RI.All_the_versions1[i][b])
    boot.TKinter.window.FetchingFiles(RI,a,All_the_versions)
else:
    e=boot.initialise()
    RI=boot(main=e[0],main_dict=e[1],links=[])
    RI.links=boot.initialise_links(e)
    for i in RI.links:
        print(i)
    boot.TKinter.window.FetchingFiles(RI)