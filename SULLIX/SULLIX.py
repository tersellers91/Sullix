from pathlib import Path
import questionary
from pyfiglet import figlet_format
from subprocess import run
import os
# Questionary is a very simple TUI module

# Stuff for finding files paths:

home = Path.home()
true_dir = str(home) + '/Pictures'
items = os.listdir(true_dir)



questionary.print(figlet_format('SULLIX', font='broadway', width=150))

picker = questionary.select('Choose your wallpaper', choices=items).ask()



run('swww img ' + str(home) + '/Pictures/' + picker, shell=True)





