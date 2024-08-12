from pick import pick
import os
import makeMainFile
def makePluginYAML(pluginName, author, version, api):
    # Prompt the user for confirmation
    validation, index = pick(
        ["oui", "non"],
        "Vous avez sélectionné :\n"
        f"Plugin name: {pluginName}\n"
        f"Auteur: {author}\n"
        f"API: {api}\n"
        f"Version: {version}\n"
        "Confirmez-vous ce choix ?"
    )

    if validation == "oui":
        full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), pluginName)
        try:
            os.mkdir(full_path)
            os.makedirs(os.path.join(full_path, "src", author.lower(), pluginName.lower()), exist_ok=True)
            print(f"Directory '{full_path}' a été créé")
            pluginFile = os.path.join(full_path, "plugin.yml")
            with open(pluginFile, 'w') as file:
                file.write(f"name: {pluginName}\n")
                file.write(f"author: {author}\n")
                file.write(f"version: {version}\n")
                file.write(f"api: {api}\n")
                file.write(f"main: {str.lower(author)}\\{str.lower(pluginName)}\\Main")
            
            print(f"Fichier 'plugin.yml' créé à l'emplacement: {pluginFile}")
        except FileExistsError:
            print("Dossier déjà créé")
        
        return True
    else:
        print("Création du plugin annulée.")
        return False
if __name__ == "__main__":
    init()