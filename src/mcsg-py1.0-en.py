#作者 Github@layou233
#从原mcsg.js脚本重写
import base64, json, webbrowser
from urllib import request
def getUuid(playerName):
     url="https://api.mojang.com/users/profiles/minecraft/"+playerName #Mojang API
     return json.loads(request.urlopen(url).read().decode("utf-8"))["id"]
def getSkinUrl(uuid):
     url="https://sessionserver.mojang.com/session/minecraft/profile/"+uuid #Mojang API
     return json.loads(base64.b64decode(json.loads(request.urlopen(url).read().decode("utf-8"))["properties"][0]["value"]).decode("utf-8"))["textures"]["SKIN"]["url"]

if input('Choose the working mode(enter the number):\n1 - Get skin through playername\n2 - Get skin through UUID\n') == "1":
     q="Playername"
else:
     q="UUID"
i=input('Enter the'+q+'\n')
if q == "Playername":
     sign=getUuid(i)
else:
     sign=i
url=getSkinUrl(sign)
print('The skin URL of '+i+' is\n',url)
input('\nUse Enter to open it in your browser')
webbrowser.open(url)
