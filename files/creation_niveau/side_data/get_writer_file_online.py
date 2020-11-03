import requests

def filefetch(url,dest,name):
    myfile = requests.get(url)
    open("{}/{}".format(dest,name), 'wb').write(myfile.content)

url = 'https://www.python.org/static/img/python-logo@2x.png'
# dest="C:/Users/Henry PC/Documents/001 Github prog Sharing/Wolf_escape/files/creation_niveau/create level"
# dest="C:/Users/Henry PC/Documents/001 Github prog Sharing/Wolf_escape/files/creation_niveau/create level/getdone"
dest="getdone"
name="PythonImage.png"
filefetch(url,dest,name)

url="https://repl.it/@HanraLatalliar/Sprites#Spritelist.py"
name="Spritelist.{}".format("html")
filefetch(url,dest,name)

url="https://raw.githubusercontent.com/HenraL/Wolf_escape_Sprite/main/file/Common_file/Spritelist.py"
name="Spritelist_git.{}".format("py")
filefetch(url,dest,name)