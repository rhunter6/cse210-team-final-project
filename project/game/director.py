import arcade
from game import constants
from game.point import Point

from game.live_actors.player import Player
from game.live_actors.bullet import Bullet

from game.props.platform import Platform
from game.props.wall import Wall


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

        # TESTING
        self.bullet_list = []

    def setup(self):
        """ Initalize the game and creates the sprites.
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
        opaque_objects = [self.platform_list, self.wall_list]
        
        # player
        self.the_player = Player(25, color="white")
        self.the_player.center_x = 200
        self.the_player.center_y = 300
        self.player_list.append(self.the_player)

        # platform
        ground = Platform(constants.SCREEN_WIDTH, 15, color="white")
        ground.center_x = constants.SCREEN_WIDTH / 2
        ground.center_y = 25
        self.platform_list.append(ground)

        # walls
        wall_x_list = [25, int(constants.SCREEN_WIDTH-25) ]
        for x in wall_x_list:
            wall = Wall(20, int(constants.SCREEN_HEIGHT/2), color="white")
            wall.center_x = x
            wall.center_y = int(constants.SCREEN_HEIGHT / 3)
            self.wall_list.append(wall)


        player_sprite = self.the_player
        platforms = opaque_objects
        gravity_constant = constants.GRAVITY
        ladders = self.ladder_list


        self.PHYSICS = arcade.PhysicsEnginePlatformer(  player_sprite,
                                                                        platforms,
                                                                        gravity_constant,
                                                                        ladders
                                                                    )

        self.PHYSICS.enable_multi_jump(2)

        # Set the background color
        arcade.set_background_color(arcade.color.JET)

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
        bullet = Bullet()
        
        orientation = self.the_player.get_orientation()
        bullet.set_orientation(orientation)

        # position the bullet
        start_x = self.the_player.center_x
        start_y = self.the_player.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        
        bullet.set_bullet_velocity()

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
                self.the_player.set_orientation("UP")

                # track jump count for multijump
                self.PHYSICS.increment_jump_counter()

        elif key == arcade.key.DOWN:
            self.the_player.change_y = -constants.MOVEMENT_SPEED
            self.the_player.set_orientation("DOWN")

        elif key == arcade.key.LEFT:
            self.the_player.change_x = -constants.MOVEMENT_SPEED
            self.the_player.set_orientation("LEFT")

        elif key == arcade.key.RIGHT:
            self.the_player.change_x = constants.MOVEMENT_SPEED
            self.the_player.set_orientation("RIGHT")

        # SHOOTING
        elif key == arcade.key.SPACE:
            # get where the player is facing
            orientation = self.the_player.get_orientation()
            position = self.the_player._get_position()



            # shoot a bullet in that direction
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
