#revisiting the levels (again)
file="""
a|e|azea|ze|aeaze|a|eaeazez|aezae|azezaea|eaeae|aeaeaee\n
a|z|eaea|zea|eaeazeaz|eaezae|aezae|zae|zajj|jza|ea|zezae\n
a|e|a|ea|zeaz|ezaezaez|aezaez|aezae|aez|aeza|ea|eza|ezaea\n
a|e|a|z|e|azea|eazeaeae|azezae|zaeaz|eza|ea|ea|eaeae|aeaee\n
a|z|e|a|e|azeae|aeazeaze|aezaea|ezaez|ae|zaj|jj|zae|az|ezae\n
a|e|a|e|a|z|eaze|zaezaezae|zaeza|ezaea|ezaeza|e|ae|zae|z|aea\n
a|e|a|z|e|a|z|eae|azeaeaeaz|ezaez|aeaze|zaeaeae|aea|ea|ea|e|e\n
a|z|e|a|e|a|z|e|ae|aeazeazea|ezaea|ezaez|aez|ajjj|za|ea|z|ezae\n
a|e|a|e|a|z|e|a|z|e|zaezaezae|zaeza|ez|aea|ez|aezae|ae|zae|zaea\n
a|e|a|z|e|a|z|e|a|e|azeaeaeaze|zae|za|eazez|aea|eaea|eae|ae|a|ee\n
a|z|e|a|e|a|z|e|a|e|a|eazeazeae|zaeae|zae|za|ez|ajj|jz|ae|aze|zae\n
a|e|a|e|a|z|e|a|z|e|z|a|ezaezaez|aezae|za|eae|zaeza|ea|e|zaez|a|ra\n"""
fiile="""1|a|e|azea|ze|aeaze|a|eaeazez|aezae|azezaea|eaeae|aeaeaee
2|a|z|eaea|zea|eaeazeaz|eaezae|aezae|zae|zajj|jza|ea|zezae
3|a|e|a|ea|zeaz|ezaezaez|aezaez|aezae|aez|aeza|ea|eza|ezaea
4|a|e|a|z|e|azea|eazeaeae|azezae|zaeaz|eza|ea|ea|eaeae|aeaee
5|a|z|e|a|e|azeae|aeazeaze|aezaea|ezaez|ae|zaj|jj|zae|az|ezae
6|a|e|a|e|a|z|eaze|zaezaezae|zaeza|ezaea|ezaeza|e|ae|zae|z|aea
7|a|e|a|z|e|a|z|eae|azeaeaeaz|ezaez|aeaze|zaeaeae|aea|ea|ea|e|e
8|a|z|e|a|e|a|z|e|ae|aeazeazea|ezaea|ezaez|aez|ajjj|za|ea|z|ezae
9|a|e|a|e|a|z|e|a|z|e|zaezaezae|zaeza|ez|aea|ez|aezae|ae|zae|zaea
10|a|e|a|z|e|a|z|e|a|e|azeaeaeaze|zae|za|eazez|aea|eaea|eae|ae|a|ee
11|a|z|e|a|e|a|z|e|a|e|a|eazeazeae|zaeae|zae|za|ez|ajj|jz|ae|aze|zae
12|a|e|a|e|a|z|e|a|z|e|z|a|ezaezaez|aezae|za|eae|zaeza|ea|e|zaez|a|ra"""

fiiile="""1|#23:38 20/10/20201|2|3|4
2|#23:55 20/10/20202|2|3|4
"""

CreatingGameLine=""
GameLine=[]
CreatingGameSprite=""
GameSprite=[]
#with fiile as file:
    #for line in file:
     #   if line!="\n":
      #     CreatingGameLine+=line
       # elif line=="\n":
        #    GameLine.append(CreatingGameLine)
         #   CratingGameLine=""

for line in fiile:
    if line!="\n":
        CreatingGameLine+=line
    elif line=="\n":
        GameLine.append(CreatingGameLine)
        CreatingGameLine=""

#print(GameLine)

CreatingGameLine2=""
GameLine2=[]
CreatingGameSprite2=""
GameSprite2=[]
for line in fiiile:
    if line!="|" and line!="\n":
        CreatingGameSprite2+=line
        #print("line=",line)
        #print("CreatingGameSprite2=",CreatingGameSprite2)
    elif line=="|" and line!="\n":
        #print("CreatingGameSprite2=",CreatingGameSprite2)
        #print("GameSprite2=",GameSprite2)
        GameSprite2.append(CreatingGameSprite2)
        CreatingGameSprite2=""
    elif line=="\n":
        GameLine2.append(GameSprite2)
        CreatingGameLine2=""
        GameSprite2=[]

print(GameLine2)
