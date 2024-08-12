from pick import pick
from src.makePluginYAML import init

def infoRequest():
    api, index = pick(["5.0.0", "4.0.0"], "Quelle est la version de PocketMine que vous souhaitez utiliser?")
    print(api)
    pluginName = input("Merci de renseigner le nom de votre plugin: ").strip()
    author = input("Merci de renseigner votre username: ").strip()
    version = input("Merci de renseigner la version de votre plugin: ").strip()
    return [pluginName, author, version, api]

info = infoRequest()
while not init(info[0], info[1], info[2], info[3]):
    info = infoRequest()

