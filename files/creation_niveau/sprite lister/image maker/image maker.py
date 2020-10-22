image=[]
line=[]
ddd="""       /\                                                                        /\ 
      /  \                                                                      /  \ 
     / |  \                                                                    / |  \ 
    /  |   \                                                                  /  |   \ 
   /   |    \                                                                /   |    \ 
  /    _     \                                                              /    _     \ 
 /    |_|     \  !L'action à laquelle vous vous apprêtez est irréversible  /    |_|     \ 
/______________\      êtes-vous sûre de vouloir supprimer ce sprite?!     /______________\ 

"""

for i in ddd:
    if i!='\n':
        line.append("{}".format(i))
    elif i=="\n":
        image.append(line)
        line=[]

print(line)
f=open("results.txt","w")
f.write("image={}\n".format(image))
f.close()

face="""   __________
  / __   __  \\
 / |__| |__|  \\
|              |
 \\ \\________/ /
  \\__________/

"""
line=[]
image=[]
for i in face:
    if i!='\n':
        line.append("{}".format(i))
    elif i=="\n":
        image.append(line)
        line=[]

print(line)
f=open("results.txt","a")
f.write("face={}\n".format(image))
f.close()

facesad="""   __________
  / __   __  \\
 / |__| |__|  \\
|   ________   |
 \\ /        \\ /
  \\__________/

"""
line=[]
image=[]
for i in facesad:
    if i!='\n':
        line.append("{}".format(i))
    elif i=="\n":
        image.append(line)
        line=[]

print(line)
f=open("results.txt","a")
f.write("facesad={}\n".format(image))
f.close()
