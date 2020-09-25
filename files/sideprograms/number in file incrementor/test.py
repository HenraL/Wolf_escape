for b in range(600):
    print("b= ",b)
    f=open("test.txt","r")
    test=f.read()
    f.close
    if len(test)==0:
        f=open("test.txt","w")
        f.write("0")
        f.close()
        test=0
    List=[]
    List.append(test)
    for i in List:
        #a=List[i]
        print("i=",i)
        
        if i.isnumeric()==True:
            test=int(i)
            print("success")
            f=open("test.txt","w")
            f.write(str(test+10000))
            f.close()
        else:
            print("fail")
            f=open("test.txt","w")
            f.write("1")
            f.close()

pause=input("Press enter to continue...")
