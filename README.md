# Sullix
TUI front-end for swww wallpaper tool.

Dependencies:
swww (make sure that swww-daemon is running)
pip

And make sure you are on a wayland environment that would need swww (don't be on x11 or be on a full desktop environment like KDE Plasma)

To install run the following:


1. git clone https://github.com/tersellers91/Sullix.git
2. cd Sullix
3. sudo pip install -e .
4. To run the tool, just type Sullix in your terminal. It looks for the wallpapers in the Pictures directory in your /home/name folder. Ex:/home/greg/Pictures/wallpaper.png


On step 3, if you receive a message talking about some environment that is externally managed, instead use the command "sudo pip install -e . --break-system-packages"


How to uninstall:

sudo pip uninstall Sullix (--break-system-packages) 


That's it.
