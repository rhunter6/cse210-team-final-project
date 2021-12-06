import arcade
from game import constants
from game.point import Point

from game.actor import Actor
from game.actors.player import Player
from game.actors.bullet import Bullet

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
        self.coin_list = []

        # "props"
        self.platform_list = []
        self.wall_list = []
        self.ladder_list = []

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
        arcade.set_background_color(arcade.color.JET)

    def create_sprites(self):
        """ Draw the sprites
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        # "actors"
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.projectile_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

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

        # platforms

        platforms_to_draw = [
        #   [ Position (Point),                                    width (INT),                 height (INT), color ]
            [ Point(constants.SCREEN_WIDTH/2, 15),              constants.SCREEN_WIDTH,    30,  "brown" ],
            [ Point((constants.SCREEN_WIDTH/2-200), 215),       constants.SCREEN_WIDTH,    30,  "brown" ],
            [ Point((constants.SCREEN_WIDTH/2+200), 415),       constants.SCREEN_WIDTH,    30,  "brown" ],
            [ Point((constants.SCREEN_WIDTH/2-200), 615),       constants.SCREEN_WIDTH,    30,  "brown" ],
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
            [ Point(10,200),                                    20,            1200,        "blue"    ],
            [ Point(constants.SCREEN_WIDTH-10, 200),            20,            1200,        "blue"    ]
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
        #   [ Position (Point),                              width (INT),    height (INT),   color ]
            [ Point(150,200),                                    20,            1200,        "green"    ],
            [ Point(constants.SCREEN_WIDTH-100, 200),            20,            1200,        "green"    ]
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


        # player
        self.the_player = Player(10, color="white")
        self.the_player.center_x = 200
        self.the_player.center_y = 100
        self.player_list.append(self.the_player)


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

        # "actors"
        self.player_list.draw()
        self.enemy_list.draw()
        self.projectile_list.draw()
        self.coin_list.draw()

        # "props"
        self.platform_list.draw()
        self.wall_list.draw()
        self.ladder_list.draw()

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

    def on_update(self, delta_time):
        """ Does physics and other updates
        ARGS:
            self (Director): an instance of Director
        RETURNS:
            none
        """
        self.projectile_list.update()
        self.PHYSICS.update()
