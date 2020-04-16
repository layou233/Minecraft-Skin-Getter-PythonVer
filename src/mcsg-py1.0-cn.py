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

if input('请选择模式(输入序号):\n1 - 通过游戏ID获取皮肤\n2 - 通过UUID获取皮肤\n') == "1":
     q="游戏ID"
else:
     q="UUID"
i=input('请输入'+q+'\n')
if q == "游戏ID":
     sign=getUuid(i)
else:
     sign=i
url=getSkinUrl(sign)
print(i,'的皮肤文件链接为',url)
input('\n使用 回车 在浏览器中打开')
webbrowser.open(url)
