import arcade
import sys
import random 

from arcade.sprite_list.spatial_hash import check_for_collision
from game import constants
from game.point import Point

from game.actor import Actor
from game.actors.player import Player
from game.actors.trophy import Trophy
from game.actors.bullet import Bullet
from game.actors.enemy import Enemy

from game.actors.platform import Platform
from game.actors.wall import Wall
from game.actors.ladder import Ladder



class Director(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        The constructor class
        """
        super().__init__(width, height, title)

        # Sprite lists
        # "actors"
        self.player_list = []
        self.enemy_list = []
        self.projectile_list = []
        self.trophy_list = []

        # "props"
        self.platform_list = []
        self.wall_list = []
        self.ladder_list = []

        #bg

        self.game_over = False
        self.background = []

        self.current_level = 1

    def setup(self):
        """ Initalize the game
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """

        # create sprites
        self.create_sprites()

        # establish the laws of physics
        self.setup_physics()

        # Set the background color
        self.background = arcade.load_texture("project/game/assets/images/bg3.png")
        # arcade.set_background_color(arcade.color.JET)

        
    def create_sprites(self):
        """ Draw the sprites
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # "actors"
        if self.game_over == False:
            self.player_list = arcade.SpriteList()
        
        self.enemy_list = arcade.SpriteList()
        self.projectile_list = arcade.SpriteList()
        self.trophy_list = arcade.SpriteList()

        # "props"
        self.platform_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.ladder_list = arcade.SpriteList()
        
        # player cannot move through these:
        self.solid_props = [self.platform_list, self.wall_list]

        if self.current_level == 1:
            self.level_01_sprites()
        
    def level_01_sprites(self):

        POSITION = 0
        WIDTH = 1
        HEIGHT = 2
        COLOR = 3

        platform_0_height = 0
        platform_1_height = 150
        platform_2_height = 300
        platform_3_height = 450
        platform_4_height = 600
        platform_5_height = 750

        # platforms

        platforms_to_draw = [
        #   [ Position (Point),                                             width (INT),                 height (INT), color ]
            [ Point((constants.SCREEN_WIDTH/2),     platform_0_height+15),               constants.SCREEN_WIDTH,    30,  "black" ],
            [ Point((constants.SCREEN_WIDTH/2-200), platform_1_height+15),         constants.SCREEN_WIDTH,    30,  "black" ],
            [ Point((constants.SCREEN_WIDTH/2+200), platform_2_height+15),         constants.SCREEN_WIDTH,    30,  "black" ],
            [ Point((constants.SCREEN_WIDTH/2-200), platform_3_height+15),         constants.SCREEN_WIDTH,    30,  "black" ],
            [ Point((constants.SCREEN_WIDTH/2+200), platform_4_height+15),         constants.SCREEN_WIDTH,    30,  "black" ],
            [ Point((constants.SCREEN_WIDTH/2-200), platform_5_height+15),         constants.SCREEN_WIDTH,    30,  "black" ],
        ]

        for p in platforms_to_draw:

            width = p[WIDTH]
            height = p[HEIGHT]
            fill_color = p[COLOR]
            x = p[POSITION].get_x()
            y = p[POSITION].get_y()

            platform = Platform(width, height, color=fill_color)
            platform.center_x = x
            platform.center_y = y
            self.platform_list.append(platform)

        # walls
        walls_to_draw = [
        #   [ Position (Point),                              width (INT),    height (INT),   color ]
            [ Point(10,200),                                    20,            1200,        "black"    ],
            [ Point(constants.SCREEN_WIDTH-10, 200),            20,            1200,        "black"    ]
        ]

        for w in walls_to_draw:

            width = w[WIDTH]
            height = w[HEIGHT]
            fill_color = w[COLOR]
            x = w[POSITION].get_x()
            y = w[POSITION].get_y()

            wall = Wall(width, height, color=fill_color)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)

        # ladders
        ladders_to_draw = [
        #   [ Position (Point),                                             width (INT),    height (INT),   color ]
            [ Point(constants.SCREEN_WIDTH-190, platform_0_height+105),            20,            150,        "green"    ],
            [ Point(190,                        platform_1_height+105),            20,            150,        "green"    ],
            [ Point(constants.SCREEN_WIDTH-190, platform_2_height+105),            20,            150,        "green"    ],
            [ Point(190,                        platform_3_height+105),            20,            150,        "green"    ],
            [ Point(constants.SCREEN_WIDTH-190, platform_4_height+105),            20,            150,        "green"    ],
        ]

        for l in ladders_to_draw:

            width = l[WIDTH]
            height = l[HEIGHT]
            fill_color = l[COLOR]
            x = l[POSITION].get_x()
            y = l[POSITION].get_y()

            wall = Ladder(width, height, color=fill_color)
            wall.center_x = x
            wall.center_y = y
            self.ladder_list.append(wall)

        # enemies
        enemies_to_draw = [
        #   [ Position (Point),                              width (INT),    height (INT),   color ]
            [ Point(500, platform_0_height+80),                 100,            100,        "black"    ],
            [ Point(800, platform_0_height+80),                 100,            100,        "black"    ],
            [ Point(500, platform_1_height+80),                 100,            100,        "black"    ],
            [ Point(800, platform_1_height+80),                 100,            100,        "black"    ],
            [ Point(400, platform_2_height+80),                 100,            100,        "black"    ],
            [ Point(600, platform_2_height+80),                 100,            100,        "black"    ],
            [ Point(800, platform_2_height+80),                 100,            100,        "black"    ],
            [ Point(400, platform_3_height+80),                 100,            100,        "black"    ],
            [ Point(600, platform_3_height+80),                 100,            100,        "black"    ],
            [ Point(300, platform_4_height+80),                 100,            100,        "black"    ],
            [ Point(500, platform_4_height+80),                 100,            100,        "black"    ],
            [ Point(900, platform_4_height+80),                 100,            100,        "black"    ],
            [ Point(450, platform_5_height+80),                 100,            100,        "black"    ],
            [ Point(750, platform_5_height+80),                 100,            100,        "black"    ]
        ]

        for e in enemies_to_draw:

            width = e[WIDTH]
            height = e[HEIGHT]
            fill_color = e[COLOR]
            x = e[POSITION].get_x()
            y = e[POSITION].get_y()
            
            enemy_img = "project/game/assets/images/enemy1.png"
            #enemy = Enemy(width, height, color=fill_color)
            enemy = Enemy(enemy_img, 0.15)
            enemy.center_x = x
            enemy.center_y = y
            enemy.spawn_x = x
            self.enemy_list.append(enemy)

        # player
        player_img = "project/game/assets/images/robot1.png"
        #self.the_player = Player(10, color="white")
        self.the_player = Player(player_img, 0.5)
        self.the_player.center_x = 200
        self.the_player.center_y = 100
        self.player_list.append(self.the_player)

        # trophy
        trophy_img = "project/game/assets/images/trophy.png"
        trophy = Trophy(trophy_img, 0.10)
        trophy.center_x = 1250
        trophy.center_y = 660
        self.trophy_list.append(trophy)


    def setup_physics(self):
        player_sprite = self.the_player
        platforms = self.solid_props
        gravity_constant = constants.GRAVITY
        ladders = self.ladder_list

        self.PHYSICS = arcade.PhysicsEnginePlatformer(  player_sprite,
                                                        platforms,
                                                        gravity_constant,
                                                        ladders
                                                    )

        self.PHYSICS.enable_multi_jump(constants.DOUBLE_JUMP)


    def on_draw(self):
        """
        Render the screen.
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,self.background)

        # "actors"
        self.player_list.draw()
        self.enemy_list.draw()
        self.projectile_list.draw()
        self.trophy_list.draw()

        # "props"
        self.platform_list.draw()
        self.wall_list.draw()
        self.ladder_list.draw()

        #if the hero is touching robot, draw complaints message and play corrisponding audio
        if self.check_robot_complaining(): 
            self.draw_robot_complaining()
            self.play_robot_complaining()
        
        #if the player gets the trophy, draw game won screen
        if self.check_player_won(): 
            self.draw_game_won()
            self.play_winning_sound()
            
    def draw_robot_complaining(self):
        """draws a game over screen with user friendly messages
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        msg_text = "STOP TOUCHING ME!"
        start_x =  constants.SCREEN_WIDTH//2 - 250
        start_y = constants.SCREEN_HEIGHT//2
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=40, color=arcade.color.YELLOW_ORANGE,font_name="Kenney Blocks")


    def draw_game_won(self):
        """draws a you won screen with user friendly messages
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        msg_text = "GOOD JOB"
        start_x =  constants.SCREEN_WIDTH//2 - 200
        start_y = constants.SCREEN_HEIGHT//2
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=40, color=arcade.color.YELLOW_ORANGE, font_name="Kenney Blocks")
        msg_text = "YOU WON THE GAME" 
        start_x = constants.SCREEN_WIDTH//2 - 263
        start_y = constants.SCREEN_HEIGHT//2 -100
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.GREEN)
        msg_text = "Press Enter to Play again" 
        start_x = constants.SCREEN_WIDTH//2 - 275
        start_y = constants.SCREEN_HEIGHT//2 -200
        arcade.draw_text(msg_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.GREEN)
        
    def shoot(self):
        """ Shoots a single bullet
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # create the bullet
        bullet = Bullet()

        # position the bullet
        start_x = self.the_player.center_x
        start_y = self.the_player.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        
        # make the bullet go in the direction the player is facing
        orientation = self.the_player.get_orientation()
        bullet.set_orientation(orientation)
        bullet.set_bullet_direction()

        if constants.DEBUG_MODE:
            print(f"shooting at direction: {bullet.get_orientation()}")

        self.projectile_list.append(bullet)
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed.
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """

        # BASIC DIRECTIONS
        if key == arcade.key.UP:
            if self.PHYSICS.can_jump():
                self.the_player.change_y = constants.MOVEMENT_SPEED
                
                # removed shooting up and down
                #self.the_player.set_orientation("UP")

                # track jump count for multijump
                self.PHYSICS.increment_jump_counter()

        elif key == arcade.key.DOWN:
            self.the_player.change_y = -constants.MOVEMENT_SPEED
            #self.the_player.set_orientation("DOWN")

        elif key == arcade.key.LEFT:
            self.the_player.change_x = -constants.MOVEMENT_SPEED
            self.the_player.set_orientation("LEFT")

        elif key == arcade.key.RIGHT:
            self.the_player.change_x = constants.MOVEMENT_SPEED
            self.the_player.set_orientation("RIGHT")

        # SHOOTING
        elif key == arcade.key.SPACE:
            # shoot a bullet
            self.shoot()
            #play associated sound
            self.play_shooting_sound()

        # Restart
        else:
            if key == arcade.key.ENTER:
                self.restart()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key.
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.the_player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.the_player.change_x = 0

    def check_collisions(self):
        """ Checks for collisions between bullets, walls and enemies
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        for bullet in self.projectile_list:

            # bullet-wall collision
            is_colliding_with_wall = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if is_colliding_with_wall:
                self.destroy_bullet(bullet)
                self.debug_console('BULLET colliding with WALL')

            # bullet-enemy collision
            for enemy in self.enemy_list:
                is_colliding_with_enemy = arcade.check_for_collision(bullet, enemy)
                if is_colliding_with_enemy:
                    self.destroy_bullet(bullet)
                    enemy.change_hp(-1)
                    enemy_hp = enemy.get_hp()
                    self.debug_console('BULLET colliding with ENEMY')
                    self.debug_console(f'ENEMY._hp = {enemy_hp}')

    def check_robot_complaining(self):
        """ Checks for enemy collision with the player
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # player-enemy collision
        for enemy in self.enemy_list:
            is_colliding_with_enemy = arcade.check_for_collision(self.the_player, enemy)
            if is_colliding_with_enemy:
                return(is_colliding_with_enemy)
    
    def check_player_won(self):
        """ Checks for trophy collision with the player
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # player-enemy collision
        is_won = arcade.check_for_collision_with_list(self.the_player, self.trophy_list)
        return is_won

            
    def check_for_enemy_deaths(self):
        """ Checks for enemies with 0 HP and removes them from play
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        for enemy in self.enemy_list:
            hp = enemy.get_hp()
            if hp == 0:
                self.enemy_list.remove(enemy)

    def enemy_movement(self):
        """ Moved enemies
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        for enemy in self.enemy_list:
            distance_from_spawn = abs(enemy.center_x - enemy.spawn_x)
            if distance_from_spawn > 100:
                enemy.reverse_direction()


    def destroy_bullet(self, bullet):
        """ Destroys a bullet
        """
        self.projectile_list.remove(bullet)

    def on_update(self, delta_time):
        """ Does physics and other updates
        ARGS:
            self (Director): an instance of Director
            delta_time: a module that keeps game running at live time.
        RETURNS:
            none
        """
        self.check_player_won()
        self.check_collisions()
        self.check_for_enemy_deaths()
        self.enemy_movement()
        self.enemy_list.update()
        self.projectile_list.update()
        self.PHYSICS.update()

    def debug_console(self,string):
        if constants.DEBUG_MODE:
            print(string)

    def restart(self):
        """Restarts game by repositing the actors.
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none"""
        self.player_list.clear
        self.enemy_list.clear
        self.projectile_list.clear 
        self.trophy_list.clear

        # "props"
        self.platform_list.clear
        self.wall_list.clear
        self.ladder_list.clear
         
        self.setup()

    def play_robot_complaining(self):
        """plays audio file of robot complaining
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # Loading the audio files
        complaining = arcade.load_sound("project/game/assets/sounds/mixkit-game-notification-wave-alarm-987.wav",False)
        
        # Playing the audio
        arcade.play_sound(complaining,1.0,-1,False)

    def play_winning_sound(self):
        """plays audio file for when the game is won
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
            """
        # Loading the audio files
        win = arcade.load_sound("project/game/assets/sounds/mixkit-melodic-bonus-collect-1938.wav",False)
        
        # Playing the audio
        arcade.play_sound(win,1.0,-1,False)

    

    def play_shooting_sound(self):
        """plays audio file for when the bullets are shot
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
            """
        # Loading the audio files
        shoot = arcade.load_sound("project/game/assets/sounds/mixkit-short-laser-gun-shot-1670.wav",False)
        
        # Playing the audio
        arcade.play_sound(shoot,1.0,-1,False)