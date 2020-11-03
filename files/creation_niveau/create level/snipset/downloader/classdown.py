class dealsys:
    def __init__(DS,currentd,namespf,filenamebool):
        # global DS
        DS.cd=currentd
        DS.spf=namespf
        DS.fbool=filenamebool
        # DS.slash=slash
    def pause():
        pause=input("Please press enter to continue...")
    def checkos():
        global slash
        if platform.system()=="Windows":
           slash="\\"
        else:
            slash="/"
        return slash
    def getCurrent(slash):
        global currentd
        currentd=os.getcwd()
        currentd+=slash
        return currentd
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

class getimg (dealsys):
    def checkndownloadsubfold(current,innerBackground):
        for i in range(len(innerBackground)):
            getimg.getName(current,"{}".format(innerBackground[i]))
            if filenamebool==False:
                getimg.create("{}".format(current),"img")
    def check_inner_img(current,innerimglist):
        for i in range(len(innerimglist)):
            if i==0:
                getimg.getName(current,"{}".format(innerimglist[i]))
            else:
                getimg.getName(current,"img{}{}".format(slash,innerimglist[i]))
            
            if filenamebool==False:
                if i==0:
                    getimg.create("img","{}".format(current))
                elif i==1:
                    getimg.create("{}{}img{}background".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}background{}".format(current,slash,slash,slash))
                elif i==2:
                    getimg.create("{}{}img{}Credits".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}Credits{}".format(current,slash,slash,slash))
                elif i==3:
                    getimg.create("{}{}img{}end".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}end{}".format(current,slash,slash,slash))
                elif i==4:
                    getimg.create("{}{}img{}Follow-me".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}Follow-me{}".format(current,slash,slash,slash))
                elif i==5:
                    getimg.create("{}{}img{}ingame".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}ingame{}".format(current,slash,slash,slash))
                elif i==6:
                    getimg.create("{}{}img{}launch_load".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}launch_load{}".format(current,slash,slash,slash))
                elif i==7:
                    getimg.create("{}{}img{}sprite".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}sprite{}".format(current,slash,slash,slash))
                elif i==8:
                    getimg.create("{}{}img{}tut_image".format(current,slash,slash),"{}{}img".format(current,slash))
                    getimg.checkndownloadsubfold("{}{}img{}tut_image{}".format(current,slash,slash,slash))
   
