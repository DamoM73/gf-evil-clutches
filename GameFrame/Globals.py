
class Globals:

    """
    Holds the overall game information and variables that can be accessed 
    from any code file. 
    """
    
    # - Indicate that the game is in play
    running = True
    
    # - Set the screen redrawn rate
    FRAMES_PER_SECOND = 30
    
    # - Set the screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # - Tracks the players score
    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name
    window_name = 'GF Game'

    # - Set the order of the rooms
    levels = ["WelcomeScreen","EndScreen"]

    # - Set the starting level
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends
    end_game_level = 1

    # - This variable keeps track of the room that will follow the current room
    # - Change this value to move through rooms in a non-sequential manner 
    next_level = 0

    # - Change variable to True to exit the program
    exiting = False


    # ----- User Defined Global Variables below this line ----- #

    
