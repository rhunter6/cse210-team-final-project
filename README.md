# Final Project - Mine Sweeper
This is a game where using logic and a bit of luck you can clear the board of all of the mines.  Hopefully without getting blown up first!

Left click to dig out a square and expose what is beneath the surface, but be careful because if you dig up a mine it will blow up and you will lose. We have also buried a lot of clues for you to find so if you dig up a number it will let you know exactly how many mines are touching it.

If you are sure, you know where a mine is right click on it once to mark it with a flag, if you are not 100% sure right click twice to make it a question mark, and a third right click will return it to its original value so you can act like you were not even there. 

That is pretty much it.  Once you have dug up every hole that does not have a min in it YOU WIN!


## Getting Started
---
Make sure you have Python 3.8.0 or newer and Arcade 2.1 or newer installed 
and running on your machine. You can install Arcade by opening a terminal 
and running the following command.
```
$ python -m pip install arcade
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 minesweeper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the minesweeper folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- minesweeper         (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Arcade 2.1

## Features to Include 
---
THIS SECTION IS TABBED OUT TO BE EASIER TO READ IF YOU DOWNLOAD IT OR HIT THE EDIT BUTTON!

#1 = must have
#2 = nice to have
#3 = just for fun if there is time

Start Screen #1
    select grid size #2
    start button #1
    game instructions #1

Grid Screen (Game Board) #1
    grid #1
    mines #1
    clues #1
        these are the numbers that will surround the mines
    scoreboard #1
        count of flags remaining #2
        count of mines remaining #2
    reset button #1
        make button interactive when clicked #3
            on click #3
            after click still alive #3
            after click dead #3 

Win Screen #1
    make it a fun screen with a guy that digs up all of the mines #3

Lose Screen #1
    make it a fun scene #3

## Timeline
---
We will complete this project over the next 4 weeks
    Week 1. Initial brainstorm and planning, create readme file. (this week)
    Week 2. Identify all classes and modules build frame of game.
    Week 3. Write functions and get game functioning.
    Week 4. Workout any bugs and make game enhancements if there is time.
    Week 5. Finalize enhancements and rollout game.


## Authors
---
Jermey Diamond socjeremyd@gmail.com
