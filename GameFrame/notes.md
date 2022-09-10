# GameFrame Folder

This folder holds most of the code provided by GameFrame. 

When making a game, the only file in this folder that you need to edit is the `Globals.py` file. 

## `__init__.py` 

Inside folders there is a file called `__init__.py` It is this file that allows us to group files into different folders and still have the game know where to find everything. 

Whenever we add a file to a folder, we need to add an entry to the `__init__.py` file in the same folder to let the rest of the program know that the new file is there.

## `GameFrame/Globals.py`

The `Globals.py` file holds the overall game information and variables that can be accessed from any code file. As well as editing the `Globals.py` file to set game information, you may need to access or update information in the file from other parts of the program. 

To do this you need to import the file as follows: 

``` python
from GameFrame import Globals
```

### Variables

#### `running` 

This variable indicates that the game is in play. 

Set this variable to False to end the game. 

``` python
Globals.running = False
```

#### `FRAMES_PER_SECOND `

This variable sets how often the screen is redrawn. It is set by default to 30 times every second. If this rate is increased (or decreased), all movement must be adjusted accordingly. If an object moves 5 pixels every frame, then it will travel further in a second at 40 Frames per second (200 pixels), than it will at 30 (150 pixels). 

#### `SCREEN_WIDTH` 

The width of the game screen. By default this is set to 800

#### `SCREEN_HEIGHT`

The height of the game screen. By default this is set to 600 

#### `SCORE` 

This variable is provided to track a players score and is initially set to 0. 

#### `LIVES` 

This variable is provided to track a players lives and is initially set to 3. 

#### `window_name` 

The text that is stored in this variable will be displayed on the game window. 

#### `levels` 

This is an array that hold the names of all the levels in the game, in the order that a player progresses through them. The names in this array, must match with files that are in the `Rooms` folder. 

An example could be 

``` python
Levels = [‘StartScreen’, ‘MazeLevel’, ‘PlatformLevel’, ‘EndScreen’]
```

#### `start_level` 

The level index from the levels array, that will be launched when the game starts, this is usually 0 (the first item) 

#### `end_game_level` 

The level index from the levels array, that will be run when the game ends (usually an end screen or high score screen)