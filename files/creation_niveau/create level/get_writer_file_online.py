import requests

def filefetch(url,dest,name):
    myfile = requests.get(url)
    open("{}/{}".format(dest,name), 'wb').write(myfile.content)

url = 'https://www.python.org/static/img/python-logo@2x.png'
dest="C:/Users/Henry PC/Documents/001 Github prog Sharing/Wolf_escape/files/creation_niveau/create level"
name="PythonImage.png"
filefetch(url,dest,name)

url="https://repl.it/@HanraLatalliar/Sprites#Spritelist.py"
name="Spritelist.{}".format("html")
filefetch(url,dest,name)
