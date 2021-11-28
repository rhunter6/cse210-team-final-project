#I got this info from this link
#https://api.arcade.academy/en/latest/examples/sprite_move_keyboard_better.html?highlight=move%20right%20to%20left
import arcade

class Move(arcade.Window) :
    
    """
    this is the one that moves the player. it should move them left, right
    up or down. that's all this should do. Or it could just be a mouse move. no buttons. 
    """
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        self.player_list = None
        
        self.player_sprite = None 
        
        #Track the current state fo what key is pressed
        self.left_pressed = False 
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False 
        
    def setup(self):
        """Set up the game and initialize the variables."""
        
        self.player_list = arcade.SpriteList()
        
    def on_draw(self):
        """
        Render the screen 
        """
        arcade.start_render()
        
        self.player_sprite.draw()
        
    pass
    
