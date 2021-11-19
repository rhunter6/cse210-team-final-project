"""
The root package contains all the source code for the game.
"""
from game import constants
import arcade


class Game(arcade.window): 
    
    def setup(self): 
        pass

    def on_draw(self):
        pass

    def update(self):
        pass

    def restart(self):
        pass
    
    def draw_game_over(self):
        pass

    def draw_score(self): 
        pass
    
    def check_keys(self):
        pass
    
    def on_key_press(self):
        pass
    
    def on_key_release(self, key: int, modifiers: int):
        if key in self.held_keys:
            self.held_keys.remove(key)
    
    def check_collisions(self):
        pass
    
    def cleanup(self):
        pass
    
    def create_enemys(self): 
        pass
    
