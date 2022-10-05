
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
    window_name = "Evil Clutches"

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
    
    # demon variables
    demon_min_spawn = 15        # ticks of game clock
    demon_max_spawn = 150       # ticks of game clock
    demon_speed = 10
    
    # fireball variables
    fireball_speed = 20
    fireball_max = 1
    unharmed_kill_count = 0
    
    # baby variables
    baby_min_spawn = 30         # ticks of game clock
    baby_max_spawn = 200        # ticks of game clock
    baby_speed = 5
    
    # baby rescue target vaariable
    baby_rescued = 0
    baby_target = 10
    
    # bonus variables
    bonus_chance = 100
    bonus_time = 300
    bonus_speed = 8
    invincible_duration = 300
    
