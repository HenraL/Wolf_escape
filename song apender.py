continnue=1
chosen=False
song=[]
while continnue:
    if chosen==False:
        tipe=input("What command do you whant to use? (1) !play, (2) !lyrics, (3) !queued, (4) !remove")
        try:
            tipe=int(tipe)
            if tipe==1:tipe="!play "
            elif tipe==2:tipe="!lyrics "
            elif tipe==3:tipe="!queue "
            elif tipe==4:tipe="!remove "
            else: tipe="!play "
            chosen=True
        except:
            print("please only enter a number.")
    else:
        getname=input("Please enter the name of the desired song\n{}".format(tipe))
        song.append("{}{}".format(tipe,getname))
        getcont=input("Do you which to add an annother song? [(y)es/(n)o]")
        if getcont=="y" or getcont=="Y":
            continnue=1
        else:
            continnue=0

for i in range(len(song)):
    print(song[i])
