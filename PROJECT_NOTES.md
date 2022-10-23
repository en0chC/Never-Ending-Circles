# Notes:
-	Cite everything
-	Keep track of time spent on project and enter timesheet form, 
	this is for each checkpoint (TP1, TP2, TP3)
-	Include library in the project file
-	Note down any changes, design modifications, and progress on the 
	project



# To Do:
- 	Add buffer time at the start of the game to ensure 
everything is first displayed and then the countdown started



# Features to Add:
TP 1
- 	Start countdown


TP 2
- 	Score based on how on time the player is - Perfect multiplier
- 	Stats - Progress through level
- 	Pop up state - "Perfect", "Early", "Late"


TP 3
- 	Speed up multiplier that increases score multiplier
- 	Invincible mode
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


# File Structure
__main__.py | file loaded to run the game

-	assets
	-	sprites

game.py | main game loop

utils.py | helper functions