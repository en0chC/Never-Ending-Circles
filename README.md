# Never Ending Circles
Repository for my 15-112 Term Project called "Never Ending Circles"
This project will be based on the rhythm game “A Dance of Fire 
and Ice”. In the game the player will guide two circles that are 
constantly orbiting one another, and the only input that the 
player needs to play is a keypress whenever a circle overlaps 
the path that has been set to be in time with the beat or melody 
of the music. 

# How to Run the Game:
Run the __main__.py file to start the game.
Use w and s or up and down arrow keys to navigate the menus and
press enter to select a menu option.
When you load a level, press enter to start playing, there will
be a countdown timer and as soon as it reaches 0, the game starts.
Be sure to start playing as soon as the timer reaches 0 as it is
designed to reach 0 right before the circle starts overlapping
the tiles.
The keys "f", "j", "d" and "k" are the input keys that need to be 
pressed when the circle overlaps the tile.
At any time in a level (except during the countdown), press the
escape key to open the pause menu where you can exit to the main
menu and toggle "Invincible mode on or off.
When "Invincible" mode is on, the circles will automatically snap
onto the tiles without needing any player input. Note that the
leaderboard will not be updated if you have turned on "Invincible"
mode. If you wish to disable this feature to test server functions
edit line 699 in the gameStates.py file.

# How to install any needed libraries
The libraries are included in the project files but if need be, 
to install pygame and vlc, open up the command prompt and enter
"pip install pygame" and "pip install python-vlc"

# List of shortcut commands
-	Escape key to open up the pause menu during a game
-	r key to restart the level anytime while playing the level
