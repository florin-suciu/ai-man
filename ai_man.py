#===============================================================================
# IMPORTS
#===============================================================================
import os
import pygame


#===============================================================================
# PRIVATE CLASSES
#===============================================================================
class Game():
    """
    The game class, main class.
    """

    def __init__(self):
        """
        Initializes a game object.
        """
        global screen, sounds

        # draw main screen.

        # center window
        os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

        # initialize sounds
        if play_sounds:
            pygame.mixer.pre_init(44100, -16, 1, 512)

        pygame.init()

        pygame.display.set_caption("AI Shooter")

        size = (640, 480)
        screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        # load sounds
        if play_sounds:
            pygame.mixer.init(44100, -16, 1, 512)
            sounds["short_sound"] = pygame.mixer.Sound("mysounds/short_sound.ogg")
            sounds["start"] = pygame.mixer.Sound("mysounds/start.ogg")
            sounds["end"] = pygame.mixer.Sound("mysounds/end.ogg")
            sounds["options"] = pygame.mixer.Sound("mysounds/options.ogg")
            sounds["coin"] = pygame.mixer.Sound("mysounds/coin.ogg")

        self.font = pygame.font.Font("fonts/prstart.ttf", 16)

    def showMenu(self):
        """
        Show game menu
        Redraw screen only when enter is pressed, when that occurs,
        exit from this screen and start the game.
        """
        global screen

        # draw main menu
        start_pos = 120
        screen.fill([0, 0, 0])
        screen.blit(self.font.render("Start game", True, pygame.Color('yellow')), [240, start_pos])
        screen.blit(self.font.render("Options", True, pygame.Color('white')), [267, start_pos + 50])
        screen.blit(self.font.render("Help", True, pygame.Color('white')), [290, start_pos + 100])
        screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
        screen.blit(self.font.render("(c) 2011 UBB Cluj", True, pygame.Color('white')), [45, start_pos + 280])
        screen.blit(self.font.render("ALL RIGHTS RESERVED", True, pygame.Color('white')), [50, start_pos + 300])

        pygame.display.flip()

        in_menu = True
        option = 0  # 0 = start game, 1 = options, 2 = help, 3 = quit
        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if option == 0:
                            continue
                        elif option == 1:
                            option = 0
                            screen.blit(self.font.render("Start game", True, pygame.Color('yellow')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('white')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('white')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 2:
                            option = 1
                            screen.blit(self.font.render("Start game", True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('yellow')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('white')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 3:
                            option = 2
                            screen.blit(self.font.render("Start game", True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('white')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('yellow')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_DOWN:
                        if option == 3:
                            continue
                        elif option == 2:
                            option = 3
                            screen.blit(self.font.render("Start game", True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('white')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('white')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('yellow')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 1:
                            option = 2
                            screen.blit(self.font.render("Start game", True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('white')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('yellow')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 0:
                            option = 1
                            screen.blit(self.font.render("Start game", True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render("Options", True, pygame.Color('yellow')), [267, start_pos + 50])
                            screen.blit(self.font.render("Help", True, pygame.Color('white')), [290, start_pos + 100])
                            screen.blit(self.font.render("Exit", True, pygame.Color('white')), [290, start_pos + 150])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_RETURN:
                        # user has chosen a menu
                        in_menu = False

        if option == 3:
            # exit game
            pass
        elif option == 1:
            self.draw_options()
        elif option == 2:
            self.draw_help()
        else:
            # option = 0, start a new game
            self.draw_level_selection()

    def get_speed_string(self, ai_speed):
        '''
        This function returns the string which displays the speed of the AI.
        '''
        if (ai_speed) == SLOW:
            return "Speed: SLOW"
        elif (ai_speed) == NORMAL:
            return "Speed: NORMAL"
        elif (ai_speed) == FAST:
            return "Speed: FAST"

    def draw_options(self):
        """
        This function allows for the modification of options.
        """
        global screen, play_sounds, ai_speed
        start_pos = 160
        screen.fill([0, 0, 0])

        sound_string = "Sound: %s" % (play_sounds is True and "ON" or "OFF")
        screen.blit(self.font.render(sound_string, True, pygame.Color('yellow')), [240, start_pos])
        speed_string = self.get_speed_string(ai_speed)
        screen.blit(self.font.render(speed_string, True, pygame.Color('white')), [240, start_pos + 40])
        screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])

        pygame.display.flip()

        option = 0  # 0 - sound, 1 - quit
        in_options = True
        while in_options:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if option == 0:
                            continue
                        elif option == 1:
                            option = 0
                            screen.blit(self.font.render(sound_string, True, pygame.Color('yellow')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('white')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 2:
                            option = 1
                            screen.blit(self.font.render(sound_string, True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('yellow')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_DOWN:
                        if option == 2:
                            continue
                        elif option == 1:
                            option = 2
                            screen.blit(self.font.render(sound_string, True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('white')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('yellow')), [295, start_pos + 80])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 0:
                            option = 1
                            screen.blit(self.font.render(sound_string, True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('yellow')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_RETURN:
                        if option == 2:
                            in_options = False
                        elif option == 0:
                            if play_sounds:
                                sounds["options"].play()
                            play_sounds = not play_sounds
                            sound_string = "Sound: %s" % (play_sounds is True and "ON" or "OFF")
                            screen.fill([0, 0, 0])
                            screen.blit(self.font.render(sound_string, True, pygame.Color('yellow')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('white')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])
                            pygame.display.update()
                        elif option == 1:
                            if play_sounds:
                                sounds["options"].play()
                            ai_speed += 1
                            if ai_speed == 3:
                                ai_speed = 0
                            speed_string = self.get_speed_string(ai_speed)
                            screen.fill([0, 0, 0])
                            screen.blit(self.font.render(sound_string, True, pygame.Color('white')), [240, start_pos])
                            screen.blit(self.font.render(speed_string, True, pygame.Color('yellow')), [240, start_pos + 40])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 80])
                            pygame.display.update()

        self.showMenu()

    def draw_level_selection(self):
        """
        This function draws the level selection menu.
        """
        global screen
        screen.fill([0, 0, 0])

        start_pos = 130

        screen.blit(self.font.render("A walk in the park", True, pygame.Color('yellow')), [180, start_pos])
        screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
        screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
        screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
        screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])

        pygame.display.flip()

        in_level_slection = True
        option = 0  # 0 = park, 1 = city, 2 = jungle, 3 = sparta, 4 = back

        while in_level_slection:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if option == 0:
                            continue
                        elif option == 1:
                            option = 0
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('yellow')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 2:
                            option = 1
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('yellow')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 3:
                            option = 2
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('yellow')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 4:
                            option = 3
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('yellow')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_DOWN:
                        if option == 4:
                            continue
                        elif option == 3:
                            option = 4
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('yellow')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 2:
                            option = 3
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('yellow')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 1:
                            option = 2
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('white')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('yellow')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                        elif option == 0:
                            option = 1
                            screen.blit(self.font.render("A walk in the park", True, pygame.Color('white')), [180, start_pos])
                            screen.blit(self.font.render("The City", True, pygame.Color('yellow')), [260, start_pos + 40])
                            screen.blit(self.font.render("Welcome to the jungle", True, pygame.Color('white')), [160, start_pos + 80])
                            screen.blit(self.font.render("This is spartaa!!", True, pygame.Color('white')), [190, start_pos + 120])
                            screen.blit(self.font.render("Back", True, pygame.Color('white')), [295, start_pos + 220])
                            pygame.display.update()
                            if play_sounds:
                                sounds["short_sound"].play()
                    elif event.key == pygame.K_RETURN:
                        # user has chosen an option.
                        in_level_slection = False

        # We have the option:
        if option == 4:
            self.showMenu()
        else:
            self.create_game(option)

    def draw_help(self):
        """
        This function draws the help on the screen.
        """
        global screen
        start_pos = 60
        screen.fill([0, 0, 0])
        screen.blit(self.font.render("The goal of the game is to collect", True, pygame.Color('white')), [20, start_pos])
        screen.blit(self.font.render("all the coins.", True, pygame.Color('white')), [20, start_pos + 20])
        screen.blit(self.font.render("You are the green soldier and start", True, pygame.Color('white')), [20, start_pos + 60])
        screen.blit(self.font.render("off at the lower center of the screen.", True, pygame.Color('white')), [20, start_pos + 80])
        screen.blit(self.font.render("The red soldier is controlled by the", True, pygame.Color('white')), [20, start_pos + 100])
        screen.blit(self.font.render("AI and starts off on the top center of", True, pygame.Color('white')), [20, start_pos + 120])
        screen.blit(self.font.render("the screen.", True, pygame.Color('white')), [20, start_pos + 140])
        screen.blit(self.font.render("Control your soldier with the arrow", True, pygame.Color('white')), [20, start_pos + 180])
        screen.blit(self.font.render("keys, up, down, left, right.", True, pygame.Color('white')), [20, start_pos + 200])
        screen.blit(self.font.render("Some levels don't contain any walls,", True, pygame.Color('white')), [20, start_pos + 240])
        screen.blit(self.font.render("while others are like mazes.", True, pygame.Color('white')), [20, start_pos + 260])
        screen.blit(self.font.render("Good luck!", True, pygame.Color('white')), [235, start_pos + 320])
        pygame.display.flip()

        in_help = True
        while in_help:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        in_help = False
        self.showMenu()

    def create_game(self, option):
        """
        This function creates a game with the level selected.
            0 - A walk in the park
            1 - Big City
            2 - Welcome to the jungle
            3 - This is spartaa!!
        """
        global update_squares, free_positions, speed_value, ai_speed, walled_off

        NOTHING, WALL, PLAYER, ENEMY, COIN = range(5)
        screen.fill([0, 0, 0])

        # level will now be drawn
        lvl_width = 16
        lvl_height = 12
        level_map = {}  # will start at (1,1) and end at (12,16)

        if option == 0:
            level_file = open("maps/park.map", "r")
        elif option == 1:
            level_file = open("maps/city.map", "r")
        elif option == 2:
            level_file = open("maps/jungle.map", "r")
        elif option == 3:
            level_file = open("maps/sparta.map", "r")

        index = 1
        for line in level_file:
            current_line = line.replace("\n", "")
            inner_index = 1
            for character in current_line:
                if character == ".":
                    level_map[index, inner_index] = NOTHING
                elif character == "x":
                    level_map[index, inner_index] = WALL
                elif character == "g":
                    level_map[index, inner_index] = PLAYER
                elif character == "i":
                    level_map[index, inner_index] = ENEMY
                elif character == "c":
                    level_map[index, inner_index] = COIN
                inner_index += 1
            index += 1
        level_file.close()

        sprite_nothing = None
        sprite_wall = None

        # map was read, now load appropriate sprites
        map_sprites = pygame.transform.scale(pygame.image.load("images/level_sprites.gif").convert(), [160, 81])
        if option == 0:
            sprite_nothing = map_sprites.subsurface(0, 0, 40, 40)
            sprite_wall = map_sprites.subsurface(41, 0, 40, 40)
        elif option == 1:
            sprite_nothing = map_sprites.subsurface(81, 0, 40, 40)
            sprite_wall = map_sprites.subsurface(120, 0, 40, 40)
        elif option == 2:
            sprite_nothing = map_sprites.subsurface(0, 41, 40, 40)
            sprite_wall = map_sprites.subsurface(41, 41, 40, 40)
        elif option == 3:
            sprite_nothing = map_sprites.subsurface(81, 41, 40, 40)
            sprite_wall = map_sprites.subsurface(120, 41, 40, 40)
        # load coin sprite
        coin_sprite_file = pygame.transform.scale(pygame.image.load("images/coin.gif").convert(), [41, 41])
        coin_sprite = coin_sprite_file.subsurface(0, 0, 40, 40)

        # blit whole level
        for i in range(1, lvl_height + 1):
            for j in range(1, lvl_width + 1):
                coordinates = [(j - 1) * 40, (i - 1) * 40]
                if level_map[i, j] in (COIN, NOTHING, PLAYER, ENEMY):
                    screen.blit(sprite_nothing, coordinates)
                elif level_map[i, j] == WALL:
                    screen.blit(sprite_wall, coordinates)

        # make list of wall coordinates
        wall_coordinates = [[i, j] for (i, j) in level_map if level_map[i, j] == WALL]

        # load player and AI sprites, draw them
        player_sprites = pygame.transform.scale(pygame.image.load("images/mysprites.GIF").convert(), [168, 84])

        player_down = player_sprites.subsurface(0, 0, 40, 40)
#        player_left = player_sprites.subsurface(40, 0, 40, 40)
#        player_up = player_sprites.subsurface(81, 0, 40, 40)
#        player_right = player_sprites.subsurface(121, 0, 39, 39)

        enemy_down = player_sprites.subsurface(0, 41, 40, 40)
#        enemy_left = player_sprites.subsurface(40, 41, 40, 40)
#        enemy_up = player_sprites.subsurface(81, 41, 40, 40)
#        enemy_right = player_sprites.subsurface(121, 41, 39, 39)

        # draw coins
        for i in range(1, lvl_height + 1):
            for j in range(1, lvl_width + 1):
                coordinates = [(j - 1) * 40, (i - 1) * 40]
                if level_map[i, j] == COIN:
                    screen.blit(coin_sprite, coordinates)

        # draw level map
        pygame.display.flip()

        player_position = [[j, i] for (i, j) in level_map if level_map[i, j] == PLAYER][0]
        enemy_position = [[j, i] for (i, j) in level_map if level_map[i, j] == ENEMY][0]

        free_positions = [[x, y] for (x, y) in level_map if (level_map[x, y] == NOTHING) or (level_map[x, y] == COIN)]
        coin_positions = [[x, y] for (x, y) in level_map if level_map[x, y] == COIN]

        # draw player and enemy sprites
        screen.blit(player_down, [(player_position[0] - 1) * 40, (player_position[1] - 1) * 40])
        update_squares.append([(player_position[0] - 1) * 40, (player_position[1] - 1) * 40, 40, 40])
        screen.blit(enemy_down, [(enemy_position[0] - 1) * 40, (enemy_position[1] - 1) * 40])
        update_squares.append([(enemy_position[0] - 1) * 40, (enemy_position[1] - 1) * 40, 40, 40])

        pygame.display.update(update_squares)
        update_squares = []

        # create player and enemy objects
        player = Player(100, player_position)
        enemy = Player(100, enemy_position)

        seconds = 0

        # start game loop
        # we have the following useful variables:
        #    - player_position    --> [8, 12]
        #    - enemy_position     --> [8, 1]
        #    - update_squares     --> []
        #    - wall_coordinates   --> [[11, 11], [5, 2], [3, 9], ...]
        #    - level_map          --> {(7, 3): 0, (6, 9): 0, (12, 1): 0, (11, 11): 1, ... }
        in_help = True
        while in_help and player.status and enemy.status and coin_positions:
            #===================================================================
            # USER
            #===================================================================
            for event in pygame.event.get():
                # CHECK FOR KEY PRESSES
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if (player.x - 1, player.y) in level_map and\
                            [player.x - 1, player.y] not in wall_coordinates and\
                                [player.x - 1, player.y] != [enemy.x, enemy.y]:
                            # position is free, move player to that position
                            free_positions += [[player.x, player.y]]
                            screen.blit(sprite_nothing, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                            player.x -= 1
                            if [player.x, player.y] in coin_positions:
                                coin_positions.remove([player.x, player.y])
                                if play_sounds:
                                    sounds["coin"].play()
                            free_positions.remove([player.x, player.y])
                            screen.blit(player_down, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                        else:
                            if play_sounds:
                                sounds["options"].play()
                    elif event.key == pygame.K_DOWN:
                        if (player.x + 1, player.y) in level_map and\
                            [player.x + 1, player.y] not in wall_coordinates and\
                                [player.x + 1, player.y] != [enemy.x, enemy.y]:
                            # position is free, move player to that position
                            free_positions += [[player.x, player.y]]
                            screen.blit(sprite_nothing, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                            player.x += 1
                            if [player.x, player.y] in coin_positions:
                                coin_positions.remove([player.x, player.y])
                                if play_sounds:
                                    sounds["coin"].play()
                            free_positions.remove([player.x, player.y])
                            screen.blit(player_down, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                        else:
                            if play_sounds:
                                sounds["options"].play()

                    elif event.key == pygame.K_LEFT:
                        if (player.x, player.y - 1) in level_map and\
                            [player.x, player.y - 1] not in wall_coordinates and\
                                [player.x, player.y - 1] != [enemy.x, enemy.y]:
                            # position is free, move player to that position
                            free_positions += [[player.x, player.y]]
                            screen.blit(sprite_nothing, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                            player.y -= 1
                            if [player.x, player.y] in coin_positions:
                                coin_positions.remove([player.x, player.y])
                                if play_sounds:
                                    sounds["coin"].play()
                            free_positions.remove([player.x, player.y])
                            screen.blit(player_down, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                        else:
                            if play_sounds:
                                sounds["options"].play()

                    elif event.key == pygame.K_RIGHT:
                        if (player.x, player.y + 1) in level_map and\
                            [player.x, player.y + 1] not in wall_coordinates and\
                                [player.x, player.y + 1] != [enemy.x, enemy.y]:
                            # position is free, move player to that position
                            free_positions += [[player.x, player.y]]
                            screen.blit(sprite_nothing, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                            player.y += 1
                            if [player.x, player.y] in coin_positions:
                                coin_positions.remove([player.x, player.y])
                                if play_sounds:
                                    sounds["coin"].play()
                            free_positions.remove([player.x, player.y])
                            screen.blit(player_down, [(player.y - 1) * 40, (player.x - 1) * 40])
                            update_squares.append([(player.y - 1) * 40, (player.x - 1) * 40, 40, 40])
                        else:
                            if play_sounds:
                                sounds["options"].play()

                    elif event.key == pygame.K_ESCAPE:
                        in_help = False

                # UPDATE DISPLAY WITH LATEST CHANGES
                pygame.display.update(update_squares)
                update_squares = []
            #===================================================================
            # AI
            #===================================================================
            milli = clock.tick()
            seconds += milli / 1000.
            if seconds > speed_value[ai_speed]:
                seconds = 0
                # AI will make a move each time 0.8 - slow, 0.5 - normal or 0.2 - fast
                # seconds pass.
                move_AI_to = self.path_finder(enemy, player, free_positions)
                if move_AI_to is None:
                    # AI cannot reach player (player or AI are walled off)
                    walled_off = True
                    enemy.status = STATUS_DEAD
                    continue
                # effectively move the AI
                free_positions += [[enemy.x, enemy.y]]
                screen.blit(sprite_nothing, [(enemy.y - 1) * 40, (enemy.x - 1) * 40])
                update_squares.append([(enemy.y - 1) * 40, (enemy.x - 1) * 40, 40, 40])
                if [enemy.x, enemy.y] in coin_positions:
                    screen.blit(coin_sprite, [(enemy.y - 1) * 40, (enemy.x - 1) * 40])
                enemy.x, enemy.y = move_AI_to
                free_positions.remove([enemy.x, enemy.y])
                screen.blit(enemy_down, [(enemy.y - 1) * 40, (enemy.x - 1) * 40])
                update_squares.append([(enemy.y - 1) * 40, (enemy.x - 1) * 40, 40, 40])

                # UPDATE DISPLAY WITH LATEST CHANGES
                pygame.display.update(update_squares)
                update_squares = []

            #===================================================================
            # CHECK GAME STATUS
            #===================================================================
            if (enemy.x == player.x) and (enemy.y == player.y):
                player.status = STATUS_DEAD

        won = not coin_positions
        if player.status and enemy.status and not won:
            # user pressed ESCAPE key, display main menu
            pass
        else:
            # Display end screen.
            if play_sounds:
                sounds["end"].play()
            self.display_end_game(player, walled_off)

        # Show menu.
        self.showMenu()

    def display_end_game(self, player, walled_off):
        '''
        This function displays the end screen when a game is completed.
        '''
        global screen

        if player.status:
            colour = 'green'
            if walled_off:
                end_message = "You have won! AI cannot reach you!"
                posx = 70
                posy = 230
            else:
                end_message = "You have won!"
                posx = 230
                posy = 230

        else:
            end_message = "You have lost! Try again..."
            colour = 'red'
            posx = 120
            posy = 230

        screen.fill((205, 175, 149), (40, 210, 570, 60))
        screen.blit(self.font.render(end_message, True, pygame.Color(colour)), [posx, posy])

        pygame.display.update()

        in_end_screen = True
        seconds = 0
        blink = True
        while in_end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        in_end_screen = False
            # Blink end dialog
            milli = clock.tick()
            seconds += milli / 1000.
            if seconds > 0.500:
                seconds = 0
                if blink:
                    screen.blit(self.font.render(end_message, True, pygame.Color('yellow')), [posx, posy])
                else:
                    screen.blit(self.font.render(end_message, True, pygame.Color(colour)), [posx, posy])
                blink = not blink
                pygame.display.update()

    def get_available_moves(self, x, y, free_positions):
        '''
        This function returns a list with all squares on which player at [x,y] can move.
        '''
        global directions
        return_list = []
        for direction in directions:
            if [x + direction[0], y + direction[1]] in free_positions:
                return_list += [[x + direction[0], y + direction[1]]]
        return return_list

    def go_through_queue(self, queue, counter, free_positions):
        '''
        This function goes through each element from the queue and adds all adjacent
        non-wall cells to the queue with increased counter if the new found position
        wasn't already added to the queue with a smaller counter.
        '''
        # run through all elements from the queue with counter <counter> and add their
        # adjacent cells
        for entry in [i for i in queue if i[2] == counter]:
            for adjacent_position in self.get_available_moves(entry[0], entry[1], free_positions):
                # check if position was already added to the map
                if (adjacent_position[0], adjacent_position[1]) in [(x[0], x[1]) for x in queue]:
                    # position exists in map
                    # replace existing entry only if their counter is greater than the one we currently have
                    for existing_position in [j for j in queue if (j[0], j[1]) == (adjacent_position[0], adjacent_position[1])]:
                        if existing_position[2] > counter + 1:
                            # old position's counter is greater, add new position with smaller counter
                            queue.remove(existing_position)
                            queue.append([adjacent_position[0], adjacent_position[1], counter + 1])
                else:
                    queue.append([adjacent_position[0], adjacent_position[1], counter + 1])
        # check if we increased the counter, if not, it means that no advance was made
        # from last time, which means we cannot reach the target.
        if queue[-1][2] == counter:
            return queue, None
        return queue, counter + 1

    def retrace_move(self, queue, x, y):
        '''
        This function retraces the movement backwards from the queue.
        It will return the first position, the one with counter = 1
        '''
        end_position = [x, y]
        counter = queue[-1][2]
        while 1:
            if counter == 1:
                return end_position
            for position in [[x[0], x[1]] for x in queue if x[2] == counter - 1]:
                if position in self.get_available_moves(end_position[0], end_position[1], free_positions):
                    end_position = position
                    counter -= 1
                    break

    def path_finder(self, player1, player2, free_positions):
        '''
        This is a path finding algorithm.
        It will find the shortest path between the two players and return the first move
        from this shortest path.
        The idea is this:
        We will create a queue, add the location of the start position to it with counter 0.
        We will find all squares adjacent to that position and add them to the queue with counter 1,
        if the adjacent squares are not walls,
        or weren't already added to the queue with a smaller counter
        (wall - collision detection is made in the function
        which returns the adjacent cells for a certain square).
        We go through all items from the queue with counter 1 and repeat the above for them.
        When we have the coordinates of the target square in the queue, we have the shortest path.
        '''
        queue = [[player1.x, player1.y, 0]]
        counter = 0
        while 1:
            # because normally, free_positions do not include the position of the enemy player
            # we must add it so we can obtain this position as an adjacent one in the algorithm
            free_positions.append([player2.x, player2.y])
            queue, new_counter = self.go_through_queue(queue, counter, free_positions)
            # check if we got the second players position in the queue
            if (player2.x, player2.y) in [(x[0], x[1]) for x in queue]:
                # we have reached player2's position
                # retrace movements so we can get to the first one to return it
                return self.retrace_move(queue, player2.x, player2.y)
            if new_counter is None:
                # we made no advance from last time, target cannot be reached
                return None
            # increase counter
            counter += 1


class Player():
    def __init__(self, life, position):
        global STATUS_DEAD, STATUS_ALIVE

        self.status = STATUS_ALIVE
        self.hit_points = life
        self.x = position[1]
        self.y = position[0]

#=======================================================================================================================
# PRIVATE FUNCTIONS
#=======================================================================================================================


#=======================================================================================================================
# MAIN
#=======================================================================================================================
if __name__ == "__main__":

    # global vars
    screen = None  # will be the screen surface
    sounds = {}  # map with all sounds
    update_squares = []  # squares that need to be updated will be added to this list
    STATUS_DEAD, STATUS_ALIVE = range(2)

    # direction vectors (delta_row, delta_colum)
    directions = [(-1, 0),
                  (0, -1),
                  (0, 1),
                  (1, 0)]

    free_positions = []
    # time regarding variables
    clock = pygame.time.Clock()
    SLOW, NORMAL, FAST = range(3)
    ai_speed = NORMAL
    speed_value = {0: 0.800,
                   1: 0.500,
                   2: 0.200}
    walled_off = False
    # options
    play_sounds = True

    # start a game
    game = Game()
    if play_sounds:
        sounds["start"].play()
    game.showMenu()
