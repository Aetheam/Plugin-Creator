import os

def init(author, pluginName, full_path):
    mainFile = os.path.join(full_path, "src", author.lower(), pluginName.lower(), "Main.php")
    with open(mainFile, 'w') as file:
        file.write(f"<?php\n")
        file.write(f"namespace {str.lower(author)}\\{str.lower(pluginName)};\n\n")
        file.write(f"use pocketmine\plugin\PluginBase;\n\n")
        file.write(f'class Main extends PluginBase  {{\n\n')
        file.write(f'   protected function onEnable(): void\n       {{\n        }}\n\n')
        file.write(f'}}')