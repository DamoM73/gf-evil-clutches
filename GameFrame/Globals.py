
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
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800

    # - Tracks the players score
    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name
    window_name = "Space Rescue"

    # - Set the order of the rooms
    levels = ["WelcomeScreen","Instructions","GamePlay","EndScreen"]

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
    
    # ship vaiables
    ship_speed = 10
    ship_type = "Swerve"
    
    # skills variables
    skill_active = False
    skill_available = True
    skill_duration = 30
    skill_cooldown = 300
    
    # asteroid variables
    asteroid_min_spawn = 15        # ticks of game clock
    asteroid_max_spawn = 150       # ticks of game clock
    asteroid_speed = 10
    
    # laser variables
    laser_speed = 20
    laser_max = 1
    unharmed_kill_count = 0
    
    # astronaut variables
    astronaut_min_spawn = 30         # ticks of game clock
    astronaut_max_spawn = 200        # ticks of game clock
    astronaut_speed = 5
    
    # astronaut rescue target vaariable
    astronaut_rescued = 0
    astronaut_target = 10
    
    # bonus variables
    bonus_chance = 10
    bonus_time = 300
    bonus_speed = 8
    invincible_duration = 300
    
