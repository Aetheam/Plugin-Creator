from pick import pick
from src.makePluginYAML import makePluginYAML
from src.makeMainFile import makeMainFile
import os
def infoRequest():
    api, index = pick(["5.0.0", "4.0.0"], "Quelle est la version de PocketMine que vous souhaitez utiliser?")
    print(api)
    pluginName = input("Merci de renseigner le nom de votre plugin: ").strip()
    author = input("Merci de renseigner votre username: ").strip()
    version = input("Merci de renseigner la version de votre plugin: ").strip()
    return [pluginName, author, version, api]


info = infoRequest()
while not makePluginYAML(info[0], info[1], info[2], info[3]):
    info = infoRequest()
    
full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), info[0])
makeMainFile(info[1], info[0], full_path)

