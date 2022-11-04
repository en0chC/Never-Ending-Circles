# Notes:
-	Cite everything
-	Keep track of time spent on project and enter timesheet form, 
	this is for each checkpoint (TP1, TP2, TP3)
-	Include library in the project file
-	Note down any changes, design modifications, and progress on the 
	project



# Features to Add:
TP 1
- 	Start countdown


TP 2
- 	Score based on how on time the player is - Perfect multiplier
- 	Stats - Progress through level
- 	Pop up state - "Perfect", "Early", "Late"


TP 3
-	Multiple lives to prevent immediate fail
- 	Speed up multiplier that increases score multiplier
- 	Online Leaderboard
-	Level Editor (If time allows)
-	AI creating levels when given a sound file (If time allows)



# Time Track:
Project Proposal
-	8pm - 11pm
-	7:30pm - 8:30pm
Competitive Analysis
-	9pm - 9:40pm
Tech Demo
-	3pm - 4pm
-	8pm - 10pm
Learning pygame, proper object and file structure, etc
-	10:45am - 12:15pm
-	2:30pm - 5:00pm
Writing code (With some time spent learning more pygame functions)
-	12:15pm - 12:30pm
-	5:00pm - 12:00pm
-	9:00pm - 12:00pm
TP2:
Tile Design
-	11:30am - 1:30pm
Writing code
-	1:30pm - 11:00pm
-	12:30pm - 1:00am
-	11:00pm - 1:00am
Updating Design Docs
- 	12:30pm - 1:00pm



# TP2 Progress
-	Added Center Snap Camera
-	Added Level class
	-	Takes array that contains formatted information on tiles
		of the level and goes through each tile in sequence,
		creating Tile class instances to set up the level
-	Added Music class
-	Added Speed Change and Reverse Direction tile modifiers
-	Added fail state and sound effect
-	Created all tile type images
-	Reorganized code structure to allow for game states
-	Added different game states
	-	Title Screen, Main Menu
-	Score System
-	Checkpoint Tile

-	Invincible Mode option
-	Second Level



# TP2 Updates
-	gameState.py file
-	Not using pydub library anymore, mixer in pygame is sufficient and
	less cumbersome since there is a delay when starting pydub music
-	No save file system, user scores will be stored on a server
-	It seems that pygame mixer has a starting positioning inaccuracy
	so I may need to use another library



# TP2 Progress
-	Smooth camera
-	Background


# TP2 Updates
-	Renamed game.py to neverEndingCircles.py
-	background.py