from pathlib import Path
import questionary
from pyfiglet import figlet_format
from subprocess import run
import os

# Using questionary TUI because it is very simple


# Stuff for finding files paths:



def main():
    home = Path.home()
    natural = str(home) + '/Build/Sullix/file.txt'
    true_dir = str(home) + '/Pictures'
    items = os.listdir(true_dir)
    
    if not Path(natural).exists():
        question = questionary.text('Would you like to also enable pywal?')
        answer = question.ask()
        if answer == 'yes' or answer == 'Yes' or answer == 'y' or answer == 'Y':
            f = open(natural, 'w')
            f.write('True')
            f.close()
        elif answer == 'no':
            f = open(natural, 'w')
            f.write('False')
            f.close()
    questionary.print(figlet_format('SULLIX', font='broadway', width=150))

    picker = questionary.select('Choose your wallpaper', choices=items).ask()



    run('swww img ' + str(home) + '/Pictures/' + picker + ' --transition-type wipe', shell=True)
    if Path(natural).exists():
        with open(natural, 'r') as file:
            value = file.read().strip()
        if value == 'True':
            run('wal -i' + str(home) + '/Pictures/' + picker, shell=True)
        elif value == 'False':
            pass
if __name__ == '__main__':
    main()


