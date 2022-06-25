import arcade
import random
import Assets

class tile(arcade.Sprite):
    
    def __init__(self,x,y):
        self.center_x = x
        self.center_y = y
        self.boundary_bottom = self.center_y - 30
        self.boundary_top = self.center_y + 30
        self.boundary_left = self.center_x - 30
        self.boundary_right = self.center_x + 30
        
